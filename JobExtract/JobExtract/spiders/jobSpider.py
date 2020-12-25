import scrapy
import re




		

class PostsSpider(scrapy.Spider):
	name = "spida"

	def __init__(self,*args,**kwargs):
		super(PostsSpider, self).__init__(*args, **kwargs) 
		self.start_urls = [kwargs.get('start_url')] 


	def parse(self,response):
	
		for post in response.css("div.jobsearch-SerpJobCard"):
			yield {
				'item':post.css('div.sjcl').get()

			#'title': self.Link(post)    #post.css("div.summary li::text").get()

			}

	
	


#<a href="/jobs?q=software+engineer&amp;l=New+York%2C+NY&amp;start=20" aria-label="3" data-pp="gQAeAAABdZIJ3KcAAAABkRJrXgBLAQEBDwO85VyPi7aH6ZeKljdhdVxsWmg5h8P0Vc-IDf_XwLU0OyldeGJEWgD_iM4ShGc5-71GWQVu0glH-_lGRAN9NNs73o9gvo4vAAA" onmousedown="addPPUrlParam &amp;&amp; addPPUrlParam(this);" rel="nofollow"><span class="pn">3</span></a>




