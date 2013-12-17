from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from django.utils import timezone
import datetime

FIRST_OF_2014 = datetime.datetime(2014, 8, 20)

setup1 = FIRST_OF_2014
setup2 = FIRST_OF_2014 + datetime.timedelta(days=1)
setup3 = FIRST_OF_2014 + datetime.timedelta(days=2)
setup4 = FIRST_OF_2014 + datetime.timedelta(days=3)
setup5 = FIRST_OF_2014 + datetime.timedelta(days=4)
day1   = FIRST_OF_2014 + datetime.timedelta(days=5)
day2   = FIRST_OF_2014 + datetime.timedelta(days=6)
day3   = FIRST_OF_2014 + datetime.timedelta(days=7)
day4   = FIRST_OF_2014 + datetime.timedelta(days=8)
day5   = FIRST_OF_2014 + datetime.timedelta(days=9)
day6   = FIRST_OF_2014 + datetime.timedelta(days=10)
day7   = FIRST_OF_2014 + datetime.timedelta(days=11)
day8   = FIRST_OF_2014 + datetime.timedelta(days=12)
day9   = FIRST_OF_2014 + datetime.timedelta(days=13)
 
DATES_2014 = (
(setup1, setup1.strftime("%a, %b %d")),
(setup2, setup2.strftime("%a, %b %d")),
(setup3, setup3.strftime("%a, %b %d")),
(setup4, setup4.strftime("%a, %b %d")),
(setup5, setup5.strftime("%a, %b %d")),
(day1, day1.strftime("%a, %b %d")),
(day2, day2.strftime("%a, %b %d")),
(day3, day3.strftime("%a, %b %d")),
(day4, day4.strftime("%a, %b %d")),
(day5, day5.strftime("%a, %b %d")),
(day6, day6.strftime("%a, %b %d")),
(day7, day7.strftime("%a, %b %d")),
(day8, day8.strftime("%a, %b %d")),
(day9, day9.strftime("%a, %b %d")),
) 


