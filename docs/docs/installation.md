# Installation

Follow these steps to set up the Django Blog App locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aylift/Django_Blog.git
   ```

   ```bash
   cd Django_Blog
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up an admin account.


6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:** Open your browser and go to:

   ```
   http://localhost:8000/
   ```

---
