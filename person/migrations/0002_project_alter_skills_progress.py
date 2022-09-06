# Generated by Django 4.1 on 2022-09-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='static/image')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='skills',
            name='progress',
            field=models.IntegerField(),
        ),
    ]
