# Django Blog App - Models Documentation

## Profile Model (users app)

### Description
The `Profile` model extends the default Django `User` model by adding a profile image. It also includes an overridden `save` method to automatically resize the image if it exceeds 300x300 pixels.

### Model Definition
```python
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} Profile'
```

### Fields
- **user**: A one-to-one relationship with the built-in `User` model.
- **image**: Stores profile pictures uploaded by users.

### Methods
- **save**: Overrides the default save method to resize images larger than 300x300 pixels.

## Article Model (blog app)

### Description
The `Article` model represents a blog post with a title, content, timestamp, and an author.

### Model Definition
```python
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
```

### Fields
- **title**: A `CharField` with a maximum length of 100 characters.
- **content**: A `TextField` for storing the main article content.
- **date_posted**: A `DateTimeField` that defaults to the current timestamp.
- **author**: A foreign key linking to the `User` model, enforcing cascading deletion.

### Methods
- **get_absolute_url**: Returns the URL for viewing an individual article.

### String Representation
- The `__str__` method returns the article's title.

## Relationships
- The `Profile` model is linked to the `User` model via a one-to-one relationship.
- The `Article` model is linked to the `User` model via a foreign key, meaning a user can have multiple articles.

