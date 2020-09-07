from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import UpdateView,CreateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import (CharacterTemplate,CQuestion,
                     RCTemplateCQuestions,Slams,Slam,
                     SlamChart,Answer,Gifts,UserExtension)
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


@login_required
def test_ajax(request):
    return render(request,'testajax.html')
    

# Create your views here.

@login_required
def Questions(request):
    context={}
    return render(request,"addquestion.html",context)

@login_required
def base_t(request):
    context={"display_text":"This is base Slam book page"}
    return render(request,"base.html",context)



def main_t(request):
    return render(request,"main.html")



def profile_view(request,pk):
    user=User.objects.get(pk=pk)
    userext=UserExtension.objects.get(user=pk)
    context={"usr":user,"ext":userext}
    return render(request,"profile.html",context)


#CHARACTER TEMPLATE RELATED VIEWS
@login_required
def index_t(request):
    
    if request.method =='GET' and 'id' in request.GET:
        value_t=request.GET['id']
        q = CharacterTemplate.objects.get(pk=value_t)
            #context={"display_text":"This is base Slam book page"}
        context={'template':q.cq_template}
    else:
        context={}
    return render(request,"index.html",context)


class character_tlist(ListView):
    template_name="char_tlist.html"
    model=CharacterTemplate
    context_object_name="clist"
    def get_queryset(self):
        return CharacterTemplate.objects.filter(user=self.request.user)
    

class EditTemplateName(UpdateView):
    model=CharacterTemplate
    fields = ['cq_template']
    success_url =reverse_lazy('charactertlist')


class CreateTemplate(CreateView):
    model=CharacterTemplate
    fields = ['cq_template']
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse_lazy('charactertlist')

@login_required
@csrf_exempt
def delete_char_t(request):
    candidate = CharacterTemplate.objects.get(pk = int(request.POST['id']))
    candidate.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')


#QUESTION RELATED VIEWS
# @login_required
# def index_t(request):
    
#     if request.method =='GET' and 'id' in request.GET:
#         value_t=request.GET['id']
#         q = CharacterTemplate.objects.get(pk=value_t)
#             #context={"display_text":"This is base Slam book page"}
#         context={'template':q.cq_template}
#     else:
#         context={}
#     return render(request,"index.html",context)


class cquestion_tlist(ListView):
    template_name="cquestion_list.html"
    context_object_name="clist"
    model=CQuestion
    def get_queryset(self):
        # if 'pk' in self.kwargs:
        #     tid=self.kwargs['pk']
        if self.request.user==User(pk=1):
            queryset = { 
                    'normal': CQuestion.objects.filter(user=self.request.user)}
        else:
            queryset = {'admin': CQuestion.objects.filter(user=User(pk=1)), 
                    'normal': CQuestion.objects.filter(user=self.request.user)}
        
        return queryset
    

class EditCQuestion(UpdateView):
    model=CQuestion
    fields = ['cquestion']
    success_url =reverse_lazy('listcquestion')


class CreateCQuestion(CreateView):
    model=CQuestion
    fields = ['cquestion']
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self,**kwargs):
        
        if 'pk' in self.kwargs.keys() and 'slam' in  self.kwargs.keys():
            return reverse_lazy('listcquestion',kwargs=self.kwargs)
        elif 'pk' in self.kwargs.keys() and 'slam' not in self.kwargs.keys():
            return reverse_lazy('listcquestiont',kwargs=self.kwargs)
        else:
            return reverse_lazy('listcquestion')

@login_required
@csrf_exempt
def delete_cquestion_t(request):
    candidate = CQuestion.objects.get(pk = int(request.POST['id']))
    candidate.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')
    

#RCQT RELATED VIEWS

class RCQT_tlist(ListView):
    template_name="rcqt_list.html"
    context_object_name="clist"
    model=RCTemplateCQuestions
    def get_queryset(self):
        tid=self.kwargs['pk']
        return RCTemplateCQuestions.objects.filter(user=self.request.user,ctemplate=tid)
    

@login_required
@csrf_exempt
def delete_RCQT_t(request):
    candidate = RCTemplateCQuestions.objects.get(pk = int(request.POST['id']))
    candidate.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')


@login_required
@csrf_exempt
def add_RCQT_t(request):
    print(request.POST)
    c=request.POST.getlist('id[]',0)
    k=request.POST.getlist('pk',0)
    if c and k:
         for i in c:       
             RCTemplateCQuestions.objects.get_or_create(user=request.user,ctemplate=CharacterTemplate(pk=k[0]),cquestion=CQuestion(pk=i))
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')
  
    
#SLAMS RELATED VIEWS
class slams_list(ListView):
    template_name="slams_list.html"
    context_object_name="slamslist"
    model=Slams
    def get_queryset(self):
        return Slams.objects.filter(user=self.request.user)
    

class EditSlamsName(UpdateView):
    model=Slams
    fields = ['slam_name']
    success_url =reverse_lazy('listslams')


class CreateSlams(CreateView):
    model=Slams
    fields = ['slam_name']
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse_lazy('listslams')
    
@login_required
def generate_slam(request):
    # if request.method =='GET' and 'id' in request.GET:
    #     value_t=request.GET['id']
    #     q = CharacterTemplate.objects.get(pk=value_t)
    #         #context={"display_text":"This is base Slam book page"}
    #     context={'template':q}
    
    if request.method=='POST':
        sl=Slams(user=request.user,slam_name=request.POST['slamname'])
        sl.save()
        t=RCTemplateCQuestions.objects.filter(user=request.user,ctemplate=request.POST['templateid'])
        for e in t:
            Slam.objects.get_or_create(user=request.user,slam=sl,cquestion=e.cquestion,typ=1)           
        context={'generate':sl.pk}
        print(context)
    else:
        q = CharacterTemplate.objects.filter(user=request.user)
        context={'template':q}
    return render(request,'generateslam.html',context)

