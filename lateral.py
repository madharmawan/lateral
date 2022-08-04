
from googlesearch import search
import time



    



hardcoded = ["cnn", "fox", "louder with crowder", 
            "infowars", "dailywire", "msnbc", 
            "wikipedia", "nbc", "politifact", 
            "ap news", "reuters", "washington post"]

def hardcoded_sources(query):
    ret_list = []
    for i in hardcoded:
        ret_list.append(query + " " + i)

    return ret_list


def lateral_url(query, numeral):
    # nlp to get the summary of the article
    # preprocess
    # get the new sources that are related to the document.
    hardcoded = hardcoded_sources(query)
    num = 1
    source_num = 1
    keywords = []
    print(f"Now the program will analyze your query, '{query}'. The program will output information as it figures it out.")
    for i in hardcoded:
        for j in search(i, tld="co.in", num=numeral, stop=numeral):
                print("source " + str(num) + " " + j)
                num += 1

    return


        



def main():
    again = True
    while again:
        query = input("Type the topic below to start the lateral reading! Paste your Topic and press Enter. You should either try and give a general topic or input something more specific, but you might get better results inputting specific subjects. \nTopic: ")
        q1 = True
        while q1:
            number_source = input("The program will try to get at minimum 12 sources related to your query. But you can change this to 24 if you want to, but it might take a bit more time. Do you want this? Type 1 or 2 based on the prompt below.\n1) Do 12 sources\n2) Do 24 sources\n\nYour Answer: ")
            if number_source == "1":
                q1 = False
                lateral_url(query, 1)
            elif number_source == "2":
                q1 = False
                lateral_url(query, 2)
            else:
                print("You tried putting in an invalid token. Please only type 1 or 2.")
                time.sleep(3)
            
        print("Lateral reading process completed.")
        yes = input("Do you want to try again? Type 2 if you are finished, and anything else to try again.\nInput: ")
        if yes == "2":
            again = False
    print("Process Finished. If you want to learn more about Lateral Reading, watch the Crash Course on Navigating Digital Information: https://www.youtube.com/watch?v=L4aNmdL3Hr0&list=PLH2l6uzC4UEXA16X3eHd8DEGIlBV0ctqP")

if __name__ == '__main__':
    main()