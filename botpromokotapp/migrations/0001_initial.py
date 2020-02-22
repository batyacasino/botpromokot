# Generated by Django 3.0 on 2020-02-05 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaigns',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Cupons',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('rating', models.FloatField()),
                ('goto_link', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=50)),
                ('discount', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.CharField(max_length=200)),
                ('promocode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botpromokotapp.Campaigns')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botpromokotapp.Categories')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botpromokotapp.Types')),
            ],
            options={
                'ordering': ['-rating'],
            },
        ),
    ]