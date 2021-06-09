# Generated by Django 2.2.1 on 2020-08-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=20)),
                ('country', models.CharField(choices=[('USA', 'USA'), ('Nepal', 'Nepal'), ('China', 'China')], max_length=50)),
            ],
        ),
    ]
