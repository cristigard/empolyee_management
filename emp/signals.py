from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Employee, DeletedEmployee


@receiver(pre_delete, sender=Employee)
def delete_person(sender, instance, using, **kwargs):
    DeletedEmployee.objects.create(first_name = instance.first_name, 
                                    last_name = instance.last_name,
                                    email = instance.email,
                                    manager = str(instance.manager),
                                    cim = int(instance.cim), 
                                    role = instance.role,
                                    employment_date= instance.employment_date
                                    )