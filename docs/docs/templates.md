# Django Blog App - Templates Guide

## Introduction
Templates in Django define the structure and layout of the HTML pages. The Django Blog App uses templates to render pages for user authentication, profile management, blog articles, and API responses.

## Template Directory Structure
The templates are organized as follows:
```
project_root/
│── users/
│   ├── templates/
│   │   ├── users/
│   │   │   ├── register.html
│   │   │   ├── profile.html
│   │   │   ├── login.html
│   │   │   ├── logout.html
│── blog/
│   ├── templates/
│   │   ├── blog/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── article.html
│   │   │   ├── article_form.html
│   │   │   ├── delete_confirm.html
│   │   │   ├── about.html
│── API/
│   ├── templates/
│   │   ├── API/
│   │   │   ├── test-api.html
```

## Users App Templates

### `register.html`
- Displays the user registration form.
- Uses `{% crispy form %}` if Django Crispy Forms is installed.
- Includes messages for successful registration.

### `profile.html`
- Displays and allows users to update their profile.
- Includes profile picture upload functionality.

### `login.html`
- Provides a login form for users.
- Uses `{% csrf_token %}` for security.
- Redirects authenticated users to their profile.

### `logout.html`
- Displays a logout confirmation message.
- Provides a link to log back in.

## Blog App Templates

### `base.html`
- Defines a common structure for all pages.
- Includes navigation bar and footer.
- Uses `{% block content %}` to inject page-specific content.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}Django Blog{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'about' %}">About</a>
        <a href="{% url 'login' %}">Login</a>
        <a href="{% url 'logout' %}">Logout</a>
    </nav>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

### `home.html`
- Displays a list of articles.
- Uses a `for` loop to iterate through posts.
- Implements pagination.

### `article.html`
- Displays the details of a single article.
- Shows title, content, author, and date.

### `article_form.html`
- Used for creating and updating articles.
- Includes fields for title and content.
- Form submission handled via `{% csrf_token %}`.

### `delete_confirm.html`
- Asks users to confirm before deleting an article.
- Uses Django's `{% url 'article-delete' article.pk %}`.

### `about.html`
- Static page displaying information about the blog.

## API App Templates

### `test-api.html`
- Simple test page to confirm API functionality.
- Can be extended with JavaScript to test API endpoints interactively.

## Conclusion
Templates structure the frontend of the Django Blog App. They use Django’s templating engine to render dynamic content and follow best practices with inheritance and reusable components.

