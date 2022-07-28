import imageio
import tweepy
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image

mask = imageio.imread('smackdown.png')
mask_color = np.array(Image.open('smackdown.png'))
client = tweepy.Client(
    bearer_token='AAAAAAAAAAAAAAAAAAAAAGZUfQEAAAAAJL4%2F5CCljkNf41XJtYuXOi0kgDg%3DMJqDOzZMThwbISFVKmcUMSw6jDsjM8cVGZszcwgW5sos6CfjpV')

query = '#wwe -is:retweet'

date = '2022-07-22'
start_1 = '23:00:00'
end_1 = '23:59:59'

response = client.search_recent_tweets(query=query, max_results=100, start_time=str(date) + 'T' + str(start_1)+'Z',
                                       end_time=str(date) + 'T' + str(end_1)+'Z')

wordlist = []
for tweet in response.data:
    words = tweet.text.split()
    for word in words:
        wordlist.append(word)

print(wordlist)
wordlist_string = (" ").join(wordlist)

wc = WordCloud(background_color='white', width = 600, height=400, mask = mask).generate(wordlist_string)

wc.to_file('smackdown'+str(date)+'.png')

image_colors = wc.ImageColorGenerator(mask_color)

fig, axes = plt.subplots(1, 3)
axes[0].imshow(wc, interpolation="bilinear")
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
axes[2].imshow(image_colors, cmap=plt.cm.gray, interpolation="bilinear")
for ax in axes:
    ax.set_axis_off()
plt.show()