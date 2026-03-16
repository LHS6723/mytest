from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)     # 제품명
    description = models.TextField()            # 설명
    price = models.IntegerField()               # 가격
    image=models.ImageField(upload_to="menu_images")

    class Meta:
        db_table = 'dish'   # MySQL 테이블 이름 지정

    def __str__(self):
        return self.name
