

from googlesearch import search
from newspaper import Article
import time
from newspaper.article import ArticleException, ArticleDownloadState



    



hardcoded = ["cnn", "fox", "louder with crowder", 
            "infowars", "dailywire", "msnbc", 
            "wikipedia", "nbc", "politifact", 
            "ap news", "reuters", "washington post"]

def hardcoded_sources(query):
    ret_list = []
    for i in hardcoded:
        ret_list.append(query + " " + i)

    return ret_list


def lateral_url(query):
    # nlp to get the summary of the article
    # preprocess
    # get the new sources that are related to the document.
    hardcoded = hardcoded_sources(query)
    num = 1
    source_num = 1
    keywords = []
    print(f"Now the program will analyze your query, '{query}'. The program will output information as it figures it out.")
    for i in hardcoded:
        for j in search(i, tld="co.in", num=1, stop=1):
            try:
                a = Article(j)
                # Download article
                a.download()
                
                a.parse()
                a.nlp()
                num = "Source " + str(source_num)
                url = "URL: " + a.url
                if a.authors:
                    authors = "Authors: " + ", ".join(a.authors)
                else: 
                    authors = "No authors found."
                if a.summary:
                    summary = "Summary: " + a.summary
                else: 
                    summary = "No summary found."
                print(num + "\n" + url + "\n" + authors + "\n" + summary + "\n\n")
                source_num += 1
                time.sleep(3)
                keywords.extend(a.keywords)
            except:
                print("Link #" + str(source_num) + " resulted in an error. The link was\n" + j + "\n if you wanted to look at it yourself.")
                time.sleep(1)
                source_num += 1
                pass
    print("\n\nHere is a list of keywords that were found during your search.")
    print(keywords)
    return


        



def main():
    query = input("Type the topic below to start the lateral reading! Paste your Topic and press Enter. You should either try and give a general topic or input something more specific, but you might get better results inputting specific subjects. \nTopic: ")
    lateral_url(query)
    print("Lateral reading process completed.")

    


if __name__ == '__main__':
    main()