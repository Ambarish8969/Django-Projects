# Generated by Django 4.2.4 on 2023-08-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
