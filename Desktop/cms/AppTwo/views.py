from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth  import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from AppTwo.models import Client
from datetime import date
from django.contrib import messages
from django.core.exceptions import ValidationError

# Create your views here.


def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)

        if user:
            login(request, user)

            return HttpResponseRedirect(reverse('user_cms'))
        else:
            context["error"]= "Invalid Username or password. Please try again."
            return render(request, "AppTwo/login.html", context)
    else:
        return render(request,"AppTwo/login.html",context)


def cms(request):
    context = {}
    context['user']= request.user
    all_clients= Client.objects.all()

    today = str(date.today())

    ordered_dates = Client.objects.order_by('expiry_date').filter(expiry_date__gte= today)

    expiring_hosting = Client.objects.order_by('hosting_expiry_date').filter(hosting_expiry_date__gte= today)

    sll_expiry_dates = Client.objects.order_by('sll_expiry_date').filter(sll_expiry_date__gte= today)

    amc_expiry_dates = Client.objects.order_by('amc_expiry_date').filter(amc_expiry_date__gte= today)

    update_log= Client.objects.order_by('updated_date').filter(updated_date__lte= today)

    chatbot_last_dates= Client.objects.order_by('chatbot_last_date').filter(chatbot_last_date__lte= today)

    return render(request,"AppTwo/cms.html",{'view_clients':all_clients,'dates':ordered_dates,'hostingdates':expiring_hosting,
    'sll_dates':sll_expiry_dates, 'amc_dates':amc_expiry_dates, 'updated_logs':update_log,'chatbot_dates':chatbot_last_dates})


def user_logout(request):
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))



def show_form(request):

    return render(request,"AppTwo/addclient.html" )



def form_submit(request):


    client_name = request.POST['client_name']
    location = request.POST['location']
    email = request.POST['email']
    phone = request.POST['phone']
    reference = request.POST['reference']
    project_name = request.POST['project_name']
    domain_name = request.POST['domain_name']
    acc_name = request.POST['acc_name']
    acc_password = request.POST['acc_password']
    purchase_date = request.POST['purchase_date']
    expiry_date = request.POST['expiry_date']
    amount = request.POST['amount']

    hosting_account = request.POST['hosting_account']
    hosting_pass = request.POST['hosting_pass']
    hosting_date = request.POST['hosting_date']
    hosting_expiry_date = request.POST['hosting_expiry_date']
    hosting_amount = request.POST['hosting_amount']

    sll_type = request.POST['sll_type']
    sll_account = request.POST['sll_account']
    sll_date = request.POST['sll_date']
    sll_expiry_date = request.POST['sll_expiry_date']
    sll_amount = request.POST['sll_amount']

    amc_date = request.POST['amc_date']
    amc_expiry_date = request.POST['amc_expiry_date']
    amc_amount = request.POST['amc_amount']

    project_update = request.POST['project_update']
    updated_date = request.POST['updated_date']
    project_details = request.POST['project_details']
    time_spent=request.POST['time_spent']

    chatbot_type = request.POST['chatbot_type']
    credits_purchased = request.POST['credits_purchased']
    chatbot_amount = request.POST['chatbot_amount']
    chatbot_date = request.POST['chatbot_date']
    chatbot_last_date = request.POST['chatbot_last_date']


    my_clients = Client(client_name=client_name,location=location,email=email ,phone=phone,reference=reference,
            project_name=project_name,domain_name=domain_name,acc_name=acc_name,acc_password=acc_password,
            purchase_date=purchase_date,expiry_date=expiry_date,amount=amount,
            hosting_account=hosting_account,hosting_pass=hosting_pass,hosting_date=hosting_date,
            hosting_expiry_date=hosting_expiry_date,hosting_amount=hosting_amount,
            sll_type=sll_type, sll_account=sll_account, sll_date=sll_date, sll_expiry_date=sll_expiry_date, sll_amount=sll_amount,
            amc_date=amc_date, amc_expiry_date=amc_expiry_date, amc_amount=amc_amount,
            project_update=project_update, updated_date=updated_date, project_details=project_details,time_spent=time_spent,
            chatbot_type=chatbot_type, credits_purchased=credits_purchased, chatbot_amount=chatbot_amount, chatbot_date=chatbot_date, chatbot_last_date=chatbot_last_date)


    my_clients.save()
    messages.success(request,'Client Data saved successfully! ')
    return HttpResponseRedirect(reverse('add_client'))

    # else:
    #      raise ValidationError("value has an invalid date format. It must be in YYYY-MM-DD format.")




def edit_client(request,id):

    all_clients = Client.objects.get(id=id)
    context= {'all_clients':all_clients}
    return render(request,'AppTwo/edit-client.html',context)

def update(request,id):

    all_clients= Client.objects.get(id=id)

    all_clients.client_name = request.POST['client_name']
    all_clients.location = request.POST['location']
    all_clients.email = request.POST['email']
    all_clients.phone = request.POST['phone']
    all_clients.reference = request.POST['reference']
    all_clients.project_name = request.POST['project_name']
    all_clients.domain_name = request.POST['domain_name']
    all_clients.acc_name = request.POST['acc_name']
    all_clients.acc_password = request.POST['acc_password']
    all_clients.purchase_date = request.POST['purchase_date']
    all_clients.expiry_date = request.POST['expiry_date']
    all_clients.amount = request.POST['amount']

    all_clients.hosting_account = request.POST['hosting_account']
    all_clients.hosting_pass = request.POST['hosting_pass']
    all_clients.hosting_date = request.POST['hosting_date']
    all_clients.hosting_expiry_date = request.POST['hosting_expiry_date']
    all_clients.hosting_amount = request.POST['hosting_amount']

    all_clients.sll_type = request.POST['sll_type']
    all_clients.sll_account = request.POST['sll_account']
    all_clients.sll_date = request.POST['sll_date']
    all_clients.sll_expiry_date = request.POST['sll_expiry_date']
    all_clients.sll_amount = request.POST['sll_amount']

    all_clients.amc_date = request.POST['amc_date']
    all_clients.amc_expiry_date = request.POST['amc_expiry_date']
    all_clients.amc_amount = request.POST['amc_amount']

    all_clients.project_update = request.POST['project_update']
    all_clients.updated_date = request.POST['updated_date']
    all_clients.project_details = request.POST['project_details']

    all_clients.chatbot_type = request.POST['chatbot_type']
    all_clients.credits_purchased = request.POST['credits_purchased']
    all_clients.chatbot_amount = request.POST['chatbot_amount']
    all_clients.chatbot_date = request.POST['chatbot_date']
    all_clients.chatbot_last_date = request.POST['chatbot_last_date']

    all_clients.save()

    messages.success(request,'Edited successfully! ')
    return HttpResponseRedirect(reverse('user_cms'))





















# def edit_client(request,pk):
#     item = get_object_or_404(Client, pk=pk)
#     if request.method== "POST":
#         form = Client(request.POST,instance=item)
#         if form.is_valid:
#             form.save()
#             return redirect('user_cms')
#
#     else:
#         form=Client(instance=item)
#         return render(request, 'AppTwo/edit-client.html',{'form':form})










    #     form = form_submit(request.POST,instance=post)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.save()
    #         return redirect('AppTwo:user_cms')
    # else:
    #     form= form_submit(instance=post)
    #     template='AppTwo/addclient.html'
    #     content={'form':form}
    #     return render(request,template, context)
