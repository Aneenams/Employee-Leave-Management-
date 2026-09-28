from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Leave(models.Model):
    head_name=models.ForeignKey(User, on_delete= models.CASCADE)
    employee_name=models.CharField(max_length=50)
    reason=models.TextField(max_length=500)
    start_date=models.DateField()
    end_date=models.DateField()

    LEAVE_TYPE_CHOICES=(    
        ('Casual','Casual'),
        ('Sick','Sick'),
        ('Annual','Annual'),
        ('Emergency','Emergency')
    )

    STATUS_CHOICES=(
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected')
    )

    leave_type=models.CharField(max_length=50,choices=LEAVE_TYPE_CHOICES)

    status=models.CharField(max_length=15,choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.employee_name}"