from django.db import models

# class Amin(models.Model):
#     username = models.BigIntegerField(unique=True)
#     password = models.CharField(max_length=100)

#     class Meta:
#         db_table = "amin_table"


# class Candidatein(models.Model):
#     # picture = models.ImageField()
#     name = models.CharField(max_length=100, blank=False)
#     bio_data = models.CharField(max_length=500,blank=False)

# class Meta:
#      db_table = "Candidatein_table"


# class Leader(models.Model):
#       picture = models.ImageField
#       name = models.CharField(max_length=100, blank=False)
#       bio_data = models.CharField(max_length=500,blank=False)
#     #   fullname = models.CharField(max_length=100, blank=False)
#     #   bio_data = models.CharField(max_length=500,blank=False)
# #     symbole = models.CharField(max_length=100, blank=False)
# #     title =models.CharField(max_length=100)
# class Meta:
#      db_table = "Leader_table"


class createregister(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    adharnumber = models.CharField(max_length=14, blank=False)
    # educationalqualificatiom_choise = (
    # ("SSC", "SSC"), ("Intermediate", "Intermediate"), ("U.G", "U.G"), ("P.G", "P.G"), ("Ph.D", "Ph.D"),
    # ("None", "None"))
    # educationalqualificatiom = models.CharField(max_length=100, blank=False, choices=educationalqualificatiom_choise)
    phonenumber = models.CharField(max_length=10, blank=False)
    # gender_choice = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("Prefer Not To Say", "Prefer Not To Say"))
    # gender = models.CharField(max_length=20, blank=False, choices=gender_choice)
    birthdate = models.DateField(blank=False)
    address = models.CharField(max_length=100, blank=False)
    # address1 = models.CharField(max_length=100, blank=False)
    # country_choise = (("INDIA", "INDIA"), ("INDIA", "INDIA"))
    # country = models.CharField(max_length=20, blank=False, choices=country_choise)
    # city = models.CharField(max_length=30, blank=False)
    # region = models.CharField(max_length=20, blank=False)
    # postalcode = models.CharField(max_length=6, blank=False)

    class Meta:
        db_table = "createregister_table"




class signup(models.Model):
    username = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    class Meta:
        db_table = "signup_table"
