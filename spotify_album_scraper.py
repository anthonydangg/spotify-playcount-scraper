from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import csv

link = input('Paste your Spotify album url:\n')

driver = webdriver.Chrome()
driver.get(link)
time.sleep(5)

# Finds title tracks and streams
track_elements = driver.find_elements(By.CSS_SELECTOR, 'a[data-testid="internal-track-link"]')
track_links = [track.get_attribute('href') for track in track_elements]

track_streams = {}
name = []
plays = []

for link in track_links:
    driver.get(link)
    time.sleep(5)

    name.append(driver.find_element(By.CSS_SELECTOR, 'h1[data-encore-id="text"]').text)
    plays.append(driver.find_element(By.CSS_SELECTOR, 'span[data-testid="playcount"]').text)
    
track_streams['Name'] = name
track_streams['Plays'] = plays
print(track_streams)

driver.quit()

with open('album_data.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(track_streams.keys())
    for i in range(len(name)):
        writer.writerow([val[i] for val in track_streams.values()])