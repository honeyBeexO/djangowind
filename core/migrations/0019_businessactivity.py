# Generated by Django 5.0.4 on 2024-07-24 19:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_subsector_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when_to_start', models.DateField(default=datetime.date.today, null=True)),
                ('commercial_name', models.CharField(blank=True, max_length=256, null=True)),
                ('business_choice', models.CharField(choices=[('NON', 'Non'), ('OUI', 'Oui'), ('OUI', 'Oui')], default='Non', max_length=64)),
                ('is_micro', models.BooleanField(default=False)),
                ('sector', models.ForeignKey(default='Autre', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.sector')),
                ('sub_sector', models.ForeignKey(default='Autre', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.subsector')),
            ],
        ),
    ]
