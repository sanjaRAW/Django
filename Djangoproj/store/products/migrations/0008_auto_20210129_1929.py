# Generated by Django 3.1.5 on 2021-01-29 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_about_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumb', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('real_name', models.CharField(blank=True, max_length=32, null=True)),
                ('lastname', models.CharField(blank=True, max_length=256, null=True)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
                ('contacttype', models.CharField(choices=[('phone number', 'phone number'), ('email', 'email'), ('address', 'address'), ('name+surname', 'real_name')], max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
