import pyodbc
from ticket_problem_management.models import *
from django.db import transaction

# dbconn = pyodbc.connect(
#   Driver='{SQL Server}',
#   Server='xxxxxxxx',
#   Database='xxxxxx',
#   UID='xxxxxxx',
#   PWD='xxxxxxxx'
# )

@transaction.atomic
def map_log_search_access(): 
  dbconn = pyodbc.connect(
    Driver='{SQL Server}',
    Server='xxxx',
    Database='xxxxx',
    UID='xxxx',
    PWD='xxxxxx'
  )
  new_log_search_access = []
  sql = "SELECT * FROM [TicketProblemManagement].[dbo].[logs_search_access] WHERE username != '{}'".format('pongpat.cho@majorcineplex.com')
  cursor = dbconn.execute(sql)

  for detail in cursor.fetchall():
    temp = LogsSearchAccess(
      ip          = detail.ip,
      username    = detail.username,
      branch_code = detail.branch_code,
      search_by   = "Reference number",
      search_key  = detail.payment_ref_id,
      created_at  = detail.created_at
    )
    new_log_search_access.append(temp)
  
  LogsSearchAccess.objects.bulk_create(new_log_search_access)

@transaction.atomic
def map_bank():
  dbconn = pyodbc.connect(
    Driver='{SQL Server}',
    Server='xxxx',
    Database='xxxxx',
    UID='xxxxx',
    PWD='xxxxx'
  )
  sql = "SELECT * FROM [TicketProblemManagement].[dbo].[bank]"
  cursor = dbconn.execute(sql)
  new_bank = []
  for detail in cursor.fetchall():
    temp_bank = Bank(
      name       = detail.name,
      is_active  = detail.is_active,
      created_at = detail.created_at,
      updated_at = detail.updated_at
    )
    new_bank.append(temp_bank)
  Bank.objects.bulk_create(new_bank)

@transaction.atomic
def get_new_bank_map_name_id():
  dbconn = pyodbc.connect(
    Driver='{SQL Server}',
    Server='xxxx',
    Database='TicketProblemManagement',
    UID='xxxxx',
    PWD='xxxxx'
  )
  sql = "SELECT * FROM [TicketProblemManagement_new].[dbo].[bank]"
  cursor = dbconn.execute(sql)
  new_bank_name_id = {}
  for detail in cursor.fetchall():
    new_bank_name_id[detail.name] = detail.id
  return new_bank_name_id

@transaction.atomic
def map_problem_management_history():
  dbconn = pyodbc.connect(
    Driver='{SQL Server}',
    Server='xxxxx',
    Database='xxxxxx',
    UID='xxxxx',
    PWD='xxxxx'
  )
  # this also map problem_management_history_refund_detail and bank
  sql = "SELECT * FROM [TicketProblemManagement].[dbo].[problem_management_history_refund_detail]"
  cursor = dbconn.execute(sql)
  problem_management_history_refund_details = {}
  for detail in cursor.fetchall():
    problem_management_history_refund_details[detail.history_id] = detail
  refund_history_ids = list(problem_management_history_refund_details.keys())
  
  sql = "SELECT * FROM [TicketProblemManagement].[dbo].[bank]"
  cursor = dbconn.execute(sql)
  old_bank_id_name = {}
  for detail in cursor.fetchall():
    old_bank_id_name[detail.id] = detail.name

  sql = "SELECT * FROM [TicketProblemManagement].[dbo].[problem_management_history] WHERE username != '{}'".format('pongpat.cho@majorcineplex.com')
  cursor = dbconn.execute(sql)

  new_bank_name_id = get_new_bank_map_name_id()
  new_problem_management_history = []
  new_problem_management_history_refund_detail = []
  for detail in cursor.fetchall():
    temp_history = ProblemManagementHistory(
      branch_code = detail.branch_code,
      ip          = detail.ip,
      username    = detail.username,
      reason      = detail.reason,
      solution    = detail.solution,
      search_by   = "Reference number",
      search_key  = detail.payment_ref_id,
      created_at  = detail.created_at,
      updated_at  = detail.updated_at
    )
    new_problem_management_history.append(temp_history)
  
    if detail.id in refund_history_ids:
      temp = problem_management_history_refund_details[detail.id]
      temp_history_detail = ProblemManagementHistoryRefundDetail(
        history_id      = temp_history.id,
        bank_id         = new_bank_name_id[old_bank_id_name[temp.bank_id]],
        bank_location   = temp.bank_location,
        account_number  = temp.account_number,
        account_name    = temp.account_name,
        refund_datetime = temp.refund_datetime,
        created_at      = temp.created_at,
        updated_at      = temp.updated_at
      )
      new_problem_management_history_refund_detail.append(temp_history_detail)
  
  ProblemManagementHistory.objects.bulk_create(new_problem_management_history)
  ProblemManagementHistoryRefundDetail.objects.bulk_create(new_problem_management_history_refund_detail)

def map_data():
  print("map_log_search_access")
  map_log_search_access()
  print("map_bank")
  map_bank()
  print("map_problem_management_history")
  map_problem_management_history()
  print("======================================")