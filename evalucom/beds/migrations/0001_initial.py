# Generated by Django 3.0.4 on 2020-04-01 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_1', models.CharField(max_length=100)),
                ('line_2', models.CharField(max_length=100)),
                ('line_3', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beds', models.IntegerField(default=0)),
                ('dementia_beds', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DummyHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dementia_beds', models.IntegerField(default=0)),
                ('normal_beds', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('provider', models.CharField(max_length=200)),
                ('local_authority', models.CharField(max_length=20)),
                ('no_beds', models.IntegerField(default=0)),
                ('vacant_beds', models.IntegerField()),
                ('closed', models.BooleanField(default=False)),
                ('vacancy_updated', models.DateField(verbose_name='last updated')),
                ('beds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beds.Bed')),
                ('full_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beds.Address')),
            ],
        ),
    ]