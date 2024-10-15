import http.client
import json

conn = http.client.HTTPSConnection("jobs-search-api.p.rapidapi.com")

job_role_search = str(input("What Job Role are you looking for: "))
job_location = str(input("What Job Location are you looking for: "))

payload = f'{{"search_term":"{job_role_search}","location":"{job_location}","results_wanted":5,"site_name":["indeed","linkedin","zip_recruiter","glassdoor"],"distance":50,"job_type":"fulltime","is_remote":false,"linkedin_fetch_description":false,"hours_old":72}}'

headers = {
    'x-rapidapi-key': "1a20cedd60msh43d38c1f42ba976p12bf72jsndf09cdb52f10",
    'x-rapidapi-host': "jobs-search-api.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/getjobs", payload, headers)

res = conn.getresponse()
data = res.read()

final_data = data.decode("utf-8")

data = json.loads(final_data)

# Iterate over the job listings and print them in a readable format
for job in data['jobs']:
    print(f"Job Title: {job['title']}")
    print(f"Company: {job['company']}")
    print(f"Location: {job['location']}")
    print(f"Job URL: {job['job_url']}")
    print(f"Date Posted: {job['date_posted'] if job['date_posted'] else 'Not specified'}")
    print("-" * 40)