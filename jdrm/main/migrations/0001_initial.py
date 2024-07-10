# Generated by Django 5.0 on 2024-07-09 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditsDev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_audit', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('name_audit', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('number_of_plant', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'audits_dev',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255)),
                ('codename', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150, unique=True)),
                ('first_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150)),
                ('last_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150)),
                ('email', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('object_repr', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100)),
                ('model', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255)),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventDev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_metric', models.DateField(blank=True, null=True)),
                ('description_metric', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('id_metric_audit', models.IntegerField(blank=True, null=True)),
                ('location_metric', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('name_event', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('name_metric', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('time_metric', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'event_dev',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_audit', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=500, null=True)),
                ('responsible', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'management',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ManagementConfig1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name_section', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=500, null=True)),
                ('description_sub_section', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=1000, null=True)),
                ('estimation', models.IntegerField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=4000, null=True)),
                ('executor', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=250, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'management_config_1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ManagementConfig2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name_section', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=500, null=True)),
                ('description_sub_section', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=1000, null=True)),
                ('estimation', models.IntegerField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=4000, null=True)),
                ('executor', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=250, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'management_config_2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MsreplicationOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optname', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=128)),
                ('value', models.BooleanField()),
                ('major_version', models.IntegerField()),
                ('minor_version', models.IntegerField()),
                ('revision', models.IntegerField()),
                ('install_failures', models.IntegerField()),
            ],
            options={
                'db_table': 'MSreplication_options',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewAudits',
            fields=[
                ('audit_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('auditor', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('brief_description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('status', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50, null=True)),
            ],
            options={
                'db_table': 'New_Audits',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50, null=True)),
                ('message', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'New_Chat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewEvents',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('auditor', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('short_description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('status', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50, null=True)),
            ],
            options={
                'db_table': 'New_Events',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewPlants',
            fields=[
                ('name_of_plant', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('plant_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'New_Plants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewReport',
            fields=[
                ('date', models.DateField(blank=True, null=True)),
                ('section', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('evaluation_category', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('sub_item_number', models.IntegerField(blank=True, null=True)),
                ('evaluation', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('responsible_for_evaluation', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('requirements_of_the_roadmap', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('control_element', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('comments', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('list_of_events_for_the_year', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('performer', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('report_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'New_Report',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewUsers',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('login', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50)),
                ('password', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50)),
                ('lastname', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50)),
                ('firstname', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50)),
                ('role', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'New_Users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlantsDev',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name_of_plant', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
            ],
            options={
                'db_table': 'plants_dev',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RefreshtokenDev',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('expiry_date', models.DateTimeField()),
                ('token', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'refreshtoken_dev',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RolesDev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=20, null=True)),
            ],
            options={
                'db_table': 'roles_dev',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SptFallbackDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xserver_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=30)),
                ('xdttm_ins', models.DateTimeField()),
                ('xdttm_last_ins_upd', models.DateTimeField()),
                ('xfallback_dbid', models.SmallIntegerField(blank=True, null=True)),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=30)),
                ('dbid', models.SmallIntegerField()),
                ('status', models.SmallIntegerField()),
                ('version', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'spt_fallback_db',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SptFallbackDev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xserver_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=30)),
                ('xdttm_ins', models.DateTimeField()),
                ('xdttm_last_ins_upd', models.DateTimeField()),
                ('xfallback_low', models.IntegerField(blank=True, null=True)),
                ('xfallback_drive', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=2, null=True)),
                ('low', models.IntegerField()),
                ('high', models.IntegerField()),
                ('status', models.SmallIntegerField()),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=30)),
                ('phyname', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=127)),
            ],
            options={
                'db_table': 'spt_fallback_dev',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SptFallbackUsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xserver_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=30)),
                ('xdttm_ins', models.DateTimeField()),
                ('xdttm_last_ins_upd', models.DateTimeField()),
                ('xfallback_vstart', models.IntegerField(blank=True, null=True)),
                ('dbid', models.SmallIntegerField()),
                ('segmap', models.IntegerField()),
                ('lstart', models.IntegerField()),
                ('sizepg', models.IntegerField()),
                ('vstart', models.IntegerField()),
            ],
            options={
                'db_table': 'spt_fallback_usg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SptMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastrun', models.DateTimeField()),
                ('cpu_busy', models.IntegerField()),
                ('io_busy', models.IntegerField()),
                ('idle', models.IntegerField()),
                ('pack_received', models.IntegerField()),
                ('pack_sent', models.IntegerField()),
                ('connections', models.IntegerField()),
                ('pack_errors', models.IntegerField()),
                ('total_read', models.IntegerField()),
                ('total_write', models.IntegerField()),
                ('total_errors', models.IntegerField()),
            ],
            options={
                'db_table': 'spt_monitor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SupplyChain',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('metric', models.IntegerField(blank=True, null=True)),
                ('id_audit', models.IntegerField(blank=True, null=True)),
                ('name_metric', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=500, null=True)),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=500, null=True)),
                ('responsible', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'supply_chain',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersDev',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('login', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True, unique=True)),
                ('number_of_plant', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('password', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
            ],
            options={
                'db_table': 'users_dev',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuditsDevManagement',
            fields=[
                ('audits_dev', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.auditsdev')),
            ],
            options={
                'db_table': 'audits_dev_management',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserPlants',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.usersdev')),
            ],
            options={
                'db_table': 'user_plants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.usersdev')),
            ],
            options={
                'db_table': 'user_roles',
                'managed': False,
            },
        ),
    ]