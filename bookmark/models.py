from django.db import models

# Create your models here.

# 데이터베이스를 sql 없이 다루려고 모델을 사용
# 우리가 데이터를 객체화해서 다루겠다
# 모델 = 테이블, 모델의 필드 = 테이블의 컬럼, 인스턴스 = 테이블의 레코드,
# 필드의 값 = 레코드의 컬럼 데이터값
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는 것
    # 1.데이터베이스의 컬럼 종류
    # 2.제약 사항 (글자 수)
    # 3. Form 의 종류
    # 4. Form 에서 제약 사항

    def __str__(self):
        return "이름 : "+self.site_name+", 주소 : "+self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

# 모델을 만들었다 => DB에 어떤 데이터를 어떤 혛태로 넣을지 결정
# 마이그레이션(migrate) => DB에 모델의 내용을 반영(테이블 생성)

