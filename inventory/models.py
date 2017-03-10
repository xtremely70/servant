from django.db import models

# Create your models here.

class Style(models.Model):
    """
    status field)
        1 : active
        -1 : inactive
    """
    # choices for site : 해당 스타일이 생산되는 공장
    YENTHE = 1
    BGGARMENT = 2
    SITE_CHOICES = (
        (YENTHE, 'yt'),
        (BGGARMENT, 'bg')
    )

    # choices for status : 스타일 상태
    ACTIVE = 1
    INACTIVE = 0
    DELETED = -1
    STATUS_CHOICES = (
        (ACTIVE, '정상'),
        (INACTIVE, '승인 필요'),
        (DELETED, '삭제됨')
    )

    style_no = models.CharField(max_length=20, unique=True, db_index=True)
    style_year = models.IntegerField()
    style_season = models.CharField(max_length=2, default='')
    order_qty = models.IntegerField(default=0)
    site = models.SmallIntegerField(
        choices=SITE_CHOICES,
        default=YENTHE
    )
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=INACTIVE
    )
    memo = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    saved_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.style_no

class Supplier(models.Model):
    # choices for status : 스타일 상태
    ACTIVE = 1
    INACTIVE = 0
    DELETED = -1
    STATUS_CHOICES = (
        (ACTIVE, '정상'),
        (INACTIVE, '승인 필요'),
        (DELETED, '삭제됨')
    )

    name = models.CharField(max_length=60, unique=True)
    memo = models.TextField(blank=True, default='')
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=INACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    saved_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    supplied_by = models.ForeignKey(
        'Supplier',
        on_delete=models.CASCADE
    )
    spec = models.CharField(max_length=64, default='', blank=True)
    unit = models.CharField(max_length=10, default='', blank=True)
    status = models.SmallIntegerField(default=0)
    memo = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    saved_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' (' + self.supplied_by.name + ')'

class Rawmaterial(models.Model):
    style = models.ForeignKey(
        'Style',
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE
    )
    qty = models.IntegerField(default=0)
    unit_price = models.IntegerField(default=0)
    ordered_at = models.DateField(null=True, blank=True)    # 주문일
    shipped_at = models.DateField(null=True, blank=True)    # 선적일
    stocked_at =  models.DateField(null=True, blank=True)   # 공장 입고일
    status = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    saved_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.style.style_no + ' - ' + self.item.name + \
            '(' + self.item.supplied_by.name + ')'
