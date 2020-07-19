from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views

from rest_framework.decorators import api_view

from ticket_problem_management.functions import search_transaction_branch_by_ref_number, search_transaction_branch_by_name_email_phone
from api.functions import *

# Create your views here.
@api_view(['GET'])
def test_api(request):
  print(request.GET)
  t = {
    'a': request.GET.get('a'),
    'b': request.GET.get('b')
  }
  return Response(data=t)

@api_view(['GET'])
def get_booking_detail(request):
  branch_search_key = request.GET.get('branch_search_key', '')
  booking_search_by = request.GET.get('booking_search_by', '')
  booking_search_key = request.GET.get('booking_search_key', '')

  datas = {
    'detail'  : '',
    'msg'     : '',
    'complete': ''
  }
  complete = False
  if branch_search_key and booking_search_by and booking_search_key:
    if branch_search_key:
      branch_server, msg, complete = get_branch_server_ip(branch_search_key)

    if complete:
      if booking_search_by == "payment_ref_number":
        datas['detail'] = search_transaction_branch_by_ref_number(branch_server, booking_search_key)
      elif booking_search_by == "name/email/phone":
        datas['detail'] = search_transaction_branch_by_name_email_phone(branch_server, booking_search_key)
  
  try:
    datas['msg'] = msg
  except:
    datas['msg'] = 'Required parameters are not giving'
  datas['complete'] = complete
  return Response(data=datas)
