from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Post
from django.utils.text import slugify


def create_slug(instance,new_slug=None):
    slug=slugify(instance.title)
    if new_slug is not None:
        slug= new_slug
    qs= Post.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug="%s-%s" %(slug, qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

@receiver(pre_save,sender=Post)
def pre_save_post_reciever(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


# pre_save.connect(pre_save_post_reciever,sender=Post)


