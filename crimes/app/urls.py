"""crimes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    re_path(r'^petitioner/', petitioner),
    re_path(r'^accused/', GetAccusedForm),
    re_path(r'^victim/', GetVictimForm),
    re_path(r'^incident/', GetIncidentForm),
    re_path(r'^investigationOfficer/', GetInvestigationOfficerForm),
    re_path(r'^firForm/', GetFIRForm),
    re_path(r'^case/', GetCaseForm),
    re_path(r'^showpetitioner/', showPetitioner, {'type':'petitioner'}),
    re_path(r'^showAccused/', showPetitioner, {'type':'accused'}),
    re_path(r'^showVictim/', showPetitioner, {'type':'victim'}),
    re_path(r'^showIncident/', showPetitioner, {'type':'incident'}),
    re_path(r'^showInvestigationOfficer/', showPetitioner, {'type':'investigation-officer'}),
    re_path(r'^showFIR/', showPetitioner, {'type':'fir'}),
    re_path(r'^showcase/', showPetitioner, {'type':'case'}),
    re_path(r'^updatePetitioner/', updateForm, {'type': 'petitioner'}),
    re_path(r'^updateAccused/', updateForm, {'type': 'accused'}),
    re_path(r'^updateVictim/', updateForm, {'type': 'victim'}),
    re_path(r'^updateIncident/', updateForm, {'type': 'incident'}),
    re_path(r'^updateInvestigationOfficer/', updateForm, {'type': 'investigation-officer'}),
    re_path(r'^updateFIR/', updateForm, {'type': 'fir'}),
    re_path(r'^updateCase/', updateForm, {'type': 'case'}),
    re_path(r'^deletePetitioner', deleteForm, {'type': 'petitioner'}),
    re_path(r'^deleteAccused/', deleteForm, {'type': 'accused'}),
    re_path(r'^deleteVictim/', deleteForm, {'type': 'victim'}),
    re_path(r'^deleteIncident/', deleteForm, {'type': 'incident'}),
    re_path(r'^deleteInvestigationOfficer/', deleteForm, {'type': 'investigation-officer'}),
    re_path(r'^deleteFIR/', deleteForm, {'type': 'fir'}),
    re_path(r'^deleteCase/', deleteForm, {'type': 'case'}),
    re_path(r'', home),
]

