from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('Web design', 'Web design'),
        ('Graphics design', 'Graphics design'),
        ('Python', 'Python'),
        ('Javascript', 'JavaScript'),
        ('Java', 'Java'),
        ('Ethical Hacking', 'Ethical Hacking'),
        ('Database', 'Database'),
        ('computer basics','computer basics'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web_design')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



class Employ(models.Model):
    DEPARTMENT_CHOICES = [
        ('Full-stack developer', 'Full-stack developer'),
        ('Front-end developer', 'Front-end developer'),
        ('Back-end developer', 'Back-end developer'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='Full-stack developer')
    image = models.ImageField(upload_to='employee_images/', null=True, blank=True)

    def __str__(self):
        return self.name
