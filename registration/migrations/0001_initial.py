# Generated by Django 2.2.7 on 2019-11-18 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('no_of_child', models.IntegerField()),
                ('no_of_adult', models.IntegerField()),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
            ],
        ),
    ]
