# Generated by Django 4.1.5 on 2023-05-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0005_auto_20200611_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('cover_image', models.ImageField(upload_to='book_covers')),
                ('image', models.ImageField(upload_to='images/')),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('description', models.TextField()),
            ],
        ),
    ]
