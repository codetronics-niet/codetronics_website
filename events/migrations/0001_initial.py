# Generated by Django 2.2.5 on 2019-09-10 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('student_name', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254)),
                ('mobile_number', models.IntegerField()),
                ('roll_no', models.IntegerField()),
                ('branch', models.CharField(choices=[('ECE', 'Electronics'), ('CSE', 'Computer Science'), ('IT', 'IT'), ('EN', 'Electrical'), ('ME', 'Mechanical'), ('CE', 'Civil'), ('BT', 'Biotech')], default='ECE', max_length=3)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
