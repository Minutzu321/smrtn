# Generated by Django 3.2.5 on 2021-07-30 09:12

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210730_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executabil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.FileField(upload_to='programe/%d/%m/%Y/')),
                ('ora_data_upload', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='utilizator',
            name='acceptat',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='utilizator',
            name='cod_secret',
            field=models.UUIDField(default=uuid.UUID('523d33fe-5179-4ac5-9ab7-d3a07e9f8096')),
        ),
    ]