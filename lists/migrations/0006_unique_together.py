# Generated by Django 2.2.6 on 2019-12-07 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_remove_duplicates'),
    ]

    operations = [
		migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('list', 'text')]),
        ),
    ]
