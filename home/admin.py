from django.contrib import admin
from home.models import Info
from home.models import Feedback
from home.models import Mail

# Register your models here.

admin.site.register(Info)
admin.site.register(Feedback)
admin.site.register(Mail)