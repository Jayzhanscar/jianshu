from django.test import TestCase
from common.mongohelper import get_db
# Create your tests here.

if __name__ == '__main__':
     a = get_db()
     my = a.gg_search
     my.insert({"name": "zhangcvdvsdvsvsan", "age": 18})
     print(a)

