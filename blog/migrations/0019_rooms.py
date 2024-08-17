# Generated by Django 4.1.7 on 2023-06-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_signup_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(max_length=50)),
                ('bed', models.IntegerField(max_length=50)),
                ('bathroom', models.IntegerField(max_length=50)),
                ('details', models.TextField(max_length=300)),
                ('roomsleft', models.IntegerField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='picture')),
            ],
        ),
    ]