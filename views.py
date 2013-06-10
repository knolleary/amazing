from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from datetime import datetime

def render(context):
  response = render_to_response('amazing/index.html',context)
  m = hashlib.md5()
  m.update(datetime.utcnow().isoformat())
  response['etag'] = m.hexdigest()
  return response
  
@csrf_exempt
def validate_config(request):
  # Cheat a bit; any config is valid as we will default the size
  # if not specified
  return HttpResponse('{"valid":true}')
  
  
def sample(request):
  context = {"w":19,"h":25,"d":19}
  return render(context);
  
def edition(request):
  # default to large - as that is what existing subscribers will expect
  context = {"w":19,"h":25,"d":19}
  if "size" in request.GET:
      if request.GET["size"] == "small":
          context = {"w":9,"h":12,"d":40}
      elif request.GET["size"] == "medium":
          context = {"w":13,"h":17,"d":27}
      elif request.GET["size"] == "large":
          context = {"w":19,"h":25,"d":19}
      
  return render(context)

