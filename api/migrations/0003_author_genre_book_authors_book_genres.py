# Generated by Django 4.2.7 on 2023-11-14 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_language_publisher_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='api.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='api.genre'),
        ),
    ]
