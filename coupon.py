<<<<<<< Updated upstream
__author__ = 'GirlLunarExplorer'
=======
#!/usr/bin/env python
__author__ = 'tracyrohlin'
>>>>>>> Stashed changes

from selenium import webdriver

class Coupon:
    def __init__(self, coupon_code):
        self.coupon_code = coupon_code
        if len(coupon_code) != 19:
            raise Exception("Enter code surrounded by quotes, with space between each group")

        self.driver = webdriver.Firefox()
        self.driver.get("https://www.petsmartpetshotelsurvey.com/")

        self.completely_satisfied = "//td[@class='Opt5 inputtyperbloption']/span"
        self.satisfied = "//td[@class='Opt4 inputtyperbloption']/span"
        self.neutral = "//td[@class='Opt3 inputtyperbloption']/span"
        self.disatisfied = "//td[@class='Opt2 inputtyperbloption']/span"
        self.completely_disatisfied = "//td[@class='Opt1 inputtyperbloption']/span"
        #self.yes = "//div[@class='Opt1 rbloption']/span/span"
        self.yes = self.completely_disatisfied
        self.no = "//td[@class='Opt2 inputtyperbloption']/span"

    def click_next(self):
        next = self.driver.find_element_by_id("NextButton")
        next.click()
        self.driver.implicitly_wait(5)

    def input_coupon_code(self):
        codes = self.coupon_code.split()
        box_ids =['CN1', 'CN2', 'CN3', 'CN4']
        for code, box_id in zip(codes, box_ids):
            self.driver.find_element_by_id(box_id).send_keys("", code)

        hotel_option = self.driver.find_elements_by_xpath("//div[@class='rbloption'][2]/label")[0]
        hotel_option.click()
        self.click_next()

    def drop_down_menu(self):
        #clicks the options for 18&over, not an employee, pet did not stay overnight
        i = 1
        for i in range(1,4):
            self.driver.find_element_by_xpath("//select[@id='R0{0}000']/option[@value='2']".format(i)).click()

        self.click_next()

    def survey_questions(self, survey):
        for question in survey:
            question.click()
        self.click_next()

    def completelysatisfied(self):
        survey = self.driver.find_elements_by_xpath(self.completely_satisfied)
        self.survey_questions(survey)

    def answer_no(self):
        survey = self.driver.find_elements_by_xpath(self.no)
        self.survey_questions(survey)

    def pawgress_report(self):
        yes = "//div[@class='Opt1 rbloption']/span/span"
        survey = self.driver.find_elements_by_xpath(yes)
        self.survey_questions(survey)

    def answer_yes(self):
        survey = self.driver.find_elements_by_xpath(self.yes)
        self.survey_questions(survey)

    def reservation(self):
        in_person = "//div[@class='Opt2 rbloption']/span/span"
        option = self.driver.find_element_by_xpath(in_person)
        option.click()
        self.click_next()

    def get_code(self):
        valid_code = self.driver.find_element_by_xpath("//p[@class='ValCode']")
        return valid_code.text



def petshotel_coupon_retrieval(coupon_code):
    coupon = Coupon(coupon_code)
    coupon.input_coupon_code()
    coupon.drop_down_menu()

    """Rates the satisfaction of:
        Question 1: The speed and efficiency of pet drop-off
        Question 2:  The way the employees interacted with the pet
        Question 3:  The cleanliness of the drop-off area
        Question 4:  The friendliness of the employees
        Question 5:  The interaction with the employees"""
    i = 0
    while i < 4:
        #cycles through the next 4 pages, which ask similar questions on customer satisfaction
        coupon.completelysatisfied()
        i += 1

    #did you experience a problem with this service
    coupon.answer_no()

    #would you recommend this service to a family member or friend?
    coupon.completelysatisfied()

    #did you receive a pawgress report?
    coupon.pawgress_report()

    #did an employee review the report with you?
    coupon.answer_yes()

    #did you visit the Banfield pet hospital?
    coupon.answer_no()

    """State whether you agree:
    Question 1:  The pawgress report included personalized details on my pet's day
    Question 2:  I feel comfortable leaving my pet at the hotel
    Question 3:  The employees made me feel welcome
    Question 4:  The employees understood my pets' needs."""
    coupon.completelysatisfied()

    #how did you complete your reservation?
    coupon.reservation()

    #tell us why you are satisfied with your service
    #left intentionally blank
    coupon.click_next()

    #was this your first time using this service?
    coupon.answer_no()

    #was this hotel your first choice of day camp?
    coupon.answer_yes()

    #have you used another pet day care service other than ours?
    coupon.answer_no()

    #did you research our service online before booking an appointment?
    coupon.answer_no()

    #would you like to provide your email for future promotions?
    coupon.answer_no()

    #gets final coupon code
    coupon.get_code()

print petshotel_coupon_retrieval("0601 1875 1575 7297")
