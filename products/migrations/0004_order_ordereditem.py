# Generated by Django 3.1.3 on 2020-11-15 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AllProfile', '0001_initial'),
        ('products', '0003_auto_20201114_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=200, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='AllProfile.normalprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('in_terms_of', models.CharField(choices=[('Kg', 'Kg'), ('L', 'L'), ('Pack', 'Pack'), ('Piece', 'Piece'), ('Quarter', 'Quarter'), ('Square cm', 'Square cm'), ('Square m', 'Square m'), ('Unit', 'Unit'), ('cm', 'cm'), ('db', 'db'), ('dozen', 'dozen'), ('ft', 'ft'), ('gallon', 'gallon'), ('gm', 'gm'), ('inch', 'inch'), ('m', 'm'), ('mg', 'mg'), ('ml', 'ml'), ('mm', 'mm'), ('pound', 'pound'), ('square ft', 'square ft'), ('tone', 'tone'), ('watt', 'watt')], default='Kg', max_length=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
        ),
    ]
