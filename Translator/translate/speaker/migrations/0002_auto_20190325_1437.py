# Generated by Django 2.1.7 on 2019-03-25 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('german', models.CharField(max_length=4096)),
                ('english', models.CharField(max_length=4096)),
            ],
        ),
        migrations.DeleteModel(
            name='dict_ge_en',
        ),
    ]
