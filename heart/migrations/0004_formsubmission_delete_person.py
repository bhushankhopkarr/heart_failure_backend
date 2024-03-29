# Generated by Django 5.0.2 on 2024-02-28 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0003_person_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField()),
                ('time', models.CharField()),
                ('condition', models.CharField()),
                ('prediction', models.FloatField()),
                ('age', models.IntegerField()),
                ('highBP', models.IntegerField()),
                ('highChol', models.IntegerField()),
                ('smoker', models.IntegerField()),
                ('stroke', models.IntegerField()),
                ('diabetic', models.IntegerField()),
                ('diffWalk', models.IntegerField()),
                ('mentalHlth', models.IntegerField()),
                ('genHlth', models.IntegerField()),
                ('physHlth', models.IntegerField()),
                ('regEx', models.IntegerField()),
                ('bmi', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
