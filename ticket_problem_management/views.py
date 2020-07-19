import logging
import operator

from datetime import *
from .functions import *

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db import transaction
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
def index(request):
  branch_details = get_all_branch_details()
  current_date = datetime.today().strftime("%Y-%m-%d")

  context = {
    'branch_names'  : branch_details,
    'search_date_to': current_date,
    'tab'           : 'problem'
  }

  return render(request, 'index.html', context)

@transaction.atomic
def problem_search(request):
  def guard():
    if len(search_branch_code) != 3:
      return False, "Invalid search_branch_code."
    elif search_branch_code not in list(TblBranch.objects.using('ticket_sale').values_list('branch_nickname', flat=True)):
      return False, "Not found search_branch_code in branch list."
    elif len(search_by) > 25:
      return False, "Max size of search_by is 25 characters."
    elif len(search_key) > 100:
      return False, "Max size of search_key is 100 characters."
    else:
      return True, "success"

  if not request.user.is_authenticated:
    return index(request)

  page = request.GET.get('page', 1)
  search_branch_code = request.GET.get('search_branch_code')
  search_by = request.GET.get('search_by')
  search_key = request.GET.get('search_key')
  current_date = datetime.today().strftime("%Y-%m-%d")
  ip = get_client_ip(request)

  guard_complate, result = guard()
  purchase_ticket_trans = []
  histories = {}

  if guard_complate:
    branch_servers = TblBranch.objects.using('ticket_sale').values_list('branch_server', flat=True).get(branch_nickname=search_branch_code)
    try:
      if search_by == 'Reference number':
        purchase_ticket_trans = search_transaction_branch_by_ref_number(branch_server=branch_servers, payment_transaction_reference=search_key)
      elif search_by == 'Name/Email/Phone':
        purchase_ticket_trans = search_transaction_branch_by_name_email_phone(branch_server=branch_servers, search_key=search_key)
      else:
        purchase_ticket_trans = []
    except Exception as e:
      esult = "Connect to branch server failed."
      logging.getLogger("error_logger").error(repr(e))
    LogsSearchAccess.objects.create(ip=ip, username=request.user.username, branch_code=search_branch_code, search_by=search_by, search_key=search_key)
    
    if len(purchase_ticket_trans) == 0:
      histories = ProblemManagementHistory.objects.values().filter(branch_code=search_branch_code, search_by=search_by, search_key=search_key).order_by('-updated_at')
      if histories.exists():
        histories = list(histories)

  paginator = Paginator(purchase_ticket_trans, 10)
  try:
    purchase_ticket_trans = paginator.page(page)
  except EmptyPage:
    purchase_ticket_trans = paginator.page(paginator.num_pages)

  bank_list = list(Bank.objects.values('id', 'name'))
  branch_details = get_all_branch_details()
  context = {
    'search_branch_code'     : search_branch_code,
    'search_by'              : search_by,
    'search_key'             : search_key,
    'purchase_ticket_details': purchase_ticket_trans,
    'branch_names'           : branch_details,
    'bank_list'              : bank_list,
    'search_date_to'         : current_date,
    'histories_in_search'    : histories,
    'page'                   : page,
    'last_page'              : paginator.num_pages,
    'result'                 : result
  }
  return render(request, 'index.html', context)

def history_search(request):
  def guard():
    if len(search_date_from) != 10:
      return False, "Max size of search_date_from is 10 characters."
    elif len(search_date_to) != 10:
      return False, "Max size of search_date_to is 10 characters."
    else:
      return True, "success"
      
  if not request.user.is_authenticated:
    result = 'login falied'
  else:
    search_branch_code = request.GET.get('search_branch_code')
    search_date_from = request.GET.get('search_date_from')
    search_date_to = request.GET.get('search_date_to')

    guard_complate, result = guard()
    if guard_complate:
      search_date_to = datetime.strptime(search_date_to, '%Y-%m-%d').date()
      search_date_to += timedelta(days=1)
      search_date_to = search_date_to.strftime('%Y-%m-%d')

      histories = ProblemManagementHistory.objects.values('branch_code', 'ip', 'username', 'reason', 'solution', 'search_by', 'search_key', 'updated_at').filter(updated_at__range=(search_date_from, search_date_to))

      if search_branch_code != "":
        histories = histories.filter(branch_code=search_branch_code)
      if histories.exists():
        histories = list(histories.order_by('-updated_at'))
      else:
        histories = {}
      
      context = {
        'histories'         : histories,
        'result'            : result
      }
      html = render_to_string('ticket_problem_history_detail.html', context)
    else:
      pass

  try:
    context = {
      'html'              : html,
      'result'            : result
    }
  except:
    context = {
      'html'              : "",
      'result'            : result
    }
  return JsonResponse(context)

