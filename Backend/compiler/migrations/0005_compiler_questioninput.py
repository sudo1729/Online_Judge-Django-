# Generated by Django 3.2.4 on 2021-06-07 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0004_alter_compiler_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='compiler',
            name='questionInput',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]