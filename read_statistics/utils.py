#!/user/bin/env python
# -*- coding:utf-8 -*-
import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum, ReadDetail


def read_statistics_once_read(request, obj):
    content_type = ContentType.objects.get_for_model(obj)
    key = "%s_%s_num" % (content_type.model, obj.pk)
    if not request.COOKIES.get(key):
        '''
        if ReadNum.objects.filter(content_type=content_type, object_id=obj.pk).count():
            # exist record
            readnum = ReadNum.objects.get(content_type=content_type, object_id=obj.pk)
        else:
            # not exist record
            readnum = ReadNum(content_type=content_type, object_id=obj.pk)
        '''
        # 以上注释代码可用以下代码代替
        readnum, is_read_num_created = ReadNum.objects.get_or_create(content_type=content_type, object_id=obj.pk)

        # 总阅读计数加1
        readnum.read_num += 1
        readnum.save()

        date = timezone.now().date()
        '''
        if ReadDetail.objects.filter(content_type=content_type, object_id=obj.pk, date=date):
            read_detail = ReadDetail.objects.get(content_type=content_type, object_id=obj.pk, date=date)
        else:
            read_detail = ReadDetail(content_type=content_type, object_id=obj.pk, date=date)
        '''
        read_detail, is_read_detail_created = ReadDetail.objects.get_or_create(content_type=content_type,
                                                                               object_id=obj.pk, date=date)
        # 当天阅读计数加1
        read_detail.read_num += 1
        read_detail.save()
    return key


def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return read_nums
