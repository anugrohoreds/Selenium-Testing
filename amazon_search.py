from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in")
search_term = "You'll Never Walk Alone"
assert "Amazon" in driver.title
searchbox = driver.find_element_by_id("twotabsearchtextbox")
searchbox.clear()
searchbox.send_keys(search_term)
searchbox.send_keys(Keys.RETURN)
assert f"Amazon.in:{search_term}" in driver.title
assert "No Results Found." not in driver.page_source
driver.close()
