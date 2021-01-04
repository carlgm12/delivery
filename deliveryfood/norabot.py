# from django.shortcuts import render
# from django.http import HttpResponse
# from deliveryfood.form import MenuForm
# from deliveryfood.models import MenuEmployee

# whatsApp
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
# from requests import get

# date time
# from datetime import date
import time

# models
from deliveryfood.models import Employee


def createconexion():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://web.whatsapp.com/")

    return driver


def contacts():
    all_contact = ["Javier", "Glenda"]

    return all_contact


def sendmenu():

    todaynow = time.strftime("%H")  # Formato de 24 horas
    print(":", todaynow)
    hourini = time.strftime("%H")  # Formato de 24 horas
    endhour = int(hourini) + 5
    print("hora:", endhour)

    driver = createconexion()
    all_names = contacts()

    # quitar menu hoy
    all_menu = [
        "Hello! I share with you todays menu :)",
        "Options 1:Corn Pie, Salad and Dessert",
        "Option 2:Chicken Nugget Rice, Salad and Dessert",
        "Option 3:Rice with hamburger, Salad and Dessert",
        "Option 4:Premium chicken Salad and Dessert",
        "Please respond with number",
    ]

    i = 0

    try:
        time.sleep(18)
        # time.sleep(5)

        while i < len(all_names):

            user = driver.find_element_by_xpath(
                '//span[@title="{}"]'.format(all_names[i])
            )
            user.click()

            time.sleep(5)

            # enviar el menu
            for x in range(0, len(all_menu)):
                input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
                input_box = driver.find_element_by_xpath(input_xpath)
                input_box.send_keys(all_menu[x])

                time.sleep(2)

                # VOr2j green dot

                # enviar text
                button = driver.find_element_by_class_name("_2Ujuu")
                button.click()

            time.sleep(15)

            message = driver.find_elements_by_class_name("_1VzZY")[-1]

            print(message.text.lower())

            if int(message.text.lower()):
                # buscar en db usuario activo
                empls = Employee.objects.filter(name="Javier").values()
                for i, c in enumerate(empls):
                    url_menu_user = "http://127.0.0.1:8000/listMenuEmp/" + str(c["id"])

                salad = [
                    "please select a preference salad",
                    "1-carrot 2-potato 3-lettuce 4-chicken",
                    "please select with number(ej:1,2,3)",
                ]

                # sub menu opciones
                for y in range(0, len(salad)):
                    input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
                    input_box = driver.find_element_by_xpath(input_xpath)
                    input_box.send_keys(salad[y])

                    time.sleep(2)

                    button = driver.find_element_by_class_name("_2Ujuu")
                    button.click()

                time.sleep(10)

                sudmenu_msg = driver.find_elements_by_class_name("_1VzZY")[-1]

                print(sudmenu_msg.text.lower())

                # insert a base de datos con menu empleado
                time.sleep(2)

                input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
                input_box = driver.find_element_by_xpath(input_xpath)
                input_box.send_keys(url_menu_user)
                time.sleep(2)
                button = driver.find_element_by_class_name("_2Ujuu")
                button.click()

            else:
                input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
                input_box = driver.find_element_by_xpath(input_xpath)
                input_box.send_keys("you could choice a menu until 11pm")
                button.click()

            time.sleep(2)

            i += 1

    except Exception as e:
        print(e)
    driver.close
