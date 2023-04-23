# Generated by Django 4.1.7 on 2023-03-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commands', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('oneLine', models.TextField()),
                ('reviews', models.ManyToManyField(blank=True, null=True, to='core.review')),
            ],
        ),
    ]
