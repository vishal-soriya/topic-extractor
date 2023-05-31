# keyword-extractor
## Overview
This projects gets the any weburl as parameter and returns the important topics in the text visible on the website.

## Installation and Setup
1. Clone the github repo: **git clone https://github.com/vishal-soriya/keyword-extractor.git**
2. Enable the virtualenv:
3. Install depedancies: **pip3 install -r requirements.txt**

## Packages used
1. Beautifulsoup : Used to scrape the data from web
2. Gensim : For the topic modeling and corpus building
3. re : For handling some strings and removeing unecessary clutter from the text content
4. urllib : It is used for webrequests and scrapping

## Services created for implementation
1. **Scrapper** : Scrapper service used to scrape the website data using beutifulsoup and get all the text data from it.
2. **DataCleaner** : DataCleaner service used to tokenize the text content, remove common stopwords, punctuations, emojiz, etc and gives the clean tokens list from the content
3. **TopicExtractor** : TopicExtractor service performs the business logic of find the topics from the given token list using bag of words and bigrames. LDA algorith is used to get the important topics from the content.


## Execution of the code
Here, main.py is the starting point to provide the web url using parameter, It will be using scrapper, cleaning and tokenization service to find the topics from the url.

Example:
**python3 main.py --weburl "https://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?%20s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster"

Outputs for the given 3 urls are as below:
1. https://edition.cnn.com/2013/06/10/politics/edward-snowden-profile/: 
['cnn', 'snowden', 'nsa', 'government', 'guardian', 'biden', 'presidency', 'audio', 'privacy', 'work']
2. https://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?%20s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster :
['toaster', 'slice', 'cuisinart', 'stainless', 'stars', 'toast', 'bread', 'white', 'toasting', 'steel']
3. http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/ :
['rei', 'coop', 'gear', 'path', 'outdoors', 'uncommon', 'privacy', 'camping', 'store', 'life']
**
