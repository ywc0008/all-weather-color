
from django.db import models


class SystemEvents(models.Model):
    CustomerID = models.CharField(max_length=1000, null=True)
    ReceivedAt = models.DateTimeField('ReceivedAt', null=True)
    DeviceReportedTime = models.DateTimeField('DeviceReportedTime', null=True)
    Facility = models.IntegerField(default=0, null=True)
    Priority = models.IntegerField(default=0, null=True)
    FromHost = models.CharField(max_length=1000, null=True)
    Message = models.CharField(max_length=1000, null=True)
    NTSeverity = models.IntegerField(default=0, null=True)
    Importance = models.IntegerField(default=0, null=True)
    EventSource = models.CharField(max_length=1000, null=True)
    EventUser = models.CharField(max_length=1000, null=True)
    EventCategory = models.IntegerField(default=0, null=True)
    EventID = models.IntegerField(default=0, null=True)
    EventBinaryData = models.CharField(max_length=1000, null=True)
    MaxAvailable = models.IntegerField(default=0, null=True)
    CurrUsage = models.IntegerField(default=0, null=True)
    MinUsage = models.IntegerField(default=0, null=True)
    MaxUsage = models.IntegerField(default=0, null=True)
    InfoUnitID = models.IntegerField(default=0, null=True)
    SysLogTag = models.CharField(max_length=1000, null=True)
    EventLogType = models.CharField(max_length=1000, null=True)
    GenericFileName = models.CharField(max_length=1000, null=True)
    SystemID = models.IntegerField(default=0, null=True)

    class Meta:
        db_table ='SystemEvents'


class SystemEventsProperties(models.Model):
    question = models.ForeignKey(SystemEvents, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    class Meta:
        db_table ='SystemEventsProperties'