from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import telebot
from .models import *


bot = telebot.TeleBot('7197563219:AAHLN4aP4utrmuLYPmJ-4FXLLMGlU5jqY-0')

class HomePageView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('main:login')
        category = Category.objects.all()
        book = Book.objects.all().order_by('?')[:9]
        donation_request = DonationRequest.objects.all()[:4]
        favorite = FavoriteBook.objects.filter(profile__user=request.user)
        favorite_count = favorite.count()

        context = {
            "category": category,
            "books": book,
            "donation_request": donation_request,
            "favorite": favorite_count
        }
        return render(request, 'index-2.html', context)
 
class BooksCategoryView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('main:login')        
        books_list = Book.objects.filter(category_id=pk).order_by('?')
        category = Category.objects.get(id=pk)
        category_all = Category.objects.all()

        categorys = Category.objects.all().order_by('-id')[:15]
        favorite = FavoriteBook.objects.filter(profile__user=request.user)
        favorite_count = favorite.count()
        

        context = {
            'books': books_list,
            'category': category,
            'categorys':categorys,
            'category_all':category_all,
            'favorite': favorite_count
        }
        return render(request, 'shop.html', context)

class LoginView(View):
    def get(self, request):
        category = Category.objects.all()
        context = {
            'category': category
        }

        return render(request, 'login.html', context)

    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:home')  
        else:
            message = "Invalid username or password."
            return render(request, 'login.html', {'message': message})
        
class RegisterView(View):
    def get(self, request):
        category = Category.objects.all()
        context = {
            'category': category
        }

        return render(request, 'register.html', context)

    def post(self, request):
        username = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            message = "Username already exists."
            return render(request, 'register.html', {'message': message})
        elif password != confirm_password:
            message = "Passwords do not match."
            return render(request, 'register.html', {'message': message})
        else:
            user = User.objects.create_user(username=username, password=password)
            profile = Profile.objects.create(user=user, name=name, email=username)
            bot.send_message('-1002071369946', f'''
New user Registered:

Name: {name}
Email: {username}

''')
            return redirect('main:login')
        

class AboutView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('main:login')  
        category = Category.objects.all()
        favorite = FavoriteBook.objects.filter(profile__user=request.user)
        favorite_count = favorite.count()
        context = {
            'category': category,
            'favorite': favorite_count
        }
        if not request.user.is_authenticated:
            return redirect('main:login')
        return render(request, 'about.html', context)
    

class ContactView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('main:login')
        category = Category.objects.all()
        favorite = FavoriteBook.objects.filter(profile__user=request.user)
        favorite_count = favorite.count()
        context = {
            'category': category,
            'favorite': favorite_count
        }
        return render(request, 'contact.html', context)
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        category = Category.objects.all()
        favorite = FavoriteBook.objects.filter(profile__user=request.user)
        favorite_count = favorite.count()


        bot.send_message('-1002054350918', f'''
New Contact Message:
                         
Name: {username}
Email: {email}
Phone: {phone}
Message: {message}

''')
        return redirect('main:contact')
    
class DonationView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('main:login')  
        category = Category.objects.all()
        favorite = FavoriteBook.objects.filter(profile__user=request.user)
        favorite_count = favorite.count()
  
        if not request.user.is_authenticated:
            return redirect('main:login')
        donations = DonationRequest.objects.all().order_by('?')[:20]
        context = {
            'donations': donations,
            'category': category,
            'favorite': favorite_count
        }

        return render(request, 'donation.html', context)

class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('main:login')
        user = request.user
        category = Category.objects.all()
        favorite = FavoriteBook.objects.filter(profile__user=request.user)
        favorite_count = favorite.count()
        donations = Donation.objects.filter(profile__user=user)

        favorite_books = FavoriteBook.objects.filter(profile__user=user)
        user_profile = Profile.objects.get(user=user)
        print(favorite_books)

        return render(request, 'shop-detail.html', {'donations': donations, 'favorite_books': favorite_books, 'user_profile': user_profile, 'category': category, 'favorite': favorite_count})


class FavoriteBooksView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('main:login')
        user = request.user
        book = Book.objects.get(id=pk)
        profile = Profile.objects.get(user=user)

        favorite_book = FavoriteBook.objects.filter(profile=profile, book=book).first()
        if favorite_book:
            favorite_book.delete()
            FavoriteBook.objects.create(profile=profile, book=book)

        else:
            FavoriteBook.objects.create(profile=profile, book=book)

        return redirect('main:profile')


class DeleteFavoriteBooksView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('main:login')
        user = request.user
        book = Book.objects.get(id=pk)
        profile = Profile.objects.get(user=user)

        favorite_book = FavoriteBook.objects.filter(profile=profile, book=book).first()
        if favorite_book:
            favorite_book.delete()

        return redirect('main:profile')
class DonationsView(View):
    def get(self, request, pk):
        category = Category.objects.all()
        favorite = FavoriteBook.objects.filter(profile__user=request.user)
        favorite_count = favorite.count()
  
        if not request.user.is_authenticated:
            return redirect('main:login')
        donation = DonationRequest.objects.get(id=pk)
        context = {
            'donation': donation,
            'category': category,
            'favorite': favorite_count
        }
        return render(request, 'checkout.html', context)

class DonationsProfileView(View):
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('main:login')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        cart_number = request.POST.get('cart_number')
        donate_amount = request.POST.get('donate_amount')
        message = request.POST.get('message')

        profile = Profile.objects.get(user=request.user)

        donation_request = DonationRequest.objects.get(id=pk)

        donation = Donation.objects.create(
            profile=profile,
            amount=donate_amount,
            message=message,
            region=donation_request.region, 
            donation_request=donation_request
        )
        bot.send_message('-1002059747106', f'''
New Donation:

Name: {profile.name}
Phone: {phone}
Email: {profile.email}
Cart Number: {cart_number}
Amount: {donate_amount}
Message: {message}

''')
   

       
        return redirect('main:profile') 


class LogoutView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('main:login')
        logout(request)
        return redirect('main:login')