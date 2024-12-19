from django_filters import FilterSet
import django_tables2 as tables
from .models import Permit, Employee



class PersonTable(tables.Table):
    class Meta:
        model = Permit
        template_name = "django_tables2/bootstrap.html"
        fields = ("number", "status", "work_description", "master_of_work", "department")