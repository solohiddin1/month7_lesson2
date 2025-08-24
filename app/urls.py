from django.urls import path
from .views import *

urlpatterns = [
    path('movie/',MovieView.as_view()),
    path('detail/<int:pk>/',MovieDetailView.as_view()),
    path('year/<int:pk>/',MovieYear.as_view()),
    path('year/',MovieYear.as_view()),

    path('year_from_body/',MovieFromBody.as_view()),

    path('actor/',ActorView.as_view()),
    path('detail_actor/<int:pk>/',ActorDetailView.as_view()),
    # path('actor_year/<int:pk>/',ActorYear.as_view()),
    # path('actor_year/',ActorYear.as_view()),MovieFromBody

]