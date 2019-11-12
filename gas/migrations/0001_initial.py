# Generated by Django 2.2.4 on 2019-11-12 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=11)),
                ('unidade_conversao', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
            options={
                'db_table': 'gas',
            },
        ),
    ]
