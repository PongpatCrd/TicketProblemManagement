from ticket_problem_management.models import *
from django.db.models import Q

import re

# cal similarity of data and given search_key  (data of one record)
def cal_similarity_with_search_key(data, search_key):
  one_line_data = re.sub("[\[\]\,\ ]", "", str(data)).lower()
  default_len = len(one_line_data)

  for word in search_key.split(' '):
    one_line_data = one_line_data.replace(word.lower(), '')
  new_len = len(one_line_data)

  similarity_rate = 1.0 - (new_len/default_len)
  return similarity_rate

def get_branch_server_ip(search_key):
  tbl_branchs = TblBranch.objects.using('ticket_sale').values('branch_fullname', 'branch_nickname', 'branchcodevista', 'branch_server').filter(
    ~Q(branch_server=None) &
    Q(branch_status=1) 
  )
  
  max_similarity = 0
  target_server_list = []
  for tbl_branch in tbl_branchs:
    text = tbl_branch['branch_fullname'] + tbl_branch['branch_nickname'] + tbl_branch['branchcodevista']
    cal_similarity = cal_similarity_with_search_key(text, search_key)

    if cal_similarity > max_similarity:
      max_similarity = cal_similarity
      target_server_list = []
      target_server_list.append(tbl_branch['branch_server'])
    elif cal_similarity == max_similarity:
      target_server_list.append(tbl_branch['branch_server'])
    
  detail = ''
  msg = ''
  complete = False
  if len(target_server_list) == 1:
    detail = target_server_list[0]
    msg = 'Success'
    complete = True
  elif len(target_server_list) > 1:
    msg = 'Found more than 1 branch relate to information given'
  elif len(target_server_list) == 0:
    msg = 'Not found server from infomation given'
  else:
    msg = 'Error while finding branch detail'

  return (detail, msg, complete)
