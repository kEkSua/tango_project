import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_project.settings')
import django
django.setup()
from rango.models import Category, Page


def populate():
    # First, we will create lists of dictionaries containing the pages we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "https://docs.python.org/3/tutorial/",
         'views': 32},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         'views': 3},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/",
         'views': 12}]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.11/intro/tutorial0/",
         "views": 14},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         "views": 23},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         "views": 14}]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/",
         "views": 34},
        {"title": "Flask",
         "url": "http://flask.pocoo.org",
         "views": 12}]

    cats = {"Python": {"pages": python_pages, 'views': 128, 'likes': 64},
            "Django": {"pages": django_pages, 'views': 64, 'likes': 32},
            "Other Frameworks": {"pages": other_pages, 'views': 32, 'likes': 16}}

    # If you want to add more catergories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.

    for cat, cat_data in cats.items():
        category = add_category(cat, cat_data['views'], cat_data['likes'])
        for page in cat_data['pages']:
            add_page(category, page['title'], page['url'])

    # Print out the categories we have added.
    for category in Category.objects.all():
        for page in Page.objects.filter(category=category):
            print("- {0} - {1}".format(str(category), str(page)))


def add_page(category, title, url, views=0):
    page = Page.objects.get_or_create(category=category, title=title)[0]
    page.url = url
    page.views = views
    page.save()
    return page


def add_category(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes
    category.save()
    return category

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
