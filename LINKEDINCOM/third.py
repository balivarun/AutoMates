# this file uses local storage folder for browser data
# login to the account before executing the actual script

# this is the third modification of the Linkedin Automation
# Purpose: To make this script completely handsfree
# Description: this script should open each job in new tabs, then fill each job and close the tab.
# 
# Note: script should scroll wherever necessary to see more jobs :-B

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep
import random

from selenium.webdriver.chrome.options import Options


class LinkedinBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=chrome-data")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option('excludeSwitches', ["enable-automation"])

        self.driver = webdriver.Chrome('D:\libtools\chromedriver\chromedriver.exe', options=chrome_options)
        self.driver.get("https://linkedin.com/jobs")
        sleep(2)

    def go_jobs(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/feed')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/jobs')]")\
            .click()
        sleep(2)

    def apply_job(self):
        sleep(4)
        # Section to click the Easy Apply Button on job page
        gerat = True
        while gerat:
            try:
                self.driver.find_element_by_xpath("//button[@class='jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view']").click()
                print('Clicked the Easy Button')
                gerat = False
            except NoSuchElementException:
                print('Cannot find the button, click Another Job')
                sleep(6)
        sleep(2)

        gerat = True
        while gerat:
            try:
                self.driver.find_element_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']").click()
                print('Next / Submit')
                sleep(2)
            except NoSuchElementException:
                gerat = False
        print("job applied")

    def click_job_card(self):
        # jobs = self.driver.find_elements_by_xpath('//*[text()="Easy Apply")]')
        sleep(5)
        easyJobs = []
        while len(easyJobs) == 0:
            try:
                easyJobs = self.driver.find_elements_by_xpath("//*[text()='Easy Apply']/ancestor::*[@class='ember-view job-card-square__link display-flex flex-grow-1 flex-column align-items-stretch full-width js-focusable-card']")
            except NoSuchElementException:
                print(xx, 'is not there..')
            print(len(easyJobs))
        # jobs = self.driver.find_elements_by_xpath("//li[contains(text(), 'Easy Apply')]")
        print(len(easyJobs))
        cl = random.randint(0, len(easyJobs)-1)
        print('clicking the {} job'.format(cl))
        yehut = True
        while yehut:
            try:
                easyJobs[cl].click()
                yehut = False
            except ElementNotInteractableException:
                print('scroll a bit please, cannot see the element yet')
                sleep(2)
        sleep(2)

    def check_job_card(self):  # checks if there are any job cards on the page.
        try:
            card_list = self.driver.find_element_by_class_name("job-card-square__link").click()
        except NoSuchElementException:
            print("selenium.common.exceptions.NoSuchElementException")
            card_list = []
        print(card_list)
        return len(card_list)

    def _get_names(self):
        print('hello')


Lbot = LinkedinBot()
Lbot.click_job_card()
Lbot.apply_job()

seri = 20  # number large enough to start the loop :-)

while seri:
    Lbot.go_jobs()
    Lbot.click_job_card()
    Lbot.apply_job()
    seri -= 1
