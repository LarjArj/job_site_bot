import sys
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random
import time


### Functionality that handles the actual scraping of indeed.com based on input of JobTitile and Location from UI
def traverse(jobTitle,location):
	jobList=[]
	Browser=BrowserManager()
	Browser.setBrowser_Url('https://www.indeed.com')
	browser = Browser.browser

	jobInput = browser.find_element_by_name("q")
	locationInput =browser.find_element_by_name("l")
	locationInput.send_keys(location)

	jobInput.send_keys(jobTitle,Keys.ENTER)


	time.sleep(4)
	increment=1
	

	
	second_ranges = [[5.87,9.44],[3.32,10.43]]  # random time ranges 
	#to delay clicking on website elements and avoid triggering captcha protocols
	alternate = False
	nextPage = True
	while nextPage:
		sec=[]
		if alternate:
			sec=second_ranges[0]
		else:
			sec=second_ranges[1]

		alternate = not alternate
		elems=browser.find_elements_by_css_selector(".clickcard")

		for i,job in enumerate(elems):
			seconds = random.uniform(sec[0],sec[1])
			try:
				
				time.sleep(seconds)
				job.click()

				if tabExists(browser):
					window_before = browser.window_handles[0]
					window_after  = browser.window_handles[1]
					browser.switch_to(window_after)
					desc=browser.find_element_by_id('jobDescriptionText').text
					print(desc)
					jobList.append(desc)
					browser.close()
					browser.switch_to(window_before)

					
					continue

				container=browser.find_element_by_xpath("//*[(@id = 'vjs-container-iframe')]")
			
				#switch into i-frame # not acessible otherwise
				browser.switch_to.frame(container)
				# add attributes
				desc = browser.find_element_by_css_selector(".jobsearch-JobComponent-embeddedBody").text
				print(desc)
				jobList.append(desc)
				browser.switch_to.default_content()
			except:
				print("selenium traversal error")


				#time.sleep(seconds)
				#window_before = browser.window_handles[0]
				#time.sleep(seconds)
				#window_after  = browser.window_handles[1]
				#print(browser.window_handles)
				#browser.switch_to(window_after)
				#desc=browser.find_element_by_id('jobDescriptionText').text
				#print(desc)
				#jobList.append(desc)
				#browser.close()
				#browser.switch_to(window_before)


		increment+=1
		pg=str(increment)
		next_page = browser.find_element_by_link_text(pg)

		if next_page == [] or nextPage == False or next_page is None:
			return
		seconds=random.uniform(1.4544,5.522232)

		time.sleep(seconds)
		next_page.click()
		popup=browser.find_elements_by_xpath("//*[@id='popover-x']/button")
		
		if len(popup)>0:
			for i in popup:
				time.sleep(2)
				i.click()
	return jobList

def tabExists(browser):
	return True if len(browser.window_handles) > 0 else False


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




#browser = webdriver.Chrome(ChromeDriverManager().install())
#browser.get('https://www.indeed.com/jobs?q=software%20engineer&l&ts=1604546936908&rq=1&rsIdx=2&fromage=last&newcount=4153&vjk=4d5675f328bae7ed')