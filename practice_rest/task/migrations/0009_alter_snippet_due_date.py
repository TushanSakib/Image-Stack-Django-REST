# Generated by Django 4.2.6 on 2023-10-30 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_snippet_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
