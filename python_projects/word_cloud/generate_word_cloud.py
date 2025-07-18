from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

text = "This is an example text to demonstrate word cloud generation in Python. Word clouds are useful for visualizing word frequencies."


wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=STOPWORDS).generate(text)


plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()