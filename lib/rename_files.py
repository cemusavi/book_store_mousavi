import os
from datetime import datetime


def splitter(pic_name):
    name = os.path.basename(pic_name)
    pre, ext = os.path.splitext(name)
    return ext


def file_name_profile(instance, pic_name):
    ext = splitter(pic_name)
    return "{}-{}{}".format(instance.username,
                            str(datetime.now()), ext)


def rename_profile(instance, pic_name):
    name = file_name_profile(instance, pic_name)
    return "accounts/profiles/{}/{}".format(instance.username, name)


def rename_product_pic(instance, pic_name):
    ext = splitter(pic_name)
    return "products/books_pictures/{}{}".format(instance.book.title, ext)
