# Generated by Django 4.2.6 on 2023-10-21 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('heading', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]
