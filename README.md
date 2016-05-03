# InstagramNewYearsResolutions
Instgram scraping script

This is a python script that scrape the Instgram website to find the number of tags for #day1 to #day365. The goal is 
to see how quickly this trend drops off over the course of the year and try to draw parallels to how long most people 
keep New Years Resolutions. This project was inspired when I saw the 365 day challenge on Instagram where people try to 
post a photo each day with a tag for that day (ex #day 47). 

This script uses Python 2.7 with the <a href="http://docs.python-requests.org/en/master/">Requests library</a> and the 
<a href="https://www.crummy.com/software/BeautifulSoup/">Beautiful Soup library</a>.

The script will create a CSV file containing the day number and the number of times a hashtag was used for that day.
(ex. 47,132996 ). A sample file is in the repository.
