# import libraries

from bs4 import BeautifulSoup
import requests
import time

#function to filter
print("put some Skill that you are not familiar with")
unfamiliar_skill = input('>')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
    # get requests
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # get the first post into website
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_= 'clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
        # scrap published_date
        Date = job.find('span',class_ = 'sim-posted').text
        if 'few' in Date:
            # scrap the company name
            company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
            # scrap the job skills
            skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
            # job Discribtion
            More_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open (f'D:\{index}.txt' ,'w') as f: 
                           f.write(f"Company Name: {company_name.strip()}")
                           f.write(f"required Skills: {skills.strip()}")
                           f.write(f"More_info: {More_info}")
                print("file save: {index}")

# program scraping every 10 min
if __name__=='__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes....")
        time.sleep(time_wait *60)