#Platypus E-Commerce
##Platypus is a Django-based e-commerce platform designed to provide a seamless shopping experience for premium products and personalized event planning services. Built with Python, ##Django, and Bootstrap, it offers a user-friendly interface for browsing products, managing carts, registering users, and submitting event or contact inquiries.
##Features

##Product Browsing: Explore products by category, view details, and add items to a cart.
##User Authentication: Register and log in using username, email, or phone number with a custom authentication backend.
##Shopping Cart: Add products to a session-based cart, view cart details, and proceed to checkout (authenticated users only).
##Order Management: Place orders with delivery address and view order confirmations.
##Event Inquiry: Submit inquiries for event planning with details like event date, type, budget, and guest count.
##Contact Us Form: Submit name, email, and message directly from the homepage, stored in the database.
##About Us Page: Learn about Platypus’s mission and services.
##Admin Panel: Manage products, categories, orders, event inquiries, and contact submissions via Django’s admin interface.
##Responsive Design: Bootstrap-powered UI for a consistent experience across devices.

#Tech Stack

##Backend: Python, Django
##Frontend: HTML, CSS, Bootstrap 5, JavaScript
##Database: SQLite (local), PostgreSQL (Heroku)
##Authentication: Custom EmailOrPhoneBackend alongside Django’s ModelBackend
##Static Files: Managed via Django’s staticfiles app
##Deployment: render

#Prerequisites

##Python 3.8+
##Git
##Virtualenv (recommended)
##A GitHub account (for version control)

#Setup Instructions
#Follow these steps to set up and run the Platypus project locally.
#1. Clone the Repository
##git clone https://github.com/your-username/platypus-ecommerce.git
##cd platypus-ecommerce

#2. Create a Virtual Environment
##python -m venv venv
##source venv/bin/activate  # On Windows: .\venv\Scripts\activate

#3. Install Dependencies
##Ensure you have a requirements.txt file. If not, generate one:
##pip freeze > requirements.txt

##Install dependencies:
###pip install -r requirements.txt

##Typical dependencies include:

###django
###django-crispy-forms
###pillow (for image handling)

#4. Configure Environment Variables
##Create a .env file or set environment variables for sensitive settings:
##DJANGO_SECRET_KEY='your-secure-secret-key'
##DEBUG=True

#Built with ❤️ by [Phaust Technologies].
