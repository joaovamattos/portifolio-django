# Generated by Django 2.1.7 on 2019-04-17 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
