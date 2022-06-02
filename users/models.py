from django.db import models
from django.contrib.auth.models import User 
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile (models.Model):
	user = models.OneToOneField (User, on_delete = models.CASCADE)
	image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
	student_id = models.CharField(max_length = 20)
	hostel = models.CharField (max_length = 25, default = 'SR')
	room = models.IntegerField(default = 0)
	mobile = models.IntegerField(default = 0)
	year = models.IntegerField(default = 2021)
	first_branch = models.CharField(max_length = 50, default = 'NA')
	second_branch = models.CharField(max_length = 50, default = 'NA')

	def __str__ (self):
		return f'{self.user.username} Profile'

	def image_save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)
		if img.height > 300 and img.height > 300 :
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.image_save(self.image.path)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
