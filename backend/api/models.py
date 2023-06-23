from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import pandas as pd
from django.core.exceptions import ValidationError

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

#using nsu class schedule
from api import ScheduleNSU

COURSE_TYPE  = (("","Theory"),
                ("L","Lab/Practical"))

# Create your models here.

# # Custom validator function for credit
# def validate_total_credit(credit):
#         if credit > 11:
#             raise ValidationError("total credit cannot extend 11")
#         else:
#             return credit
        





class Educator(models.Model):
    name = models.CharField(_("Name "), max_length=50)
    initial = models.CharField(_("Short initial  "), max_length=50)
    designation = models.CharField(_("Designation "), max_length=50,blank=True)
    email = models.EmailField(_("Email"), max_length=254,blank=True)
    ext = models.IntegerField(_("Phone extention number"),blank=True,default=0)
    room = models.IntegerField(_("Room Number"),blank=True,default=0)
    mobile = models.CharField(_("Mobile Number"), max_length=50,blank=True)
    

    class Meta:
        verbose_name = _("Educator")
        verbose_name_plural = _("Educators")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Educator_detail", kwargs={"pk": self.pk})


        
class Faculty(Educator):
    total_credit = models.FloatField(_("Number of credit taken"),default=0)
    user = models.OneToOneField(User, verbose_name=_("User authenticaiton profile"), on_delete=models.CASCADE)
   
   
    def save(self, *args, **kwargs):
        self.user.is_staff = False
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
       if self.id is not None:
           c = Course.objects.get(pk=self.id)
           if c.number_of_section > self.number_of_section:
               raise ValidationError(" Section number cannot be reduced at the moment.")
       super(Course, self).save(*args, **kwargs) # Call the real save() method
       for i in range(1,self.number_of_section+1):
           Section(no=i,course=self).save()
           
    def __str__(self):
        return self.code+" ("+str(self.type)+") "

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"pk": self.pk})

class Section(models.Model):
    no = models.IntegerField(_("Section no"),unique=True,primary_key=True)
    course = models.ForeignKey("Course", verbose_name=_("Course Name"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")

    def __str__(self):
        return str(self.course)+" "+str(self.no)

    def get_absolute_url(self):
        return reverse("Section_detail", kwargs={"pk": self.pk})

class CourseTaken(models.Model):
    classroom = models.OneToOneField("Classroom", verbose_name=_("Classroom"), on_delete=models.CASCADE)
    section  = models.OneToOneField("Course", verbose_name=_("Course Section"), on_delete=models.CASCADE)
    class_slot  = models.OneToOneField("ClassSlot", verbose_name=_("Class slot"), on_delete=models.CASCADE)
    faculty = models.OneToOneField("Educator", verbose_name=_("Faculty Name"), on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
       f = self.faculty
       if f is None:
           #if faculty not available
           pass
       
       else:
           #checking whether it is a faculty to make sure the total credit must not cross 11
           if type(f).__name__ == "Faculty":
            f.total_credit = f.total_credit + self.section.credit
            if f.total_credit >11:
                raise ValidationError(str(self.faculty)+" cannot take more than 11 credit")
           
           #checking that class slot must not overlap
           c = self.class_slot
           if c.available is False:
               raise ValidationError(str(c)+" is already Booked at "+str(ScheduleNSU.class_schedule_tuple[c.slot-1]))
           c.available = False
           c.save()
           f.save()
           super(CourseTaken, self).save(*args, **kwargs) # Call the real save() method
    
    class Meta:
        verbose_name = _("Course_Taken")
        verbose_name_plural = _("Course_Takens")

    def __str__(self):
        return str(self.faculty)+ " " +str(self.section)

    def get_absolute_url(self):
        return reverse("Course_Taken_detail", kwargs={"pk": self.pk})


class Classroom(models.Model):
    building = models.CharField(_("academic building abbbrebiation"),max_length=10, choices=BUILDING)
    roomNo= models.PositiveIntegerField(_("classroom number"),primary_key=True)
    seat = models.PositiveIntegerField(_("Available seat for students"))
    details = models.CharField(_("Classroom details e.g. projector,computer et"), max_length=150)
    
    
    class Meta:
        verbose_name = _("Classroom")
        verbose_name_plural = _("Classrooms")

    def __str__(self):
        return self.building+" - "+str(self.roomNo)

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
    
    available = models.BooleanField(_("Class Slot available or not"),default=True)
    slot = models.IntegerField(_("Class day - time "),choices= schedule)
    name = models.CharField(_("Slot name/time"), max_length=50,blank=True)
    classroom = models.ForeignKey("Classroom", verbose_name=_("Classs room no"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("ClassSlot")
        verbose_name_plural = _("ClassSlots")
    
    def save(self, *args, **kwargs):
        self.name = self.schedule[self.slot-1]
        super(ClassSlot, self).save(*args, **kwargs) # Call the real save() method
    
    def __str__(self):
        return str(self.classroom)+" "+ str(self.slot)

    def get_absolute_url(self):
        return reverse("ClassSlot_detail", kwargs={"pk": self.pk})
