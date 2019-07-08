# Generated by Django 2.2.3 on 2019-07-08 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendedor', '0003_auto_20190708_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_venda', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Média comissão')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificacoes_vendedor', to='vendedor.Vendedor', verbose_name='Notificacoes')),
            ],
            options={
                'verbose_name': 'Notificação',
                'verbose_name_plural': 'Notificações',
                'ordering': ['-media_venda'],
            },
        ),
    ]
