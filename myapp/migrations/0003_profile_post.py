# Generated by Django 3.1.3 on 2021-04-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_image_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myid', models.IntegerField()),
                ('image', models.ImageField(upload_to='profile/')),
            ],
        ),
    ]