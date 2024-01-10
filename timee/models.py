from django.db import models

class Headlines(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=5000)
    description = models.TextField()
    published_date = models.DateTimeField()
    category = models.CharField(max_length=200, null=True, blank=True)
    source = models.CharField(max_length=100)
    image_urls= models.URLField(max_length=1000,default=None,blank=True, null=True)
    related_news = models.ManyToManyField('self', symmetrical=False, related_name='related_by', blank=True)
    other_sources = models.ManyToManyField('Source', related_name='headlines')

    

    def __str__(self):
        return self.title
    

class Source(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name
    


class LastFetchTime(models.Model):
    update_time = models.DateTimeField()

    @classmethod
    def get_last_update_time(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj.update_time
    
    @classmethod
    def set_last_update_time(cls, new_time):
        obj, created = cls.objects.get_or_create(pk=1)
        obj.update_time = new_time
        obj.save()

class Firme(models.Model):
    id_broj = models.CharField(max_length=100,default=None)
    naziv_kompanije = models.CharField(max_length=100,default=None)
    adresa = models.CharField(max_length=50,default=None)
    sifra = models.IntegerField(max_length=50,default=None)
    opstina = models.CharField(max_length=50,default=None)

    def __str__(self):
        return self.naziv_kompanije
