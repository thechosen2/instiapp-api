# Generated by Django 3.1.2 on 2021-07-18 11:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('category', models.CharField(max_length=30)),
                ('sub_category', models.CharField(blank=True, max_length=30)),
                ('sub_sub_category', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
