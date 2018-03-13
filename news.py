import indicoio

from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='b75583685243458ebf4226e3628d8200')
indicoio.config.api_key = '38caeb13cea0fa05efffe6dec1ad3070'

for i in xrange(5,32):
	if i < 10:
		r = '2018-01-0' + str(i)
	else:
		r = '2018-01-' + str(i)

	for o in xrange(1,5):
		all_articles = newsapi.get_everything(q='netflix',
                                      from_parameter=r,
                                      to=r,
                                      language='en',
                                      sort_by='relevance',
                                      page=o)
		prev =0
		for x in xrange(0,19):
			y =all_articles['articles'][x]['description']
			if y==None or y=="" or y[:4]=="http":
				print prev
				continue
			#print y
			prev = indicoio.sentiment(y)
			print prev
			#print all_articles['articles'][x]['description']
			#print "---------------\n\n\n\n"




# single example
#print indicoio.sentiment("I love writing code!")

# batch example
# print indicoio.sentiment([
#     "I love writing code!",
#     "Alexander and the Terrible, Horrible, No Good, Very Bad Day"
# ])
