from playwright.sync_api import expect
from pages.login_page import Loginpage

def test_demo(page):
    pradeep = Loginpage(page)
    
    pradeep.goto()

    pradeep.Login("standard_user", "secret_sauce")
    expect(pradeep.page_title).to_be_visible()
    

    pradeep.add_items_to_cart()
    
    expect(pradeep.checkout_page_title).to_be_visible()


    pradeep.checkout("pradeep", "Jay", "12345")
    expect(pradeep.total_price).to_be_visible()
    

    pradeep.finish_checkout()
    expect(pradeep.confirmation_page_title).to_have_text("Thank you for your order!")
    expect(pradeep.back_home_button).to_be_visible()
    

    pradeep.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")
