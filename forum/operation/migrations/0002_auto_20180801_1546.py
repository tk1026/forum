# Generated by Django 2.0 on 2018-08-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.IntegerField(blank=True, null=True, verbose_name='关系发起者')),
                ('to_user', models.IntegerField(blank=True, null=True, verbose_name='关系接受者')),
                ('rel_type', models.CharField(choices=[(1, '粉丝'), (2, '关注'), (3, '互相关注')], max_length=1, verbose_name='关系类型')),
            ],
            options={
                'verbose_name_plural': '用户关系',
                'verbose_name': '用户关系',
            },
        ),
        migrations.RemoveField(
            model_name='userfollowing',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserFollowing',
        ),
    ]
