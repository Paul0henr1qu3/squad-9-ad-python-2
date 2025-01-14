from django.db import models
from seller.models import Seller


class Vendas(models.Model):
    """
        Modelo que representa a venda mensal do vendedor
    """
    meses = (('Janeiro', 'Janeiro'), ("Fevereiro", "Fevereiro"), ("Março", "Março"), ("Abril", "Abril"),
             ("Maio", "Maio"), ("Junho", "Junho"), ("Julho", "Julho"), ("Agosto", "Agosto"), ("Setembro", "Setembro"),
             ("Outubro", "Outubro"), ("Novembro", "Novembro"), ("Dezembro", "Dezembro"))

    seller = models.ForeignKey(Seller, related_name='comissao_vendedor', on_delete=models.CASCADE,
                                 verbose_name='Vendedor')

    month = models.CharField(verbose_name="Mes", choices=meses, null=False, blank=False, max_length=15)

    amount = models.DecimalField(verbose_name="Valor Minimo", decimal_places=2, max_digits=12, blank=False,
                                       null=False)

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ['-amount', ]
