from django.shortcuts import render

# from django.http import HttpResponse
from deliveryfood.form import MenuForm
from deliveryfood.models import MenuDay, MenuEmployee

# whatsApp delivery
from deliveryfood.norabot import sendmenu

# date time
# from datetime import date
# import time

# models
# from deliveryfood.models import Employee


def index(request):
    # quitar

    sendmenu()
    # Asignar un dato a la sesión

    userlevel = 1
    return render(request, "menu/index.html", {"userlevel": userlevel})


def menu_view(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, "menu/index.html")
    else:
        form = MenuForm()

    return render(request, "menu/menu_form.html", {"form": form})


def menu_list(request, level):
    if request.method == "GET":
        menuday = MenuDay.objects.all()
        context = {"menudays": menuday, "level": level}
        return render(request, "menu/menu_today_form.html", context)
    else:
        return render(request, "menu/index.html")


def menu_user(request, id_menu):
    menuday = MenuDay.objects.get(id=id_menu)
    if request.method == "GET":
        form = MenuForm(instance=menuday)
    else:
        form = MenuForm(request.POST, instance=menuday)
        if form.is_valid():
            form.save()

        return render(request, "menu/index.html")
    return render(request, "menu/menu_formUser.html", {"form": form})


def menu_employee(request, id_user):

    if id_user == "1":
        menuemp = MenuEmployee.objects.all().order_by("id")
        context = {"menuEmployee": menuemp}
        return render(request, "menu/menu_employee_form.html", context)
    else:
        menuemp = MenuEmployee.objects.filter(EmpID=id_user)
        context = {"menuEmployee": menuemp}
        return render(request, "menu/menu_employee_form.html", context)


def menu_edit(request, id_menu):
    menuday = MenuDay.objects.get(id=id_menu)
    if request.method == "GET":
        form = MenuForm(instance=menuday)
    else:
        form = MenuForm(request.POST, instance=menuday)
        if form.is_valid():
            form.save()
            sendmenu()
        return render(request, "menu/menu_today_form.html")
    return render(request, "menu/menu_form.html", {"form": form})
