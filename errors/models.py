from django.db import models


# Create your models here.
class Error(models.Model):
    PRESENTATION = 'P'    # Error that only affects a view but no a feature
    FEATURE = 'F'         # Error that only affects a specific feature
    APPLICATION = 'A'     # Error that affects the entire application
    ETYPE_CHOICES = [
        (PRESENTATION, "PRESENTATION"),
        (FEATURE, "FEATURE"),
        (APPLICATION, "APPLICATION"),
    ]

    BACKEND = 'B'
    FRONTEND = 'F'
    MOBILE = 'M'
    DESKTOP = 'D'
    LAYER_CHOICES = [
        (BACKEND, "BACKEND"),
        (FRONTEND, "FRONTEND"),
        (APPLICATION, "APPLICATION"),
        (DESKTOP, "DESKTOP"),
    ]

    e_type = models.CharField("Tipo de erro", max_length=25, choices=ETYPE_CHOICES)
    e_msg = models.TextField("Mensagem de erro")
    application = models.CharField("Aplicação", max_length=50)
    layer = models.CharField("Camada", max_length=25, choices=LAYER_CHOICES)
    time = models.DateTimeField("Hora", auto_now_add=True)

    @property
    def pretty_time(self):
        return self.time.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.application} | {self.get_layer_display()} | {self.get_e_type_display()} | {self.pretty_time}"
