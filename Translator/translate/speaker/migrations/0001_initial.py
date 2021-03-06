# Generated by Django 2.1.5 on 2019-01-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dict_ge_en',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_for_ge_phrase', models.CharField(help_text='Hash of english Word / Phrase Wortes / der Phrase', max_length=20)),
                ('key_for_en_phrase', models.CharField(help_text='Hash des deutschen Wortes / der Phrase', max_length=20)),
                ('ge_phrase', models.CharField(help_text='Deutsches Wort / Phrase', max_length=100)),
                ('en_phrase', models.CharField(help_text='English word / phrase', max_length=100)),
            ],
        ),
    ]
