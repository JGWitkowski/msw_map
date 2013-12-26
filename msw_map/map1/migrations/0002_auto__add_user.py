# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'map1_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('longtitude', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=6)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=6)),
        ))
        db.send_create_signal(u'map1', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'map1_user')


    models = {
        u'map1.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '6'}),
            'longtitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '6'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['map1']