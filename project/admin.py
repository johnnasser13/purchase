from django.contrib import admin

from project.models import *


#class CompanyAdmin(admin.ModelAdmin):
#    fields = ['cmpID', 'cmpName']
admin.site.register(Company)#, CompanyAdmin)

admin.site.register(Department)
admin.site.register(User)
admin.site.register(PurchaseRequest)
admin.site.register(PurchaseItem)
admin.site.register(Item)
admin.site.register(ApproverRequest)
admin.site.register(Approver)
admin.site.register(AC)
admin.site.register(Type)
admin.site.register(Urgency)

#@admin.register(models.Company)
#class CompanyAdmin(admin.ModelAdmin):
#    list_display = ('cmpID', 'cmpName')

