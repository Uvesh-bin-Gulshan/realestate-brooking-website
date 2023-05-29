from django.db import models


class LandingSummary(models.Model):
    Introduction=models.TextField(max_length=500)

class LandingCategory(models.Model):
    Image=models.ImageField(null=False)
    Title=models.CharField(max_length=30)
    ShortText=models.TextField(max_length=200)

class LandingFeatures(models.Model):
    Icon=models.ImageField(null=False)
    Titel=models.CharField(max_length=30)
    SmallText=models.TextField(max_length=100)

class LandingAbout(models.Model):
    Titel=models.CharField(max_length=30)
    SamllBio=models.TextField(max_length=200)


class LandingGallery(models.Model):
    #video left
    Image1=models.ImageField(null=False)
    Image2= models.ImageField(null=False)

class LandingTestimonials(models.Model):
    Testimonials=models.TextField(max_length=200)
    Image=models.ImageField(null=False)
    Name=models.CharField(max_length=20)
    Designation=models.CharField(max_length=20)




