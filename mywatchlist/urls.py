from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_xml
from mywatchlist.views import show_json

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('mywatchlist/', show_mywatchlist, name='show_mywatchlist'),
    path('mywatchlist/xml/', show_xml, name='show_xml'),
    path('mywatchlist/json/', show_json, name='show_json'),
    path('mywatchlist/html/', show_mywatchlist, name='show_mywatchlist')
]