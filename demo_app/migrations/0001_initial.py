# Generated by Django 4.1.4 on 2023-01-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srno', models.IntegerField()),
                ('ename', models.CharField(max_length=50)),
                ('empid', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('dep', models.CharField(max_length=50)),
            ],
        ),
    ]
