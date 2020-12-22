# Generated by Django 3.0.6 on 2020-05-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psygarden', '0003_auto_20200529_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='anonymity',
            field=models.CharField(choices=[('0', '0'), ('1', '1')], help_text='0不匿名，1匿名（私人花园都不匿名）', max_length=4, verbose_name='匿名'),
        ),
    ]