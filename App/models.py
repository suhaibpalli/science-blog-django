from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DIFFICULTY_LEVEL_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

SUBJECT_CHOICES = (
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('General Science', 'General Science'),
)

class Experiment(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=255)
    difficulty_level = models.IntegerField(choices=DIFFICULTY_LEVEL_CHOICES)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    main_image = models.ImageField(upload_to='experiment_images/')
    materials_list = models.TextField()
    safety_precautions = models.TextField()
    instructions = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiments')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
