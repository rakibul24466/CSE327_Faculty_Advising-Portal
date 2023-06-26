from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import pandas as pd
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.core.exceptions import ValidationError

#using nsu class schedule
from api import ScheduleNSU

#days tuple list
DAYS_OF_WEEK = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)

BUILDING =(
    ("SAC","South Academic Buidling"),
    ("NAC","North Academic Buidling"),
    ("LIB","Library Building"),
    ("ADMIN","Admin Building")
)



COURSE_TYPE  = (("","Theory"),
                ("L","Lab"))

FACULTY_DESIGNATIONS = [
    "Junior Lecturer",
    "Lecturer",
    "Senior Lecturer",
    "Assistant Professor",
    "Associate Professor",
    "Professor",
]



class Faculty(models.Model):
    name = models.CharField(_("Name "), max_length=50)
    initial = models.CharField(_("Short initial  "), max_length=50,unique=True)
    designation = models.CharField(_("Designation "), max_length=50,blank=True)
    email = models.EmailField(_("Email"), max_length=254,blank=True)
    ext = models.IntegerField(_("Phone extention number"),blank=True,default=0)
    room = models.IntegerField(_("Room Number"),blank=True,default=0)
    mobile = models.CharField(_("Mobile Number"), max_length=50,blank=True)
    total_credit = models.FloatField(_("Number of credit taken"),default=0)
    user = models.OneToOneField(User, verbose_name=_("User authenticaiton profile"), on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.user.is_staff = False
        self.user.groups.add(1)
        self.user.first_name = self.name.split(' ')[0]
        self.user.last_name= self.name.split(' ')[1]
        self.user.email = self.email
        if len(self.designation)==0:
            self.designation = FACULTY_DESIGNATIONS[0]
        super(Faculty, self).save(*args, **kwargs) # Call the real save() method

    class Meta:
        verbose_name = _("Faculty")
        verbose_name_plural = _("Faculties")

    def __str__(self):
        return self.initial

    def get_absolute_url(self):
        return reverse("Faculty_detail", kwargs={"pk": self.pk})


class Course(models.Model):
    name =  models.CharField(max_length=100)
    code = models.CharField(_("course Code"),max_length=10,unique=True)
    credit = models.FloatField(_("Course Credit"))
    type = models.CharField(_("Course Type e.g. lab,theory "),choices=COURSE_TYPE, blank=True,max_length=10)    
    number_of_section = models.IntegerField(_("Total number of Section "),default=0)
    
    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def save(self, *args, **kwargs):
       try:
            faculty = Faculty.objects.get(initial="TBA")
           
            if self.id is not None:
                c = Course.objects.get(pk=self.id)
                if c.number_of_section > self.number_of_section:
                    raise ValidationError(" Section number cannot be reduced at the moment.")
            super(Course, self).save(*args, **kwargs) # Call the real save() method
            ## random available class_slot
            class_slot = ClassSlot.objects.filter(available=True)[:self.number_of_section]
            classroom = class_slot.values_list('classroom', flat=True)
            print(class_slot[0].available)
            for i,j,k in zip(range(1,self.number_of_section+1),class_slot,classroom):
                Section(no=i,course=self,faculty=faculty,time_slot=j,classroom=Classroom.objects.get(pk=k)).save()

       except Faculty.DoesNotExist:
            raise ValidationError(" TBA has not been created yet.")
       except IntegrityError as e :
            raise ValidationError(str(e))
        
    def __str__(self):
        return self.code+" ("+str(self.type)+") "

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"pk": self.pk})



class Section(models.Model):
    no = models.IntegerField(_("Section no"),blank=True)
    course = models.ForeignKey("Course", verbose_name=_("Course Name"), on_delete=models.CASCADE,blank=True)
    faculty = models.ForeignKey("Faculty", verbose_name=_("Faculty taking the class"), on_delete=models.CASCADE,blank=True)
    time_slot = models.OneToOneField("ClassSlot", verbose_name=_("Class slot"), on_delete=models.CASCADE,blank=True)
    classroom = models.ForeignKey("Classroom", verbose_name=_("Classroom"), on_delete=models.CASCADE,blank=True)
    
    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")
    
    def save(self, *args, **kwargs):
            super(Section, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return str(self.course)+" "+str(self.no) 

    def get_absolute_url(self):
        return reverse("Section_detail", kwargs={"pk": self.pk})



class Classroom(models.Model):
    roomNo= models.CharField(_("classroom number"),max_length=50,primary_key=True)
    seat = models.PositiveIntegerField(_("Available seat for students"))
    details = models.CharField(_("Classroom details e.g. projector,computer et"), max_length=150)
    
    class Meta:
        verbose_name = _("Classroom")
        verbose_name_plural = _("Classrooms")

    def __str__(self):
        return str(self.roomNo) 

    def get_absolute_url(self):
        return reverse("Classroom_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Call the real save() method
        schedule = ScheduleNSU.class_schedule_tuple
        
        for i in schedule:
            class_slot = ClassSlot(available=True,slot=i[0],classroom=self)
            class_slot.save()
       
class ClassSlot(models.Model):
    schedule = ScheduleNSU.class_schedule_tuple
    name = models.CharField(_("Slot name/time"), max_length=50,blank=True)
    
    slot = models.IntegerField(_("Class day - time "),choices= schedule)
    available = models.BooleanField(_("Class Slot available or not"),default=True)
    
    classroom = models.ForeignKey("Classroom", verbose_name=_("Classs room no"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("ClassSlot")
        verbose_name_plural = _("ClassSlots")
    
    def save(self, *args, **kwargs):
        self.name = self.schedule[self.slot-1]
        super(ClassSlot, self).save(*args, **kwargs) # Call the real save() method
    
    def __str__(self):
        return str(self.classroom)+" "+ str(self.slot) + " " + str(self.pk)

    def get_absolute_url(self):
        return reverse("ClassSlot_detail", kwargs={"pk": self.pk})
