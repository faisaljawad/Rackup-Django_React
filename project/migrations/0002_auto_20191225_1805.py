# Generated by Django 3.0.1 on 2019-12-25 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile'),
        ),
        migrations.AddField(
            model_name='project',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FreeLancer', to='user.Profile'),
        ),
        migrations.AddField(
            model_name='project',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employeer', to='user.Profile'),
        ),
        migrations.AddField(
            model_name='project',
            name='skills_required',
            field=models.ManyToManyField(to='user.Skill'),
        ),
    ]