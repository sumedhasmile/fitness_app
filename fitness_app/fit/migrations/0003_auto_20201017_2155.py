# Generated by Django 3.0.6 on 2020-10-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0002_auto_20201016_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[['breakfast', 'breakfast'], ['lunch', 'lunch'], ['dinner', 'dinner'], ['Miscellaneous', 'Miscellaneous']], max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='food_details',
            name='calculate',
        ),
        migrations.RemoveField(
            model_name='food_details',
            name='calories',
        ),
        migrations.AddField(
            model_name='food_details',
            name='calorie',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='food_details',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]