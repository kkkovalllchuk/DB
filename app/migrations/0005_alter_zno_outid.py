# Generated by Django 4.2.7 on 2023-12-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_zno_outid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zno',
            name='OUTID',
            field=models.CharField(db_column='OUTID', editable=False, primary_key=True, serialize=False),
        ),
    ]