@transaction.atomic
def resolve_problem_save(request):
  def guard():
    if len(search_branch_code) != 3:
      return False, "Invalid search_branch_code."
    elif search_branch_code not in list(TblBranch.objects.using('ticket_sale').values_list('branch_nickname', flat=True)):
      return False, "Not found search_branch_code in branch list."
    elif len(search_by) > 25:
      return False, "Max size of search_by is 25 characters."
    elif len(search_key) > 100:
      return False, "Max size of search_key is 100 characters."
    elif len(other_bank_name) > 15:
      return False, "Max size of other_bank_name is 15 characters."
    elif len(bank_location) > 255:
      return False, "Max size of bank_location is 255 characters."
    elif len(account_number) > 20:
      return False, "Max size of account_number is 20 digits."
    elif len(account_name) > 100:
      return False, "Max size of account_name is 100 characters."
    elif len(trans_date) > 10:
      return False, "Max size of transferred_date is 10 characters."
    elif len(trans_time) > 4:
      return False, "Max size of transferred_time is 4 characters." 
    else:
      return True, "success"
  
  if not request.user.is_authenticated:
    return index(request)
  else:
    search_branch_code = request.POST.get('search_branch_code')
    search_by = request.POST.get('search_by')
    search_key = request.POST.get('search_key')
    problem_reason = request.POST.get('problem_reason')
    bank_id = int(request.POST.get('bank_id'))
    resolve_method = request.POST.get('resolve_method')
    other_bank_name = request.POST.get('other_bank_name')
    bank_location = request.POST.get('bank_location')
    account_number = request.POST.get('account_number')
    account_name = request.POST.get('account_name')
    trans_date = request.POST.get('trans_date')
    trans_time = request.POST.get('trans_time')

    guard_complete, result = guard()
    
    if not guard_complete:
      pass
    else:
      username = request.user.username
      ip = get_client_ip(request)

      if username == '':
        try:
          username = ProblemManagementHistory.objects.values('username').filter(ip=ip).exclude(username='').order_by('-id')[0]['username']
        except:
          username = ''

      history = ProblemManagementHistory.objects.create(
        ip             = ip,
        branch_code    = search_branch_code,
        username       = username,
        reason         = problem_reason,
        solution       = resolve_method,
        search_key     = search_key,
        search_by      = search_by
      )
      history_id = history.id

      if resolve_method == "คืนเงินผ่านบัญชี":
        if bank_id == -1:
          if other_bank_name not in list(Bank.objects.values_list('name', flat=True)):
            bank = Bank.objects.create(name=other_bank_name)
            bank_id = bank.id

        ProblemManagementHistoryRefundDetail.objects.create(
          history_id      = history_id,
          bank_id         = bank_id,
          bank_location   = bank_location,
          account_number  = account_number,
          account_name    = account_name,
          refund_datetime = trans_date + ' ' + trans_time[:2] + ":" + trans_time[3:]
        )

    return JsonResponse({'result': result})

def _login(request):
  def guard():
    if username.lower().find('@') == -1:
      return False, "Please use email as a username."
    elif password == '':
      return False, "Password must not empty."
    else:
      return True, "success"

  username = request.POST.get("username")
  password = request.POST.get("password", None)

  guard_complate, result = guard()

  db_username_list = list(User.objects.values_list('username', flat=True))
  if not guard_complate:
    pass

  is_user_in_ldap = this_user_in_ldap(username, password)

  if username not in db_username_list:
    if is_user_in_ldap:
      create_user(username, password)
  else:
    if is_user_in_ldap:
      user = User.objects.get(username=username)
      user.set_password(password)
      user.save()
  
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
  else:
    if result == 'success':
      result = "This username or password are not match or not in member list."
    else:
      pass
  
  return JsonResponse({'result': result})

def _logout(request):
  logout(request)
  return JsonResponse({})

