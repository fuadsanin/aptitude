# Generated by Django 4.0 on 2022-04-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_candidates_reference_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidates',
            name='reference_id',
        ),
        migrations.AddField(
            model_name='candidates',
            name='reference',
            field=models.CharField(default='', max_length=100),
        ),
    ]