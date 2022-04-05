from django.db import models

STATUS = (
    (0, "Arrested"),
    (1, "Escaped"),
    (2, "Bailed"),
    (3, "Released")
)


class Petitioner(models.Model):
    name = models.CharField(max_length=500, )
    father_name = models.CharField(max_length=500)
    address = models.TextField(max_length=1500, default="")
    contact = models.CharField(max_length=20)
    nic = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Accused(models.Model):
    name = models.CharField(max_length=500, verbose_name="Accused name")
    father_name = models.CharField(max_length=500, verbose_name="Verbose")
    alias = models.CharField(max_length=500, verbose_name="Accused alias")
    address = models.CharField(max_length=100, verbose_name="Accuse address")
    nic = models.CharField(max_length=1000, verbose_name="Accused NIC")
    gender = models.CharField(max_length=10, verbose_name="Accused gender")
    dob = models.DateField(verbose_name="Accused Date of birth")
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Accused status", )
    contact = models.CharField(max_length=20, verbose_name="Accused contact")
    phone = models.CharField(max_length=20, verbose_name="Accused phone")
    email = models.EmailField()
    photo = models.URLField(verbose_name="image of the accused")
    finger_print = models.URLField(verbose_name="accused fingerprint")

    def __str__(self):
        return self.name


class Victim(models.Model):

    name = models.CharField(max_length=500, verbose_name="Victim's name")
    father_name = models.CharField(max_length=500, verbose_name="Victim's father")
    address = models.CharField(max_length=500, verbose_name="Victim's address")
    contact = models.CharField(max_length=30, verbose_name="Victim's contact")
    nic = models.CharField(max_length=50, verbose_name="Victim's nic")

    def __str__(self):
        return self.name


class Incident(models.Model):
    place = models.TextField(max_length="")
    date = models.DateTimeField(editable=True)


class InvestigationOfficer(models.Model):
    officer_id = models.AutoField(verbose_name="Officer ID", primary_key=True)
    name = models.CharField(max_length=500, verbose_name="Officer Name")
    dob = models.DateField(verbose_name="Officer Date of birth")
    rank = models.IntegerField()
    contacts = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class FIR(models.Model):
    date_lodged = models.DateTimeField(editable=True)
    incident = models.ForeignKey(Incident, on_delete=models.PROTECT)
    petitioner = models.ForeignKey(Petitioner, on_delete=models.PROTECT)
    accused = models.ManyToManyField(Accused)

    def __str__(self):
        return self.incident.place

class Case(models.Model):
    case_id = models.IntegerField()
    law_section = models.TextField()
    case_status = models.CharField(max_length=100, verbose_name="case status")
    case_detail = models.TextField(max_length=10000)
    FIR = models.ForeignKey(FIR, on_delete=models.CASCADE)
    investigation_officer = models.ForeignKey(InvestigationOfficer, on_delete=models.CASCADE)

    def __str__(self):
        return self.case_id
