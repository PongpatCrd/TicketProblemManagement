import pyodbc
import ldap
import math

from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from datetime import *
from .models import *

def create_user(username, password):
  temp_name = username.lower()[:username.find('@')].split(".")
  User.objects.create_user(
    username   = username,
    password   = password,
    email      = username,
    first_name = temp_name[0],
    last_name  = temp_name[-1],
    is_active  = True
  )
  return 

def get_client_ip(request):
  x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
  if x_forwarded_for:
    ip = x_forwarded_for.split(',')[0]
  else:
    ip = request.META.get('REMOTE_ADDR')
  return ip

def get_all_branch_server_ip():
  tbl_branchs = TblBranch.objects.using('ticket_sale').values('branch_nickname', 'branch_server').exclude(branch_server=None).filter(branch_status=1)
  tbl_branchs = {detail['branch_nickname']: detail['branch_server'] for detail in tbl_branchs}
  return tbl_branchs

def get_all_branch_details():
  tbl_branchs = TblBranch.objects.using('ticket_sale').values('branch_nickname', 'branch_fullname', 'branchcodevista').exclude(branch_server=None).filter(branch_status=1)
  tbl_branchs = {detail['branch_nickname']: {'branch_fullname': detail['branch_fullname'], 'branch_code_vista': detail['branchcodevista']} for detail in tbl_branchs}
  return tbl_branchs

def search_transaction_branch_by_name_email_phone(branch_server, search_key):
  # output format
  # {
  #   vwBookingH_strCardNo: {
  #     'payment_type'      :[str,...],
  #     'total_price'       :int,
  #     'booking_date'      :str,
  #     'per_ticket_detail' : [
  #         {
  #           'showtime'    :str,
  #           'movie_name'  :str,
  #           'teatre'      :str,
  #           'seat_type'   :str,
  #           'seat_row'    :str,
  #           'seat_number' :int,
  #           'price'       :decimal
  #         },...
  #     ]},...
  # }
  dbconn = pyodbc.connect(
    Driver='{SQL Server}',
    Server=branch_server,
    Database='xxxxx',
    UID='xxxxx',
    PWD='xxxxx'
  )

  sql = "\
    SELECT TOP 200 [vwRowID], \
    [vwBookingH_dtmDateBooked], \
    [vwBookingD_curValue], \
    [vwScreenD_strPhyRowId], \
    [vwScreenD_strSeatId], \
    [vwAreaCat_strCode], \
    [vwSessionScreeningTime], \
    [vwScreenName], \
    [vwFilm], \
    [vwPrice_strCode], \
    [vwTransC_lgnNumber] \
    FROM [VISTA].[dbo].[viewCabBooking] with (NOLOCK) \
    WHERE (LOWER([vwBookingH_strName]) LIKE LOWER('%{0}%') OR [vwBookingH_strPhone] LIKE '%{0}%' OR LOWER([vwBookingH_strEmail]) LIKE LOWER('%{0}%')) \
    AND  [vwBookingH_dtmDateBooked] >= (SELECT DATEADD(DAY, -30, GETDATE())) \
    AND [vwBookingD_strStatus] = 'P' \
    ORDER BY [vwBookingH_dtmDateBooked] DESC, [vwScreenD_strSeatId] ASC \
  ".format(search_key)
  cursor = dbconn.execute(sql)

  transaction_details = {}
  all_transaction_number = []
  for detail in cursor.fetchall():
    trans_num = detail.vwTransC_lgnNumber
    all_transaction_number.append(trans_num)
    try:
      temp = transaction_details[trans_num]
      temp['total_price'] += round(detail.vwBookingD_curValue, 2)
      if detail.vwPrice_strCode not in temp['price_method']:
        temp['price_method'].append(detail.vwPrice_strCode)
      temp['per_ticket_details'].append(
        {
          'showtime'    :detail.vwSessionScreeningTime.strftime('%d-%m-%Y %H:%M'),
          'movie_name'  :detail.vwFilm,
          'teatre'      :detail.vwScreenName,
          'seat_type'   :detail.vwAreaCat_strCode,
          'seat_row'    :detail.vwScreenD_strPhyRowId,
          'seat_number' :detail.vwScreenD_strSeatId,
          'price'       :round(detail.vwBookingD_curValue, 2)
        }
      )
    except:
      transaction_details[detail.vwTransC_lgnNumber] = {}
      temp = transaction_details[detail.vwTransC_lgnNumber]
      temp['booking_number'] = detail.vwRowID
      temp['price_method'] = [detail.vwPrice_strCode]
      temp['trans_number'] = detail.vwTransC_lgnNumber
      temp['total_price'] = round(detail.vwBookingD_curValue, 2)
      temp['booking_date'] = detail.vwBookingH_dtmDateBooked.strftime('%d-%m-%Y %H:%M')
      temp['per_ticket_details'] = [
        {
          'showtime'    :detail.vwSessionScreeningTime.strftime('%d-%m-%Y %H:%M'),
          'movie_name'  :detail.vwFilm,
          'teatre'      :detail.vwScreenName,
          'seat_type'   :detail.vwAreaCat_strCode,
          'seat_row'    :detail.vwScreenD_strPhyRowId,
          'seat_number' :detail.vwScreenD_strSeatId,
          'price'       :round(detail.vwBookingD_curValue, 2)
        }
      ]
  all_transaction_number = list(set(all_transaction_number))
  
  if transaction_details:
    sql = "\
    SELECT [vwTransactionNumber], \
    [vwTransactionType], \
    [vwPaymentTransactionReference] \
    FROM [VISTA].[dbo].[viewCabTrans_Cash] with (NOLOCK) \
    WHERE [vwTransactionDateTime] >= (SELECT DATEADD(DAY, -35, GETDATE())) AND \
    [vwTransactionNumber] IN ("
    
    count_vwtransaction_number = len(all_transaction_number)
    for i in range(count_vwtransaction_number):
      sql += "'{}'".format(all_transaction_number[i])
      if i+1 != count_vwtransaction_number:
        sql += ", "
    sql += ") ORDER BY vwTransactionType"

    view_cab_trans_cash_details = {}
    cursor = dbconn.execute(sql)
    for detail in cursor.fetchall():
      trans_num = detail.vwTransactionNumber
      try:
        if detail.vwTransactionType not in view_cab_trans_cash_details[trans_num]['payment_type']:
          view_cab_trans_cash_details[trans_num]['payment_type'].append(detail.vwTransactionType)
          view_cab_trans_cash_details[trans_num]['payment_type'].sort()
        if detail.vwPaymentTransactionReference:
          view_cab_trans_cash_details[trans_num]['payment_ref_number'] = detail.vwPaymentTransactionReference
      except:
        view_cab_trans_cash_details[trans_num] = {
          'payment_type'      : [detail.vwTransactionType],
          'payment_ref_number': detail.vwPaymentTransactionReference
        }

    for trans_num, transaction_detail in transaction_details.items():
      transaction_detail['payment_type'] = view_cab_trans_cash_details[trans_num]['payment_type']
      transaction_detail['payment_ref_number'] = view_cab_trans_cash_details[trans_num]['payment_ref_number']
  return list(transaction_details.values())
      
