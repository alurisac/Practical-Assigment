''''
This is a Python code that uses the Selenium library to test a web form. The code opens a Chrome browser
and navigates to the web form page.It then fills in the text box with the word "Selenium" and clicks the submit button.
Finally, it checks if the message "Received!"is displayed on the page then closes thw browsor window'''



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Deprecated - no longer needed
#chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver"


chrome_options = webdriver.ChromeOptions() # Creates a new instance of the ChromeOptions class
chrome_options.add_experimental_option("detach", True)# Adds an experimental option to the ChromeOptions object.

#driver = webdriver.Chrome(executable_path=chrome_driver_path)
#driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options) # Creates a new instance of the ChromeDriver with the ChromeOptions

def test_eight_components():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")# navigates to the URL, https://www.selenium.dev/selenium/web/web-form.html
    title = driver.title # Finds the title of the current web page
    assert title == "Web form" 
    driver.implicitly_wait(0.5) # Sets the implicit wait time for the driver to 0.5 seconds
    text_box = driver.find_element(by=By.NAME, value="my-text") # Finds the text box element by its name attribute
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button") #Finds the submit button element by its CSS selector
    text_box.send_keys("Selenium") #Types Selenium into the text box element.
    submit_button.click() #Clicks the submit button.
    message = driver.find_element(by=By.ID, value="message")# Finds the message element by its ID attribute
    value = message.text
    assert value == "Received!" # checks whether the value is equal to "Received!"

    # Closes Chrome
    # driver.quit()
    driver.close() # closes the browsor window immediately. 


test_eight_components()
