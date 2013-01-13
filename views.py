from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from datetime import datetime

def index(request):
  context = {}
  return render_to_response('amazing/index.html',context)
 

def render():
  context = {}
  response = render_to_response('amazing/index.html',context)
  m = hashlib.md5()
  m.update(datetime.utcnow().isoformat())
  response['etag'] = m.hexdigest()
  return response
  
@csrf_exempt
def validate_config(request):
  return HttpResponse('{"valid":true}')
  
  
def sample(request):
  return render()
  
def edition(request):
  return render()

