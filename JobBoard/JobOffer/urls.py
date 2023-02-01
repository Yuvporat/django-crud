from django.urls import path

from . import views

urlpatterns = [
    path("jobs/",views.job_list_create_api_view),
    path("jobs/<int:pk>/",views.job_detail_api_view)

]