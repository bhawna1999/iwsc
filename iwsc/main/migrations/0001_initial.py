# Generated by Django 3.0.7 on 2021-01-24 12:10

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opportunity_type', models.CharField(max_length=50)),
                ('descrition', models.TextField()),
                ('eligibility', models.CharField(max_length=500)),
                ('deadline', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('contact_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('message', models.TextField()),
            ],
        ),
    ]