import datetime
from django.db import models
import time

import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "djangoapp.djangoapp.settings"})

if __name__ == '__main__':
    curDataTime = datetime.datetime.now()
    print(curDataTime, type(curDataTime))
    curDataTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(curDataTime, type(curDataTime))
    curDataTime = datetime.datetime.now().isoformat()
    print(curDataTime, type(curDataTime))
    curDataTime = datetime.datetime.now().ctime()
    print(curDataTime, type(curDataTime))

    mywork_date = models.DateTimeField(verbose_name=u"提交时间")
    # print(mywork_date.auto_now)
    # print(mywork_date.auto_created)
    # print(mywork_date.auto_now_add)
    # print(mywork_date.verbose_name)

    web_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(web_time, type(web_time))

