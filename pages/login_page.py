class Loginpage:
    def __init__(self, page):
        self.page = page

        # Login page locators
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('#password')
        self.login_button = page.locator("#login-button")

        #product page locators
        self.page_title =page.get_by_text("Products")
        self.backpack_item = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.fleece_jacket_item = page.locator("#add-to-cart-sauce-labs-fleece-jacket")
        self.bike_light_item = page.locator(".btn.btn_primary.btn_small.btn_inventory").nth(0)
        self.cart = page.locator('[data-test="shopping-cart-link"]')
        self.items_in_cart = page.locator('[data-test="shopping-cart-badge"]')
        

        #Cart page locators
        self.cart_page_title = page.get_by_text("Your Cart")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")
        self.checkout_button =page.locator("#checkout")
        
        #checkout page locators
        self.firstname = page.locator('[data-test="firstName"]')
        self.lastname = page.locator('#last-name')
        self.zipcode = page.get_by_placeholder("Zip/Postal Code")
        self.checkout_page_title = page.get_by_text("Checkout: Your Information")
        self.continue_button = page.get_by_role("button", name= "continue")

        #oveiew page locators
        self.finish_button = page.locator("#finish")
        self.total_price = page.locator(".summary_total_label")

        #confirmation page locators
        self.confirmation_page_title = page.locator(".complete-header")
        self.back_home_button = page.locator("#back-to-products")

        #logout locators
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator('[data-test="logout-sidebar-link"]')

       
        
    def goto(self):
            self.page.goto("https://www.saucedemo.com/")

    def Login(self, username_input, password_input):
            self.username.fill(username_input)
            self.password.fill(password_input)
            self.login_button.click()

    def add_items_to_cart(self):
            self.backpack_item.click()
            self.fleece_jacket_item.click()
            self.cart.click()
            self.continue_shopping_button.click()
            self.bike_light_item.click()
            self.cart.click()
            self.checkout_button.click()
            
    def checkout(self, firstname_input, lastname_input, zipcode_input):  
            self.firstname.fill(firstname_input)
            self.lastname.fill(lastname_input)
            self.zipcode.fill(zipcode_input)
            self.continue_button.click()
        
    def finish_checkout(self):
            self.finish_button.click()
            
    def logout(self):
            self.menu_button.click()
            self.logout_link.click()    


              



