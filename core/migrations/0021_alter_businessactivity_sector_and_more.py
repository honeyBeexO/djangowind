# Generated by Django 5.0.4 on 2024-07-24 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_businessactivity_sector_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessactivity',
            name='sector',
            field=models.ForeignKey(default='Autre', help_text="Domaine d'activité", null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.sector', verbose_name="Domaine d'activité"),
        ),
        migrations.AlterField(
            model_name='businessactivity',
            name='sub_sector',
            field=models.ForeignKey(default='Autre', help_text="Secteur d'activité", null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.subsector', verbose_name="Secteur d'activité"),
        ),
    ]
