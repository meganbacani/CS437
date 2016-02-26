from __future__ import unicode_literals

from django.db import models


# for anything that stores a list of ints, we should consider using this custom model field: http://stackoverflow.com/questions/24749762/i-have-a-list-of-long-integers-that-i-assign-to-a-django-model-charfield-the-li

# any updates need to be remigrated into the db
# list of updates
# Change listofprereqs to have NULL available



class Major(models.Model):
    majorID = models.AutoField(primary_key=True)
    majorName = models.CharField(max_length=60)

    listOfClasses = models.TextField(max_length = None, null=False) #JSON-serialized (text version)

    def __unicode__(self):
        mID = str(self.majorName)
        return mID

class Class(models.Model):

    # admin info
    classID = models.AutoField(primary_key=True)
    className = models.CharField(max_length=60)
    schoolCode = models.CharField(max_length=1) # use choices for school code?
    deptID = models.SmallIntegerField(null = False)
    courseCode = models.CharField(max_length = 5)

    # scheduler info
    creditNum = models.SmallIntegerField(null = False, default = -1)
    semOffered = models.SmallIntegerField(null = False, default = -1) # 2 if offered both semesters, 1 if offered in spring only, 0 if offered in Fall only
    listOfPrereqs = models.TextField(max_length = None, null=False) #JSON-serialized (text version)
    numPrereqs = models.SmallIntegerField(null = False, default = -1)

    def __unicode__(self):
        cID = str(self.className)
        return cID


# c = Class(className = "Computer Science", schoolCode = "E", deptID = 81, courseCode = "131", creditNum = 3, semOffered = 2,listOfPrereqs = "", numPrereqs = 0)

