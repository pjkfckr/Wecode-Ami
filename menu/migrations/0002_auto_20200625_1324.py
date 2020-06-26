# Generated by Django 3.0.7 on 2020-06-25 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytype',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.MenuCategory'),
        ),
        migrations.AlterField(
            model_name='categorytype',
            name='type_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.TypeName'),
        ),
        migrations.AlterField(
            model_name='menucategory',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.Category'),
        ),
        migrations.AlterField(
            model_name='menucategory',
            name='menu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.Menu'),
        ),
    ]
