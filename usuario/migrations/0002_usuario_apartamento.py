# Generated by Django 2.2.6 on 2019-11-04 02:38

from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    dependencies = [
        
        ('apartamento', '0002_auto_20191103_2315'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apartamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartamento.Apartamento'),
            preserve_default=False,
        ),
    ]