"""bot para seguir personas en linkdin
* Posibles mejoras
    - buscar personas que esten relacionadas con el cargo
    - enviar solicitud de conexion a empresas
    - implementar una UI y empaquetar todo en un ejecutable.
    - busqueda de ofertas de empleo en pais/ciudad especifica.

"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def navigator():
    """Función para abrir el navegador"""
    browser = webdriver.Firefox()
    return browser


def login():
    """Función para iniciar sesión"""
    browser = navigator()
    browser.get("https://www.linkedin.com")
    cookie = browser.find_element(
        By.XPATH, "/html/body/div[1]/div/section/div/div[2]/button[1]")
    if cookie:
        # Esperar hasta que el botón de las cookies sea visible y hacer clic
        cookies_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located
            ((By.XPATH, "/html/body/div[1]/div/section/div/div[2]/button[1]"))
        )
        cookies_button.click()
    else:
        print("ya se aceptaron las cookies")
    correo = ""
    contrasena = ""
    username_field = browser.find_element(By.XPATH, "//*[@id='session_key']")
    password_field = browser.find_element(
        By.XPATH, "//*[@id='session_password']")
    username_field.send_keys(correo)
    password_field.send_keys(contrasena)

    login_button = browser.find_element(
        By.CSS_SELECTOR, "button.btn-md:nth-child(3)")
    login_button.click()
    chat = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[6]/div[4]/aside/div[1]/header/div[3]/button[2]")))
    chat.click()
    # Esperar hasta que el enlace de solicitudes sea interactuable y hacer clic
    solicitudes_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[2]/a')))
    solicitudes_link.click()

    buttons = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located(
            (By.XPATH, "//main/ul/li/ul/li/div/section/div/div/button"))
    )

    for buttons in range(0, 10):
        name = browser.find_element(By.XPATH, "//a/span[2]")
        nombre = name.text
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//main/ul/li/ul/li/div/section/div/div/button"))).click()
        close = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//main/ul/li/ul/li/div/section/button")))
        print(f"Solicitud enviada a {nombre} numero de solicitud: {buttons+1}")
        close.click()
        # esperar 4 segundos
        time.sleep(4)
    if buttons == 9:
        browser.quit()


login()
