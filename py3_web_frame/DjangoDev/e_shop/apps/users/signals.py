from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()


@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    """
    post_save:接收信号的方式
    sender: 接收信号的model
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    # 是否新建，因为update的时候也会进行post_save
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()