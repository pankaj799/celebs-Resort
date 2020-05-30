from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="index"),
    path('contactUs', ContactUs.as_view(), name="contact"),
    path('book', UserCreate.as_view(), name="book"),
    path('query', QueryCreate.as_view(), name="query"),
    path('adventure', Adventure.as_view(), name="adventure"),
    path('bars', BarsAndResorts.as_view(), name="bars"),
    # path('gallery', Gallery.as_view(), name="gallery"),
    path('stories', Stories.as_view(), name="stories"),
    path('celebration', Private.as_view(), name="celebration"),
    path('email', email, name="email"),
]
