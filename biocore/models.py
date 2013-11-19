from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class User(AbstractUser):
	# includes columns via AbstractUser:
	# username, first_name, last_name, is_staff, is_active, date_joined, password, last_login, is_superuser
	# M2M groups, M2M user_permissions
	setup1 ="Wednesday, August 20" 
	setup2 ="Thursday, August 21" 
	setup3 ="Friday, August 22"
	setup4 ="Saturday, August 23"
	setup5 ="Sunday, August 24"
	day1 ="Monday, August 25"
	day2 = "Tuesday, August 26"
	day3 = "Wednesday, August 27"
	day4 = "Thursday, August 28"
	day5 ="Friday, August 29"
	day6 = "Saturday, August 30"
	day7 = "Sunday, August 31"
	day8 = "Monday, September 1"
	day9 = "Tuesday, September 2"
	
	#event starts on day 1, setup in neg #'s'
	DATES_2014 = (
	(setup1, "Wednesday, August 20"),
	(setup2, "Thursday, August 21"),
	(setup3, "Friday, August 22"),
	(setup4, "Saturday, August 23"),
	(setup5,"Sunday, August 24"),
	(day1, "Monday, August 25"),
	(day2, "Tuesday, August 26"),
	(day3, "Wednesday, August 27"),
	(day4, "Thursday, August 28"),
	(day5,"Friday, August 29"),
	(day6, "Saturday, August 30"),
	(day7, "Sunday, August 31"),
	(day8, "Monday, September 1"),
	(day9, "Tuesday, September 2"),
	)

	camping_in_2014 = models.BooleanField(default=True)
	arrival_date = models.CharField(max_length = 30, choices =DATES_2014, default=setup1)
	departure_date = models.CharField(max_length = 30, choices =DATES_2014, default = day8)
	available_for_setup = models.BooleanField(default=True)
	available_for_exedous = models.BooleanField(default=True)
	#only admin can change field below
	dues_paid = models.BooleanField (default = False)

class Travel(models.Model):
		#are you coming from one of these places? Check the box
	BAYAREA = "Bay Area"
	SEATTLE = "Seattle"
	ATLANTA = "Atlanta"
	NEW_YORK = "New York"
	PORTLAND = "Portland"
	MINN = "Minneapolis"
	LA = "Los Angeles"
	DC = "DC"

	CITY_CHOICES = (
		(BAYAREA, "Bay Area"),
		(SEATTLE, "Seattle"),
		(ATLANTA, "Atlanta"),
		(NEW_YORK, "New York"),
		(DC, "DC"),
		(PORTLAND, "Portland"),
		(MINN, "Minneapolis"),
		(LA, "Los Angeles"),
		)
	#where traveling from 
	city = models.CharField(max_length = 20, choices = CITY_CHOICES, default=BAYAREA)
	#if city not listed
	other_city = models.CharField(max_length = 20)
	traveling_with_other_biolum = models.BooleanField()
	travel_with1 = models.OneToOneField(User, related_name="rideshare1")
	travel_with2 = models.OneToOneField(User, related_name="rideshare2")
	travel_with3 = models.OneToOneField(User, related_name="rideshare3")
	travel_with4 = models.OneToOneField(User, related_name="rideshare4")

	has_ride = models.BooleanField()
	looking_for_ride = models.BooleanField()
	has_room_for_stuff = models.BooleanField()
	looking_for_stuff_sherpa = models.BooleanField()
	#if looking, how much
	stuff_description = models.CharField(max_length = 156)

class Cars(models.Model):
	sedan= "sedan or hatchback" 
	wagon="station wagon" 
	minivan="minivan" 
	sniper_van="van" 
	bigass_rv="bigass rv" 
	big_suv="bigass suv" 
	small_suv="mini suv" 
	small_pickup="mini pickup" 
	large_pickup="big pickup" 
	none="no car at camp / dragon / chariot" 
	truck="trailer truck"
	other="other"
	
	CAR_TYPES = (
	(sedan, "sedan or hatchback"),
	(wagon,'station wagon'),
	(minivan,"minivan"),
	(sniper_van, "van"),
	(bigass_rv,"bigass rv"),
	(big_suv,"bigass suv"),
	(small_suv,"mini suv"),
	(small_pickup,"mini pickup"),
	(large_pickup,"big pickup"),
	(none,"no car at camp / dragon / chariot"),
	(truck,"trailer truck"),
	(other, "other"),
	)

	#will the vehicle you drive or ride in be parked in camp?
	primary_driver = models.OneToOneField(User)
	parking_vehicle_in_camp = models.BooleanField(default=True)
	make_of_car = models.CharField(max_length = 24)
	type_of_car = models.CharField(max_length=24, choices = CAR_TYPES)
	#if other
	car_color = models.CharField(max_length = 24)
	other_type = models.CharField(max_length = 24)
	car_length_feet = models.CharField(max_length = 2)
	car_length_inches = models.CharField(max_length = 2)
	car_width_feet = models.CharField(max_length = 2)
	car_width_inches = models.CharField(max_length = 2)
	#are you coming from one of these places? Check the box

class Settings(models.Model):
	campers_in_2014 = models.OneToOneField(User)
	camping_in_2014 = models.BooleanField(default = True)

# class ChefShifts
# #Chef will moderate all other shifts for their meal - allow more or less kp and sous

# class MealRestrictions


# class 


# 	def has_answered_essentials(self):
# 		return True

