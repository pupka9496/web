from django.db import models

class MsreplicationOptions(models.Model):
    optname = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    value = models.BooleanField()
    major_version = models.IntegerField()
    minor_version = models.IntegerField()
    revision = models.IntegerField()
    install_failures = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'MSreplication_options'


class NewAudits(models.Model):
    audit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    auditor = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    plant = models.ForeignKey('NewPlants', models.DO_NOTHING, blank=True, null=True)
    brief_description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    report = models.ForeignKey('NewReport', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'New_Audits'


class NewChat(models.Model):
    name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    plant = models.ForeignKey('NewPlants', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('NewUsers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'New_Chat'


class NewEvents(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    auditor = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    plant = models.ForeignKey('NewPlants', models.DO_NOTHING, blank=True, null=True)
    short_description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'New_Events'


class NewPlants(models.Model):
    name_of_plant = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    plant_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'New_Plants'


class NewReport(models.Model):
    date = models.DateField(blank=True, null=True)
    plant = models.ForeignKey(NewPlants, models.DO_NOTHING, blank=True, null=True)
    section = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    evaluation_category = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sub_item_number = models.IntegerField(blank=True, null=True)
    evaluation = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    responsible_for_evaluation = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    requirements_of_the_roadmap = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    control_element = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    comments = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    list_of_events_for_the_year = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    performer = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    report_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'New_Report'


class NewUsers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    password = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    lastname = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    firstname = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    plant = models.ForeignKey(NewPlants, models.DO_NOTHING)
    role = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'New_Users'


class AuditsDev(models.Model):
    description_audit = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name_audit = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    number_of_plant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audits_dev'


class AuditsDevManagement(models.Model):
    audits_dev = models.OneToOneField(AuditsDev, models.DO_NOTHING, primary_key=True)  # The composite primary key (audits_dev_id, management_id) found, that is not supported. The first column is selected.
    management = models.ForeignKey('Management', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'audits_dev_management'
        unique_together = (('audits_dev', 'management'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EventDev(models.Model):
    date_metric = models.DateField(blank=True, null=True)
    description_metric = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_metric_audit = models.IntegerField(blank=True, null=True)
    location_metric = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name_event = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name_metric = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    time_metric = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_dev'


class Management(models.Model):
    id_audit = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    responsible = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'management'


class ManagementConfig1(models.Model):
    id_management = models.ForeignKey(Management, models.DO_NOTHING, db_column='id_management', blank=True, null=True)
    sub_name_section = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description_sub_section = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    estimation = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=4000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_events = models.ForeignKey(EventDev, models.DO_NOTHING, db_column='id_events', blank=True, null=True)
    executor = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'management_config_1'


class ManagementConfig2(models.Model):
    id_management = models.ForeignKey(Management, models.DO_NOTHING, db_column='id_management', blank=True, null=True)
    sub_name_section = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description_sub_section = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    estimation = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=4000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_events = models.ForeignKey(EventDev, models.DO_NOTHING, db_column='id_events', blank=True, null=True)
    executor = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'management_config_2'


class PlantsDev(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_of_plant = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_dev'


class RefreshtokenDev(models.Model):
    id = models.BigIntegerField(primary_key=True)
    expiry_date = models.DateTimeField()
    token = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    user = models.OneToOneField('UsersDev', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refreshtoken_dev'


class RolesDev(models.Model):
    name = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_dev'


class SptFallbackDb(models.Model):
    xserver_name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    xdttm_ins = models.DateTimeField()
    xdttm_last_ins_upd = models.DateTimeField()
    xfallback_dbid = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    dbid = models.SmallIntegerField()
    status = models.SmallIntegerField()
    version = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'spt_fallback_db'


class SptFallbackDev(models.Model):
    xserver_name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    xdttm_ins = models.DateTimeField()
    xdttm_last_ins_upd = models.DateTimeField()
    xfallback_low = models.IntegerField(blank=True, null=True)
    xfallback_drive = models.CharField(max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    low = models.IntegerField()
    high = models.IntegerField()
    status = models.SmallIntegerField()
    name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    phyname = models.CharField(max_length=127, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'spt_fallback_dev'


class SptFallbackUsg(models.Model):
    xserver_name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    xdttm_ins = models.DateTimeField()
    xdttm_last_ins_upd = models.DateTimeField()
    xfallback_vstart = models.IntegerField(blank=True, null=True)
    dbid = models.SmallIntegerField()
    segmap = models.IntegerField()
    lstart = models.IntegerField()
    sizepg = models.IntegerField()
    vstart = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spt_fallback_usg'


class SptMonitor(models.Model):
    lastrun = models.DateTimeField()
    cpu_busy = models.IntegerField()
    io_busy = models.IntegerField()
    idle = models.IntegerField()
    pack_received = models.IntegerField()
    pack_sent = models.IntegerField()
    connections = models.IntegerField()
    pack_errors = models.IntegerField()
    total_read = models.IntegerField()
    total_write = models.IntegerField()
    total_errors = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spt_monitor'


class SupplyChain(models.Model):
    id = models.BigIntegerField(primary_key=True)
    metric = models.IntegerField(blank=True, null=True)
    id_audit = models.IntegerField(blank=True, null=True)
    name_metric = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    responsible = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supply_chain'


class UserPlants(models.Model):
    user = models.OneToOneField('UsersDev', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, plants_id) found, that is not supported. The first column is selected.
    plants = models.ForeignKey(PlantsDev, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_plants'
        unique_together = (('user', 'plants'),)


class UserRoles(models.Model):
    user = models.OneToOneField('UsersDev', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, role_id) found, that is not supported. The first column is selected.
    role = models.ForeignKey(RolesDev, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_roles'
        unique_together = (('user', 'role'),)


class UsersDev(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    lastname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    login = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    number_of_plant = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    password = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_dev'
