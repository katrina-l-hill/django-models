# Lab 27: Django Models

## Overview

Build out a project with one model and wire up that model using Django Views.

## Feature Tasks

### Model

- create snack_tracker_project project
- create snacks app
- add snacks app to project
- create Snack model
  - make sure it extends from proper base class
  - add name as a CharField with maximum length of 64 characters.
  - add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
    - from django.contrib.auth import get_user_model
  - add description TextField
- add model to admin
- modify Snack model have user friendly display in admin
- create migrations and migrate data
- create a super user
- run development server
- add a few snacks via Admin panel
- create another user and more snacks via Admin panel
- confirm that snacks behave as expected with proper name, purchaser and description.

### Views for Snacks App

- Where to create these views?
  - Dig around and see if there’s a sensible spot.
  - HINT There is one correct place for your app’s views.
- create SnackListView
  - extend ListView
  - give a template of snack_list.html
  - associate Snack model
- update url patterns for project
  - empty path should include snacks.urls
- update snacks app urls
  - empty sub-path should be handled by SnackListView
    - Don’t forget to use as_view()
- add detail view
  - link snack_detail.html template
  - associate Snack model
- update app urlpatterns to handle detail view
  - account for primary key in url
  - path would look like localhost:8000/1/ to get to snack with id of 1

### Templates

- add templates folder in root of project
  - register templates folder in project settings TEMPLATES section
- create base.html ancestor template
  - add main html document
  - use Django Templating Language to allow child templates to insert content
- create snack_list.html template
  - extend base template
  - use Django Templating Language to display each snack’s name
- view home page (aka snack_list) and confirm snacks showing properly
- create snack_detail.html template
  - template should extend base
  - content should display snack’s name, description and purchaser
- add link in snack_list template to related detail page for each snack
- add a link back to Home (aka snack_list) page from detail page.

### Setup

1. Create a virtual environment --> python –m venv .venv
2. Activate the virtual environment --> source .venv/bin/activate (for Linux and MacOS); .\.venv\Scripts\activate (for Windows)
3. Install Django --> pip install django
4. Create and start a Django project --> django-admin startproject djangho_snack_tracker_project .
5. Set up migrations --> python manage.py migrate
6. Run development server --> python manage.py runserver
7. Create a Django app --> python manage.py startapp snacks
8. Need to complete 3 steps before making migrations: TUV --> (1) templates (folder with base.html), (2) urls (in snacks folder), and (3) views(in snacks folder)
9. Make and apply migrations --> python manage.py makemigrations snacks
10. Apply the migrations --> python manage.py runserver
11. Create a super user as the administator of the site --> python manage.py createsuperuser
# username: admin
# email address: admin@admin.com
# password: admin
12. Test that the TUV and migrations worked in the development server
13. Add /admin to the end of the local host url to log in with the admin credentials
14. Add /1 to the end of the local host to see the first item

### Tests

python manage.py test
