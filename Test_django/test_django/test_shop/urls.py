
from django.urls import re_path
from .apis import (PublisherApi, AddAuthor, AddAuthorDetail, AuthorDetail, BookCreate,
																	CreateBookAuthor)

urlpatterns = [
	re_path(r'^publish/?$', PublisherApi.as_view(), name="publisher"),
	re_path(r'^author/?$', AddAuthor.as_view(), name="author"),
	re_path(r'^authordatail/?$', AddAuthorDetail.as_view(), name='detail'),
	re_path(r'^getauthor/(?P<auid>[\w-]+)/?$', AuthorDetail.as_view(), name='detail_get'),
	re_path(r'^book/create/?$', BookCreate.as_view(), name='book_create'),
	re_path(r'^book/publish/create?$', CreateBookAuthor.as_view(), name='book_publish'),

]