@login_required
@csrf_exempt
def delete_slams(request):
    candidate = Slams.objects.get(pk = int(request.POST['id']))
    candidate.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

#SLAM RELATED VIEWS-RELATION
    
class list_slam(ListView):
    template_name="list_slam.html"
    context_object_name="clist"
    model=Slam
    def get_queryset(self):
        tid=self.kwargs['pk']
        return Slam.objects.filter(user=self.request.user,slam=tid)
    

@login_required
@csrf_exempt
def delete_slam(request):
    candidate = Slam.objects.get(pk = int(request.POST['id']))
    candidate.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')


@login_required
@csrf_exempt
def add_slam(request):
    print(request.POST)
    c=request.POST.getlist('id[]',0)
    k=request.POST.getlist('pk',0)
    if c and k:
         for i in c:       
             Slam.objects.get_or_create(user=request.user,slam=Slams(pk=k[0]),cquestion=CQuestion(pk=i),typ=1)
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

#User
class list_user(ListView):
    template_name="list_user.html"
    context_object_name="clist"
    model=User
    
    
@login_required
@csrf_exempt
def send_slam(request):
    print(request.POST)
    c=request.POST.getlist('id[]',0)
    k=request.POST.getlist('pk',0)
    txt=request.POST.getlist('mess',0)
    if c and k:
         for i in c:
             SlamChart.objects.get_or_create(fr=request.user,to=User(pk=i),slam=Slams(pk=k[0]),mess=txt[0])
             
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

#INBOX SEND RESPONSES
class Inbox(ListView):
    template_name="inbox.html"
    context_object_name="clist"
    model=SlamChart
    def get_queryset(self):
        return SlamChart.objects.filter(to=self.request.user,is_to=True).order_by('-date_time')
    
class Sent(ListView):
    template_name="sent.html"
    context_object_name="clist"
    model=SlamChart
    def get_queryset(self):
        return SlamChart.objects.filter(fr=self.request.user,is_fr=True).order_by('-date_time')
    

class Response(ListView):
    template_name="response.html"
    context_object_name="clist"
    model=SlamChart
    def get_queryset(self):
        return SlamChart.objects.filter(fr=self.request.user,response=False).order_by('-date_time')
  


@login_required
@csrf_exempt
def delete_sent(request):
    candidate = SlamChart.objects.get(pk = int(request.POST['id']))
    if candidate.is_to==False:    
        candidate.delete()
    else:
        candidate.is_fr=False
        candidate.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

@login_required
@csrf_exempt
def delete_inbox(request):
    candidate = SlamChart.objects.get(pk = int(request.POST['id']))
    if candidate.is_fr==False:    
        candidate.delete()
    else:
        candidate.is_to=False
        candidate.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')



    
class view_slam(ListView):
    template_name="view_slam.html"
    context_object_name="clist"
    model=Slam
    def get_queryset(self):
        tid=self.kwargs['pk']
        k=SlamChart.objects.get(pk=tid)
        l=Slams(pk=k.slam)
        if not k.response:
            queryset = {'chart': SlamChart.objects.get(pk=tid), 
                    'slam':Slam.objects.filter(slam=l.pk) }
        else:
            queryset = {'chart': SlamChart.objects.get(pk=tid), 
                    'slam':Answer.objects.filter(slamchart=k.pk) }
            
        return queryset
    
    
class edit_slam(ListView):
    template_name="edit_slam.html"
    context_object_name="clist"
    model=Slam
    def get_queryset(self):
        tid=self.kwargs['pk']
        k=SlamChart.objects.get(pk=tid)
        l=Slams(pk=k.slam)
        k.isreadslam=True
        k.save()
        if not k.response:
            queryset = {'chart': SlamChart.objects.get(pk=tid), 
                    'slam':Slam.objects.filter(slam=l.pk) }
        else:
            queryset = {'chart': SlamChart.objects.get(pk=tid), 
                    'slam':Answer.objects.filter(slamchart=k.pk) }

        return queryset

@login_required
@csrf_exempt
def response_slam(request):
    print(request.POST)
    c=request.POST.getlist('id[]',0)
    s=request.POST.getlist('ans[]',0)
    k=request.POST.getlist('pk',0)
    txt=request.POST.getlist('mess',0)
    if not txt:
        txt=[]
        txt.append("")
    if c and k and s:
         for i in range(len(c)):
             print(c[i])
             sl=Slam.objects.get(pk=c[i])
             #sq=CQuestion(pk=sl.cquestion)
             #print(sq)
             sc=SlamChart.objects.get(pk=k[0])
             sc.response=True
             sc.rmess=txt[0]
             sc.save()
             Answer.objects.get_or_create(cquestion=sl.cquestion,slamchart=SlamChart(pk=k[0]),ans=s[i])
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

class view_response(ListView):
    template_name="view_response.html"
    context_object_name="clist"
    model=Answer
    def get_queryset(self):
        tid=self.kwargs['pk']
        k=SlamChart.objects.get(pk=tid)
        return Answer.objects.filter(slamchart=k.pk)
    
    
    
    
    
class Gift_view(ListView):
    template_name="gifts.html"
    model=Gifts
    context_object_name="glist"
    