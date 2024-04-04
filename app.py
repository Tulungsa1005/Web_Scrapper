# Import necessary libraries
import newspaper
import json
# Ask the user to enter the URL
url = input("Enter the URL of the article : ")
# Try to create an Article object, download the article, and parse it
try :
    article = newspaper.Article(url=url, language='en')
    article.download()
    article.parse()
# Catch exceptions related to downloading or parsing the article    
except newspaper.article.ArticleException :
    print("An error occurred while downloading or parsing the article. Please check the URL and try again.")
    exit()
# Perform natural language processing tasks on the article's content
article.nlp()
# Create a dictionary to store various attributes of the article
article_dict = {
    "Title": article.title,
    "Text": article.text,
    "Authors": ', '.join(article.authors) if article.authors else 'No authors listed.',
    "Published Date": article.publish_date.strftime('%Y-%m-%d %H:%M:%S') if article.publish_date else 'No publish date available.',
    "Top Image URL": article.top_image if article.top_image else 'No top image available.',
    "Keywords": ', '.join(article.keywords) if article.keywords else 'No keywords available.',
    "Summary": article.summary if article.summary else 'No summary available.',
    "Meta Description": article.meta_description if article.meta_description else 'No meta description available.',
    "Meta Keywords": article.meta_keywords if article.meta_keywords else 'No meta keywords available.',
    "Meta Language": article.meta_lang if article.meta_lang else 'No meta language available.',
    "Canonical Link": article.canonical_link if article.canonical_link else 'No canonical link available.',
    "Source URL": article.source_url if article.source_url else 'No source URL available.',
    "Tags": article.tags if article.tags else 'No tags available.',
    "Images": article.images if article.images else 'No images available.',
    "Videos": article.movies if article.movies else 'No videos available.'
}
# Iterate through the dictionary and print each key-value pair
for key, value in article_dict.items():
    if isinstance(value, set):
        print(f"{key} :")
        for i, item in enumerate(value, start=1):
            print(f"{i}. {item.encode('utf-8').decode('utf-8')}\n")
        print("\n")
    else:
        print(f"{key} :\n{value.encode('utf-8').decode('utf-8')}\n\n")