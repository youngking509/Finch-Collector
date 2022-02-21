# Generated by Django 4.0.2 on 2022-02-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('habitat', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('population', models.IntegerField()),
                ('threats', models.CharField(max_length=100)),
            ],
        ),
    ]