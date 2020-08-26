from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from adminsortable.models import SortableMixin

class Machine(SortableMixin):
    name = models.CharField(verbose_name="マシン名", max_length=100)
    progress = models.IntegerField(verbose_name="進行度", default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ["the_order"]

    def __str__(self):
        return self.name
