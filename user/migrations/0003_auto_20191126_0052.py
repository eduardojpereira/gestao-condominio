# Generated by Django 2.2.6 on 2019-11-26 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191126_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apartamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartamento.Apartamento'),
        ),
    ]
