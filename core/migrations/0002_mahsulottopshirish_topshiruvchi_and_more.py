# Generated by Django 4.1.7 on 2023-03-06 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulottopshirish',
            name='topshiruvchi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.ishchilar', verbose_name='xizmatni yakunlvchi'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mahsulottopshirish',
            name='product_repaired',
            field=models.CharField(max_length=150, verbose_name="Maxsulotni ta'mirlash"),
        ),
    ]
