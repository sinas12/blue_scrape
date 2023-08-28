
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def scrape(url):
    # Fetch the content of the URL
    driver = webdriver.Edge()
    driver.get(url)

    
    # Get the element with class name of gLFyf ( in google it was the class name of search textarea )
    element =  driver.find_element(By.CLASS_NAME, "gLFyf")

    # type " Hi mom ! " in the selected element and press enter
    element.send_keys('Hi mom !' + Keys.RETURN)

    # Get the page source
    html_content = driver.page_source
    f = open("page_source_of_google_after_typing_hi_mom.txt", "x")
    f.write(html_content)
    f.close()
    # in here you can do any thing else because you have the page_source of the page after typing the text
    # Be creative My friend !


# Example usage
url = "https://www.google.com/"
matches = scrape(url)






