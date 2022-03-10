from django.urls import path

from lettings.views import lettings_index, letting

urlpatterns = [
    path('', lettings_index, name='lettings_index'),
    path('<int:letting_id>/', letting, name='letting'),
]
