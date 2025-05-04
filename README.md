Platypus E-Commerce
Platypus is a Django-based e-commerce platform designed to provide a seamless shopping experience for premium products and personalized event planning services. Built with Python, Django, and Bootstrap, it offers a user-friendly interface for browsing products, managing carts, registering users, and submitting event or contact inquiries.
Features

Product Browsing: Explore products by category, view details, and add items to a cart.
User Authentication: Register and log in using username, email, or phone number with a custom authentication backend.
Shopping Cart: Add products to a session-based cart, view cart details, and proceed to checkout (authenticated users only).
Order Management: Place orders with delivery address and view order confirmations.
Event Inquiry: Submit inquiries for event planning with details like event date, type, budget, and guest count.
Contact Us Form: Submit name, email, and message directly from the homepage, stored in the database.
About Us Page: Learn about Platypus’s mission and services.
Admin Panel: Manage products, categories, orders, event inquiries, and contact submissions via Django’s admin interface.
Responsive Design: Bootstrap-powered UI for a consistent experience across devices.

Tech Stack

Backend: Python, Django
Frontend: HTML, CSS, Bootstrap 5, JavaScript
Database: SQLite (local), PostgreSQL (Heroku)
Authentication: Custom EmailOrPhoneBackend alongside Django’s ModelBackend
Static Files: Managed via Django’s staticfiles app
Deployment: Heroku

Prerequisites

Python 3.8+
Git
Virtualenv (recommended)
Heroku CLI (for deployment)
A GitHub account (for version control)

Setup Instructions
Follow these steps to set up and run the Platypus project locally.
1. Clone the Repository
git clone https://github.com/your-username/platypus-ecommerce.git
cd platypus-ecommerce

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

3. Install Dependencies
Ensure you have a requirements.txt file. If not, generate one:
pip freeze > requirements.txt

Install dependencies:
pip install -r requirements.txt

Typical dependencies include:

django
django-crispy-forms
pillow (for image handling)

4. Configure Environment Variables
Create a .env file or set environment variables for sensitive settings:
DJANGO_SECRET_KEY='your-secure-secret-key'
DEBUG=True

Generate a secure SECRET_KEY:
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

5. Apply Migrations
Set up the database:
python manage.py makemigrations
python manage.py migrate

6. Create a Superuser
Create an admin account to access /admin/:
python manage.py createsuperuser

7. Collect Static Files
python manage.py collectstatic

8. Run the Development Server
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.
Project Structure
platypus-ecommerce/
├── platypus/              # Project settings and URLs
├── store/                 # Main app for products, orders, and forms
│   ├── migrations/        # Database migrations
│   ├── templates/store/   # HTML templates (home, about, contact, etc.)
│   ├── static/            # CSS, JS, and images
│   ├── models.py          # Product, Category, Order, Contact models
│   ├── views.py           # Views for homepage, products, cart, etc.
│   ├── forms.py           # ContactForm, EventInquiryForm
├── users/                 # App for user authentication
│   ├── migrations/        # User model migrations
│   ├── templates/users/   # Registration and login templates
│   ├── backends.py        # Custom EmailOrPhoneBackend
│   ├── templatetags/      # Custom form_filters for Bootstrap styling
├── .gitignore             # Excludes venv, db.sqlite3, etc.
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies

Deployment to Heroku

Install Heroku CLI: Follow Heroku’s guide.
Log in to Heroku:heroku login


Create a Heroku App (if not already created):heroku create platypus-ecommerce


Add PostgreSQL Add-on:heroku addons:create heroku-postgresql:hobby-dev


Set Environment Variables:heroku config:set DJANGO_SECRET_KEY='your-secure-secret-key'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS='platypus-ecommerce.herokuapp.com'


Add Procfile:Create Procfile in the project root:web: gunicorn platypus.wsgi


Update requirements.txt:Ensure gunicorn is included:pip install gunicorn
pip freeze > requirements.txt


Push to Heroku:git push heroku main
heroku run python manage.py migrate


Open the App:heroku open



Deployed URL: https://platypus-ecommerce.herokuapp.com/
Usage

Homepage: Browse featured products, categories, and submit a contact form.
Register/Login: Create an account or log in at /users/register/ or /login/.
Products: View products at /products/ and add to cart (/add-to-cart/<id>/).
Cart & Checkout: Manage cart at /cart/ and place orders at /checkout/ (requires login).
Event Inquiry: Submit event details at /event-inquiry/ (requires login).
About Us: Learn about Platypus at /about/.
Admin Panel: Manage data at /admin/ (superuser login required).

Contributing

Fork the repository.
Create a feature branch:git checkout -b feature/your-feature


Commit changes:git commit -m "Add your feature"


Push to your fork:git push origin feature/your-feature


Open a pull request on GitHub.

Troubleshooting

CSRF Errors: Ensure {% csrf_token %} is included in all POST forms and CsrfViewMiddleware is in MIDDLEWARE.
Template Errors: Verify {% load form_filters %} in templates using add_class.
Database Issues: Run python manage.py makemigrations and migrate after model changes.
Static Files: Run python manage.py collectstatic and check STATICFILES_DIRS.

License
This project is licensed under the MIT License.
Contact
For questions or feedback, use the Contact Us form on the homepage or open an issue on GitHub.

Built with ❤️ by [Phaust Technologies].
