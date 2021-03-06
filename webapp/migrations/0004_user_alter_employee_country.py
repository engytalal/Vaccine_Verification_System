# Generated by Django 4.0.5 on 2022-07-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_employee_delete_employees_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('Na_id', models.IntegerField()),
                ('country', models.CharField(blank=True, choices=[('Jaban', 'Jaban'), ('Egypt', 'Egypt')], max_length=50, null=True)),
                ('adress', models.IntegerField()),
                ('phone_num', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='country',
            field=models.CharField(blank=True, choices=[('Jaban', 'Jaban'), ('Egypt', 'Egypt')], max_length=50, null=True),
        ),
    ]
