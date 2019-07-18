# Generated by Django 2.2.3 on 2019-07-09 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150, verbose_name='Logradouro')),
                ('number', models.CharField(blank=True, max_length=10, verbose_name='Numero')),
                ('complement', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complemento')),
                ('city', models.CharField(max_length=150, verbose_name='Cidade')),
                ('state', models.CharField(max_length=150, verbose_name='Estado')),
                ('country', models.CharField(default='Brasil', max_length=150, verbose_name='País')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endreços',
                'ordering': ['city', 'state'],
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('name', models.CharField(max_length=30, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=30, verbose_name='Sobrenome')),
                ('age', models.DateField(verbose_name='Idade')),
                ('email', models.EmailField(max_length=80, verbose_name='Email')),
                ('comission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comission', to='comission.ComissionPlan', verbose_name='Comissao')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='seller.Address', verbose_name='Endereco')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
                'ordering': ['name', 'age'],
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddd', models.CharField(max_length=2, verbose_name='DDD')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Numero')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_phone', to='seller.Seller', verbose_name='Vendedor')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
                'ordering': ['ddd', 'phone_number'],
            },
        ),
    ]
