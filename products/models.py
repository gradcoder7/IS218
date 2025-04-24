from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    size_choices = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large')]
    size = models.CharField(max_length=2, choices=size_choices)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Feedback on {self.product.name}"
