from rest_framework import serializers

from .models import Publisher, Book, Author, AuthorDetail


class PublisherSerializer(serializers.ModelSerializer):
	""" 出版社序列化"""

	class Meta:
		model = Publisher
		fields = ('name', 'addr', 'phone')


class AuthorDetailSerializer(serializers.SerializerMethodField):
	""" 作者详情序列化"""

	class Meta:
		model = AuthorDetail
		fields = ('city', 'email')


class AuthotSerializer(serializers.ModelSerializer):
	""" 作者序列化 """
	city = serializers.SerializerMethodField()

	def get_city(self, obj):
		return obj.author_detail.city
	email = serializers.SerializerMethodField()

	def get_email(self, obj):
		return obj.author_detail.email

	class Meta:
		model = Author
		fields = (['name', 'city', 'email'])


class BookSerializer(serializers.ModelSerializer):
	""" 书本保存序列化 """

	class Meta:
		model = Book
		fields = ('title', 'price')


class PublishSerializer(serializers.ModelSerializer):
	""" 创建出版社 """

	class Meta:
		model = Publisher
		fields = ('name', 'addr', 'phone')
