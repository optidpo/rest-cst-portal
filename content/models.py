from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
  customer = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True)
  email = models.EmailField(max_length=200, blank=True)
  username = models.CharField(max_length=60, null=True, blank=True)   
  fullname = models.CharField(max_length=100, null=True)
  phonenumber = models.IntegerField(default=0, null=False)
  created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created, ', null=True)
  updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

  def save_profile(self):
    self.customer()

  def delete_profile(self):
    self.delete()
   
  def __str__(self):
    return(self.id)

class Game(models.Model):
  title = models.CharField(max_length=150, verbose_name='Game Title', null=True)
  description =  models.CharField(max_length=250, verbose_name='About Game', null=True)
  price = models.IntegerField(default=0, null=False)
  gameimg = CloudinaryField('image')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created, ', null=True)
  updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

  def save_game(self):
    self.save()

  def delete_game(self):
    self.delete()
   
  def __str__(self):
    return str(self.title)

  @classmethod
  def all_games(cls):
    return cls.objects.all()

class Orders(models.Model):
  customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Customer', null = True)
  game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Game', null = True)
  created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created, ', null=True)
  updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

  def save_order(self):
    self.save()
   
  def __str__(self):
    return str(self.id)

class Card(models.Model):
  customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Customer', null = True)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Profile', null= True)
  cardNumber = models.CharField(max_length=50, verbose_name='Card Number', null=True)
  amount = models.IntegerField(default=0, null=False)
  created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created, ', null=True)
  updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

  def save_card(self):
    self.save()

    
  def __str__(self):
    return str(self.cardNumber)



