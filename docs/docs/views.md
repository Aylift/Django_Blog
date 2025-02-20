# Django Blog App - Views Documentation

## Users App Views

### `register(request)`
Handles user registration.
- If `POST`, processes form submission and creates a new user.
- Displays a success message and redirects to login on success.
- If `GET`, displays the registration form.

```python
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Dear {username}, you have been successfully signed up!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
```

### `profile(request)`
Handles user profile updates.
- If `POST`, updates user and profile details.
- Displays a success message and redirects to profile on success.
- If `GET`, loads existing user and profile forms.

```python
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile's been updated!")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
```

## Blog App Views

### `home(request)`
Displays all blog posts on the homepage.

```python
def home(request):
    return render(request, 'blog/home.html', {'title': 'Home', 'posts': Article.objects.all()})
```

### `about(request)`
Displays the about page.

```python
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
```

### Class-Based Views for Articles

- **`ArticleListView`**: Lists articles with pagination.
- **`ArticleDetailView`**: Displays article details.
- **`ArticleCreateView`**: Allows logged-in users to create articles.
- **`ArticleUpdateView`**: Allows article authors to update their posts.
- **`ArticleDeleteView`**: Allows article authors to delete their posts.

```python
class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4
```

```python
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

## API App Views

### `GetAllArticles`
Returns a list of all articles.

```python
class GetAllArticles(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
```

### `GetArticle`
Retrieves a single article by ID.

```python
class GetArticle(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article
```

### `CreateArticle`
Allows authenticated users to create articles.

```python
class CreateArticle(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
```

### `test_api(request)`
Renders an API test page.

```python
def test_api(request):
    return render(request, 'API/test-api.html')
```

