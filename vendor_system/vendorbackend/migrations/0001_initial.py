# Generated by Django 3.2.5 on 2021-07-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.IntegerField()),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('phone_number', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('availability', models.CharField(max_length=1000)),
                ('acceptance_score', models.IntegerField()),
                ('total_job_offers', models.IntegerField()),
                ('rating_score', models.IntegerField()),
                ('total_ratings', models.IntegerField()),
                ('fixed_cost', models.IntegerField()),
                ('distance_cost', models.CharField(max_length=1000)),
                ('size_cost', models.CharField(max_length=1000)),
            ],
        ),
    ]