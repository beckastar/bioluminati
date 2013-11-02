from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	# includes columns via AbstractUser:
	# username, first_name, last_name, is_staff, is_active, date_joined, password, last_login, is_superuser
	# M2M groups, M2M user_permissions
	def has_answered_essentials(self):
		return True
