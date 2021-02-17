# Generated by Django 3.1.5 on 2021-02-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(default='todoをここに書いてください。', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
        ),
    ]
