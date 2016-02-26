from django.contrib import admin

from .models import Major, Class


# Things to work on:
# 1. Compressing the add forms so they look better
# 2. Appending the lists when seeing it in the admin site, so that they don't take up too much space'
# 3. sorting of results by ID (might have to sort within database)



class MajorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Major Data', {'fields' : ['majorName']}),
        ('Scheduling Data', {'fields' : ['listOfClasses']})
    ]

    list_display = ('majorID', 'majorName', 'listOfClasses')
    list_filter = ('majorID', 'majorName', 'listOfClasses')
    search_fields = ('majorID', 'majorName', 'listOfClasses')


class ClassAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Class Data', {'fields' : ['className', 'schoolCode','deptID','courseCode']}),

        ('Scheduling Data', {'fields' : ['creditNum','listOfPrereqs','numPrereqs','semOffered']})
    ]

    list_display = ('classID', 'className', 'schoolCode', 'deptID', 'courseCode', 'creditNum', 'listOfPrereqs', 'numPrereqs', 'semOffered')
    list_filter = ('classID', 'className', 'schoolCode', 'deptID', 'courseCode', 'creditNum', 'listOfPrereqs', 'numPrereqs', 'semOffered')
    search_fields = ('classID', 'className', 'schoolCode', 'deptID', 'courseCode', 'creditNum', 'listOfPrereqs', 'numPrereqs', 'semOffered')





admin.site.register(Major, MajorAdmin)
admin.site.register(Class, ClassAdmin)