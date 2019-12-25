# Generated by Django 3.0.1 on 2019-12-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('bids_count', models.IntegerField()),
                ('validity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
