# TourRadar-WebScraping
Python script to collect data for a specific tour location from the tours listed on TourRadar

Input should be the website link as a string in the variable name "URL".
The script will output 2 lists:
1. No. of days of the tours
2. Average price of the tours

Overall flow of the script:
It uses request and beautifulsoup to extract the page source of the website. Then using FindAll, I take the number of tours listed in the website. 
As the website holds 15 tours in one page, so I calculated the no. of pages from it.

Then in a for loop, I run the script again in a similar fashion to extract the information we desire.

For more info, go through this easy example: https://realpython.com/beautiful-soup-web-scraper-python/#scraping-the-monster-job-site
