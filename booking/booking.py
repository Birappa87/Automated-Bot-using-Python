from selenium import webdriver
import os
import booking.constants as const
from booking.Booking_Filteration import BookingFilteration
from booking.Booking_Report import BookingReport
from prettytable import PrettyTable



class Booking(webdriver.Chrome):
  def __init__(self , driver_path =r"C:\Users\hp\Downloads\chromedriver_win32", teardown = False):
    self.teardown = teardown
    self.driver_path = driver_path
    os.environ['PATH'] +=self.driver_path
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches',['enable-logging'])
    super(Booking , self).__init__(options=options)
    self.implicitly_wait(15)
    self.maximize_window()
  
  #exiting Browser after Booking 
  def __exit__(self, exc_type , exc_val , exc_tb):
    if self.teardown:
      self.quit()


  def land_first_page(self):
    self.get(const.BASE_URL)

  def change_currency(self , currency = None):
    currency_element = self.find_element_by_css_selector(
      'button[data-modal-aria-label="Select your currency"]'
    )
    currency_element.click()

    selected_currency_element = self.find_element_by_css_selector(
      f'a[data-modal-header-async-url-param="changed_currency=1;selected_currency={currency}"]'
    )
    
    selected_currency_element.click()
  
  
  def select_place_to_go(self , place):
    search_field = self.find_element_by_id("ss")
    search_field.clear()
    search_field.send_keys(place)
    first_result = self.find_element_by_css_selector(
      'li[data-i="0"]'
    )
    first_result.click()

  def select_date(self , check_in_date , check_out_date ):
    check_in_date = self.find_element_by_css_selector(
      f'td[data-date="{check_in_date}"]'
    )
    check_in_date.click()

    check_out_date = self.find_element_by_css_selector(
      f'td[data-date="{check_out_date}"]'
    )
    check_out_date.click()

  def select_adults(self , count=1):
    selection_element = self.find_element_by_id("xp__guests__toggle")
    selection_element.click()
    
    while True:
      decrease_adults_count = self.find_element_by_css_selector(
      'button[aria-label="Decrease number of Adults"]'
      )
      decrease_adults_count.click()
      #if adult count reaches to 1 the we should get outof loop
      adults_value_element = self.find_element_by_id("group_adults")
      adults_vaue  = adults_value_element.get_attribute("value") #get aduct min value
      if int(adults_vaue) ==1:
        break
    
    increase_button_element = self.find_element_by_css_selector(
      'button[aria-label="Increase number of Adults"]'
      )

    for _ in range(count-1):
      increase_button_element.click()
 
  def click_search(self):
    search_btn = self.find_element_by_css_selector(
      'button[type="submit"]'
    )
    search_btn.click()

  def apply_filteration(self):
    filteration = BookingFilteration(driver=self)
    filteration.apply_star_rating(3,4,5)

    filteration.sort_price_lowest_first()

  def report_results(self):
    hotel_boxes = self.find_element_by_id(
      "hotellist_inner"
      )

    report = BookingReport(hotel_boxes)
    table = PrettyTable(
      field_names = ["Hotel Name" ,"Hotel Prrice" , "Hotel Score"]
    )
    table.add_rows(report.pull_deal_box_attributes())
    print(table)