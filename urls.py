from django.views.generic.simple import direct_to_template
from django.conf.urls import patterns, include, url
import os

urlpatterns = patterns('',
    (r'^$','amazing.views.index'),
    (r'^edition/?$','amazing.views.edition'),
    (r'^sample/?$','amazing.views.sample'),
    (r'^validate_config/?$','amazing.views.validate_config'),
    (r'^configure/?$','amazing.views.configure'),

    (r'^meta.json$',direct_to_template,{'template':'amazing/meta.json'}),
    (r'^icon.png$', 'django.views.static.serve',{'path': 'icon.png','document_root': os.path.dirname(__file__),}),
)
