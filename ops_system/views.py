from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext
from django.http import HttpResponseRedirect
from utils import *
import json
@login_required(login_url='/')
def index(request):
    if request.method=='POST':
	return 403
    dicts={'a_n':12,'r_n':12,'u_n':14}
    num=[40,38,2]
    info=json.dumps(num)
    res=json.dumps(dicts)
    sys_info_dict=get_system_info()
    return render_to_response('index.html', RequestContext(request,{'Dict': res,'info':info,'info_dict':sys_info_dict}))

def login_view(request):
    if request.user.is_authenticated():
	return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active:
	    login(request, user)
	    #return render_to_response('index.html',RequestContext(request))
	    return HttpResponseRedirect(reverse('index'))
        else:
	    print request.user.is_authenticated
	    return render_to_response('login.html',RequestContext(request,{'error':'Bad Username or Password'})) 
    else:
	return render_to_response('login.html',RequestContext(request,{'error':''}))

@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/')
def host_list(request):
    return render_to_response('host_list.html', RequestContext(request))