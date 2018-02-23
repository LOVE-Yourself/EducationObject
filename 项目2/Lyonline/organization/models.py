from django.db import models
from datetime import datetime
# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'城市名称')
    desc = models.CharField(max_length=200,verbose_name=u'城市描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        print('------>????',self.name)
        return self.name



class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')
    catgory = models.CharField(verbose_name=u'机构分类',default='pxjg',max_length=20,choices=(('pxjg','培训机构'),('gx','高校'),('gr','个人')))
    address = models.CharField(max_length=150,verbose_name=u'机构地址')
    fav_nums = models.IntegerField(default=0,verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='org/%Y/%m',max_length=200,verbose_name=u'封面图')
    click_nums = models.IntegerField(default=0,verbose_name=u'点击数')
    students = models.IntegerField(default=0,verbose_name=u'学习人数')
    courses_nums = models.IntegerField(default=0,verbose_name=u'课程数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    city = models.ForeignKey(CityDict,verbose_name=u'所在区域')

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name

    def org_teachers(self):
        org_teacher_list = self.teacher_set.all()
        return org_teacher_list

    def org_courses(self):
        org_course_list = self.course_set.all()
        return org_course_list

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name=u'所属机构')
    name = models.CharField(max_length=50,verbose_name=u'教师名')
    image = models.ImageField(upload_to='teacher/%Y/%m',max_length=200,verbose_name=u'教师头像',null=True,blank=True)
    work_years = models.IntegerField(verbose_name=u'工作年限',default=0)
    work_company = models.CharField(verbose_name=u'就职公司',max_length=50)
    work_position = models.CharField(max_length=50,verbose_name=u'公司职位')
    points = models.CharField(max_length=50,verbose_name=u'教学特点')
    fav_nums = models.IntegerField(default=0,verbose_name=u'收藏人数')
    click_nums = models.IntegerField(default=0,verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name


