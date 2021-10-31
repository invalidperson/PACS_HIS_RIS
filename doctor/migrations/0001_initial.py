# Generated by Django 3.2.8 on 2021-10-31 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Prescription_By_Doctort', to=settings.AUTH_USER_MODEL, verbose_name='Assigned Doctor')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Prescription_Of_Patient', to=settings.AUTH_USER_MODEL, verbose_name='Assigned Patient')),
            ],
        ),
    ]
