# Generated by Django 4.2.1 on 2023-06-24 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bancomat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.CharField(max_length=250)),
                ('extensions', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UserApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('fiscalCode', models.CharField(max_length=250)),
                ('birthDate', models.DateField()),
                ('birthPlace', models.CharField(max_length=250)),
                ('residence', models.CharField(max_length=250)),
                ('smartContractList', models.CharField(max_length=250)),
                ('extensions', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'PayShare_App_userApp',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipientCode', models.CharField(max_length=250)),
                ('idUserApp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PayShare_App.userapp')),
            ],
        ),
        migrations.CreateModel(
            name='SmartContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userAppIdList', models.CharField(max_length=250)),
                ('transactionIdList', models.CharField(max_length=250)),
                ('extensions', models.CharField(max_length=250)),
                ('finalTransactionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PayShare_App.transaction')),
                ('idBancomat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PayShare_App.bancomat')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('userAppList', models.CharField(max_length=250)),
                ('bEnd', models.CharField(max_length=250)),
                ('dStart', models.CharField(max_length=250)),
                ('dateEnd', models.DateField()),
                ('bFinalObjcet', models.BooleanField()),
                ('importObject', models.CharField(max_length=250)),
                ('split', models.CharField(max_length=250)),
                ('extensions', models.CharField(max_length=250)),
                ('recipientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PayShare_App.userapp')),
                ('smartContractId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PayShare_App.smartcontract')),
            ],
        ),
        migrations.CreateModel(
            name='BancomatSmartContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bEnd', models.BooleanField()),
                ('idBancomat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PayShare_App.bancomat')),
                ('idSmartContract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PayShare_App.smartcontract')),
            ],
        ),
    ]
