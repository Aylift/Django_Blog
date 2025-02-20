# Django Blog App Documentation

Welcome to the documentation for the Django Blog App! This application allows users to create, read, update, and delete blog posts. It also includes user authentication, a commenting system, and a responsive design to ensure accessibility on different devices.

## Features

- **User Authentication**: Supports user login, registration, and logout.
- **Blog Management**: Users can create, update, delete, and read blog posts.
- **Comment System**: Enables users to comment on blog posts.
- **Responsive Design**: Uses Bootstrap for a mobile-friendly UI.
- **Admin Panel**: Django’s built-in admin panel is configured to manage users and posts efficiently.

## Project Layout

```
mkdocs.yml    # Configuration file for MkDocs documentation.
docs/
    index.md  # Documentation homepage.
```

## Directory Structure

```
Django_Blog/
│   manage.py            # Django project management script
│   db.sqlite3           # SQLite database file (for development only)
│
├───API/                 # API app for handling blog-related API endpoints
│   │   admin.py        # Registers models in the Django admin panel
│   │   apps.py         # API app configuration
│   │   models.py       # Database models for the API
│   │   serializers.py  # Serializers for converting models to JSON
│   │   tests.py        # Unit tests for the API
│   │   urls.py         # URL routing for API endpoints
│   │   views.py        # API views handling business logic
│   │   __init__.py     # Marks directory as a Python package
│   ├───migrations/     # Database migration files
│   ├───templates/API/  # API-related templates
│   └───__pycache__/    # Compiled Python files
│
├───blog/               # Main blog app for handling blog content
│   │   admin.py        # Blog models registered in Django admin
│   │   apps.py         # Blog app configuration
│   │   models.py       # Database models for blog posts
│   │   tests.py        # Unit tests for the blog
│   │   urls.py         # URL routing for blog views
│   │   views.py        # Handles HTTP requests and rendering templates
│   │   __init__.py     # Marks directory as a Python package
│   ├───migrations/     # Database migrations for blog models
│   ├───static/blog/    # CSS, JS, and other static files
│   ├───templates/blog/ # HTML templates for rendering blog pages
│   └───__pycache__/    # Compiled Python files
│
├───blog_project/       # Main project folder (Django settings, URLs, WSGI)
│   │   asgi.py         # ASGI configuration for async support
│   │   settings.py     # Django project settings
│   │   urls.py         # Root URL configuration
│   │   wsgi.py         # WSGI configuration for deployment
│   │   __init__.py     # Marks directory as a Python package
│   └───__pycache__/    # Compiled Python files
│
├───media/              # Stores user-uploaded files (e.g., profile pictures)
│   └───profile_pics/   # Profile images uploaded by users
│
└───users/              # User authentication and profile management
    │   admin.py        # Registers user models in Django admin
    │   apps.py         # User app configuration
    │   forms.py        # User-related forms (registration, profile updates)
    │   models.py       # User models
    │   signals.py      # Signals for user model events
    │   tests.py        # Unit tests for user functionality
    │   views.py        # Handles user-related views (login, registration)
    │   __init__.py     # Marks directory as a Python package
    ├───migrations/     # Database migrations for user models
    ├───templates/users/# User-related HTML templates
    └───__pycache__/    # Compiled Python files
```

## Additional Notes
- **Remove `db.sqlite3` in production**: Use PostgreSQL or another robust database.
- **Environment Variables**: Store sensitive information like secret keys and database credentials in `.env` files.
- **API Documentation**: The API is structured with Django REST Framework and follows RESTful principles.
- **Deployment**: Use `gunicorn` and `nginx` for serving the Django application in production.

This structured overview provides a clearer understanding of the Django Blog App, its components, and how it operates.
