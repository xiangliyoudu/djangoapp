# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AppCategory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    categorycode = models.CharField(db_column='categoryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parentid = models.BigIntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='creationTime', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.BigIntegerField(db_column='modifyBy', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='modifyDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'app_category'

    def __str__(self):
        return self.categoryname


class AppInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    softwarename = models.CharField(db_column='softwareName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apkname = models.CharField(db_column='APKName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supportrom = models.CharField(db_column='supportROM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    interfacelanguage = models.CharField(db_column='interfaceLanguage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    softwaresize = models.DecimalField(db_column='softwareSize', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.
    devid = models.BigIntegerField(db_column='devId', blank=True, null=True)  # Field name made lowercase.
    appinfo = models.CharField(db_column='appInfo', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    status = models.BigIntegerField(blank=True, null=True)
    onsaledate = models.DateTimeField(db_column='onSaleDate', blank=True, null=True)  # Field name made lowercase.
    offsaledate = models.DateTimeField(db_column='offSaleDate', blank=True, null=True)  # Field name made lowercase.
    flatformid = models.BigIntegerField(db_column='flatformId', blank=True, null=True)  # Field name made lowercase.
    categorylevel3 = models.BigIntegerField(db_column='categoryLevel3', blank=True, null=True)  # Field name made lowercase.
    downloads = models.BigIntegerField(blank=True, null=True)
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.BigIntegerField(db_column='modifyBy', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='modifyDate', blank=True, null=True)  # Field name made lowercase.
    categorylevel1 = models.BigIntegerField(db_column='categoryLevel1', blank=True, null=True)  # Field name made lowercase.
    categorylevel2 = models.BigIntegerField(db_column='categoryLevel2', blank=True, null=True)  # Field name made lowercase.
    logopicpath = models.CharField(db_column='logoPicPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    logolocpath = models.CharField(db_column='logoLocPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    versionid = models.BigIntegerField(db_column='versionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'app_info'

    def __str__(self):
        return self.softwarename

class AppPromotion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    appid = models.BigIntegerField(db_column='appId', blank=True, null=True)  # Field name made lowercase.
    adpicpath = models.CharField(db_column='adPicPath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    adpv = models.BigIntegerField(db_column='adPV', blank=True, null=True)  # Field name made lowercase.
    carouselposition = models.IntegerField(db_column='carouselPosition', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.BigIntegerField(db_column='modifyBy', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='modifyDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'app_promotion'


class AppVersion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    appid = models.BigIntegerField(db_column='appId', blank=True, null=True)  # Field name made lowercase.
    versionno = models.CharField(db_column='versionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    versioninfo = models.CharField(db_column='versionInfo', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    publishstatus = models.BigIntegerField(db_column='publishStatus', blank=True, null=True)  # Field name made lowercase.
    downloadlink = models.CharField(db_column='downloadLink', max_length=500, blank=True, null=True)  # Field name made lowercase.
    versionsize = models.DecimalField(db_column='versionSize', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.BigIntegerField(db_column='modifyBy', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='modifyDate', blank=True, null=True)  # Field name made lowercase.
    apklocpath = models.CharField(db_column='apkLocPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    apkfilename = models.CharField(db_column='apkFileName', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'app_version'

    def __str__(self):
        return self.versionno

class BackendUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    usercode = models.CharField(db_column='userCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usertype = models.BigIntegerField(db_column='userType', blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.BigIntegerField(db_column='modifyBy', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='modifyDate', blank=True, null=True)  # Field name made lowercase.
    userpassword = models.CharField(db_column='userPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'backend_user'

    def __str__(self):
        return self.username

class DataDictionary(models.Model):
    id = models.BigIntegerField(primary_key=True)
    typecode = models.CharField(db_column='typeCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typename = models.CharField(db_column='typeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valueid = models.BigIntegerField(db_column='valueId', blank=True, null=True)  # Field name made lowercase.
    valuename = models.CharField(db_column='valueName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.BigIntegerField(db_column='modifyBy', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='modifyDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_dictionary'

    def __str__(self):
        return self.typename


class DevUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    devcode = models.CharField(db_column='devCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devname = models.CharField(db_column='devName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devpassword = models.CharField(db_column='devPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devemail = models.CharField(db_column='devEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devinfo = models.CharField(db_column='devInfo', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.BigIntegerField(db_column='modifyBy', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='modifyDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dev_user'

    def __str__(self):
        return self.devname