class User(AbstractUser):
	# includes columns via AbstractUser:
	# username, first_name, last_name, is_staff, is_active, date_joined, password, last_login, is_superuser
	# M2M groups, M2M user_permissions
	setup1 = FIRST_OF_2014
	setup2 = FIRST_OF_2014 + datetime.timedelta(days=1)
	setup3 = FIRST_OF_2014 + datetime.timedelta(days=2)
	setup4 = FIRST_OF_2014 + datetime.timedelta(days=3)
	setup5 = FIRST_OF_2014 + datetime.timedelta(days=4)
	day1   = FIRST_OF_2014 + datetime.timedelta(days=5)
	day2   = FIRST_OF_2014 + datetime.timedelta(days=6)
	day3   = FIRST_OF_2014 + datetime.timedelta(days=7)
	day4   = FIRST_OF_2014 + datetime.timedelta(days=8)
	day5   = FIRST_OF_2014 + datetime.timedelta(days=9)
	day6   = FIRST_OF_2014 + datetime.timedelta(days=10)
	day7   = FIRST_OF_2014 + datetime.timedelta(days=11)
	day8   = FIRST_OF_2014 + datetime.timedelta(days=12)
	day9   = FIRST_OF_2014 + datetime.timedelta(days=13)
	 
	DATES_2014 = (
	(setup1, setup1.strftime("%a, %b %d")),
	(setup2, setup2.strftime("%a, %b %d")),
	(setup3, setup3.strftime("%a, %b %d")),
	(setup4, setup4.strftime("%a, %b %d")),
	(setup5, setup5.strftime("%a, %b %d")),
	(day1, day1.strftime("%a, %b %d")),
	(day2, day2.strftime("%a, %b %d")),
	(day3, day3.strftime("%a, %b %d")),
	(day4, day4.strftime("%a, %b %d")),
	(day5, day5.strftime("%a, %b %d")),
	(day6, day6.strftime("%a, %b %d")),
	(day7, day7.strftime("%a, %b %d")),
	(day8, day8.strftime("%a, %b %d")),
	(day9, day9.strftime("%a, %b %d")),
	) 

	# CHEF_DINNERS_2014 = (
	# (, 'chef dinner'),
	# (setup2, setup2.strftime("%a, %b %d"), 'chef dinner'),
	# (setup3, setup3.strftime("%a, %b %d"), 'chef dinner'),
	# (setup4, setup4.strftime("%a, %b %d"), 'chef dinner'),
	# (setup5, setup5.strftime("%a, %b %d"), 'chef dinner'),
	# (day1, day1.strftime("%a, %b %d"), 'chef dinner'),
	# (day2, day2.strftime("%a, %b %d"), 'chef dinner'),
	# (day3, day3.strftime("%a, %b %d"), 'chef dinner'),
	# (day4, day4.strftime("%a, %b %d"), 'chef dinner'),
	# (day5, day5.strftime("%a, %b %d"), 'chef dinner'),
	# (day6, day6.strftime("%a, %b %d"), 'chef dinner'),
	# (day7, day7.strftime("%a, %b %d"), 'chef dinner'),
	# (day8, day8.strftime("%a, %b %d"), 'chef dinner'),
	# (day9, day9.strftime("%a, %b %d"), 'chef dinner'),
	# )
 
	phone = models.CharField(max_length=13)
	twitter =models.CharField(max_length=20)
	facebook = models.CharField(max_length = 30)
	blogsite = models.CharField(max_length = 30)

	breakfast = "breakfast"
	dinner = "dinner"
	DAILY_MEALS = (
		(breakfast, "breakfast"),
		(dinner, "dinner"),
		)
	camping_in_2014 = models.BooleanField(default=True)
	arrival_date = models.CharField(max_length = 30, choices =DATES_2014, default=setup1)
	first_meal_in_camp = models.CharField(max_length=20, choices=DAILY_MEALS, default=dinner)
	departure_date = models.CharField(max_length = 30, choices =DATES_2014, default = day8)
	available_for_setup = models.BooleanField(default=True)
	helping_with_setup = models.BooleanField(default = False)
	available_for_exedous = models.BooleanField(default=True)
	helping_with_exedous = models.BooleanField(default = True)
	#only admin can change field below
	dues_paid = models.BooleanField (default = False)

class Restrictions(models.Model):
	vegan="vegan"
	vegetarian="vegetarian"
	pescatarian="pescatarian"
	gluten_free="gluten free"
	no_peppers="no peppers"
	no_shellfish="no shellfish"
	no_cucumbers="no cucumbers"
	no_pork ="no pork"
	no_olives="no olives"
	no_dairy="no dairy"
	no_nuts="no nuts"
	diabetic="diabetic"
	hates_cilantro="no cilantro"


	COMMON_RESTRICTIONS=(
	(vegan,"vegan"),
	(vegetarian,"vegetarian"),
	(pescatarian,"pescatarian"),
	(gluten_free,"gluten free"),
	(no_peppers,"no peppers"),
	(no_shellfish,"no shellfish"),
	(no_cucumbers,"no cucumbers"),
	(no_pork,"no pork"),
	(no_olives,"no olives"),
	(no_dairy,"no dairy"),
	(no_nuts,"no nuts"),
	(diabetic,"diabetic"),
	(hates_cilantro,"cilantro NO!"),
	)
	user=models.ForeignKey(User)
	restriction = models.CharField(max_length=30)


# class Dinner(models.Model):
# 	user=models.ForeignKey(User)
# 	chef="chef" 
# 	sous_chef="sous_chef" 
# 	kp1="kp" 
# 	kp2="kp" 
# 	SHIFTS= (
# 		(chef,"chef"),
# 		(sous_chef,"sous_chef"),
# 		(kp1,"kp"),
# 		(kp2,"kp"),
# 		) 
# 	menu = models.CharField(max_length=400)



