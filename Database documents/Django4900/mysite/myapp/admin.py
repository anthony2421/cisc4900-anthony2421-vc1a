from django.contrib import admin
from .models import County
from .models import School
from .models import Pathways

# Register your models here.
admin.site.register(County)
admin.site.register(School)
admin.site.register(Pathways)
