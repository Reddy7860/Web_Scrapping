## Part 1
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up ChromeDriver with options to run headless and disable image loading
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-features=RendererCodeIntegrity')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
prefs = {'profile.managed_default_content_settings.images': 2}
options.add_experimental_option('prefs', prefs)
service = Service('chromedriver')
driver = webdriver.Chrome(service=service, options=options)


# Start the browser and navigate to the page
driver = webdriver.Chrome()
driver.get("https://www.moodys.com/account/sign-in")

# Fill in the email and password fields
wait = WebDriverWait(driver, 10)
email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-testid="emailInput"]')))
email_field.send_keys("saitham@uncc.edu")

wait = WebDriverWait(driver, 10)
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="emailContinueButton"]')))
continue_button.click()

wait = WebDriverWait(driver, 10)
password_field = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@data-testid="password"]')))
password_field.send_keys("suhas2216")

wait = WebDriverWait(driver, 10)
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="loadingButton"]')))
continue_button.click()

## Part 2
## We need to perform the manual steps by selecting the Reports & Insights -> Rating & Assesment News

## Part 3
# Fill in the email and password fields
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="mdcSearchWithin "]/input')))
search_box.click()
search_box.send_keys("Acquisition")


wait = WebDriverWait(driver, 10)
go_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="mdc-gray-btn mdcBtn"]')))
go_button.click()

## Part 4
url = 'https://www.moodys.com/researchandratings/research-type/ratings-assessments-news/-/00300E/00300E/-/-1/0/-/0/-/-/-/-/-/-/-/-/global/pdf/-/rra'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

driver.get(url)

# Extract content from the page source
content = driver.page_source


# Print the content
print(content)

## Part 5 
url = 'https://www.moodys.com/credit-ratings/Merlin-Acquisition-Corporation-credit-rating-867975763/reports?category=Ratings_and_Assessments_Reports_rc|Issuer_Reports_rc&type=Rating_Action_rc|Announcement_rc|Announcement_of_Periodic_Review_rc,Credit_Opinion_ir_rc|Issuer_Comment_rc'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

driver.get(url)

# Extract content from the page source
content = driver.page_source

# Print the content
print(content)
