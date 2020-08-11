# Generated by Django 3.0.7 on 2020-08-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_remove_userprofile_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('organiser', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='resumetemplate',
            old_name='resumetempate',
            new_name='resumetemplate',
        ),
    ]
