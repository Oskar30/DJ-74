# Generated by Django 4.1.7 on 2023-08-02 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_tag_options_tag_articles_delete_scope'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
    ]
