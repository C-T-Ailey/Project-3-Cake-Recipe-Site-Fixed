# Generated by Django 4.0.5 on 2022-06-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_recipe_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]