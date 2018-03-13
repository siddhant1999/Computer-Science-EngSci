import indicoio
indicoio.config.api_key = '38caeb13cea0fa05efffe6dec1ad3070'

# single example
x = indicoio.sentiment_hq("I like code!")
print x

# batch example
'''indicoio.sentiment_hq([
    "I love writing code!",
    "Alexander and the Terrible, Horrible, No Good, Very Bad Day"
])'''