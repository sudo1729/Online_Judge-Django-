# Generated by Django 3.2.4 on 2021-06-20 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Compiler', '0003_auto_20210620_0533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compiler',
            old_name='expectedOuput',
            new_name='expectedOutput',
        ),
    ]