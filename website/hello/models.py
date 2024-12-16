from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from docxtpl import DocxTemplate


# Create your models here.

# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     postemploee = models.CharField(max_length=50)






class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    create_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TypeOfWork(models.Model):
    name = models.CharField(max_length=255, unique=True)

    create_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class Employee(AbstractBaseUser, PermissionsMixin):
    roles = {
        "DIRECTOR": "DIRECTOR",
        "MASTER": "MASTER",
        "WORKER": "WORKER",
        "DAILYMANAGER": "DAILYMANAGER",
        "STATIONENGINEER": "STATIONENGINEER",
    }
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=255, choices=roles)
    email = models.EmailField(unique=True)

    # optional fields
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name


class Permit(models.Model):
    type_of_permit = {
        "SIMPLE": "simple",
        "LINEAR": "linear",
        "FIRE": "fire",
    }

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, verbose_name="Департамент")
    type_of_permit_create = models.CharField(max_length=255, choices=type_of_permit)
    number = models.CharField(max_length=255, null=False)
    master_of_work = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="masterofwork")
    executor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="executorofwork")
    countWorker = models.CharField(max_length=255, null=False)
    employ = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="employofwork")
    master = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="master")
    master_signature = models.CharField(max_length=255)
    work_description = models.CharField(max_length=255)
    start_of_work = models.DateTimeField(max_length=255)
    end_of_work = models.DateTimeField(max_length=255)

    #    type_of_work = ArrayField(
    #       ArrayField(
    #          models.CharField(max_length=10, blank=True),
    #         size=8,
    #     ),
    #     size=8,
    # )
    condition = models.CharField(max_length=255)

    director = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="time")
    signature_from_director = models.CharField(max_length=255)

    daily_manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="dailymanager")
    signature_from_daily_manager = models.CharField(max_length=255)

    station_engineer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="statengineer")
    signature_from_station_engineer = models.CharField(max_length=255)

    create_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # file_name = models.CharField(max_length=255)
    # file_path = models.CharField(max_length=255)

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        # if self.signature_from_daily_manager:
        #     hp = HistoryPermit(
        #
        #     )
        #     hp.save()
        super(Permit, self).save(*args)

    def __str__(self):
        return self.number

    def to_docx(self):
        doc = DocxTemplate("C:\\Users\\Сергей\\Desktop\\Шаблоны для ЭНД\\test.docx")
        context = {
            'manager': self.master_of_work,
            'managerPost': self.master,
            'executor': self.executor,
            'executorPost': self.executor,
            'countMember': self.master,
            'member': self.executor,
            'work': self.work_description,
            'dateStart': self.start_of_work,
            'timeStart': self.start_of_work,
            'dateEnd': self.end_of_work,
            'timeEnd': self.end_of_work,
            'dateDelivery': self.master,
            'timeDelivery': self.master,
            'conditions': self.condition,
            'director': self.director,
            'directorPost': self.director,
            'personal': self.executor,
            'personalPost': self.executor
        }
        doc.render(context)

        doc.save(self.generate_file_name())

    def generate_file_name(self) -> str:
        return self.number.__str__() + ".docx"

    def print_docx(self):
        pass

    def signature(self): #-> #State:
        pass
        #
        # # if self.master_signature is None:
        # #     return State{
        # #         self.master
        # #     }
        # # if self.signature_from_daily_manager
        # MOCK_ADDRESS = constants.ZERO_ADDRESS
        # DEFAULT_INITIAL_BALANCE = to_wei(10000, 'ether')
        #
        # GENESIS_PARAMS = {
        #     'difficulty': constants.GENESIS_DIFFICULTY,
        # }
        #
        # GENESIS_STATE = {
        #     MOCK_ADDRESS: {
        #         "balance": DEFAULT_INITIAL_BALANCE,
        #         "nonce": 0,
        #         "code": b'',
        #         "storage": {}
        #     }
        # }
        #
        # chain = BaseMainnetChain.vm_configuration(AtomicDB(), GENESIS_PARAMS, GENESIS_STATE)
        #
        # mock_address_balance = chain.get_vm().state.get_balance(MOCK_ADDRESS)
        #
        # print(f"The balance of address {encode_hex(MOCK_ADDRESS)} is {mock_address_balance} wei")

        # return State

class State:
    permit: Permit
    who_notify: [Employee]


class HistoryPermit(models.Model):
    type_of_permit = {
        "SIMPLE": "simple",
        "LINEAR": "linear",
        "FIRE": "fire",
    }

    department_name = models.CharField(max_length=255)
    type_of = models.CharField(max_length=255, choices=type_of_permit)
    number = models.CharField(max_length=255, null=False)
    master_of_work = models.CharField(max_length=255)
    worker = models.CharField(max_length=255)
    # employ =
    master = models.CharField(max_length=255)
    work_description = models.CharField(max_length=255)
    start_of_work = models.DateTimeField(max_length=255)
    end_of_work = models.DateTimeField(max_length=255)
    #    type_of_work = ArrayField(
    #       ArrayField(
    #          models.CharField(max_length=10, blank=True),
    #         size=8,
    #     ),
    #     size=8,
    # )
    condition = models.CharField(max_length=255)

    time_of_permit = models.CharField(max_length=255, verbose_name="Наряд выдал")
    signature_from_director = models.CharField(max_length=255)
    signature_from_daily_manager = models.CharField(max_length=255)

    create_at = models.DateTimeField()
    updated_at = models.DateTimeField()



