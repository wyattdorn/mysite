# Generated by Django 2.0 on 2018-01-16 01:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_class', models.CharField(choices=[('BN', 'Barbarian'), ('BD', 'Bard'), ('CC', 'Cleric'), ('DD', 'Druid'), ('FR', 'Fighter'), ('MK', 'Monk'), ('PN', 'Paladin'), ('RR', 'Ranger'), ('RE', 'Rogue'), ('SR', 'Sorcerer'), ('WK', 'Warlock'), ('WD', 'Wizard')], default='FR', max_length=2)),
                ('level', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('sub_class', models.CharField(max_length=200)),
                ('race', models.CharField(max_length=200)),
                ('is_alive', models.BooleanField(default=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charactermanager.Player'),
        ),
    ]
