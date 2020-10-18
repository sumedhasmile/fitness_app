# Generated by Django 3.0.6 on 2020-10-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0003_auto_20201017_2155'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='food_details',
            name='category',
            field=models.CharField(choices=[['breakfast', 'breakfast'], ['lunch', 'lunch'], ['dinner', 'dinner'], ['Miscellaneous', 'Miscellaneous']], default=0, max_length=500),
            preserve_default=False,
        ),
    ]
