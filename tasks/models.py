from django.db import models
from django.db.models.signals import pre_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICE = (
        ('PENDING','Pending'),
        ('IN_PROGRESS','In_progress'),
        ('COMPLETED','Completed')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='PENDING')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1, related_name='project')
    employee = models.ManyToManyField(Employee, related_name='employee')
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    

class TaskDetail(models.Model):
    HIGH = 'H'
    MIDIUM = 'M'
    LOW = 'L'
    PRIORITY_CHOICES = (
        (HIGH, 'Hight'),
        (MIDIUM, 'Medium'),
        (LOW, 'Low')
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='details')
    
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=LOW)

    def __str__(self):
        return self.priority

@receiver(pre_save, sender=Task)
def task_notification(sender, instance, **kwargs):
    instance.is_completed = True

@receiver(m2m_changed, sender=Task.employee.through)
def task_email_notification(sender, instance, action, **kwargs):
    if action == 'post_add':
        send_emails = [emp.email for emp in instance.employee.all()]
        send_mail(
            "New Task Assigned",
            f"You have been assigned to the Task : {instance.title}",
            "zahidallsquare@gmail.com",
            send_emails
        )
