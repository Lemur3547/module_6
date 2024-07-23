# Generated by Django 4.2 on 2024-07-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_product_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category', 'price', 'name'], 'permissions': [('can_cancel_publication', 'Может отменять публикацию продукта'), ('can_edit_description', 'Может менять описание продукта'), ('can_edit_category', 'Может менять категорию продукта')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]