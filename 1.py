import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin

def task():
    driver = webdriver.Chrome()
    driver.get('https://jobs.marksandspencer.com/job-search')
    max_page = 3
    job_list = []

    for page in range(1, max_page):
        driver.get(urljoin('https://jobs.marksandspencer.com', f'job-search?country%5B0%5D=United%20Kingdom&page={page}&radius='))
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ais-Hits-item')))

        jobs = driver.find_elements(By.CLASS_NAME, 'ais-Hits-item')

        for job in jobs:
            title = job.find_element(By.TAG_NAME, 'h3').text
            url = job.find_element(By.TAG_NAME, 'a').get_attribute('href')
            job_list.append({
                "title": title,
                "url": url
            })

    with open('job_listings.json', 'w') as f:
        json.dump(job_list, f, indent=4)


if __name__ == '__main__':
    task()