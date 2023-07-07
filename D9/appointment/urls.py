from django.urls import path, include

from .views import AppointmentView

urlpatterns = [
    path('', AppointmentView.as_view(), name='appointments'),
    #path('appointment/', include(('appointment.urls', 'appointment'), namespace='appointment')),
    #path('accounts/', include('allauth.urls')),
]
