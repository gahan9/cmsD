# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUSModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', parent_link=True, related_name='first_cms_contactusmodel', auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(verbose_name='Full Name', max_length=150)),
                ('last_name', models.CharField(verbose_name='Full Name', max_length=150)),
                ('email_address', models.EmailField(verbose_name='Email Address', max_length=200)),
                ('contact_number', models.IntegerField(verbose_name='Contact Number', max_length=10)),
                ('comment_box', models.TextField(verbose_name='Text Area', max_length=2000)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
