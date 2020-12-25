import sys
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

def traverse():
	jobList={}
	Browser=BrowserManager()
	Browser.setBrowser_Url('https://www.indeed.com/jobs?q=software%20engineer&l&ts=1604546936908&rq=1&rsIdx=2&fromage=last&newcount=4153&vjk=4d5675f328bae7ed')
	print("hello")
	browser = Browser.browser

	#browser = webdriver.Chrome(ChromeDriverManager().install())
	#browser.get('https://www.indeed.com/jobs?q=software%20engineer&l&ts=1604546936908&rq=1&rsIdx=2&fromage=last&newcount=4153&vjk=4d5675f328bae7ed')
	time.sleep(4)
	increment=1
	

	#clock
	#try:
		#pass
	#except expression as identifier:
		#pass
	#else:
		#pass

	second_ranges = [[2.874672224,5.42234222],[3.324444,4.43221]]
	for val in range(1,15):
		elems=browser.find_elements_by_css_selector(".clickcard")
		for job,i in enumerate(elems):
			seconds = random.uniform(2.233132899999999,4.56777799999212222)
			time.sleep(seconds)
			i.click()
			container=browser.find_element_by_xpath("//*[(@id = 'vjs-container-iframe')]")
			
			#switch into i-frame
			browser.switch_to.frame(container)
			# add attributes
			title_desc = browser.find_element_by_css_selector(".jobsearch-JobComponent-embeddedBody").text
			jobList[job] = title_desc
			browser.switch_to.default_content()

		increment+=1
		pg=str(increment)
		
		next_page = browser.find_element_by_link_text(pg)
		seconds=random.uniform(1.4544,5.522232)
		time.sleep(3)
		next_page.click()
		popup=browser.find_elements_by_xpath("//*[@id='popover-x']/button")
		if len(captcha)>0:
			for i in popup:
				time.sleep(2)
				i.click()
	return jobList



class BrowserManager:

	def __init__(self):
		self.browser= webdriver.Chrome(ChromeDriverManager().install())
		self.cur_url = None
		
		

	def setBrowser_Url(self,url):
		self.browser.get(url)
	
		#self.cur_url=self.browser.current_url
	
		
		
		
	
		



#window_after = driver.window_handles[1]
#driver.switch_to.window(window_after)
#new window