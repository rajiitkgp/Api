# Generated by Django 2.0.6 on 2018-06-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('crop', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('season', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=200)),
                ('production', models.CharField(max_length=200)),
                ('yields', models.CharField(max_length=200)),
                ('yield_units', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'area_production_yield',
                'managed': False,
            },
        ),
    ]
