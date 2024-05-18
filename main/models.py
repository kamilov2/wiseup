from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name




class Book(models.Model):
    title = models.CharField(max_length=200)
    book = models.FileField(upload_to="books/")
    book_image = models.ImageField(upload_to="books/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


class DonationRequest(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="donation-requests/")
    region = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Donation Request"
        verbose_name_plural = "Donation Requests"

    def __str__(self):
        return self.name


class Donation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    region = models.CharField(max_length=100, null=True, blank=True)
    donation_request = models.ForeignKey(DonationRequest, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Donation"
        verbose_name_plural = "Donations"

    def __str__(self):
        return f"Donation of {self.amount} by {self.profile.name}"


class FavoriteBook(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Favorite Book"
        verbose_name_plural = "Favorite Books"

    def __str__(self):
        return f"{self.profile.name}'s favorite: {self.book.title}"
