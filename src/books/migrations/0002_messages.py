# Generated by Django 3.1.3 on 2021-03-08 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.book')),
                ('case_study', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('books.book',),
        ),
    ]
