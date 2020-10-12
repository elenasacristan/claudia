from django.db import models

class Index(models.Model):
    heading = models.CharField(max_length=300)
    description = models.TextField()
    cta = models.CharField(max_length=70)

    def __str__(self):
        return "{} - {}".format(self.heading, self.description[:20])

class Services(models.Model):
    heading = models.CharField(max_length=300)
    description = models.TextField()
    subheading = models.CharField(max_length=70)

    def __str__(self):
        return "{} - {}".format(self.heading, self.description[:20])

class BulletPoint(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description[:20]

class About(models.Model):
    heading = models.CharField(max_length=300)
    subheading = models.CharField(max_length=300)
    description = models.TextField()
    sentence_bottom = models.CharField(max_length=300)
    cta = models.CharField(max_length=70)

    def __str__(self):
        return "{} - {}".format(self.heading, self.description[:20])