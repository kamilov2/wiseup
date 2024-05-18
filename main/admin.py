from django.contrib import admin
from .models import Profile, Category, Book, DonationRequest, Donation, FavoriteBook

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user')
    search_fields = ('name', 'email', 'user__username')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'category__name')

@admin.register(DonationRequest)
class DonationRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    search_fields = ('name', 'region')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'amount', 'date', 'region', 'donation_request')
    search_fields = ('profile__name', 'amount', 'region', 'donation_request__name')
    list_filter = ('region', 'donation_request')

@admin.register(FavoriteBook)
class FavoriteBookAdmin(admin.ModelAdmin):
    list_display = ('profile', 'book', 'added_date')
    search_fields = ('profile__name', 'book__title')
    list_filter = ('added_date',)

