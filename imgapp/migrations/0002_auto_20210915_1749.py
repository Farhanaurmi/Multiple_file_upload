# Generated by Django 3.2.7 on 2021-09-15 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imgapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TweetFile',
            new_name='ImgFile',
        ),
        migrations.RenameModel(
            old_name='Tweets',
            new_name='Posts',
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
    ]
