# Generated by Django 4.2.4 on 2023-10-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timestamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unix', models.BigIntegerField()),
                ('utc', models.CharField(max_length=255)),
            ],
        ),
    ]
