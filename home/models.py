from django.db import models

class Home(models.Model):
    dep_dis = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='slider_images/', default='slider_images/default-placeholder.jpg')
    alt_text = models.CharField(max_length=255, blank=True, null=True)
   
    def __str__(self):
        return self.dep_dis[:50]  # Display first 50 characters of description
class Events(models.Model):
    e_title=models.CharField(max_length=255)
    e_dis=models.TextField()
    e_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.e_title
class Facility(models.Model):
    dep_fac = models.CharField(max_length=100, blank=True, null=True)
    dep_dic = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.dep_fac

class FacilityImage(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='Facility')

    def __str__(self):
        return f"Image for {self.facility.dep_fac}"

class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    alt_text = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.alt_text or 'No Alt Text'
class principal(models.Model):
    principal_image=models.ImageField(upload_to='Princpal_image')
    principal_name=models.CharField(max_length=255)
    principal_possition=models.TextField()
    def __str__(self):
        return self.principal_name
class staffDetails(models.Model):
    staff_image=models.ImageField(upload_to='staff_image')
    staff_name=models.CharField(max_length=255)
    staff_possition=models.TextField()
    def __str__(self):
        return self.staff_name
class Photogallery(models.Model):
    school_image=models.ImageField(upload_to='staff_image')
    image_dis=models.TextField()
    def __str__(self):
        return self.image_dis
class Videogallery(models.Model):
    video_url=models.TextField()
    video_description=models.TextField()
    def __str__(self):
     return self.video_description
class news(models.Model):
    news_tite=models.TextField()
    image = models.ImageField(upload_to='event_images/',default='event_images/default.jpg', blank=True, null=True)
    news_description=models.TextField()
    def _str_self():
        return self.news_tite