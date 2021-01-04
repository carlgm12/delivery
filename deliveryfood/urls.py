from django.conf.urls import url
from deliveryfood.views import (
    index,
    menu_view,
    menu_list,
    menu_employee,
    menu_edit,
    menu_user,
)

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^new$", menu_view, name="menu_create"),
    url(r"^listMenu/(?P<level>\d+)/$", menu_list, name="menu_list"),
    url(r"^listMenuEmp/(?P<id_user>\d+)/$", menu_employee, name="menu_employee"),
    url(r"^MenuUser/(?P<id_menu>\d+)/$", menu_user, name="menu_user"),
    url(r"^editar/(?P<id_menu>\d+)/$", menu_edit, name="menu_edit"),
]
