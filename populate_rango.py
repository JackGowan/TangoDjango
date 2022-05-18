import os #What is os?
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
#Using the settings from the 'tango_with_django_project' folder?? I'm not sure...
#Its clearly a method from os
import django
django.setup()  #Calling the method Setup - I don't know what this does

#It is used if you run your Django app as standalone. It will load your settings and populate Django's application registry.
# You can read the detail on the Django documentation. As mentioned in the docs, django.setup() may only be called once.

from rango.models import Category, Page


# For an explanation of what is going on here, please refer to the TwD book.

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views': 3200},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views': 1040},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views': 502}]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
        'views': 7231},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
        'views': 12},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 98}]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
        'views': 50},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views': 100}]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}}

    # add_cat & add_page are functions (see below),
    #This For loop will add the above items into the database!!!

    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

#this is printing out the categories and pages
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

#adding a page to the database
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

#adding a category to the database
def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
#
# Code within a conditional if __name__ == '__main__' statement will therefore only be
# executed when the module is run as a standalone Python script. Importing the module will
# not run this code; any classes or functions will however be fully accessible to you.