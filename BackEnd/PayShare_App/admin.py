from django.contrib import admin

from .models  import Transaction, BancomatSmartContract, SmartContract, Bancomat, UserApp, Group

# Register your models here.

admin.site.register(Transaction)
admin.site.register(UserApp)
admin.site.register(Bancomat)
admin.site.register(SmartContract)
admin.site.register(BancomatSmartContract)
admin.site.register(Group)
