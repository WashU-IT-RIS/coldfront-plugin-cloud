from coldfront.core.resource.models import Resource, ResourceType
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        resource_type_obj = ResourceType.objects.get("storage")
        parent_resource_obj = None

        Resource.objects.get_or_create(
            resource_type=resource_type_obj,
            parent_resource=None,
            name="Qumulo",
            description="Qumulo storage",
            is_available=True,
            is_public=True,
            is_allocatable=True,
            requires_payment=True,
        )
