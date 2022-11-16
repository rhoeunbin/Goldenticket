
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationid', models.CharField(max_length=20)),
                ('locationname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('relateurl', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=20)),
                ('lgt', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PlayDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playid', models.CharField(max_length=20)),
                ('playname', models.CharField(max_length=50)),
                ('genrename', models.CharField(max_length=20)),
                ('playstate', models.CharField(max_length=20)),
                ('playstdate', models.DateField()),
                ('playenddate', models.DateField()),
                ('poster', models.CharField(max_length=80)),
                ('locationname', models.CharField(max_length=30)),
                ('playcast', models.CharField(max_length=50, null=True)),
                ('runtime', models.CharField(max_length=10, null=True)),
                ('age', models.CharField(max_length=10, null=True)),
                ('locationid', models.CharField(max_length=20)),
                ('image1', models.CharField(max_length=80, null=True)),
                ('image2', models.CharField(max_length=80, null=True)),
                ('image3', models.CharField(max_length=80, null=True)),
                ('image4', models.CharField(max_length=80, null=True)),
                ('ticketprice', models.CharField(max_length=80, null=True)),
                ('summary', models.CharField(max_length=200, null=True)),
                ('guidance', models.CharField(max_length=50, null=True)),
                ('like_users', models.ManyToManyField(related_name='performance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
