# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'biocore_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('blogsite', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('camping_in_2014', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('arrival_date', self.gf('django.db.models.fields.DateTimeField')(max_length=30, null=True)),
            ('first_meal_in_camp', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('departure_date', self.gf('django.db.models.fields.DateTimeField')(max_length=30, null=True)),
            ('available_for_setup', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('helping_with_setup', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('available_for_exedous', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('helping_with_exedous', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('dues_paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'biocore', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'biocore_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'biocore.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'biocore_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'biocore.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])

        # Adding model 'Restrictions'
        db.create_table(u'biocore_restrictions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['biocore.User'])),
            ('restriction', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'biocore', ['Restrictions'])

        # Adding model 'Meal'
        db.create_table(u'biocore_meal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_am', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('chef', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['biocore.User'], null=True)),
            ('kps_needed', self.gf('django.db.models.fields.IntegerField')()),
            ('sous_needed', self.gf('django.db.models.fields.IntegerField')()),
            ('courier_needed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('courier_description', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
        ))
        db.send_create_signal(u'biocore', ['Meal'])

        # Adding model 'MealSignup'
        db.create_table(u'biocore_mealsignup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['biocore.Meal'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['biocore.User'])),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'biocore', ['MealSignup'])

        # Adding model 'Travel'
        db.create_table(u'biocore_travel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default='Bay Area', max_length=20)),
            ('other_city', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('traveling_with_other_biolum', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_ride', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('looking_for_ride', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_room_for_stuff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('looking_for_stuff_sherpa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('stuff_description', self.gf('django.db.models.fields.CharField')(max_length=156)),
            ('primary_driver', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['biocore.User'])),
            ('parking_vehicle_in_camp', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('make_of_car', self.gf('django.db.models.fields.CharField')(max_length=24, blank=True)),
            ('type_of_car', self.gf('django.db.models.fields.CharField')(max_length=24, blank=True)),
            ('car_color', self.gf('django.db.models.fields.CharField')(max_length=24, blank=True)),
            ('other_type', self.gf('django.db.models.fields.CharField')(max_length=24, blank=True)),
            ('car_length_feet', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('car_width_feet', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'biocore', ['Travel'])

        # Adding model 'Sleep'
        db.create_table(u'biocore_sleep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sharing_space', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sharing_with', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('tent_width_feet', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('tent_length_feet', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'biocore', ['Sleep'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'biocore_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'biocore_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'biocore_user_user_permissions'))

        # Deleting model 'Restrictions'
        db.delete_table(u'biocore_restrictions')

        # Deleting model 'Meal'
        db.delete_table(u'biocore_meal')

        # Deleting model 'MealSignup'
        db.delete_table(u'biocore_mealsignup')

        # Deleting model 'Travel'
        db.delete_table(u'biocore_travel')

        # Deleting model 'Sleep'
        db.delete_table(u'biocore_sleep')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'biocore.meal': {
            'Meta': {'object_name': 'Meal'},
            'chef': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biocore.User']", 'null': 'True'}),
            'courier_description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'courier_needed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_am': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kps_needed': ('django.db.models.fields.IntegerField', [], {}),
            'sous_needed': ('django.db.models.fields.IntegerField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'biocore.mealsignup': {
            'Meta': {'object_name': 'MealSignup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biocore.Meal']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biocore.User']"})
        },
        u'biocore.restrictions': {
            'Meta': {'object_name': 'Restrictions'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restriction': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biocore.User']"})
        },
        u'biocore.sleep': {
            'Meta': {'object_name': 'Sleep'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sharing_space': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sharing_with': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'tent_length_feet': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'tent_width_feet': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'biocore.travel': {
            'Meta': {'object_name': 'Travel'},
            'car_color': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'car_length_feet': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'car_width_feet': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "'Bay Area'", 'max_length': '20'}),
            'has_ride': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_room_for_stuff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'looking_for_ride': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'looking_for_stuff_sherpa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'make_of_car': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'other_city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'other_type': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'parking_vehicle_in_camp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'primary_driver': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biocore.User']"}),
            'stuff_description': ('django.db.models.fields.CharField', [], {'max_length': '156'}),
            'traveling_with_other_biolum': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type_of_car': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'})
        },
        u'biocore.user': {
            'Meta': {'object_name': 'User'},
            'arrival_date': ('django.db.models.fields.DateTimeField', [], {'max_length': '30', 'null': 'True'}),
            'available_for_exedous': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'available_for_setup': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'blogsite': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'camping_in_2014': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'departure_date': ('django.db.models.fields.DateTimeField', [], {'max_length': '30', 'null': 'True'}),
            'dues_paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'first_meal_in_camp': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'helping_with_exedous': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'helping_with_setup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['biocore']