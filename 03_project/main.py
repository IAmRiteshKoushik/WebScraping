from bs4 import BeautifulSoup
import requests
import time

print("Skill that you are not familiar with")
unfamiliar_skill = input('>')
print(f"Filtering out: {unfamiliar_skill}")

def find_jobs():
    '''Function that extracts job details and transfers it to a file.'''

    url = 'insert-URL'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        
        # Gathering the published date
        published_date = job.find('span', class_ = 'sim-posted').span.text
        # Taking only the recent jobs - "Posted few days ago"
        if 'few' in published_date:

            # Fetching the details
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']  # link to the job
            
            if unfamiliar_skill not in skills:
                with open(fr'posts/{index}.txt', 'w') as f:
                    # Printing out the details for everyjob profile "HTML card"
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More info: {more_info}")
                print(f'File saved: {index}')
        
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} minutes')
        time.sleep(time_wait * 60)