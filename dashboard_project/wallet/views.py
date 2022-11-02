from django.views.generic import ListView, View
from django.http import JsonResponse

from decimal import Decimal
from .models import WalletUsers


class UsersView(ListView):
    model = WalletUsers
    template_name = 'index.html'
    context_object_name = 'users'


class CreateUserView(View):
    def post(self, request):
        obj = WalletUsers.objects.create(
            firstname = request.POST.get('firstname'),
            lastname = request.POST.get('lastname'),
            email = request.POST.get('email'),
            balance = request.POST.get('balance')
        )

        data = {
            'id': obj.id,
            'firstname': obj.firstname,
            'lastname': obj.lastname,
            'email': obj.email,
            'balance': obj.balance,
        }

        # return redirect('/')

        return JsonResponse(data, safe=False)

class CreditUserView(View):
    def get(self, request):
        id = request.GET.get('id')
        credit = request.GET.get('credit')
        credit = checkIfDecimal(credit)
        obj = WalletUsers.objects.get(id=id)
        obj.balance += Decimal(f'{credit}.00')
        obj.save()
        data = {
            'balance': obj.balance
        }
        return JsonResponse(data)


class DebitUserView(View):
    def get(self, request):
        id = request.GET.get('id')
        debit = request.GET.get('debit')
        debit = checkIfDecimal(debit)
        obj = WalletUsers.objects.get(id=id)
        obj.balance -= Decimal(f'{debit}.00')
        obj.save()
        data = {
            'balance': obj.balance
        }
        return JsonResponse(data)


class DeleteUserView(View):
    def  get(self, request):
        id = request.GET.get('id', None)
        WalletUsers.objects.get(id=id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

def checkIfDecimal(num):
    num = int(num)
    if num//1 == num/1:
        return num
    else:
        return num[:-2]



        

   