def personal_member_detail(request):
  search_key = request.GET.get('personal_search_key', '').strip()

  if not request.user.is_authenticated:
    result = 'login failed'
  elif search_key:
    membership_ids = CogneticMembersCard.objects.using('vista_loyal').values_list('card_membershipid', flat=True).filter(
      Q(card_membershipid__icontains=search_key) |
      Q(card_cardnumber__icontains=search_key) |
      Q(card_membername__icontains=search_key)
    ).distinct()[:1000]
    membership_ids = list(membership_ids)
    
    person_ids = CogneticMembersMembership.objects.using('vista_loyal').values_list('membership_personid', flat=True).filter(
      Q(membership_id__in=membership_ids)
    ).distinct()[:1000]
    person_ids = list(person_ids)

    ex_search_key = search_key.split(' ')
    if len(ex_search_key) > 1:
      cognetic_core_persons = CogneticCorePerson.objects.using('vista_loyal').values().filter(
        Q(person_id__in=person_ids) |
        Q(person_firstname__icontains=ex_search_key[0]) &
        Q(person_lastname__icontains=ex_search_key[1])
      ).order_by('-person_creationdate')
    else:
      cognetic_core_persons = CogneticCorePerson.objects.using('vista_loyal').values().filter(
        Q(person_id__in=person_ids) |
        Q(person_id__icontains=search_key) |
        Q(person_firstname__icontains=search_key) |
        Q(person_lastname__icontains=search_key) |
        Q(person_email__icontains=search_key) |
        Q(person_username__icontains=search_key) |
        Q(person_mobilephone__icontains=search_key)
      ).order_by('-person_creationdate')
    cognetic_core_persons = cognetic_core_persons[:1000]
    
    # create members_club_name_map
    cognetic_members_club_name_map = {detail['club_id']: detail['club_name'] for detail in CogneticMembersClub.objects.using('vista_loyal').values()}

    cognetic_members_memberships = CogneticMembersMembership.objects.using('vista_loyal').values('membership_id', 'membership_personid', 'membership_expires').filter(
      Q(membership_personid__in=cognetic_core_persons.values_list('person_id', flat=True)) &
      ~Q(membership_deleted=1)
    )
    
    # create membership_expire_map
    membership_ids = []
    membership_expire_map = {}
    for detail in cognetic_members_memberships:
      membership_expire_map[detail['membership_personid']] = {
        'membership_id': detail['membership_id'],
        'membership_expires': detail['membership_expires'].strftime('%d-%m-%Y %H:%M:%S')
      }
      membership_ids.append(detail['membership_id'])

    cognetic_members_cards = CogneticMembersCard.objects.using('vista_loyal').values('card_membershipid', 'card_cardnumber', 'card_expires').filter(
      card_membershipid__in=membership_ids
    ).order_by('card_expires')
    
    # create member_card_number_map, member_card_expire_map
    member_card_number_map = {}
    member_card_expire_map = {}
    for detail in cognetic_members_cards:
      try:
        member_card_number_map[detail['card_membershipid']].append(detail['card_cardnumber'])
        member_card_expire_map[detail['card_membershipid']].append(detail['card_expires'].strftime('%d-%m-%Y %H:%M:%S'))
      except:
        member_card_number_map[detail['card_membershipid']] = [detail['card_cardnumber']]
        member_card_expire_map[detail['card_membershipid']] = [detail['card_expires'].strftime('%d-%m-%Y %H:%M:%S')]
    
    for cognetic_core_person in cognetic_core_persons:
      try:
        cognetic_core_person['person_clubid'] = cognetic_members_club_name_map[cognetic_core_person['person_clubid']]
      except:
        cognetic_core_person['person_clubid'] = None
      try:
        cognetic_core_person['membership_id'] = membership_expire_map[cognetic_core_person['person_id']]['membership_id']
      except:
        cognetic_core_person['membership_id'] = None
      try:
        cognetic_core_person['membership_expires'] = membership_expire_map[cognetic_core_person['person_id']]['membership_expires']
      except:
        cognetic_core_person['membership_expires'] = None
      try:
        for i in range(len(member_card_number_map[cognetic_core_person['membership_id']])):
          try:
            cognetic_core_person['card_details'].append(
              member_card_number_map[cognetic_core_person['membership_id']][i] + 
              ' | ' +  
              member_card_expire_map[cognetic_core_person['membership_id']][i])
          except:
            cognetic_core_person['card_details'] = [
              member_card_number_map[cognetic_core_person['membership_id']][i] + 
              ' | ' +  
              member_card_expire_map[cognetic_core_person['membership_id']][i]
            ]
      except:
        cognetic_core_person['card_details'] = [None]
      
    context = { 'cognetic_core_persons': cognetic_core_persons }
    
    html = render_to_string('personal_member_detail_table.html', context)
    result = 'success'
  else:
    result = 'Please fill in search key.'

  ip = get_client_ip(request)
  LogsSearchAccess.objects.create(ip=ip, username=request.user.username, branch_code='-', search_by='personal_member_detail', search_key=search_key)

  try:
    context = {
      'html'  : html,
      'result': result
    }
  except:
    context = {
      'html': '',
      'result': result
    }
  return JsonResponse(context)