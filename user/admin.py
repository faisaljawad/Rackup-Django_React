from django.contrib import admin

# Register your models here.
from user.models import User, Skill, Profile, Review, Certification, Account

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Account)
admin.site.register(Certification)
