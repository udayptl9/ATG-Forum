# Generated by Django 3.0.3 on 2020-03-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_privacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='privacy',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=20),
        ),
    ]
