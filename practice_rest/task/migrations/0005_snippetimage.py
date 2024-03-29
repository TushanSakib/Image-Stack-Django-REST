# Generated by Django 4.2.6 on 2023-10-30 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_snippet_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='SnippetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/profile')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='task.snippet')),
            ],
        ),
    ]
