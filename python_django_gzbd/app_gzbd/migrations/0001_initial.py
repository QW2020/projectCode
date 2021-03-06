# Generated by Django 2.0.5 on 2020-09-07 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Epidemic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('diagnosis', models.IntegerField(blank=True, null=True)),
                ('overseas_import', models.IntegerField(blank=True, null=True)),
                ('cure', models.IntegerField(blank=True, null=True)),
                ('death', models.IntegerField(blank=True, null=True)),
                ('therapy', models.IntegerField(blank=True, null=True)),
                ('observation', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
