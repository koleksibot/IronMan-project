from django.db import models
import datetime


class AboutUs(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    details = models.TextField(default='I am A...')
    image = models.ImageField(upload_to="Other/AboutUs/", null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '%s' % self.name + ', ' + str(self.time_stamp)

    def save(self, *args, **kwargs):
        """
        This part is very important for uploading a file because
        It will replace the previous file and insert the new file.
        :return: delete old file when replacing by updating the file
        """
        try:
            this = AboutUs.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(AboutUs, self).save(*args, **kwargs)