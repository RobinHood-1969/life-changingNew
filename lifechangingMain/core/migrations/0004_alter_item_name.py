# Generated by Django 5.0.6 on 2024-06-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_t_donor_td_howtocontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(choices=[('select', 'Select'), ('shoes', 'Shoes'), ('clothes', 'Clothes'), ('food items', 'Food Items')], default='select', max_length=50),
        ),
    ]
