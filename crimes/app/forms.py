from django.forms import *
from .models import *


class PetitionForm(ModelForm):
    class Meta:
        model = Petitioner
        fields = ['name','father_name', 'address', 'contact','nic']


class AccusedForm(ModelForm):

    class Meta:
        model = Accused
        fields = ['name','father_name', 'alias', 'address', 'nic', 'gender', 'dob', 'status', 'contact', 'phone', 'email']


class VictimForm(ModelForm):

    class Meta:
        model = Victim
        fields = ['name', 'father_name', 'address', 'contact', 'nic']

class IncidentForm(ModelForm):

    class Meta:
        model = Incident
        fields = ['place', 'date']

class InvestigationOfficerForm(ModelForm):

    class Meta:
        model = InvestigationOfficer
        fields = ['name', 'dob', 'rank', 'contacts']

class FIRForm(ModelForm):
    incident = ModelChoiceField(queryset=Incident.objects.all(), required=False)
    petitioner = ModelChoiceField(queryset=Petitioner.objects.all(), required=False)
    accused = ModelChoiceField(queryset=Accused.objects.all(), required=False)

    class Meta:
        model = FIR
        fields = ['date_lodged',  'complaint', 'incident', 'petitioner', 'accused']


class CaseForm(ModelForm):

    class Meta:
        model = Case
        fields = ['law_section', 'case_status', 'case_detail', 'FIR', 'investigation_officer']


class UpdatePetitionForm(ModelForm):
    id  = IntegerField(required=True)
    nic = CharField(required=False)
    class Meta:
        model = Petitioner
        fields = ['name','father_name', 'address', 'contact','nic']


class UpdateAccusedForm(ModelForm):
    id = IntegerField(required=True)

    class Meta:
        model = Accused
        fields = ['name','father_name', 'alias', 'address', 'nic', 'gender', 'dob', 'status', 'contact', 'phone', 'email']


class UpdateVictimForm(ModelForm):
    id  = IntegerField(required=True)

    class Meta:
        model = Victim
        fields = ['name', 'father_name', 'address', 'contact', 'nic']


class UpdateIncidentForm(ModelForm):
    id  = IntegerField(required=True)

    class Meta:
        model = Incident
        fields = ['place', 'date']


class UpdateInvestigationOfficerForm(ModelForm):
    id  = IntegerField(required=True)

    class Meta:
        model = InvestigationOfficer
        fields = ['name', 'dob', 'rank', 'contacts']


class UpdateFIRForm(ModelForm):
    id  = IntegerField(required=True)
    incident = ModelChoiceField(queryset=Incident.objects.all(), required=False)
    petitioner = ModelChoiceField(queryset=Petitioner.objects.all(), required=False)
    accused = ModelChoiceField(queryset=Accused.objects.all(), required=False)

    class Meta:
        model = FIR
        fields = ['date_lodged',  'complaint', 'incident', 'petitioner', 'accused']


class UpdateCaseForm(ModelForm):
    id  = IntegerField(required=True)
    class Meta:
        model = Case
        fields = ['law_section', 'case_status', 'case_detail', 'FIR', 'investigation_officer']

class DeleteForm(Form):

    id = IntegerField(required=True)

    class Meta:
        fields = ['id']