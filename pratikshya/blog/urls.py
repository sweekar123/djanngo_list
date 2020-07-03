from django.urls import path
from .views import (
	JournalCreateView,
	JournalDeleteView,
	JournalDetailView,
	JournalListView,
	JournalUpdateView,
	)


app_name='blog'
urlpatterns = [
  path('',JournalListView.as_view(),name='journal-list'),
  path('create',JournalCreateView.as_view(),name='journal-create'),
  path('<int:id>/',JournalDetailView.as_view(),name='journal-detail'),
  path('<int:id>/update/',JournalUpdateView.as_view(),name='journal-update'),
  path('<int:id>/delete/',JournalDeleteView.as_view(),name='journal-delete'),
] 

