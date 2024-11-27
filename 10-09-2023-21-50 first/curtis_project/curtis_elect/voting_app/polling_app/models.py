from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User)


class voters(models.Model) :
    gender_choices = [
        ("M", "Male"),
        ("F", "Female"),
]
    voter_id = models.CharField(max_length=20)
    voter_name = models.CharField(max_length=100, unique=True, null=False)
    voter_gender = models.CharField(max_length=6, choices=gender_choices, null=False)
    voter_email = models.EmailField(max_length=20, unique=True, null=False)
    voter_contact = models.IntegerField( unique=True, null=False)
    voter_image = models.ImageField(unique=True, null=False)
    
    
    # profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)
    
    # def __str__(self):
    #     return self.user.username


    # def __str__(self) -> str:
    #     return super().__str__()
    def __str__(self):
        return "%s" %(self.voter_name)
    
    class meta:
        db_table="voter"
    
# class vote(models.Model):
#     vote_id = models.CharField(max_length=20)
#     voter_name = models.CharField(max_length=100, unique=True, null=False)
#     email = models.EmailField(max_length=20, unique=True, null=False)
#     candidate_post = models.CharField(max_length=100, unique=True, null=False)
#     candidate_voted_for = models.CharField(max_length=100, unique=True, null=False)
    

class candidates(models.Model):
    gender_choices = [
        ("M", "Male"),
        ("F", "Female"),
]
    candidate_id = models.CharField(max_length=20)
    candidate_name = models.CharField(max_length=20, unique=True, null=False)
    candidate_gender = models.CharField(max_length=6, choices=gender_choices, null=False)
    candidate_image = models.ImageField(unique=True, null=False)
    candidate_post = models.CharField(max_length=20, unique=True, null=False)
    candidate_biography = models.TextField(max_length=500, null=False, default=False)

    def __str__(self):
        return "%s" %(self.candidate_name)
    
    class meta:
        db_table="candidate"

# class position(models.Model):
#     candidate_name = models.CharField(max_length=20, unique=True, null=False)
#     maximum_votes = models.IntegerField( null=False)
#     priority = models.IntegerField( null=False)

# class add_voter(models.Model):
#     gender_choices = [
#         ("M", "Male"),
#         ("F", "Female"),
# ]
#     voter_name = models.CharField(max_length=100, unique=True, null=False)
#     gender = models.CharField(max_length=6, choices=gender_choices, null=False)
#     email = models.EmailField(max_length=20, unique=True, null=False)
#     image = models.ImageField(unique=True, null=False)
#     phone_number = models.IntegerField( unique=True, null=False)

# class add_candidate(models.Model):
#     gender_choices = [
#         ("M", "Male"),
#         ("F", "Female"),
# ]
#     candidate_name = models.CharField(max_length=20, unique=True, null=False)
#     gender = models.CharField(max_length=6, choices=gender_choices, null=False)
#     image = models.ImageField(unique=True, null=False)
#     position = models.IntegerField( null=False)
#     biography = models.CharField(max_length=500, null=False)


# class votersForm(ModelForm):
#     class Meta:
#         model = voters
#         fields = ["voter_name", "gender", "email", "image", "phone_number"]

# class voteForm(ModelForm):
#     class Meta:
#         model = vote
#         fields = ["voter_name", "email", "candidate_post", "candidate_voted_for"]

# class candidatesForm(ModelForm):
#     class Meta:
#         model = candidates
#         fields = ["candidate_name", "gender", "image", "position", "biography"]

# class positionForm(ModelForm):
#     class Meta:
#         model = position
#         fields = ["candidate_name", "maximum_votes", "priority"]

# class add_voterForm(ModelForm):
#     class Meta:
#         model = add_voter
#         fields = ["voter_name", "gender", "email", "image", "phone_number"]

# class add_candidateForm(ModelForm):
#     class Meta:
#         model = add_candidate
#         fields = ["candidate_name", "gender", "image", "position", "biography"]