import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swat_musassa.settings')
django.setup()
from django.db.models import OuterRef, Subquery, F, Count, Q
from app.models import VisaRenewal, Employe, SaudiKapilDetail, TrackEmail
from datetime import timedelta, date
from django.conf import settings
from django.urls import reverse_lazy
from core.models import VisaType


# for key, valu in settings.COUNTRIES_WITH_FLAGS.items():
    
#     print(key, valu)

# COUNTRY_CHOICES = [(key, value) for value, key in settings.COUNTRIES_WITH_FLAGS.items()]
# print(settings.COUNTRIES_WITH_FLAGS.items().__len__() == COUNTRY_CHOICES.__len__())

# print(SaudiKapilDetail.del_items.get(id="65ef329c-4ebc-4fb2-b41c-826b4ef419ba"))

# print(VisaType.objects.all())

# emp = Employe.objects.all().first()
# TrackEmail.objects.create(employe=emp, issue_date=emp.issue_date, expiry_date=emp.expiry_date)

# outer = TrackEmail.objects.filter(employe=OuterRef("pk")).values_list("employe__id")


# track_emails = TrackEmail.objects.filter(
#             employe=OuterRef("pk"), 
#             issue_date=F("employe__issue_date"),expiry_date=F("employe__expiry_date")
#                                                  ).values_list("employe__id",flat=True)

# print(TrackEmail.objects.filter(created_at__date=date.today()))


# TrackEmail.objects.all().delete()