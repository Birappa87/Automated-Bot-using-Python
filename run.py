from booking.booking import Booking
try :
   with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency = 'USD')
    bot.select_place_to_go("India")
    bot.select_date(check_in_date = "2021-09-16" , check_out_date = "2021-09-20")
    bot.select_adults(5)
    bot.click_search()
    bot.apply_filteration()
    bot.refresh() #A workaround to let our bot to grab the data properly
    bot.report_results()
except:
   print("Try Again after sometime")
