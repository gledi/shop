# Generated by Django 4.0.3 on 2022-04-02 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(limit_choices_to=models.Q(('is_manager', True)), null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.employee'),
        ),
    ]
