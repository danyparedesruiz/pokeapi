# Generated by Django 4.1.7 on 2023-02-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('naturaleza', models.CharField(max_length=100)),
                ('peso', models.IntegerField()),
                ('ataque', models.IntegerField()),
            ],
        ),
    ]
