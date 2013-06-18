from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from datetime import datetime
import cStringIO,gzip

def render(request,context):
  t = loader.get_template('amazing/index.html')
  c = RequestContext(request,context)
  
  zbuf = cStringIO.StringIO()
  zfile = gzip.GzipFile(mode='wb',compresslevel=6,fileobj=zbuf)
  zfile.write(t.render(c).encode('utf-8'))
  zfile.close()
  
  cc = zbuf.getvalue()
  response = HttpResponse(cc)
  response['Content-Encoding'] = 'gzip'
  response['Content-Length'] = str(len(cc))
 
  m = hashlib.md5()
  m.update(datetime.utcnow().isoformat())
  response['ETag'] = '"'+m.hexdigest()+'"'
  return response
  
@csrf_exempt
def validate_config(request):
  # Cheat a bit; any config is valid as we will default the size
  # if not specified
  return HttpResponse('{"valid":true}')
  
  
def sample(request):
  context = {"w":19,"h":25,"d":19}
  return render(request,context);
  
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
      
  return render(request,context)

