from django.db import models

# Create your models here.
from django.db.models import F


class Locomotive(models.Model):
    model_name = models.TextField("Name of Model", primary_key=True)
    sections = models.DecimalField("Count of sectioins", decimal_places=0, max_digits=3)

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = "Locomotive"
        verbose_name_plural = "Locomotives"


class AvailableTechwork(models.Model):
    id = models.AutoField('ID', primary_key=True)
    to_name = models.TextField("Name of TO", default='None', max_length=144)

    def __str__(self):
        return self.to_name

    class Meta:
        verbose_name = "AvailableTechwork"
        verbose_name_plural = "AvailableTechworks"


class TechWork(models.Model):
    to_name = models.TextField("Name of TO", default='None', max_length=144)
    model_name = models.ForeignKey('Locomotive', on_delete=models.CASCADE)
    norms_in_days = models.FloatField("Norms in days", default=0)

    def __int__(self):
        return str(self.model_name) + str(self.to_name)

    class Meta:
        verbose_name = "TechWork"
        verbose_name_plural = "TechWorks"
        unique_together = (("to_name", "model_name"),)


class MonthWorkDay(models.Model):
    year = models.IntegerField("Year", default="2023")
    month = models.TextField("Month", default="Jan")
    workdays = models.DecimalField("Count of workdays", decimal_places=0, max_digits=3)

    def __str__(self):
        return self.month + '[' + str(self.year) + ']'

    class Meta:
        verbose_name = "MonthWorkDay"
        verbose_name_plural = "MonthWorkDays"
        unique_together = (("year", "month"),)


class Canava(models.Model):
    record_name = models.TextField("Name of record", default='rls-depo', max_length=144, primary_key=True)
    place_column = models.IntegerField("Column", default=1)
    place_row = models.IntegerField("Row", default=1)
    machine = models.ForeignKey('Locomotive', on_delete=models.CASCADE, default='Свободно')

    def __str__(self):
        return "Column " + str(self.place_column) + " - " + "Row " + str(self.place_row)

    class Meta:
        verbose_name = "Canava"
        verbose_name_plural = "Canavas"


class CellRecord(models.Model):
    locomotive = models.ForeignKey('Locomotive', on_delete=models.CASCADE, default='ТЭМ2')
    techwork = models.ForeignKey('AvailableTechwork', on_delete=models.CASCADE, default='TO-3')
    month = models.ForeignKey('MonthWorkDay', on_delete=models.CASCADE, default='Dec[2023]')
    volume = models.DecimalField("Volume", decimal_places=1, max_digits=3, editable=False, default=1)

    def __str__(self):
        return str(self.locomotive) + ' - ' + str(self.techwork) + ' - ' + str(self.month)

    class Meta:
        verbose_name = "CellRecord"
        verbose_name_plural = "CellRecords"
        unique_together = (("locomotive", "techwork", "month"),)

    def save(self, *args, **kwargs):
        try:
            ids = CellRecord.objects.get(id=self.id)
        except CellRecord.DoesNotExist:
            ids = None
        if ids:  # if some items are found in the database
            self.volume = ids.volume + 1
            return super(CellRecord, self).save(*args, **kwargs)
        else:
            return super(CellRecord, self).save(*args, **kwargs)
