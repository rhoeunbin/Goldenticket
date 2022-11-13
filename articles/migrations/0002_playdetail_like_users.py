

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playdetail',
            name='like_users',
            field=models.ManyToManyField(related_name='performance', to=settings.AUTH_USER_MODEL),
        ),
    ]
