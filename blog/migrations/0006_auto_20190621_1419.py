# Generated by Django 2.2.2 on 2019-06-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190621_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogger',
            options={'ordering': ['user', 'bio']},
        ),
        migrations.RenameField(
            model_name='blogger',
            old_name='blogger',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='blogger',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
