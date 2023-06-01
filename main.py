from services.scrapper import Scrapper
from services.lda import TopicExtractor
import argparse
import urllib

# web_url = "https://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?%20s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster"
# web_url = "http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/"
# web_url = "https://edition.cnn.com/2013/06/10/politics/edward-snowden-profile/"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--weburl",
        type=str,
        required=True,
        help="Enter the web-url to parse the topics from"
    )
    args = parser.parse_args()

    sc = Scrapper()
    try:
        content = sc.scrape_data(web_url=args.weburl)
        lda = TopicExtractor()
        important_keywords = lda.get_topics(content.lower())
        print(important_keywords)
    except urllib.error.HTTPError:
        print("Error while scrapping the data from given url")
    except urllib.error.URLError:
        print("Invalid url provided")
    except ValueError:
        print("Unknown value found")
    except KeyError:
        print("Keyerror: key not found")
    except Exception:
        print("Something went wrong!")