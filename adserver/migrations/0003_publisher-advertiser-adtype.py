# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-04 20:47
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0002_image-upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified date')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(max_length=200, verbose_name='Slug')),
                ('has_image', models.BooleanField(default=True, verbose_name='Has image?')),
                ('image_width', models.PositiveIntegerField(blank=True, null=True)),
                ('image_height', models.PositiveIntegerField(blank=True, null=True)),
                ('has_text', models.BooleanField(default=True, verbose_name='Has text?')),
                ('max_text_length', models.PositiveIntegerField(blank=True, help_text='Max length does not include HTML tags', null=True)),
                ('allowed_html_tags', models.CharField(blank=True, default='a b strong i em code', help_text='Space separated list of allowed HTML tag names', max_length=255, verbose_name='Allowed HTML tags')),
                ('template', models.TextField(blank=True, help_text='Override the template for rendering this ad type', null=True, verbose_name='Ad template')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified date')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(max_length=200, verbose_name='Publisher Slug')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified date')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(max_length=200, verbose_name='Publisher Slug')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='secret',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, help_text='Sized according to the ad type', max_length=255, null=True, upload_to='images/%Y/%m/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='link',
            field=models.URLField(default='http://example.com', max_length=255, verbose_name='Link URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='text',
            field=models.TextField(blank=True, help_text='Different ad types have different text requirements', verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='adtype',
            name='publisher',
            field=models.ForeignKey(blank=True, help_text='For publisher-specific ad types', null=True, on_delete=django.db.models.deletion.CASCADE, to='adserver.Publisher'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='ad_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='adserver.AdType'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='advertiser',
            field=models.ForeignKey(blank=True, default=None, help_text='The advertiser for this campaign. A campaign without an advertiser is run by the ad network.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='campaigns', to='adserver.Advertiser'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='publishers',
            field=models.ManyToManyField(blank=True, help_text='Ads for this campaign are eligible for display on these publishers', related_name='flights', to='adserver.Publisher'),
        ),
    ]
