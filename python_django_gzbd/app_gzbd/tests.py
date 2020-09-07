from django.test import TestCase

# Create your tests here.

from app_gzbd.models import User;
import random,datetime;

def bd_test():
    # 插入数据
    user = User(user_name="qw" + str(random.randint(1, 10)), password="111",
                      create_date=datetime.datetime.now());
    user.save();

