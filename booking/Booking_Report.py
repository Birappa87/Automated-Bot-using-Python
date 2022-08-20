#This file is going to include method that willparse 
#Report Data

from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
  def __init__(self , boxes_section_element:WebElement):
    self.boxes_section_element = boxes_section_element
    self.deal_boxes  = self.pull_deal_boxes()

  def pull_deal_boxes(self):
    return self.boxes_section_element.find_elements_by_class_name(
      'sr_property_block'
    )

  def pull_deal_box_attributes(self):
    collections = []
    for deal_box in self.deal_boxes:
      hotel_name = deal_box.find_element_by_class_name(
        'sr-hotel__name'
      ).get_attribute("innerHTML").strip()
      hotel_price = deal_box.find_element_by_class_name(
        'bui-price-display__value'
      ).get_attribute("innerHTML").strip()
      hotel_score = deal_box.get_attribute(
        'data-score'
      ).strip()

      collections.append(
        [hotel_name , hotel_price ,hotel_score]
      )
    return collections 

    with open("Data_Table.csv" , "w") as DT:
      DT.write("Hotel_Name; Hotel_Price; Rating \n")
      for i in range(len(hotel_name)-1):
        DT.write(Hotel_Name[i].text +";"+hotel_price[i].text+";"+hotel_score.text+";"+"\n")