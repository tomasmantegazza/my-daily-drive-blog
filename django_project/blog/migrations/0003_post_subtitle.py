# Generated by Django 4.2.6 on 2023-10-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='Sin subtítulo', max_length=100),
        ),
    ]