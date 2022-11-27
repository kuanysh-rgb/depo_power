from django.contrib import admin
from .models import Locomotive, TechWork, MonthWorkDay, AvailableTechwork, Canava, CellRecord
# Register your models here.

admin.site.register(Locomotive)
admin.site.register(TechWork)
admin.site.register(MonthWorkDay)
admin.site.register(AvailableTechwork)
admin.site.register(Canava)
admin.site.register(CellRecord)
