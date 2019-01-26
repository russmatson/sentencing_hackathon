#! /usr/local/bin/pypy -O


# using https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years-violent.csv as template

SEX = ["Female", "Male"]
RACE = ["African-American", "Asian", "Caucasian", "Hispanic", "Native American", "Other"]
AGE = ["Less than 25", "25-35", "35-45", "More than 45"]

# extra categories
MARITAL_STATUS = ["Divorced", "Married", "Single"]
EMPLOYMENT_STATUS = ["Unemployed", "Not looking", "Student", "Part-time employed", "Employed"]
TYPE_OF_CRIMES = ["LEAVE_BIKE_DROPOFF_ZONE", "LEAVE_BIKE_RIDING_ZONE", "VANDALISM_LOCK_BROKEN", "VANDALISM_OTHER", "BIKE_STOLEN", "HITTING_BIKER_OPENING_DOOR", "HITTING_BIKER_WHILE_DRIVING"]
AMOUNT_OF_DAMAGE = [15, 30, 100, 250, 600, "NA", "NA"]
ZIPCODE = [00000, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999, 12121]




# start

# FILE_NAME = "raw_data.csv"

# the purposes of this code is to analyze and sentence people given 
# in the raw_data.csv file.


# import 

data = []

# f = open("raw_data.csv", "r")

# for every row, read it in


person = "0,Female,Other,25-35,Divorced,Unemployed,0,55555,3,0,0,HITTING_BIKER_OPENING_DOOR,NA,1,Pre-trial detention?".split(",")

# tidy 


for person in data:
	analyze_person( person ) 

# model 

# for person in data:
	# analyze

# performs the sentencing on the person in question
def sentence_leave_bike_dropoff_zone( person ):
	# number of times offended
	# total damage done
	# prior record
	# 

	print "Sentenced to max fine"

def sentence_leave_bike_riding_zone( person ):
	print "LEAVE_BIKE_DROPOFF_ZONE"
	print "Sentenced to "

def sentence_lock_broken( person ):
	print "LEAVE_BIKE_DROPOFF_ZONE"
	print "Sentenced to "

def sentence_vandalism_other( person ):
	print "LEAVE_BIKE_DROPOFF_ZONE"
	print "Sentenced to "

def sentence_bike_stolen( person ):
	print "Sentenced to "

def decide_detention_open_door( person ):
	print "Sentenced to max prisontime"

def decide_detention_driving( person ):
	print "Sentenced to "

def analyze_person( person ):

	crime = person[11]
	
 	if (crime == "LEAVE_BIKE_DROPOFF_ZONE") : 
 		sentence_leave_bike_dropoff_zone( person )
		
	if (crime == "LEAVE_BIKE_RIDING_ZONE") :
		sentence_leave_bike_riding_zone( person )
	
	if (crime == "VANDALISM_LOCK_BROKEN") :
		sentence_lock_broken( person )

	if (crime == "VANDALISM_OTHER") :
		sentence_vandalism_other( person )
	
	if (crime == "BIKE_STOLEN") :
		sentence_bike_stolen( person )
		
	if (crime == "HITTING_BIKER_OPENING_DOOR") :
		decide_detention_open_door( person )
	
	if (crime == "HITTING_BIKER_WHILE_DRIVING") :
		decide_detention_driving( person )





analyze_person( person )