# class Breakfast(models.Model):
# 	user=models.ForeignKey(User)
# 	chef="chef" 
# 	sous_chef="sous_chef" 
# 	kp1="kp" 
# 	kp2="kp" 
# 	SHIFTS= (
# 		(chef,"chef"),
# 		(sous_chef,"sous_chef"),
# 		(kp1,"kp"),
# 		(kp2,"kp"),
# 		) 
# 	menu = models.CharField(max_length=400)
# 	time = models.CharField(max_length=20)
# 	shift =models.CharField(max_length=20, choices=SHIFTS, default=kp1)

class Meal(models.Model):
	is_am = models.BooleanField()
	start_time = models.DateTimeField()
	chef = models.ForeignKey(User, null=True)	
	kps_needed = models.IntegerField()
	sous_needed = models.IntegerField()
	courier_needed = models.BooleanField()
	description = models.CharField(max_length=400)
	courier_description = models.CharField(max_length=400, blank=True)

MEAL_POSITIONS = (
	("chef", "chef"),
	("sous chef", "sous chef"),
	("kp", "kp")
)

class MealSignup(models.Model):
	meal = models.ForeignKey(Meal)
	user = models.ForeignKey(User)
	position = models.CharField(max_length=20, choices=MEAL_POSITIONS)

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
	OTHER = "Other"

	CITY_CHOICES = (
		(BAYAREA, "Bay Area"),
		(SEATTLE, "Seattle"),
		(ATLANTA, "Atlanta"),
		(NEW_YORK, "New York"),
		(DC, "DC"),
		(PORTLAND, "Portland"),
		(MINN, "Minneapolis"),
		(LA, "Los Angeles"),
		(OTHER, "Other"),
		)
	#where traveling from 
	city = models.CharField(max_length = 20, choices = CITY_CHOICES, default=BAYAREA)
	#if city not listed
	other_city = models.CharField(max_length = 20)
	traveling_with_other_biolum = models.BooleanField()

	has_ride = models.BooleanField()
	looking_for_ride = models.BooleanField()
	has_room_for_stuff = models.BooleanField()
	looking_for_stuff_sherpa = models.BooleanField()
	#if looking, how much
	stuff_description = models.CharField(max_length = 156)

	na = "the car I'm coming in is not being parked at camp"
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
	(na, "the vehicle I ride in is not being parked at camp"),
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
	(none, "none"),
	)

	#will the vehicle you drive or ride in be parked in camp?
	primary_driver = models.ForeignKey(User)
	parking_vehicle_in_camp = models.BooleanField(default=True)
	make_of_car = models.CharField(max_length = 24, blank=True)
	type_of_car = models.CharField(max_length=24, choices = CAR_TYPES, blank=True)
	#if other
	car_color = models.CharField(max_length = 24, blank=True)
	other_type = models.CharField(max_length = 24, blank=True)
	car_length_feet = models.CharField(max_length = 2, blank=True)
	car_width_feet = models.CharField(max_length = 2, blank=True)
	#are you coming from one of these places? Check the box

class Sleep(models.Model):
 	tent_not_in_uber="tent not in uber"
 	tent_under_uber="tent under uber"
 	standard_hexayurt = "standard hexayurt"
 	special_hexayurt = "special hexayurt"
 	rv_truck_car = "camping in your vehicle or rv"
 	sleeping_possibilities = (
 		(tent_not_in_uber,"tent not in uber"),
 		(tent_under_uber, "tent under uber"),
 		(standard_hexayurt, "standard hexayurt, six foot"),
 		(special_hexayurt, "special hexayurt"),
 		(rv_truck_car, "camping in your vehicle or rv"),
 		)
 	sharing_space = models.BooleanField(default=True)
 	sharing_with = models.CharField(max_length = 25)
 	tent_width_feet = models.CharField(max_length=5)
 	tent_length_feet = models.CharField(max_length=5)


