from django.db import models

class MSAT(models.Model):
    r_id = models.IntegerField()
    stud_id = models.CharField(max_length = 50)
    response = models.CharField(max_length = 500)
    timestamp = models.IntegerField()  # To store duartion in seconds
    mark_scored = models.IntegerField()
    answered = models.CharField(max_length = 500)

    def __str__(self):
    	return self.stud_id