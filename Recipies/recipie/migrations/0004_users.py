# Generated by Django 4.2.4 on 2023-08-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipie', '0003_recipie_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('otp', models.IntegerField()),
            ],
        ),
    ]
