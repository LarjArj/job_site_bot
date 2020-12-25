import scrapy
import re



class PostsSpider(scrapy.Spider):
	name = "posts"

	start_urls = [
			'https://www.indeed.com/jobs?q=software%20engineer&l=New%20York%2C%20NY'
	]


	def parse(self,response):
		for post in response.css("div.jobsearch-SerpJobCard"):


			yield {
				'summary':	self.li_add(post), 
				'title':    self.get_title(post) #post.css("a").get()
				
				#'title': self.Link(post)    #post.css("div.summary li::text").get()

			}
				
				
		x = response.css('div.pagination a::attr(href)').get()
		next_page = self.nextLink(x)
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)



		#page = response.url.split('/')[-1]
		#filename = 'posts-%s.html' % page
		#with open(filename, 'wb') as f:
		 	#f.write(response.body)

	def li_count(self,post):
		count=0
		x=post.css("div.summary").get()
		y=re.split('<|>|</|\n',x)
		for char in y:
			if char=='/li':
				count+=1
		return count


	def li_add(self,post): # li:nth-child()
		iterator_range=self.li_count(post)
		summary_list=[]
		for i in range(1,iterator_range+1):
			summary_list.append(self.getNewLi(post,i))

		return summary_list

	def getNewLi(self,post,idx): 
		upper=".summary li:nth-child("
		mid=str(idx)
		lower=")::text"
		return post.css(upper+mid+lower).get()

	def get_title(self,post): #title Link
		x=None
		output=""
		linkString=post.css("a").get()
		title_index = linkString.find("title=")
		class_index = linkString.find("class=")
		if title_index!=-1 and class_index!=-1:
			output=linkString[title_index:class_index]
			x=output.split("title=")
		return x

	def getLocation(self,post):
		string=post.css(".sjcl").get()

	
	def nextLink(self,next_page):
		base_url='https://www.indeed.com'
		new_url=base_url+next_page
		return new_url










