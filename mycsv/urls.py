from django.urls import path

# I need to import my  views
from .views import Home , Company_Upload , deleterow , printrow

# I'm setting the path urls for the views
urlpatterns = [

path('',Home,name='home'),

path('companyupload',Company_Upload,name='companyupload'),

path('deleterow',deleterow,name='deleterow'),

path('printrow',printrow,name='printrow'),
    
]
