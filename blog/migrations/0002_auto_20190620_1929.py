# Generated by Django 2.2.2 on 2019-06-20 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID for this post across whole site', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID for this comment across whole site', primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID for this post across whole site', primary_key=True, serialize=False)),
                ('bio', models.TextField(help_text='A brief biography of the user', max_length=1000)),
                ('blogger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
