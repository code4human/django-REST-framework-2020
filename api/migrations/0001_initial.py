# Generated by Django 3.0.5 on 2020-04-12 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('manu_num', models.AutoField(primary_key=True, serialize=False, verbose_name='제조업체번호 PK')),
                ('manu_name', models.CharField(max_length=50, verbose_name='제조업체명')),
                ('phone', models.CharField(max_length=20, verbose_name='전화번호')),
                ('location', models.CharField(max_length=100, verbose_name='주소')),
                ('supervisor', models.CharField(max_length=30, verbose_name='담당자')),
            ],
            options={
                'verbose_name': '제조업체',
                'verbose_name_plural': '제조업체',
                'ordering': ('-manu_num',),
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='이메일 주소')),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('phone', models.CharField(max_length=20, verbose_name='전화번호')),
                ('gender', models.CharField(choices=[('male', '남성'), ('female', '여성'), ('neither', '선택 안함')], default='male', max_length=10, verbose_name='성별')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='가입일')),
                ('location', models.CharField(max_length=100, verbose_name='주소')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='생년월일')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저',
                'ordering': ('-date_joined',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('many', models.IntegerField(verbose_name='주문수량')),
                ('destination', models.CharField(max_length=100, verbose_name='배송지')),
                ('date_ordered', models.DateTimeField(default=django.utils.timezone.now, verbose_name='주문일자')),
                ('message', models.CharField(blank=True, max_length=300, verbose_name='주문요청메시지')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문',
                'ordering': ('-date_ordered',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_num', models.AutoField(primary_key=True, serialize=False, verbose_name='글번호 PK')),
                ('title', models.CharField(max_length=100, verbose_name='글제목')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='글사진')),
                ('content', models.TextField(verbose_name='글내용')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성일자')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order', verbose_name='주문식별')),
            ],
            options={
                'verbose_name': '리뷰',
                'verbose_name_plural': '리뷰',
                'ordering': ('-review_num',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pro_num', models.AutoField(primary_key=True, serialize=False, verbose_name='상품번호 PK')),
                ('pro_name', models.CharField(max_length=100, verbose_name='상품명')),
                ('inventory', models.IntegerField(verbose_name='재고량')),
                ('price', models.IntegerField(verbose_name='단가')),
                ('supply_date', models.DateTimeField(verbose_name='공급일자')),
                ('supply_vol', models.IntegerField(verbose_name='공급량')),
                ('manu_num', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='api.Manufacturer', verbose_name='제조업체번호')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품',
                'ordering': ('-supply_date',),
            },
        ),
        migrations.AddField(
            model_name='order',
            name='pro_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product', verbose_name='상품이름'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MyUser', verbose_name='유저 id'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='pro_num',
            field=models.ManyToManyField(through='api.Order', to='api.Product', verbose_name='구매한 상품'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_num', models.AutoField(primary_key=True, serialize=False, verbose_name='배송번호 PK')),
                ('date_delivered', models.DateTimeField(default=django.utils.timezone.now, verbose_name='배송일자')),
                ('transport', models.IntegerField(verbose_name='운송장번호')),
                ('state', models.CharField(choices=[('preparing', '상품준비중'), ('departure', '배송출발'), ('in_progress', '배송중'), ('completed', '배송완료')], default='preparing', max_length=20, verbose_name='배송상태')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order', verbose_name='주문식별')),
            ],
            options={
                'verbose_name': '배송',
                'verbose_name_plural': '배송',
                'ordering': ('-transport',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together={('user_id', 'pro_num')},
        ),
    ]
