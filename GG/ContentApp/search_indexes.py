"""
用于全文检索bolg
"""
import datetime
from haystack import indexes
from ContentApp.models import Blog


class BlogIndex(indexes.SearchIndex, indexes.Indexable):  # 类名必须为需要检索的Model_name+Index，这里需要检索Note，所以创建NoteIndex
    text = indexes.CharField(document=True, use_template=True)  # 创建一个text字段

    title = indexes.CharField(model_attr='title')  # 创建一个author字段

    def get_model(self):  # 重载get_model方法，必须要有！
         pass

    def index_queryset(self, using=None):
         pass