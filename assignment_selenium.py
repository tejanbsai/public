from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Launch the application URL
driver.get("https://www.bt.com/")
driver.maximize_window()
driver.implicitly_wait(20)

# Handle the cookie popup if it appears

try:
    # Switch to the iframe that contains the cookie popup
    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[@name='trustarc_cm']"))
    )
    driver.switch_to.frame(iframe)

    # Close the accept Cookie pop-up
    cookie_popup = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='call']"))
    )
    #print(cookie_popup)
    cookie_popup.click()

    # Switch back to the main page
    driver.switch_to.default_content()
except:
    pass


# Hover to Mobile menu and click on mobile phones
mobile_menu = driver.find_element(By.XPATH, "//a[@href='https://www.bt.com/mobile']").click()
element = driver.find_element(By.XPATH, "//a[@href='https://www.bt.com/products/mobile/phones/']").click()


# action = ActionChains(driver)
# action.move_to_element(mobile_menu).perform()
# Click on Mobile phones
# wait = WebDriverWait(driver, 10)
# dropdown_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='https://www.bt.com/products/mobile/phones/']")))
# dropdown_element.click()

#element = driver.find_element(By.XPATH, "//a[@href='https://www.bt.com/products/mobile/phones/']").click()

# driver.execute_script("arguments[1].scrollIntoView();", element)
# element.click()


# verfiy banners

banners = driver.find_elements(By.XPATH, "//div[@class='flexpay-card_text_container__KQznu']")
print(len(banners))
assert len(banners) >=3 , "less than 3 banners are present."

driver.execute_script("window.scrollBy(0, 400)")

# Click on View SIM only deals
driver.find_element(By.XPATH, "//a[@class='bt-btn bt-btn-primary' and contains(@href, '/products/mobile/sim-only-deals/')]").click()
current_title = driver.title.lower()
verfy_title_text = "SIM only deals"
low_text = verfy_title_text.lower()
assert low_text in current_title, "SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile"

flex  = "//div[@class='flex flex-wrap']"
xpath_banner = flex+"/div"
text_banner = driver.find_element(By.XPATH, "//div[@class='simo-card-ee_social_norm__3lfdT']")
verfy_text = "30% off and double data was 125GB 250GB Essential Plan, was £27 £18.90 per month".split()
offer_text = driver.find_elements(By.XPATH, xpath_banner)
for each in offer_text:
    each_text = each.text.split()
    for each1 in verfy_text:
        assert each1 in each_text

driver.quit()
