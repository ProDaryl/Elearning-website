from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Assign permissions to the Teacher group'

    def handle(self, *args, **kwargs):
        # Get or create the Teacher group
        teacher_group, created = Group.objects.get_or_create(name='Teacher')

        # Get the permission
        add_course_permission = Permission.objects.get(codename='add_course')

        # Assign the permission to the group
        teacher_group.permissions.add(add_course_permission)

        student_group, created = Group.objects.get_or_create(name='Student')
        student_group.permissions.remove(add_course_permission)

        self.stdout.write(self.style.SUCCESS('Successfully assigned permissions to Teacher group'))
