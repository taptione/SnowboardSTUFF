# Generated by Django 2.1.2 on 2018-11-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_expiredtoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Brand name')),
            ],
            options={
                'verbose_name': 'Brand',
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Category')),
                ('parent_category', models.ForeignKey(on_delete=None, to='store.Category', verbose_name='Parent category')),
            ],
            options={
                'verbose_name': 'Category',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Gender')),
            ],
            options={
                'verbose_name': 'Gender',
                'db_table': 'genders',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('is_main', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Image',
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mame', models.CharField(max_length=256, verbose_name='Item name')),
                ('quantity', models.CharField(max_length=4, verbose_name='Quantity')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('gender', models.ForeignKey(null=True, on_delete=None, related_name='gender_set', to='store.Gender', verbose_name='Gender')),
                ('image', models.ForeignKey(on_delete=None, related_name='image_set', to='store.Image', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Item',
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='ItemStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Item status')),
            ],
            options={
                'verbose_name': 'Item status',
                'db_table': 'item_statuses',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=32, verbose_name='Value')),
                ('unit', models.CharField(max_length=32, verbose_name='Units')),
            ],
            options={
                'verbose_name': 'Size',
                'db_table': 'sizes',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.ManyToManyField(null=True, related_name='size_set', to='store.Size', verbose_name='Size'),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.ForeignKey(on_delete=None, related_name='item_status_set', to='store.ItemStatus', verbose_name='Item status'),
        ),
    ]