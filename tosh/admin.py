from django.contrib import admin
from .models import User, Education, Experience, Skillset, Project, Message, Information

# Register your models here.
admin.site.register(User)
admin.site.register(Information)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skillset)
admin.site.register(Project)
admin.site.register(Message)
