from django.urls import path
from .views import HomeView, EntryView, CreateEntryView, DeleteEntryView, updateBlogEntryView

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry-detail'),
    path('create_entry/', CreateEntryView.as_view(), name="create_entry"),
    path('update/<int:pk>/', updateBlogEntryView, name='update_entry'),
    path('delete/<int:pk>/', DeleteEntryView, name='delete_entry')
]
