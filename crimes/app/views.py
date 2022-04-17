import django.db
from django.shortcuts import render
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):

    return render(request, 'home.html', {})

@csrf_exempt
def petitioner(request):
    ctx = {
        'type' : 'petitioner'
    }
    if request.method == 'POST':
        form = PetitionForm(request.POST)
        if form.is_valid():
            petitioner_data = form.cleaned_data
            p = Petitioner(
                **petitioner_data
            )
            p.save()
            ctx["id"] =p.pk

            return render(request, 'response.html', ctx)

    else:
        form = PetitionForm()
        ctx['form'] = form
    return render(request, 'genericForm.html', ctx)

@csrf_exempt
def GetAccusedForm(request):
    ctx = {
        'count' : 0,
        'type' : 'accused'
    }
    if request.method == 'POST':
        form = AccusedForm(request.POST)
        if form.is_valid():
            accused_data = form.cleaned_data

            a = Accused(
                **accused_data
            )
            a.save()
            ctx["id"] = a.pk
            return render(request,'response.html', ctx)

    else:
        form = AccusedForm()
        ctx['form'] = form

    return render(request, 'genericForm.html', ctx)

@csrf_exempt
def GetVictimForm(request):

    ctx = {
        'count' : 0,
        'type' : 'victim'
    }

    if request.method == 'POST':
        form = VictimForm(request.POST)
        if form.is_valid():
            Victim_data = form.cleaned_data

            a = Victim(
                **Victim_data
            )
            a.save()
            ctx["id"] = a.pk
            return render(request,'response.html', ctx)

    else:
        form = VictimForm()
        ctx['form'] = form

    return render(request, 'genericForm.html', ctx)

@csrf_exempt
def GetIncidentForm(request):

    ctx = {
        'count' : 0,
        'type' : 'incident'
    }

    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident_data = form.cleaned_data

            a = Incident(
                **incident_data
            )
            a.save()
            ctx["id"] = a.pk
            return render(request, 'response.html', ctx)
    else:
        form = IncidentForm()
        ctx['form'] = form
    print(ctx)
    return render(request, 'genericForm.html', ctx)

@csrf_exempt
def GetInvestigationOfficerForm(request):

    ctx = {
        'count' : 0,
        'type' : 'investigation-officer'
    }
    if request.method == 'POST':
        form = InvestigationOfficerForm(request.POST)
        if form.is_valid():
            IO_data = form.cleaned_data

            a = InvestigationOfficer(
                **IO_data
            )
            a.save()
            ctx["id"] = a.pk
            return render(request, 'response.html', ctx)
    else:
        form = InvestigationOfficerForm()
    ctx['form'] = form
    print(ctx)
    return render(request, 'genericForm.html', ctx)

@csrf_exempt
def GetFIRForm(request):

    ctx = {
        'count' : 0,
        'type' : 'FIR'
    }

    if request.method == 'POST':
        form = FIRForm(request.POST)
        if form.is_valid():
            fir_data = form.cleaned_data

            a = FIR(**fir_data)
            a.save()
            ctx["id"] = a.pk
            return render(request, 'response.html', ctx)
    else:
        form = FIRForm()
        ctx['form'] = form

    return render(request, 'genericForm.html',ctx)

@csrf_exempt
def GetCaseForm(request):

    ctx = {
        'count' : 0,
        'type' : 'case'
    }

    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case_data = form.cleaned_data
            a = Case(**case_data)
            a.save()
            ctx["id"] = a.pk
            return render(request, 'response.html', ctx)
    else:
        form = CaseForm()
        ctx['form'] = form

    return render(request, 'genericForm.html', ctx)


ObjSwitcher = {
    'petitioner' : Petitioner,
    'accused': Accused,
    'victim' : Victim,
    'incident': Incident,
    'investigation-officer': InvestigationOfficer,
    'fir': FIR,
    'case': Case,
}

@csrf_exempt
def showPetitioner(request, type):
    objects = list(ObjSwitcher[type].objects.all())
    ctx = {
        'count' : 0,
        'objects': objects,
        'type' : type
    }
    if objects:
        fields = objects[0].get_fields
        ctx['fields'] = fields
        return render(request, 'showcontent.html', ctx)

    else:
        return render(request, 'notpresent.html', ctx)

formSwitcher = {
        'petitioner' : UpdatePetitionForm,
        'accused': UpdateAccusedForm,
        'victim' : UpdateVictimForm,
        'incident': UpdateIncidentForm,
        'investigation-officer': UpdateInvestigationOfficerForm,
        'fir': UpdateFIRForm,
        'case': UpdateCaseForm,
}

@csrf_exempt
def updateForm(request, type):

    ctx = {
        'type': type,
        'op' : 'updated'
    }


    if request.method == 'POST' :
        form = formSwitcher[type](request.POST)
        ctx['form'] = form
        if form.is_valid():
            case_data = form.cleaned_data
            print(case_data)
            o = ObjSwitcher[type].objects.get(pk=case_data['id'])
            del case_data['id']
            for k,v in case_data.items():
                setattr(o,k,v)

            o.save()
            ctx["id"] = o.pk
            return render(request, 'updateResponse.html', ctx)

    else:
        form = formSwitcher[type]()
        ctx['form'] = form

    return render(request, 'genericForm.html', ctx)

@csrf_exempt
def deleteForm(request, type):

    ctx = {
        'type': type,
        'op' : 'delete'
    }

    if request.method == 'POST' :
        form = DeleteForm(request.POST)
        ctx['form'] = form
        if form.is_valid():
            case_data = form.cleaned_data
            ctx['id'] = case_data['id']
            try:
                instance = ObjSwitcher[type].objects.get(id=case_data['id'])
                instance.delete()
                return render(request, 'deletesuccess.html', ctx)
            except:
                return render(request, 'deletefailure.html', ctx)

    else:
        form = DeleteForm()
        ctx['form'] = form
    return render(request, 'genericForm.html', ctx)