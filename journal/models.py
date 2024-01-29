from django.db import models
from django.core.validators import FileExtensionValidator


class Journal(models.Model):
    name = models.CharField(unique=True, max_length=50)
    logo = models.ImageField(upload_to='journal_logos/', null=True)
    creationDate = models.DateTimeField(null=True)
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Volume(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=300)
    description = models.TextField()
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    releaseDate = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='volume_images/', null=True)
    file = models.FileField(upload_to='volume_files/', null=True, validators=[
        FileExtensionValidator(allowed_extensions='pdf')])

    def __str__(self):
        return f"{self.journal} - {self.title}"
