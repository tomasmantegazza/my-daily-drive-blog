# Generated by Django 4.2.6 on 2023-10-12 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='', max_length=100),
        ),
    ]
