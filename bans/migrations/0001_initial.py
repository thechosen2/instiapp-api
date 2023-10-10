# Generated by Django 3.2.16 on 2023-10-10 12:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0040_remove_userprofile_followed_communities'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSOBans',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('time_of_creation', models.DateTimeField(auto_now_add=True)),
                ('reason', models.CharField(choices=[('IDF', 'Unappropriate Comment'), ('Buy&Sell', 'Unappropriate Activity in Buy and Sell'), ('Graduated ', 'Passed out from Institute'), ('InstiBan', 'Banned by Insittute Authority')], max_length=30)),
                ('detailed_reason', models.TextField(blank=True)),
                ('duration_of_ban', models.CharField(choices=[('1 month', 'One Month'), ('3 months', 'Three Months'), ('6 months', 'Six Months'), ('12 months', 'Twelve Months'), ('Permanent', 'Permanent')], max_length=20)),
                ('banned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='banned_by', to='users.userprofile')),
                ('banned_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banned_user', to='users.userprofile')),
            ],
        ),
    ]
