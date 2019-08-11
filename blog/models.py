from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    datebox = models.DateField()
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.datebox.strftime('%b %e %Y')
    