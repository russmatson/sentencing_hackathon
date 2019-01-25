import csv, random

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

id = 0
with open('raw_data.csv', 'w') as rawdatafile:
    csvwriter = csv.writer(rawdatafile)

    while (id < 500):
        if (id == 0): # header
            csvwriter.writerow(["id", "sex", "race", "age", "marital_status", "employment_status", "salary", "zipcode", "number_of_kids", "volunteer_hours_per_week", "prior_crimes", "type_of_crimes", "amount_of_damage", "number_of_times", "task"])

        sex_selector = random.randint(0, len(SEX) - 1)
        sex = SEX[sex_selector]

        race_selector = random.randint(0, len(RACE) - 1)
        race = RACE[race_selector]

        age_selector = random.randint(0, len(AGE) - 1)
        age = AGE[age_selector]

        marital_status_selector = random.randint(0, len(MARITAL_STATUS) - 1)
        marital_status = MARITAL_STATUS[marital_status_selector]

        number_of_kids = random.randint(0, 3)

        volunteer_hours_per_week = random.sample([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 10], 1)[0]

        employment_status_selector = random.randint(0, len(EMPLOYMENT_STATUS) - 1)
        employment_status = EMPLOYMENT_STATUS[employment_status_selector]
        if (employment_status == "Employed"):
            salary = random.randint(30000, 110000) # middle 50% according to https://dqydj.com/united-states-household-income-brackets-percentiles/
        elif (employment_status == "Part-time employed"):
            salary = random.randint(15000, 30000) # 10% to 25% according to above
        else:
            salary = 0

        zipcode = ZIPCODE[race_selector + employment_status_selector]

        prior_crimes = random.sample([0, 0, 0, 0, 1, 1, 2, 3], 1)[0]

        type_of_crimes_selector = random.randint(0, len(TYPE_OF_CRIMES) - 1)
        type_of_crimes = TYPE_OF_CRIMES[type_of_crimes_selector]
        amount_of_damage = AMOUNT_OF_DAMAGE[type_of_crimes_selector]
        if (type_of_crimes_selector < len(TYPE_OF_CRIMES) - 2): # no person hurt
            number_of_times = random.sample([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5], 1)[0]
            amount_of_damage *= number_of_times
            task = "Sentencing"
        else:
            number_of_times = 1
            task = "Pre-trial detention?"

        csvwriter.writerow([id, sex, race, age, marital_status, employment_status, salary, zipcode, number_of_kids, volunteer_hours_per_week, prior_crimes, type_of_crimes, amount_of_damage, number_of_times, task])

        id += 1
