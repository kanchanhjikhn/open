# Generated by Django 4.2.5 on 2023-10-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Query',
        ),
    ]
