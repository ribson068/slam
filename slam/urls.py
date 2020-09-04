"""slam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from slambook.views import (test_ajax,Questions,base_t,index_t,
                            character_tlist,delete_char_t,EditTemplateName,
                            CreateTemplate,main_t,cquestion_tlist,
                            delete_cquestion_t,EditCQuestion,CreateCQuestion,
                            delete_RCQT_t,RCQT_tlist,add_RCQT_t,slams_list,
                            CreateSlams,EditSlamsName,delete_slams,
                            list_slam,delete_slam,add_slam,generate_slam,
                            list_user,send_slam,
                            Inbox,Sent,Response,delete_inbox,delete_sent
                            ,view_slam,edit_slam,response_slam,view_response
                            ,profile_view,Gift_view)

from usermanagement import urls
from django.contrib.auth.decorators import login_required


urlpatterns = [
     url(r'^test/', test_ajax,name='test'),
    url(r'^usermanagement/', include(urls)),
    url(r'^addquestion/', Questions),
    url(r'^admin/', admin.site.urls),
    url(r'^base/', base_t),
    url(r'^createslam/',index_t,name="createslam"),
    url(r'^$',main_t,name="index_t"),
    url(r'^(?P<pk>\d+)/profile$',profile_view,name="profile_name"),
    #Character Template
    url(r'^delete_char_t/', delete_char_t,name="delete_char_t"),
    url(r'^list/',login_required(character_tlist.as_view()),name="charactertlist"),
    url(r'^(?P<pk>\d+)/edittemplate$', login_required(EditTemplateName.as_view()),name="edittemplate"),
    url(r'^createtemplate/', login_required(CreateTemplate.as_view()),name="createtemplate"),
    #Character Questions
    url(r'^delete_cquestion/', delete_cquestion_t,name="delete_cquestion"),
    url(r'^cqlist/',login_required(cquestion_tlist.as_view()),name="listcquestion"),
    url(r'^(?P<pk>\d+)/cqlist$',login_required(cquestion_tlist.as_view()),name="listcquestiont"),
    url(r'^(?P<pk>\d+)/(?P<slam>\d+)/cqlist$',login_required(cquestion_tlist.as_view()),name="listcquestion"),
    url(r'^(?P<pk>\d+)/editcquestion$', login_required(EditCQuestion.as_view()),name="editcquestion"),
    url(r'^createcquestion/', login_required(CreateCQuestion.as_view()),name="createcquestion"),
    url(r'^(?P<pk>\d+)/(?P<slam>\d+)/createcquestion$',login_required(CreateCQuestion.as_view()),name="scquestion"),
    url(r'^(?P<pk>\d+)/createcquestion$',login_required(CreateCQuestion.as_view()),name="rcquestion"),
    #RCQT
    url(r'^delete_RCQT_t/', delete_RCQT_t,name="delete_rcqt_t"),
    url(r'^(?P<pk>\d+)/rcqt$',login_required(RCQT_tlist.as_view()),name="rcqt"),
    url(r'^add_RCQT_t/',add_RCQT_t,name="add_rcqt_t"),
    #SLAMS
    url(r'^delete_slams/', delete_slams,name="deleteslams"),
    url(r'^slamslist/',login_required(slams_list.as_view()),name="listslams"),
    url(r'^(?P<pk>\d+)/editslams$', login_required(EditSlamsName.as_view()),name="editslams"),
    url(r'^createslams/', login_required(CreateSlams.as_view()),name="createslams"),
    url(r'^generateslam/', generate_slam,name="generateslam"),
    #SLAM
    url(r'^deleteslam/', delete_slam,name="deleteslam"),
    url(r'^(?P<pk>\d+)/listslam$',login_required(list_slam.as_view()),name="listslam"),
    url(r'^addslam/',add_slam,name="addslam"),
    #USER
    url(r'^(?P<pk>\d+)/listuser$',login_required(list_user.as_view()),name="listuser"),
    url(r'^sendslam/',send_slam,name="sendslam"),
    
    #INBOX RESPONSE and SENT
    url(r'^inbox/',login_required(Inbox.as_view()),name="inbox"),
    url(r'^sent/',login_required(Sent.as_view()),name="sent"),
    url(r'^response/',login_required(Response.as_view()),name="response"),
    url(r'^deleteinbox/', delete_inbox,name="deleteinbox"),
    url(r'^deletesent/', delete_sent,name="deletesent"),
    url(r'^(?P<pk>\d+)/viewslam$',login_required(view_slam.as_view()),name="viewslam"),
    url(r'^(?P<pk>\d+)/editslam$',login_required(edit_slam.as_view()),name="editslam"),
    url(r'^responseslam/',response_slam,name="responseslam"),
    url(r'^(?P<pk>\d+)/viewresponse$',login_required(view_response.as_view()),name="viewresponse"),
    #Gifts
    url(r'^gifts/',login_required(Gift_view.as_view()),name="rajeevanil")
]
