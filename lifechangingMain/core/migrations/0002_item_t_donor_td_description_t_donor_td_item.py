# Generated by Django 5.0.6 on 2024-06-22 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('select', 'Select'), ('Shoes', 'Shoes'), ('clothes', 'Clothes'), ('food items', 'Food Items')], default='select', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='t_donor',
            name='td_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='t_donor',
            name='td_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.item'),
        ),
    ]
