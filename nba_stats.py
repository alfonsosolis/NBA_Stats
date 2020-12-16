from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas
import csv
chrome_options = Options()
chrome_options.add_argument("--window-position=1280,900") ## Open Chrome in bottom right corner.
driver = webdriver.Chrome("/Users/asolis/Downloads/chromedriver",chrome_options=chrome_options )


# Website to navigate to
driver.get('https://www.basketball-reference.com/teams/')

teams = driver.find_elements_by_css_selector('table#teams_active tr[class="full_table"] a')
wins = driver.find_elements_by_css_selector('table#teams_active tr[class="full_table"]>td:nth-child(7)') ## td nth child includes th as well
losses = driver.find_elements_by_css_selector('table#teams_active tr[class="full_table"]>td:nth-child(8)') ## td nth child includes th as well
championships =driver.find_elements_by_css_selector('table#teams_active tr[class="full_table"]>td:nth-child(13)') ## td nth child includes th as well

#players = driver.find_elements_by_xpath('//td[@class="name"]') # Names of players
#salary = driver.find_elements_by_xpath('//td[@class = "hh-salaries-sorted"]') # Correspondning player salaries



#players_list = []


with open('franchise_stats.csv', mode = 'w', newline= "") as franchise_wins:
  players_writer = csv.writer(franchise_wins, delimiter = ',' , quotechar = '"', quoting = csv.QUOTE_MINIMAL)
  players_writer.writerow(["Teams", "Teams Link", "Wins", "Losses", "Rings"])
  for p in range(len(teams)):
    players_writer.writerow([teams[p].text, teams[p].get_attribute("href"), wins[p].text, losses[p].text, championships[p].text])

## Closing Browser as it is no longer needed.
driver.close()