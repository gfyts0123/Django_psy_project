# Generated by Django 2.2.4 on 2020-05-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="last_ip",
        ),
        migrations.RemoveField(
            model_name="user",
            name="last_login_date",
        ),
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name="地址"),
        ),
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name="头像绝对路径"),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_nickname",
            field=models.CharField(default="未命名", max_length=8, verbose_name="昵称"),
        ),
    ]
