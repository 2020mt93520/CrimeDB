from django.contrib import admin
from .models import *


admin.site.register(Petitioner)
admin.site.register(Accused)
admin.site.register(Victim)
admin.site.register(Incident)
admin.site.register(InvestigationOfficer)
admin.site.register(FIR)
admin.site.register(Case)
