from django.test import SimpleTestCase
from django.urls import reverse, resolve
from deliveryfood.views import menu_view, menu_list, menu_employee, menu_user, menu_edit 

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('menu_create')
        self.assertEquals(resolve(url).func, menu_view)

    def test_listMenu_url_is_resolved(self):
        url = reverse('menu_list', args=[1])
        self.assertEquals(resolve(url).func, menu_list)

    def test_listMenuEmp_url_is_resolved(self):
        url = reverse('menu_employee', args=[1])
        self.assertEquals(resolve(url).func, menu_employee)

    def test_listMenuUser_url_is_resolved(self):
        url = reverse('menu_user', args=[1])
        self.assertEquals(resolve(url).func, menu_user)

    def test_listeditar_url_is_resolved(self):
        url = reverse('menu_edit', args=[1])
        self.assertEquals(resolve(url).func, menu_edit)
            