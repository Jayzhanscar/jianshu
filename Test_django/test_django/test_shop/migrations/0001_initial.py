# Generated by Django 2.1.1 on 2018-08-31 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('publish_day', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_shop.Publisher'),
        ),
        migrations.AddField(
            model_name='author',
            name='author_detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='test_shop.AuthorDetail'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='test_shop.Book'),
        ),
    ]
