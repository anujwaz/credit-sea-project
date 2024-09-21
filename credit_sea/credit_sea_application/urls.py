from django.urls import path
from credit_sea_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.create_applicant),
    path('user_dashboard', views.read_applicant),
    path('verifier', views.verifier),
    path('loan', views.loan)
]



urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)