import xadmin
from .models import UserFavorrate,UserMessage,UserCourse,userAsk,CourseComments

class UserFavorrateAdmin(object):

    list_display = ['user', 'fav_id', 'fac_type','add_time']
    search_fields = ['user', 'fav_id', 'fac_type']
    list_filter = ['user', 'fav_id', 'fac_type','add_time']

class UserMessageAdmin(object):

    list_display = ['user', 'message', 'has_read','add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read','add_time']

class UserCourseAdmin(object):

    list_display = ['user', 'course','add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course','add_time']

class userAskAdmin(object):

    list_display = ['name', 'telphone','coure_name','add_time']
    search_fields = ['name', 'telphone','coure_name']
    list_filter = ['name', 'telphone','coure_name','add_time']

class CourseCommentsAdmin(object):

    list_display = ['user', 'course','comments','add_time']
    search_fields = ['user', 'course','comments']
    list_filter = ['user', 'course','comments','add_time']


xadmin.site.register(UserFavorrate, UserFavorrateAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(userAsk,userAskAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)