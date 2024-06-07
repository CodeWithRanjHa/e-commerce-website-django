from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    STATE_CHOICES = [
        ('Sargodha', 'Sargodha'),
        ('Kot Momin', 'Kot Momin'),
        ('Islamabad', 'Islamabad'),
        ('Rawalpindi', 'Rawalpindi'),
        ('Faislabad', 'Faislabad'),
        ('Lahore', 'Lahore'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, choices=STATE_CHOICES, null=True)
    zipcode = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


CATEGORY = (
    ('M', 'Mobiles'),
    ('El', 'Electronics'),
    ('B', 'Books'),
    ('C', 'Clothing'),
    ('AC', 'Accessories'),
)


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(choices=CATEGORY, max_length=2)
    description = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart for {self.user.username}"


STATUS = (
    ('Delivered', 'Delivered'),
    ('Pending', 'Pending'),
    ('Cancelled', 'Cancelled'),
    ('On The Way', 'On The Way'),
    ('Received', 'Received'),
    ('Paid', 'Paid'),
    
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS, default='Pending')
    

    def __str__(self):
        return f"{self.quantity} of {self.product.title} placed by {self.user.username}"





class Banners(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='banner_images')

    def __str__(self):
        return self.title
    

