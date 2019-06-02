from django.contrib import admin
from .models import *

from django.contrib.auth.models import User, Group


class MemberInline(admin.TabularInline):
    model = Member

class HouseholdAdmin(admin.ModelAdmin):
    inlines = [ MemberInline, ]


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Category)
admin.site.register(Provider)
admin.site.register(Member)
admin.site.register(Household, HouseholdAdmin)
admin.site.register(Product)
admin.site.register(LocalSettings)
