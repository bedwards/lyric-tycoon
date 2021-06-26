# Generated by Django 3.2.4 on 2021-06-26 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(db_index=True, max_length=255)),
                ('book', models.CharField(max_length=255)),
                ('sentence', models.CharField(max_length=2048)),
            ],
        ),
    ]