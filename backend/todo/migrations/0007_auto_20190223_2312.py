# Generated by Django 2.0.9 on 2019-02-23 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20190223_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='dependencies',
            field=models.ManyToManyField(blank=True, to='todo.TodoItem'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='contexts',
            field=models.ManyToManyField(blank=True, to='todo.Context'),
        ),
    ]
