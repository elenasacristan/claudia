from django.db import models

class Index(models.Model):
    heading = models.CharField(max_length=300, blank=True, default='')
    name = models.CharField(max_length=70, blank=True, default='')
    description1 = models.TextField()
    jobtitle = models.CharField(max_length=70, blank=True, default='')
    description2= models.TextField()
    cta = models.CharField(max_length=70, blank=True, default='')

    class Meta:
        verbose_name_plural = ("Index Content")

    def __str__(self):
        return format(self.heading)

class Services(models.Model):
    heading = models.CharField(max_length=300)
    description = models.TextField()
    subheading = models.CharField(max_length=70)

    class Meta:
        verbose_name_plural = ("Services")
    
    def description_as_list(self):
        return self.description.split('\n')

    def __str__(self):
        return "{} - {}".format(self.heading, self.description[:20])

class BulletPoint(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = ("Bullet Points")

    def __str__(self):
        return self.description[:20]

class About(models.Model):
    heading = models.CharField(max_length=300)
    subheading = models.CharField(max_length=300)
    description = models.TextField()
    sentence_bottom = models.CharField(max_length=300)
    cta = models.CharField(max_length=70)

    class Meta:
        verbose_name_plural = ("About Section")

    def description_as_list(self):
        return self.description.split('\n')

    def __str__(self):
        return "{} - {}".format(self.heading, self.description[:20])