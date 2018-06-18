# Generated by Django 2.0.3 on 2018-06-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(choices=[('Laptop', 'Laptop'), ('Phone', 'Phone'), ('Watch', 'Watch'), ('Sippers', 'Sippers')], max_length=50)),
                ('value', models.IntegerField(default=0)),
                ('item_stock_status', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='ItemDetails',
            new_name='Buyer',
        ),
    ]