# ecommerce-website-django


![ecommerce](https://github.com/CodeWithRanjHa/e-commerce-website-django/assets/167714618/31f7161a-8aeb-486e-92ab-84abbc375dcc)


## Description
This project is a fully functional e-commerce website built to provide a seamless online shopping experience. It includes features such as user authentication, product browsing, shopping cart, order management, and secure checkout. The website is designed with a responsive layout, ensuring optimal usability across various devices.

## Features
- User registration and login
- Product catalog with detailed descriptions
- Search functionality
- Shopping cart
- Order processing 
- Admin panel for managing products and orders

## Technologies Used
- Django
- HTML/CSS
- SQLite (for development)
- Bootstrap (for styling)


## Setup
1. **Clone the repository:**
git clone https://github.com/CodeWithRanjHa/e-commerce-website-django.git



2. **Navigate to the project directory:**

```bash
  cd e-commerce-website-django
```


3. **Install dependencies:**

```bash
  pip install -r requirements.txt
```



4. **Run migrations:**

```bash
  python manage.py migrate
```


5. **Create a superuser (admin user):**


```bash
  python manage.py createsuperuse
```



6. **Start the development server:**

```bash
  python manage.py runserver
```



7. **Open your web browser and navigate to [http://localhost:8000](http://localhost:8000)**

## Usage
User Authentication: Users can sign up for an account and log in to access additional features such as adding products to the cart.
Browsing Products: Browse through the product catalog, search for specific products, and view detailed descriptions.
Shopping Cart: Add products to the shopping cart, adjust quantities, and proceed to checkout securely.
Order Management: Track the status of orders in real-time and receive notifications at various stages of the order processing.
Admin Panel: Access the admin panel at http://localhost:8000/admin to manage products, orders, users, etc.


## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a new Pull Request


