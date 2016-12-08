from PIL import Image, ImageGrab
import string
import time
import random

class UnitHelper:
    def __init__(self,app):
        self.app = app


    def find_units(self,action):
        wd = self.app.wd
        unit_serials = self.app.config['web']
        wd.find_element_by_xpath("//div[@class='tabs-pane active-pane']/div[@id='unitserials']/textarea").send_keys(unit_serials['unitserials'])
        wd.find_element_by_xpath("//div[@class='tabs-pane active-pane']/div[@id='unitserials']/div[@class='buttons']/input[@id='unit-serial-search'] ").click()
        time.sleep(2)
        self.app.session.login_to_MES()
        time.sleep(3)
        self.get_MES_serial_list()
        wd.find_element_by_xpath("//div[@id='rca-left']/ul[@class='tabs-menu']/li[@class='menu-item']/a[@href='#tab-unit-details']").click()
        self.app.wait("//div[@class='tabs-pane with-rca-inputs active-pane']")
        self.open_random_MES(action)


    def open_disposition_window(self,action,list):
        wd = self.app.wd
        random_serial = random.choice(list)
        self.select_disposition(random_serial)
        time.sleep(3)
        if self.find_action_value(action):
            return True
        list.remove(random_serial)

    def select_disposition(self, random_serial):
        wd=self.app.wd
        wd.find_element_by_xpath("//table[@id='failureEventsTable']/tbody/tr/td[text()='%s']" % random_serial).click()
        if len(wd.find_elements_by_xpath("//div[@class='rca-margin-bottom']/input[@id='select-disposition-button']")) > 0:
            wd.find_element_by_xpath("//div[@class='rca-margin-bottom']/input[@id='select-disposition-button']").click()
        pass

    def find_action_value(self,action):
        global value
        wd = self.app.wd
        get_action_list = wd.find_elements_by_xpath("//table[@id='disp-options']/tbody/tr[1]/td[1]/select/option")
        for element in (get_action_list):
            value = element.get_attribute("data-action")
            if value == action:
                return True
            else:
                continue
        wd.find_element_by_xpath("//div[@class='buttonPanel']/button[@class='cancel_button aui-button rca-popup-button']").click()
        self.app.wait("//table[@id='failureEventsTable']")
        return False


    def get_unit_list(self):
        units = self.app.config['web']['unitserials']
        units = units.split()
        return units

    def random_string(self, prefix, maxlen, symbols=None, digits=None):
        if symbols != None:
            symbols = string.ascii_letters
            return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
        elif digits != None:
            digits = string.digits
            return prefix + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])
        else:
            all = string.ascii_letters + string.digits + string.punctuation
            return prefix + "".join([random.choice(all) for i in range(random.randrange(maxlen))])

    def take_screenshot(self):
        screen = ImageGrab.grab()
        name = self.random_string('screen',10,1,1) + '.png'
        screen.save(name,'PNG')


    def submit_unit(self):
        wd = self.app.wd
        wd.find_elements_by_xpath("//div[@class='buttonPanel']/button[@id='ok_button']").click()


    def get_MES_serial_list(self):
        wd = self.app.wd
        MES_list=[]
        list = wd.find_elements_by_xpath("//table[@id='failureEventsTable']//tr/td[3]")
        for element in list:
            unit_name = element.text
            MES_list.append(unit_name)
        return MES_list


    def open_random_MES(self,action):
        wd = self.app.wd
        list = self.get_MES_serial_list()
        while self.open_disposition_window(action,list)!= True:
            continue
        else:
            wd.find_element_by_xpath("//select[@id='select-dc']").click()
            wd.find_element_by_xpath("//select[@id='select-dc']/option[@data-action='%s']" % value).click()
            time.sleep(2)









