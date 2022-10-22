# Generated by Django 4.1.2 on 2022-10-22 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=165)),
                ('slug', models.SlugField()),
                ('preparation_time', models.IntegerField()),
                ('preparation_time_unit', models.CharField(max_length=65)),
                ('servings', models.IntegerField()),
                ('servings_unit', models.CharField(max_length=65)),
                ('preparation_steps', models.TextField()),
                ('preparation_steps_is_html', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.category')),
            ],
        ),
    ]