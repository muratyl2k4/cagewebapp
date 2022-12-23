from django.db import models


class Program(models.Model):
    programTitle = models.CharField(max_length=150 , unique = True)

    programAbstract = models.TextField(default="Program Özeti")

    programImage = models.ImageField(upload_to='djangouploads/programlar/images' , null=True)
    programFullImage = models.ImageField(upload_to='djangouploads/programlar/images' , null=True )

    def __str__(self):
        return str(self.id)