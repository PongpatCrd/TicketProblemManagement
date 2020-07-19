from django.db import models
from django.utils.timezone import now

# Create your models here.
class TblBranch(models.Model):
  id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
  branch_id = models.CharField(db_column='Branch_ID', max_length=2)  # Field name made lowercase.
  complex_id = models.IntegerField(db_column='Complex_ID', blank=True, null=True)  # Field name made lowercase.
  complex_name = models.CharField(db_column='Complex_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
  complex_order = models.IntegerField(db_column='Complex_Order', blank=True, null=True)  # Field name made lowercase.
  branchcodevista = models.CharField(db_column='BranchCodeVista', max_length=5, blank=True, null=True)  # Field name made lowercase.
  branch_fullname = models.CharField(db_column='Branch_FullName', max_length=30)  # Field name made lowercase.
  branch_thainame = models.CharField(db_column='Branch_ThaiName', max_length=30, blank=True, null=True)  # Field name made lowercase.
  branch_nickname = models.CharField(db_column='Branch_NickName', max_length=3, blank=True, null=True)  # Field name made lowercase.
  branch_callname = models.CharField(db_column='Branch_CallName', max_length=100, blank=True, null=True)  # Field name made lowercase.
  branch_server = models.CharField(db_column='Branch_Server', max_length=25, blank=True, null=True)  # Field name made lowercase.
  branch_trans = models.CharField(db_column='Branch_Trans', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_group = models.IntegerField(db_column='Branch_Group', blank=True, null=True)  # Field name made lowercase.
  branch_program = models.CharField(db_column='Branch_Program', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_dbuser = models.CharField(db_column='Branch_DbUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_dbpass = models.CharField(db_column='Branch_DbPass', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_dbname = models.CharField(db_column='Branch_DbName', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_dbtype = models.SmallIntegerField(db_column='Branch_DbType', blank=True, null=True)  # Field name made lowercase.
  branch_notheatre = models.IntegerField(db_column='Branch_NoTheatre', blank=True, null=True)  # Field name made lowercase.
  branch_noseat = models.IntegerField(db_column='Branch_NoSeat', blank=True, null=True)  # Field name made lowercase.
  branch_nolane = models.IntegerField(db_column='Branch_NoLane', blank=True, null=True)  # Field name made lowercase.
  branch_noroom = models.IntegerField(db_column='Branch_NoRoom', blank=True, null=True)  # Field name made lowercase.
  branch_nobox = models.IntegerField(db_column='Branch_NoBox', blank=True, null=True)  # Field name made lowercase.
  branch_notable = models.IntegerField(db_column='Branch_NoTable', blank=True, null=True)  # Field name made lowercase.
  branch_noice = models.IntegerField(db_column='Branch_NoIce', blank=True, null=True)  # Field name made lowercase.
  branch_orderbox = models.IntegerField(db_column='Branch_OrderBox', blank=True, null=True)  # Field name made lowercase.
  branch_orderbow = models.IntegerField(db_column='Branch_OrderBow', blank=True, null=True)  # Field name made lowercase.
  branch_db = models.CharField(db_column='Branch_DB', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_performancelocation = models.CharField(db_column='Branch_PerformanceLocation', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_location = models.CharField(db_column='Branch_Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_zone = models.CharField(db_column='Branch_Zone', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_region = models.CharField(db_column='Branch_Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_conprice = models.CharField(db_column='Branch_ConPrice', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_ename = models.CharField(db_column='Branch_EName', max_length=25, blank=True, null=True)  # Field name made lowercase.
  branch_tname = models.CharField(db_column='Branch_TName', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_mjbname = models.CharField(db_column='Branch_MJBName', max_length=3, blank=True, null=True)  # Field name made lowercase.
  branch_nickconcert = models.CharField(db_column='Branch_NickConcert', max_length=6, blank=True, null=True)  # Field name made lowercase.
  branch_boxcompany = models.SmallIntegerField(db_column='Branch_BoxCompany', blank=True, null=True)  # Field name made lowercase.
  branch_ipbowl = models.CharField(db_column='Branch_IPBowl', max_length=15, blank=True, null=True)  # Field name made lowercase.
  branch_ipconc = models.CharField(db_column='Branch_IPConc', max_length=15, blank=True, null=True)  # Field name made lowercase.
  branch_ipbowluser = models.CharField(db_column='Branch_IPBowlUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_ipbowlpass = models.CharField(db_column='Branch_IPBowlPass', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_dbbowl = models.CharField(db_column='Branch_DBBowl', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_dbconc = models.CharField(db_column='Branch_DBConc', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_groupbow = models.SmallIntegerField(db_column='Branch_GroupBow', blank=True, null=True)  # Field name made lowercase.
  branch_status = models.SmallIntegerField(db_column='Branch_Status', blank=True, null=True)  # Field name made lowercase.
  branch_bowversion = models.CharField(db_column='Branch_BowVersion', max_length=15, blank=True, null=True)  # Field name made lowercase.
  branch_bowlink = models.CharField(db_column='Branch_BowLink', max_length=15, blank=True, null=True)  # Field name made lowercase.
  branch_locationmjc = models.CharField(db_column='Branch_LocationMJC', max_length=3, blank=True, null=True)  # Field name made lowercase.
  branch_open = models.CharField(db_column='Branch_Open', max_length=8, blank=True, null=True)  # Field name made lowercase.
  branch_close = models.CharField(db_column='Branch_Close', max_length=8, blank=True, null=True)  # Field name made lowercase.
  branch_openbow = models.CharField(db_column='Branch_OpenBow', max_length=8, blank=True, null=True)  # Field name made lowercase.
  branch_contributelocation = models.CharField(db_column='Branch_ContributeLocation', max_length=3, blank=True, null=True)  # Field name made lowercase.
  branch_ipbms = models.CharField(db_column='Branch_IPBMS', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branchivrstatus = models.CharField(db_column='BranchIVRStatus', max_length=10, blank=True, null=True)  # Field name made lowercase.
  con_email = models.CharField(db_column='Con_Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
  bow_status = models.SmallIntegerField(db_column='Bow_Status', blank=True, null=True)  # Field name made lowercase.
  directlineno = models.CharField(db_column='DirectLineNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
  directline_server = models.CharField(db_column='DirectLine_Server', max_length=50, blank=True, null=True)  # Field name made lowercase.
  branch_vistadate = models.CharField(db_column='Branch_VISTADate', max_length=8, blank=True, null=True)  # Field name made lowercase.
  bow_area = models.CharField(db_column='Bow_Area', max_length=10, blank=True, null=True)  # Field name made lowercase.
  branch_servername = models.CharField(db_column='Branch_ServerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
  kiosk_qty = models.SmallIntegerField(db_column='Kiosk_Qty', blank=True, null=True)  # Field name made lowercase.
  kiosk_std = models.SmallIntegerField(db_column='Kiosk_Std', blank=True, null=True)  # Field name made lowercase.
  kiosk_pro = models.SmallIntegerField(db_column='Kiosk_Pro', blank=True, null=True)  # Field name made lowercase.
  kiosk_photo = models.SmallIntegerField(db_column='Kiosk_Photo', blank=True, null=True)  # Field name made lowercase.
  branch_kiosksaleservername = models.CharField(db_column='Branch_KioskSaleServerName', max_length=50, blank=True, null=True)  # Field name made lowercase.

  class Meta:
    managed = False
    db_table = 'Tbl_Branch'
    unique_together = (('id', 'branch_id'),)

class LogsSearchAccess(models.Model):
  id             = models.AutoField(primary_key=True)
  ip             = models.CharField(max_length=20, blank=False, null=False)
  username       = models.CharField(max_length=50, blank=False, null=False)
  branch_code    = models.CharField(max_length=3, blank=False, null=False)
  search_by      = models.CharField(max_length=25, blank=False, null=False)
  search_key     = models.CharField(max_length=100, blank=False, null=False)
  created_at     = models.DateTimeField(default=now, editable=False)

  class Meta:
    db_table = "logs_search_access"
    index_together = [
      ['ip', 'created_at'],
    ]

class ProblemManagementHistory(models.Model):
  id             = models.AutoField(primary_key=True)
  branch_code    = models.CharField(max_length=3, blank=False, null=False)
  ip             = models.CharField(max_length=20, blank=False, null=False)
  username       = models.CharField(max_length=50, blank=False, null=False)
  reason         = models.CharField(max_length=100, blank=False, null=False)
  solution       = models.CharField(max_length=100, blank=False, null=False)
  search_by      = models.CharField(max_length=25, blank=False, null=False)
  search_key     = models.CharField(max_length=100, blank=False, null=False)
  created_at     = models.DateTimeField(default=now, editable=False)
  updated_at     = models.DateTimeField(auto_now=True)

  class Meta:
    db_table="problem_management_history"
    indexes = [
      models.Index(fields=['search_key']),
    ]
    index_together = [
      ['ip', 'created_at'], 
      ['ip', 'search_by', 'search_key', 'created_at'],
      ['search_by', 'search_key', 'created_at'],
    ]

class Bank(models.Model):
  id             = models.AutoField(primary_key=True)
  name           = models.CharField(max_length=15, blank=False, null=False)
  is_active      = models.BooleanField(default=True)
  created_at     = models.DateTimeField(default=now, editable=False)
  updated_at     = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = "bank"

    indexes = [
      models.Index(fields=['name'])
    ]

class ProblemManagementHistoryRefundDetail(models.Model):
  id              = models.AutoField(primary_key=True)
  history_id      = models.PositiveIntegerField(blank=False, null=False)
  bank_id         = models.PositiveIntegerField(blank=False, null=False)
  bank_location   = models.CharField(max_length=255, blank=False, null=False)
  account_number  = models.CharField(max_length=20, blank=False, null=False)
  account_name    = models.CharField(max_length=100, blank=False, null=False)
  refund_datetime = models.DateTimeField()
  created_at     = models.DateTimeField(default=now, editable=False)
  updated_at      = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = "problem_management_history_refund_detail"
    
    index_together = [
      ['account_name', 'account_number', 'created_at']
    ]



# vista_loyal
class CogneticCorePerson(models.Model):
    person_id = models.CharField(primary_key=True, max_length=100)
    person_firstname = models.CharField(db_column='person_firstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_lastname = models.CharField(db_column='person_lastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_email = models.CharField(max_length=129, blank=True, null=True)
    person_username = models.CharField(db_column='person_userName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_password = models.CharField(max_length=100, blank=True, null=True)
    person_startpage = models.CharField(db_column='person_startPage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_type = models.CharField(max_length=100, blank=True, null=True)
    person_status = models.CharField(max_length=100, blank=True, null=True)
    person_creationdate = models.DateTimeField(db_column='person_creationDate', blank=True, null=True)  # Field name made lowercase.
    person_deleted = models.IntegerField(blank=True, null=True)
    person_languagecode = models.CharField(max_length=20, blank=True, null=True)
    person_domainid = models.IntegerField(blank=True, null=True)
    person_clubid = models.IntegerField(blank=True, null=True)
    person_title = models.CharField(max_length=100, blank=True, null=True)
    person_donotwishtoreceiveemail = models.BooleanField(db_column='person_doNotWishToReceiveEmail', blank=True, null=True)  # Field name made lowercase.
    person_homephone = models.CharField(db_column='person_homePhone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_mobilephone = models.CharField(db_column='person_mobilePhone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_address = models.CharField(max_length=1000, blank=True, null=True)
    person_suburb = models.CharField(max_length=100, blank=True, null=True)
    person_town = models.CharField(max_length=100, blank=True, null=True)
    person_state = models.CharField(max_length=100, blank=True, null=True)
    person_postcode = models.CharField(max_length=100, blank=True, null=True)
    person_country = models.CharField(max_length=100, blank=True, null=True)
    person_gender = models.CharField(max_length=100, blank=True, null=True)
    person_preferredcomplexid = models.IntegerField(db_column='person_preferredComplexid', blank=True, null=True)  # Field name made lowercase.
    person_preferredgenreid = models.IntegerField(db_column='person_preferredGenreid', blank=True, null=True)  # Field name made lowercase.
    person_birthdaydate = models.CharField(db_column='person_birthdayDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_birthdaymonth = models.CharField(db_column='person_birthdayMonth', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_centuryofbirth = models.CharField(db_column='person_centuryOfBirth', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_yearofbirth = models.CharField(db_column='person_yearOfBirth', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_ageindaysatcreationdate = models.IntegerField(db_column='person_ageInDaysAtCreationDate', blank=True, null=True)  # Field name made lowercase.
    person_ageinyearsatcreationdate = models.IntegerField(db_column='person_ageInYearsAtCreationDate', blank=True, null=True)  # Field name made lowercase.
    person_agerangeid = models.IntegerField(db_column='person_ageRangeid', blank=True, null=True)  # Field name made lowercase.
    person_agesupplied = models.CharField(db_column='person_ageSupplied', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_staticgroupid = models.IntegerField(db_column='person_staticGroupid', blank=True, null=True)  # Field name made lowercase.
    person_externalid = models.CharField(max_length=100, blank=True, null=True)
    person_maritalstatus = models.CharField(db_column='person_maritalStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    person_anniversarydate = models.DateTimeField(db_column='person_anniversaryDate', blank=True, null=True)  # Field name made lowercase.
    person_faxphone = models.CharField(max_length=100, blank=True, null=True)
    person_agreecontact = models.BooleanField(db_column='person_agreeContact', blank=True, null=True)  # Field name made lowercase.
    person_wishtoreceiveemail = models.BooleanField(db_column='person_wishToReceiveEmail')  # Field name made lowercase.
    person_wishtoreceivemail = models.BooleanField(db_column='person_wishToReceiveMail', blank=True, null=True)  # Field name made lowercase.
    person_wishtoreceivephone = models.BooleanField(db_column='person_wishToReceivePhone', blank=True, null=True)  # Field name made lowercase.
    person_wishtoreceivefax = models.BooleanField(db_column='person_wishToReceiveFax', blank=True, null=True)  # Field name made lowercase.
    person_wishtoreceivesms = models.BooleanField(db_column='person_wishToReceiveSMS', blank=True, null=True)  # Field name made lowercase.
    person_wishcontactthirdparty = models.BooleanField(db_column='person_wishContactThirdParty', blank=True, null=True)  # Field name made lowercase.
    person_specialrequirements = models.CharField(db_column='person_specialRequirements', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_formatemail = models.CharField(db_column='person_formatEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_educationlevel = models.IntegerField(db_column='person_educationLevel', blank=True, null=True)  # Field name made lowercase.
    person_householdincome = models.IntegerField(db_column='person_householdIncome', blank=True, null=True)  # Field name made lowercase.
    person_householdmembers = models.IntegerField(db_column='person_householdMembers', blank=True, null=True)  # Field name made lowercase.
    person_lastchangedate = models.DateTimeField(db_column='person_lastChangeDate', blank=True, null=True)  # Field name made lowercase.
    person_middleinitial = models.CharField(db_column='person_middleInitial', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_bademail = models.BooleanField(db_column='person_badEmail', blank=True, null=True)  # Field name made lowercase.
    person_badmailaddress = models.BooleanField(db_column='person_badMailAddress', blank=True, null=True)  # Field name made lowercase.
    person_occupation = models.IntegerField(blank=True, null=True)
    person_pinnumber = models.CharField(db_column='person_pinNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    person_lockedfromkiosk = models.BooleanField(db_column='person_lockedFromKiosk', blank=True, null=True)  # Field name made lowercase.
    person_lockeduntilkioskdate = models.DateTimeField(db_column='person_lockedUntilKioskDate', blank=True, null=True)  # Field name made lowercase.
    person_workpostcode = models.CharField(db_column='person_workPostCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_nationalid = models.CharField(db_column='person_nationalId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_mailingfrequency = models.CharField(db_column='person_mailingFrequency', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_alternatefirstname = models.CharField(db_column='person_alternateFirstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_alternatelastname = models.CharField(db_column='person_alternateLastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_typeid = models.IntegerField(db_column='person_typeId', blank=True, null=True)  # Field name made lowercase.
    person_postaladdressreference = models.CharField(db_column='person_postalAddressReference', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_emailupper = models.CharField(db_column='person_emailUpper', max_length=129, blank=True, null=True)  # Field name made lowercase.
    person_usernameupper = models.CharField(db_column='person_userNameUpper', max_length=100, blank=True, null=True)  # Field name made lowercase.
    person_devicepushtoken = models.TextField(db_column='person_devicePushToken', blank=True, null=True)  # Field name made lowercase.
    person_devicepushplatform = models.SmallIntegerField(db_column='person_devicePushPlatform')  # Field name made lowercase.
    person_isanonymous = models.BooleanField(db_column='person_isAnonymous')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cognetic_core_person'


class CogneticMembersMembership(models.Model):
    membership_id = models.CharField(primary_key=True, max_length=100)
    membership_personid = models.CharField(max_length=100)
    membership_name = models.CharField(max_length=100, blank=True, null=True)
    membership_clubid = models.IntegerField(blank=True, null=True)
    membership_expires = models.DateTimeField(blank=True, null=True)
    membership_memberstatusid = models.IntegerField(db_column='membership_memberStatusid', blank=True, null=True)  # Field name made lowercase.
    membership_howheardaboutid = models.IntegerField(db_column='membership_howHeardAboutid', blank=True, null=True)  # Field name made lowercase.
    membership_accepttermsandconditions = models.CharField(db_column='membership_acceptTermsAndConditions', max_length=100, blank=True, null=True)  # Field name made lowercase.
    membership_followuprequired = models.BooleanField(db_column='membership_followUpRequired', blank=True, null=True)  # Field name made lowercase.
    membership_followupreason = models.CharField(db_column='membership_followUpReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    membership_activated = models.BooleanField(blank=True, null=True)
    membership_pickupcomplexid = models.IntegerField(db_column='membership_pickUpComplexid', blank=True, null=True)  # Field name made lowercase.
    membership_staticgroupid = models.IntegerField(db_column='membership_staticGroupid', blank=True, null=True)  # Field name made lowercase.
    membership_since = models.DateTimeField(blank=True, null=True)
    membership_levelid = models.ForeignKey('CogneticMembersLevel', models.DO_NOTHING, db_column='membership_levelid', blank=True, null=True)
    membership_creationdate = models.DateTimeField(db_column='membership_creationDate', blank=True, null=True)  # Field name made lowercase.
    membership_joinedcomplexid = models.IntegerField(db_column='membership_joinedComplexid', blank=True, null=True)  # Field name made lowercase.
    membership_extracteddate = models.DateTimeField(db_column='membership_extractedDate', blank=True, null=True)  # Field name made lowercase.
    membership_saleschannelactivated = models.CharField(db_column='membership_salesChannelActivated', max_length=100, blank=True, null=True)  # Field name made lowercase.
    membership_previousexpiry = models.DateTimeField(db_column='membership_previousExpiry', blank=True, null=True)  # Field name made lowercase.
    membership_transactionanniversarydate = models.DateTimeField(db_column='membership_transactionAnniversaryDate', blank=True, null=True)  # Field name made lowercase.
    membership_deleted = models.BooleanField(blank=True, null=True)
    membership_nounpaidbookinguntil = models.DateTimeField(db_column='membership_noUnpaidBookingUntil', blank=True, null=True)  # Field name made lowercase.
    membership_nounpaidbookinguntilprevious = models.DateTimeField(db_column='membership_noUnpaidBookingUntilPrevious', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cognetic_members_membership'
        unique_together = (('membership_id', 'membership_clubid'),)


class CogneticMembersBulkcard(models.Model):
    bulkcard_id = models.AutoField(db_column='bulkCard_id', primary_key=True)  # Field name made lowercase.
    bulkcard_name = models.CharField(db_column='bulkCard_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bulkcard_stockref = models.CharField(db_column='bulkCard_stockRef', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bulkcard_startcard = models.CharField(db_column='bulkCard_startCard', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bulkcard_endcard = models.CharField(db_column='bulkCard_endCard', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bulkcard_cardstyleid = models.IntegerField(db_column='bulkCard_cardStyleID', blank=True, null=True)  # Field name made lowercase.
    bulkcard_addmember = models.BooleanField(db_column='bulkCard_addMember', blank=True, null=True)  # Field name made lowercase.
    bulkcard_membername = models.CharField(db_column='bulkCard_memberName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bulkcard_memberstatusid = models.IntegerField(db_column='bulkCard_memberStatusID', blank=True, null=True)  # Field name made lowercase.
    bulkcard_memberexpire = models.CharField(db_column='bulkCard_memberExpire', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bulkcard_membercomplexid = models.IntegerField(db_column='bulkCard_memberComplexID', blank=True, null=True)  # Field name made lowercase.
    bulkcard_memberspecialrequest = models.CharField(db_column='bulkCard_memberSpecialRequest', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bulkcard_addpoints = models.BooleanField(db_column='bulkCard_addPoints', blank=True, null=True)  # Field name made lowercase.
    bulkcard_addrecognitions = models.BooleanField(db_column='bulkCard_addRecognitions', blank=True, null=True)  # Field name made lowercase.
    bulkcard_memberclubid = models.IntegerField(db_column='bulkCard_memberClubID', blank=True, null=True)  # Field name made lowercase.
    bulkcard_membershipactivated = models.BooleanField(db_column='bulkCard_membershipActivated', blank=True, null=True)  # Field name made lowercase.
    bulkcard_prefix = models.CharField(db_column='bulkCard_prefix', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bulkcard_createusernamepassword = models.BooleanField(db_column='bulkCard_createUsernamePassword', blank=True, null=True)  # Field name made lowercase.
    bulkcard_creationdate = models.DateTimeField(db_column='bulkCard_creationDate', blank=True, null=True)  # Field name made lowercase.
    bulkcard_cardbatchid = models.ForeignKey('CogneticMembersCardbatch', models.DO_NOTHING, db_column='bulkCard_cardBatchID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cognetic_members_bulkCard'


class CogneticMembersCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_membershipid = models.CharField(max_length=100, blank=True, null=True)
    card_membername = models.CharField(db_column='card_memberName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    card_code = models.CharField(max_length=1000, blank=True, null=True)
    card_barcode = models.CharField(db_column='card_barCode', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    card_cardnumber = models.CharField(db_column='card_cardNumber', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    card_cardbatchid = models.IntegerField(db_column='card_cardBatchid', blank=True, null=True)  # Field name made lowercase.
    card_cardstyleid = models.IntegerField(db_column='card_cardStyleid', blank=True, null=True)  # Field name made lowercase.
    card_status = models.CharField(max_length=100, blank=True, null=True)
    card_expires = models.DateTimeField(blank=True, null=True)
    card_pickupcomplexid = models.IntegerField(db_column='card_pickUpComplexid', blank=True, null=True)  # Field name made lowercase.
    card_sentdate = models.DateTimeField(db_column='card_SentDate', blank=True, null=True)  # Field name made lowercase.
    card_isgiftcard = models.BooleanField(db_column='card_isGiftCard', blank=True, null=True)  # Field name made lowercase.
    card_cardtypeid = models.ForeignKey('Tblcardtype', models.DO_NOTHING, db_column='card_cardTypeid', blank=True, null=True)  # Field name made lowercase.
    card_bulkcardid = models.ForeignKey('CogneticMembersBulkcard', models.DO_NOTHING, db_column='card_bulkCardid', blank=True, null=True)  # Field name made lowercase.
    card_batchsequencenumber = models.BigIntegerField(db_column='card_batchSequenceNumber', blank=True, null=True)  # Field name made lowercase.
    card_issuedcomplexid = models.IntegerField(db_column='card_issuedComplexId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cognetic_members_card'


class CogneticMembersClub(models.Model):
    club_id = models.IntegerField(primary_key=True)
    club_name = models.CharField(max_length=100, blank=True, null=True)
    club_allowmultiplecardspermembership = models.BooleanField(db_column='club_allowMultipleCardsPerMembership', blank=True, null=True)  # Field name made lowercase.
    club_allowmultiplememberships = models.BooleanField(db_column='club_allowMultipleMemberships', blank=True, null=True)  # Field name made lowercase.
    club_shortcode = models.CharField(db_column='club_shortCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    club_renewalperiod = models.CharField(db_column='club_renewalPeriod', max_length=100, blank=True, null=True)  # Field name made lowercase.
    club_renewalperiodunit = models.CharField(db_column='club_renewalPeriodUnit', max_length=100, blank=True, null=True)  # Field name made lowercase.
    club_headertextpageletid = models.IntegerField(db_column='club_headerTextPageletid', blank=True, null=True)  # Field name made lowercase.
    club_domainid = models.IntegerField(blank=True, null=True)
    club_namealtlang = models.CharField(db_column='club_nameAltLang', max_length=100, blank=True, null=True)  # Field name made lowercase.
    club_leveliddefault = models.IntegerField(db_column='club_levelidDefault', blank=True, null=True)  # Field name made lowercase.
    club_issuevirtualcards = models.BooleanField(db_column='club_issueVirtualCards', blank=True, null=True)  # Field name made lowercase.
    club_primarylanguagecode = models.CharField(db_column='club_primaryLanguageCode', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cognetic_members_club'


class Tblcardtype(models.Model):
    cardtype_id = models.IntegerField(db_column='cardType_id', primary_key=True)  # Field name made lowercase.
    cardtype_name = models.CharField(db_column='cardType_name', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCardType'


class CogneticMembersLevel(models.Model):
    level_id = models.AutoField(primary_key=True)
    level_name = models.CharField(max_length=50)
    level_description = models.CharField(max_length=255, blank=True, null=True)
    level_clubid = models.IntegerField(blank=True, null=True)
    level_group = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cognetic_members_level'

      
class CogneticMembersCardbatch(models.Model):
    cardbatch_id = models.AutoField(db_column='cardBatch_id', primary_key=True)  # Field name made lowercase.
    cardbatch_name = models.CharField(db_column='cardBatch_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cardbatch_stockreference = models.CharField(db_column='cardBatch_stockReference', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cardbatch_lowcardnumber = models.CharField(db_column='cardBatch_lowCardNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cardbatch_highcardnumber = models.CharField(db_column='cardBatch_highCardNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cardbatch_complexid = models.IntegerField(db_column='cardBatch_complexid', blank=True, null=True)  # Field name made lowercase.
    cardbatch_cardstyleid = models.ForeignKey('CogneticMembersCardstyle', models.DO_NOTHING, db_column='cardBatch_cardStyleid', blank=True, null=True)  # Field name made lowercase.
    cardbatch_lastcardnumber = models.CharField(db_column='cardBatch_lastCardNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cardbatch_prefix = models.CharField(db_column='cardBatch_prefix', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cardbatch_forbulkcards = models.BooleanField(db_column='cardBatch_forBulkCards', blank=True, null=True)  # Field name made lowercase.
    cardbatch_originallowcardnumber = models.CharField(db_column='cardBatch_originalLowCardNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cognetic_members_cardBatch'


class CogneticMembersCardstyle(models.Model):
    cardstyle_id = models.AutoField(db_column='cardStyle_id', primary_key=True)  # Field name made lowercase.
    cardstyle_name = models.CharField(db_column='cardStyle_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cardstyle_clubid = models.IntegerField(db_column='cardStyle_clubid', blank=True, null=True)  # Field name made lowercase.
    card_memberlevelid = models.IntegerField(db_column='card_memberLevelid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cognetic_members_cardStyle'