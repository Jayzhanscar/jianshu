from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Publisher, AuthorDetail, Author, Book
from .servalizers import PublisherSerializer, AuthotSerializer, \
	AuthorDetailSerializer, BookSerializer,PublishSerializer

from .models import Publisher


class PublisherApi(APIView):
	""" 出版社 """

	def post(self, request, *args, **kwargs):
		serializer = PublisherSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		valid_data = serializer.validated_data
		obj = Publisher.objects.create(**valid_data)
		obj.save()
		return Response(data=obj.uuid, status=status.HTTP_200_OK)


class AddAuthor(APIView):
	""" 添加作者 """

	def post(self, request, *args, **kwargs):
		serializer = AuthotSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		vaild_data = serializer.validated_data
		print(vaild_data, request.data.get('author_detail'))
		author_detail = AuthorDetail.objects.filter(id=request.data.get('author_detail')).first()
		Author.objects.create(**vaild_data, author_detail=author_detail)
		return Response(data=vaild_data, status=status.HTTP_200_OK)


class AddAuthorDetail(APIView):
	""" 添加作者细节"""
	def post(self, request, *args, **kwargs):
		seri = AuthorDetailSerializer(data=request.data)
		return Response(data='ok', status=status.HTTP_200_OK)


class AuthorDetail(APIView):
	""" 查询作者的全部信息  ok"""

	def get(self, request, *args, **kwargs):
		uuid = kwargs.get('auid')
		queryset = Author.objects.filter(uuid=uuid).first()
		data = AuthotSerializer(queryset).data
		return Response(data=data, status=status.HTTP_200_OK)


class BookCreate(APIView):
	""" 创建书本 """

	def post(self, request, *args, **kwargs):
		""" title price ok"""

		pub = Publisher.objects.filter(uuid=request.data.get('puid')).first()
		serializer = BookSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		valid_data = serializer.validated_data
		Book.objects.create(**valid_data, publisher=pub)
		return Response(data='ok', status=status.HTTP_200_OK)


class CreateBookAuthor(APIView):
	""" 给书本添加作者 """

	def post(self, request, *args, **kwargs):
		buid = request.data.get('buid')
		auid = request.data.get('auid')
		author = Author.objects.filter(uuid=auid).first()
		book = Book.objects.filter(uuid=buid)[0]
		# import！ 对于多对多表的操作 使用add操作
		author.books.add(book)
		print(buid, auid)
		return Response(data='ok', status=status.HTTP_200_OK)









