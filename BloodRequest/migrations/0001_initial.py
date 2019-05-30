# Generated by Django 2.2.1 on 2019-05-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=20)),
                ('primaryContact', models.IntegerField()),
                ('secondaryContact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('bloodGroup', models.CharField(max_length=3)),
                ('description', models.TextField()),
            ],
        ),
    ]