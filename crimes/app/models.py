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

    class Meta:
        db_table = "petitioner"
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Petitioner._meta.fields]

    def __str__(self):
        return self.name


class Accused(models.Model):
    name = models.CharField(max_length=500, verbose_name="Accused name")
    father_name = models.CharField(max_length=500, verbose_name="Verbose")
    alias = models.CharField(max_length=500, verbose_name="Accused alias")
    address = models.CharField(max_length=100, verbose_name="Accuse address")
    nic = models.CharField(max_length=1000, verbose_name="Accused NIC", unique=True)
    gender = models.CharField(max_length=10, verbose_name="Accused gender")
    dob = models.DateField(verbose_name="Accused Date of birth")
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Accused status", )
    contact = models.CharField(max_length=20, verbose_name="Accused contact")
    phone = models.CharField(max_length=20, verbose_name="Accused phone")
    email = models.EmailField()
    photo = models.URLField(verbose_name="image of the accused")
    finger_print = models.URLField(verbose_name="accused fingerprint")

    class Meta:
        db_table = "accused"
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Accused._meta.fields]

    def __str__(self):
        return self.name


class Victim(models.Model):
    name = models.CharField(max_length=500, verbose_name="Victim's name")
    father_name = models.CharField(max_length=500, verbose_name="Victim's father")
    address = models.CharField(max_length=500, verbose_name="Victim's address")
    contact = models.CharField(max_length=30, verbose_name="Victim's contact")
    nic = models.CharField(max_length=50, verbose_name="Victim's nic", unique=True)

    class Meta:
        db_table = "victim"
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Victim._meta.fields]

    def __str__(self):
        return self.name


class Incident(models.Model):
    place = models.TextField(max_length=100)
    date = models.DateTimeField(editable=True)
    class Meta:
        db_table = "incident"
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Incident._meta.fields]

    def __str__(self):
        return self.place


class InvestigationOfficer(models.Model):
    name = models.CharField(max_length=500, verbose_name="Officer Name")
    dob = models.DateField(verbose_name="Officer Date of birth")
    rank = models.IntegerField()
    contacts = models.CharField(max_length=30)
    class Meta:
        db_table = "investigation-officer"
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in InvestigationOfficer._meta.fields]

    def __str__(self):
        return self.name


class FIR(models.Model):
    date_lodged = models.DateTimeField(editable=True)
    class Meta:
        db_table = "fir"
    complaint = models.TextField(max_length=10000)
    incident = models.ForeignKey(Incident, on_delete=models.PROTECT, null=True)
    petitioner = models.ForeignKey(Petitioner, on_delete=models.PROTECT, null=True)
    accused = models.ForeignKey(Accused, on_delete=models.PROTECT, null=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in FIR._meta.fields]

    def __str__(self):
        return self.incident.place


class Case(models.Model):
    law_section = models.TextField()
    case_status = models.CharField(max_length=100, verbose_name="case status")
    case_detail = models.TextField(max_length=10000)
    FIR = models.ForeignKey(FIR, on_delete=models.CASCADE)
    investigation_officer = models.ForeignKey(InvestigationOfficer, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = "case"
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Case._meta.fields]

    def __str__(self):
        return self.FIR
