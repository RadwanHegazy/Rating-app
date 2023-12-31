# Generated by Django 4.0 on 2023-08-13 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('api', '0007_alter_star_product_alter_star_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
        migrations.AlterField(
            model_name='star',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterUniqueTogether(
            name='star',
            unique_together={('user', 'product')},
        ),
        migrations.AlterIndexTogether(
            name='star',
            index_together={('user', 'product')},
        ),
    ]
