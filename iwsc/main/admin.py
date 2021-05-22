
from django.contrib import admin
from .models import Blog ,Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name' , 'mail' , 'contact_Number')


class BlogAdmin(admin.ModelAdmin):
	fields = [
                'opportunity_type',
				'description',
				'eligibility',
				'deadline', 
                
				]
	list_display = ('opportunity_type' ,'deadline')
	list_filter = ('opportunity_type','deadline' )


admin.site.register(Blog , BlogAdmin)
admin.site.register(Contact , ContactAdmin)
