import scrapy
import re
from scrapy_splash import SplashRequest



class PostsSpider(scrapy.Spider):
	name = "MyBot"

	start_urls = [
		'https://www.indeed.com/jobs?q=software%20engineer&l=New%20York%2C%20NY&vjk=7c7927725cf2840f'
	]
	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(url, self.parse, endpoint='render.html',args={'wait': 0.5})






	def parse(self,response):

		for post in response.css("div.jobsearch-SerpJobCard"):
			yield {
				'item': 1  #post.css('div.sjcl').get()

			#'title': self.Link(post)    #post.css("div.summary li::text").get()

			}
		



