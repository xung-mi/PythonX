# Generated by Django 4.1 on 2025-04-22 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0010_tag_alter_address_options_alter_author_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="email_address",
            field=models.EmailField(
                max_length=254, null=True, verbose_name="Email address"
            ),
        ),
    ]
