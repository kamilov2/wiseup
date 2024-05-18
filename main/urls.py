from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
 path('', views.HomePageView.as_view(), name='home'),
 path('books_category/<int:pk>/', views.BooksCategoryView.as_view(), name='books_category'),
 path('login/', views.LoginView.as_view(), name='login'),
 path('logout/', views.LogoutView.as_view(), name='logout'),
 path('register/', views.RegisterView.as_view(), name='register'),
 path('about/', views.AboutView.as_view(), name='about'),
 path('contact/', views.ContactView.as_view(), name='contact'),
 path('donation/', views.DonationView.as_view(), name='donation'),
 path('profile/', views.ProfileView.as_view(), name='profile'),
 path('favorite_books/<int:pk>/', views.FavoriteBooksView.as_view(), name='favorite_books'),
 path('delete_favorite_books/<int:pk>/', views.DeleteFavoriteBooksView.as_view(), name='delete_favorite_books'),
 path('donation_for_region/<int:pk>/', views.DonationsView.as_view(), name='donations'),
 path('donations_profile/<int:pk>/', views.DonationsProfileView.as_view(), name='donations_profile'),
]