# Generated by Django 3.2.8 on 2022-04-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AWSVirtualMachine',
            fields=[
                ('account_id', models.CharField(max_length=30, verbose_name='Account ID')),
                ('instance_id', models.CharField(editable=False, max_length=30, primary_key=True, serialize=False, verbose_name='Instance ID')),
                ('image_name', models.CharField(max_length=30, verbose_name='Image Name')),
                ('region', models.CharField(max_length=30, verbose_name='Region')),
            ],
        ),
    ]