def search_transaction_branch_by_ref_number(branch_server, payment_transaction_reference):
  # output format
  # {
  #   vwBookingH_strCardNo: {
  #     'payment_type'      :[str,...],
  #     'total_price'       :int,
  #     'booking_date'      :str,
  #     'per_ticket_detail' : [
  #         {
  #           'showtime'    :str,
  #           'movie_name'  :str,
  #           'teatre'      :str,
  #           'seat_type'   :str,
  #           'seat_row'    :str,
  #           'seat_number' :int,
  #           'price'       :decimal
  #         },...
  #     ]},...
  # }
  dbconn = pyodbc.connect(
    Driver='{SQL Server}',
    Server=branch_server,
    Database='VISTA',
    UID='vista_sa',
    PWD='vistasa@2020'
  )

  sql = "\
  SELECT TOP 200 [vwTransactionNumber], \
  [vwTransactionType], \
  [vwPaymentTransactionReference] \
  FROM [VISTA].[dbo].[viewCabTrans_Cash] with (NOLOCK) \
  WHERE [vwTransactionNumber] IN (\
    SELECT [vwTransactionNumber] \
    FROM [VISTA].[dbo].[viewCabTrans_Cash] with (NOLOCK) \
    WHERE [vwPaymentTransactionReference] = '{0}') \
  AND [vwTransactionDateTime] >= (SELECT DATEADD(DAY, -35, GETDATE())) \
  ORDER BY vwTransactionType\
  ".format(payment_transaction_reference)
  cursor = dbconn.execute(sql)

  view_cab_trans_cash_details = {}
  all_transaction_number = []
  for detail in cursor.fetchall():
    trans_num = detail.vwTransactionNumber
    try:
      if detail.vwTransactionType not in view_cab_trans_cash_details[trans_num]['payment_type']:
        view_cab_trans_cash_details[trans_num]['payment_type'].append(detail.vwTransactionType)
        view_cab_trans_cash_details[trans_num]['payment_type'].sort()
      if detail.vwPaymentTransactionReference:
        view_cab_trans_cash_details[trans_num]['payment_ref_number'] = detail.vwPaymentTransactionReference
    except:
      view_cab_trans_cash_details[trans_num] = {
        'payment_type'      : [detail.vwTransactionType],
        'payment_ref_number': detail.vwPaymentTransactionReference
      }
    all_transaction_number.append(detail.vwTransactionNumber)

  transaction_details = {}
  if all_transaction_number:
    sql = "\
      SELECT [vwRowID], \
      [vwBookingH_dtmDateBooked], \
      [vwBookingD_curValue], \
      [vwScreenD_strPhyRowId], \
      [vwScreenD_strSeatId], \
      [vwAreaCat_strCode], \
      [vwSessionScreeningTime], \
      [vwScreenName], \
      [vwFilm], \
      [vwPrice_strCode], \
      [vwTransC_lgnNumber] \
      FROM [VISTA].[dbo].[viewCabBooking] with (NOLOCK) \
      WHERE [vwBookingD_strStatus] = 'P' \
      AND [vwTransC_dtmDateTime] >= (SELECT DATEADD(DAY, -30, GETDATE())) \
      AND [vwTransC_lgnNumber] IN ("

    count_vwtransaction_number = len(all_transaction_number)
    for i in range(count_vwtransaction_number):
      sql+= "'{}'".format(all_transaction_number[i])
      if i+1 != count_vwtransaction_number:
        sql += ", "
    sql += ") ORDER BY [vwBookingH_dtmDateBooked] DESC, [vwScreenD_strSeatId] ASC"

    cursor = dbconn.execute(sql)
    for detail in cursor.fetchall():
      trans_num = detail.vwTransC_lgnNumber
      try:
        temp = transaction_details[trans_num]
        temp['total_price'] += round(detail.vwBookingD_curValue, 2)
        if detail.vwPrice_strCode not in temp['price_method']:
          temp['price_method'].append(detail.vwPrice_strCode)
        temp['per_ticket_details'].append(
          {
            'showtime'    :detail.vwSessionScreeningTime.strftime('%d-%m-%Y %H:%M'),
            'movie_name'  :detail.vwFilm,
            'teatre'      :detail.vwScreenName,
            'seat_type'   :detail.vwAreaCat_strCode,
            'seat_row'    :detail.vwScreenD_strPhyRowId,
            'seat_number' :detail.vwScreenD_strSeatId,
            'price'       :round(detail.vwBookingD_curValue, 2)
          }
        )
      except:
        transaction_details[trans_num] = {}
        temp = transaction_details[trans_num]
        temp['booking_number'] = detail.vwRowID
        temp['price_method'] = [detail.vwPrice_strCode]
        temp['total_price'] = round(detail.vwBookingD_curValue, 2)
        temp['trans_number'] = detail.vwTransC_lgnNumber
        temp['payment_ref_number'] = view_cab_trans_cash_details[trans_num]['payment_ref_number']
        temp['payment_type'] = list(set(view_cab_trans_cash_details[trans_num]['payment_type']))
        temp['booking_date'] = detail.vwBookingH_dtmDateBooked.strftime('%d-%m-%Y %H:%M')
        temp['per_ticket_details'] = [
          {
            'showtime'    :detail.vwSessionScreeningTime.strftime('%d-%m-%Y %H:%M'),
            'movie_name'  :detail.vwFilm,
            'teatre'      :detail.vwScreenName,
            'seat_type'   :detail.vwAreaCat_strCode,
            'seat_row'    :detail.vwScreenD_strPhyRowId,
            'seat_number' :detail.vwScreenD_strSeatId,
            'price'       :round(detail.vwBookingD_curValue, 2)
          }
        ]
  return list(transaction_details.values())

def this_user_in_ldap(username, password):
  """
  username must be fullname ex. pongpat choorod
  """
  connect = ldap.initialize('xxxxx')
  connect.set_option(ldap.OPT_REFERRALS, 0)
  try:
    connect.simple_bind_s(username, password)
    return True
  except:
    return False

def initial_bank():
  banks=[
    Bank(name="SCB"),
    Bank(name="KBANK"),
    Bank(name="GSB"),
    Bank(name="BBL"),
    Bank(name="TMB"),
    Bank(name="BAY"),
    Bank(name="CITI"),
    Bank(name="KTB"),
    Bank(name="NBANK"),
    Bank(name="SCIB"),
    Bank(name="GHB")
  ]
  Bank.objects.bulk_create(banks)
