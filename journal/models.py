from django.db import models
from django.core.validators import FileExtensionValidator


class Journal(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    logo = models.ImageField(upload_to='journal_logos/', null=True, blank=True)
    slogan = models.CharField(max_length=150, blank=True)
    director_name = models.CharField(max_length=150, null=True, blank=True)
    chief_editor = models.CharField(max_length=150, null=True, blank=True)
    establishment_date = models.DateTimeField(null=True, blank=True)
    DEPARTMENT_CHOICES = [
        (None, 'Select a major'),
        ('CE', 'Computer Engineering'),
        ('CS', 'Computer Science'),
        ('CVE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CME', 'Chemical Engineering'),
        ('AE', 'Aerospace Engineering'),
        ('PHY', 'Physics'),
        ('MATH', 'Mathematics'),
        ('CHEM', 'Chemistry')
    ]
    department_name = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        permissions = []
        db_table = 'Journal'


class Volume(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    cover_img = models.ImageField(upload_to='volume_cover_images/', null=True, blank=True)
    file = models.FileField(upload_to='volume_files/', null=True, validators=[
        FileExtensionValidator(allowed_extensions='pdf')])

    def __str__(self):
        return f"{self.journal} - Number: {self.number}, {self.title}"

    class Meta:
        permissions = []
        db_table = 'Volume'
