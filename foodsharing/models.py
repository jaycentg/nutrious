from django.db import models

# Create your models here.
from home.models import AppUser

class Sharing(models.Model):
    author = models.ForeignKey(AppUser, on_delete= models.CASCADE, related_name='foodsharing_posts')
    location = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    img = models.URLField(default = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fartsmidnorthcoast.com%2Flisting%2Fa-device-for-orienting-oneself-at-the-centre-of-the-universe%2Fno-image-available-icon-6%2F&psig=AOvVaw2-dCd7UtB_XHJmMsY7WB88&ust=1666987680917000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCMj01ZabgfsCFQAAAAAdAAAAABAE")

    class Meta:
        # descending order
        ordering = ['-date']