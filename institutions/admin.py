from django.contrib import admin

from students.models import DeployedStudentProgram, OutboundStudentProgram
from .models import *

admin.site.register(Institution)
admin.site.register(Memorandum)
admin.site.register(Linkage)
admin.site.register(Program)
admin.site.register(AcademicYear)
admin.site.register(Term)
admin.site.register(InboundProgram)
admin.site.register(OutboundProgram)
admin.site.register(OutboundRequirement)
admin.site.register(DeployedStudentProgram)

