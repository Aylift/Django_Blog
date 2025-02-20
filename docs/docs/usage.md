# Usage

### User Features:

- **Register/Login**: Users can sign up and log in to access the blog.
- **Profile Management**: Users can update their profiles and upload avatars.
- **Create & Manage Posts**: Users can add, edit, and delete blog posts.
- **REST API Support**: The blog supports a REST API for programmatic interaction.

# Django Blog App - Usage Guide

## Introduction
The Django Blog App is a simple yet powerful blogging platform built with Django. This guide provides instructions on how to install, configure, and use the application.

## Prerequisites
Ensure you have the following installed before proceeding:
- Python (>= 3.8)
- Django (>= 4.0)
- PostgreSQL (or SQLite for development)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/django-blog.git
   cd django-blog
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
   Your blog should now be accessible at `http://127.0.0.1:8000/`.

## Configuration

### Environment Variables
Create a `.env` file to store sensitive data:
```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

### Updating Settings
Modify `settings.py` to reflect your environment:
```python
from decouple import config
DEBUG = config('DEBUG', default=True, cast=bool)
SECRET_KEY = config('SECRET_KEY')
```

## Usage

### Creating Blog Posts Inside The App
1. Log in to the app at `http://127.0.0.1:8000`.
2. Click on the "Add Article" button in the top-right.
3. Fill in the details and then click "Post"

### Creating Blog Posts Via Admin Panel
1. Log in to the Django admin panel at `http://127.0.0.1:8000/admin/`.
2. Navigate to the "Posts" section.
3. Click "Add Post" and fill in the necessary details.
4. Save the post to publish it.

### Viewing Posts
- Visit the homepage to see a list of published blog posts.
- Click on a post title to view its details.

## Deployment
For production deployment:
1. Configure a production database (PostgreSQL, MySQL, etc.).
2. Use a production-ready web server (Gunicorn, Nginx).
3. Set `DEBUG=False` and configure `ALLOWED_HOSTS`.
4. Collect static files:
   ```sh
   python manage.py collectstatic
   ```
5. Deploy to a hosting provider (Heroku, AWS, DigitalOcean, etc.).

## Troubleshooting
- **Migrations not applied?** Run `python manage.py migrate --run-syncdb`.
- **Static files not loading?** Ensure `STATIC_ROOT` is set and run `collectstatic`.
- **Database connection issues?** Verify `DATABASE_URL` in `.env`.

### API Usage:

The Django Blog App provides a REST API for managing blog content. Here are some useful endpoints:

- **Create a new article:**

  ```http
  POST /api/article/create/
  ```

  **Request Body:**

  ```json
  {
    "title": "My New Blog Post",
    "content": "This is the content of the blog post.",
    "author": 1
  }
  ```

- **Get all articles:**

  ```http
  GET /api/articles/
  ```

- **Retrieve a specific article:**

  ```http
  GET /api/article/{id}/
  ```

### Admin Access:

- Log in to the Django admin panel at:
  ```
  http://localhost:8000/admin/
  ```
- Use the superuser credentials created earlier to manage users and posts.

### Deployment Notes:

For production use, consider:

- Configuring a PostgreSQL database
- Setting up a WSGI server like Gunicorn
- Using environment variables for sensitive settings

Enjoy blogging with Django! 🚀
