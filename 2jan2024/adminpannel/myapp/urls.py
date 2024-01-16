from django.urls import path

from .views import (
	CounterCreateView,
	CounterUpdateView,
	CounterDeleteView,
	CounterDetailView,
	CounterListView )


urlpatterns=[
path(r'^create/count/$', CounterCreateView.as_view(), name='create-count'),
path(r'^update/count/(?P<pk>\d+)$', CounterUpdateView.as_view(), name='update-count'),
path(r'^delete/count/(?P<pk>\d+)$', CounterDeleteView.as_view(), name='delete-count'),
path(r'^detail/count/(?P<pk>\d+)$', CounterDetailView.as_view(), name='detail-count'),
path(r'^list/count/$', CounterListView.as_view(), name='list-count'),

]