from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from faker import Faker
import time
from selenium.webdriver import ActionChains
import unittest


class Buy_Tshirt():

    global driver

    def tshirt_checkout(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.implicitly_wait(30)
        driver.get('http://automationpractice.com/index.php')


        #####Nevigate to registration page
        signin_bttn = driver.find_element(By.CLASS_NAME, 'login')
        signin_bttn.click()

        #time.sleep(5)

        #####Go to registration form
        #email_address = driver.find_element(By.XPATH, '//*[@id="email_create"]')
        email_address = driver.find_element(By.ID, 'email_create')
        signup_bttn = driver.find_element(By.XPATH, '//*[@id="SubmitCreate"]/span')

        #time.sleep(5)

        fake_email = Faker()
        save_email = fake_email.email()
        email_address.send_keys(save_email)
        signup_bttn.click()

        #time.sleep(10)

        #####Create An Account

        select_gender_radio = driver.find_element(By.XPATH, '//*[@id="id_gender1"]')
        select_gender_radio.click()

        input_firstname = driver.find_element(By.ID,'customer_firstname')
        input_firstname.send_keys('Nipun')

        input_firstname = driver.find_element(By.ID,'customer_lastname')
        input_firstname.send_keys('Ferdous')

        input_firstname = driver.find_element(By.ID, 'passwd')
        input_firstname.send_keys('55555')

        dob_day = driver.find_element(By.XPATH, '//*[@id="days"]/option[11]')
        dob_day.click()

        dob_month = driver.find_element(By.XPATH, '//*[@id="months"]/option[10]')
        dob_month.click()

        dob_year = driver.find_element(By.XPATH, '//*[@id="years"]/option[29]')
        dob_year.click()

        newsletter_checkbox = driver.find_element(By.ID, 'newsletter')
        newsletter_checkbox.click()

        offers_checkbox = driver.find_element(By.ID, 'optin')
        offers_checkbox.click()

        company_input = driver.find_element(By.ID, 'company')
        company_input.send_keys('Nipun')

        address_input = driver.find_element(By.ID, 'address1')
        address_input.send_keys('BRAC International')

        city_input = driver.find_element(By.ID, 'city')
        city_input.send_keys('DHAKA')

        state_input = driver.find_element(By.XPATH, '//*[@id="id_state"]/option[2]')
        state_input.click()

        zipcode_input = driver.find_element(By.ID, 'postcode')
        zipcode_input.send_keys('11111')

        mobilenumber_input = driver.find_element(By.ID, 'phone_mobile')
        mobilenumber_input.send_keys('01985920911')

        address_input = driver.find_element(By.ID, 'alias')
        address_input.clear()
        address_input.send_keys('downtown strt')

        hit_register = driver.find_element(By.XPATH, '//*[@id="submitAccount"]/span')
        hit_register.click()

        #signout = driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[2]/div/div/nav/div[2]/a')
        #signout.click()

        time.sleep(5)

        signout = driver.find_element(By.LINK_TEXT, "Sign out")
        signout.click()

        sign_in = driver.find_element(By.XPATH, '//*[@id="email"]')
        signin_password = driver.find_element(By.XPATH, '//*[@id="passwd"]')

        sign_in.send_keys(save_email)
        signin_password.send_keys('55555')

        signin_hit = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button/span')
        signin_hit.click()

        ###verify if login is successfull

        if(driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a/span').is_displayed()):
            print("login successful")
        else:
            print("login failed")

        ###selecting blue tshirt

        select_tshirt = driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[3]/a')
        select_tshirt.click()

        select_size = driver.find_element(By.ID, 'layered_id_attribute_group_2')
        select_size.click()

        select_bluecolor = driver.find_element(By.ID, 'layered_id_attribute_group_14')
        select_bluecolor.click()

        time.sleep(20)

        ##hover
        #quickview_hover = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[1]/div/a[2]')
        more_bttn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/div[2]/a[2]/span')

        actions = ActionChains(driver)
        #actions.move_to_element(quickview_hover).move_to_element(add_to_cart).click().perform()
        actions.move_to_element(more_bttn).click().perform()

        #################

        choose_blue_color = driver.find_element(By.ID, 'color_14')
        choose_blue_color.click()

        add_to_cart_click = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[3]/div/p/button/span')
        add_to_cart_click.click()

        proceed_to_checkout_1 = driver.find_element(By.CSS_SELECTOR, 'a.btn:nth-child(2) > span:nth-child(1)')
        proceed_to_checkout_1.click()

        proceed_to_checkout_2 = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]/span')
        proceed_to_checkout_2.click()

        agree_to_terms = driver.find_element(By.XPATH, '//*[@id="cgv"]')
        agree_to_terms.click()

        proceed_to_checkout_3 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/form/p/button/span')
        proceed_to_checkout_3.click()

























        #closing driver
        #driver.close()

##################################################################################################
##################################################################################################

obj = Buy_Tshirt()
obj.tshirt_checkout()