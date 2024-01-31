from bs4 import BeautifulSoup
import csv
import json
import requests
import urllib.request
import pandas as pd

def scrape_to_csv(file_name):
  with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["article", "formatted title", "url"])  # Write the header row

    search_url1 = "https://en.wikipedia.org/w/index.php?title=Special:Search&limit=500&offset=0&ns0=1&search=algorithm+intitle%3Aalgorithm&advancedSearch-current={%22fields%22:{%22intitle%22:%22algorithm%22}}"
    search_url2 = "https://en.wikipedia.org/w/index.php?advancedSearch-current=%7B%22fields%22:%7B%22intitle%22:%22algorithm%22%7D%7D&limit=500&offset=500&profile=default&search=algorithm+intitle%3Aalgorithm&title=Special:Search&ns0=1"
    search_url3 = "https://en.wikipedia.org/w/index.php?advancedSearch-current=%7B%22fields%22:%7B%22intitle%22:%22algorithm%22%7D%7D&limit=500&offset=1000&profile=default&search=algorithm+intitle%3Aalgorithm&title=Special:Search&ns0=1"
        
    response = requests.get(search_url1).text

    response += requests.get(search_url2).text
    response += requests.get(search_url3).text
    #print(response) # response is a string with all html content

    # scrape webpage
    soup = BeautifulSoup(response, 'html.parser')
    #print(soup)

    results = soup.find_all('div', class_='mw-search-result-heading')
    #print(results)

    for result in results:
      title = result.find('a').text.replace(" ", "_")
      #print(title)
      formatted_title=urllib.parse.quote(title.replace(" ", "_")) # format title for url
      #print(formatted_title)
      reads_url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/{formatted_title}/monthly/20150701/20230615"
      #print(reads_url)
      writer.writerow([title, formatted_title, reads_url])
    print("finished scrape_to_csv")

def get_list_of_urls(file_name, column_name):
  df = pd.read_csv(file_name)
  url_list = df[column_name].tolist()
  print("finished get_list_of_urls")
  return url_list

def get_data(wiki_url_list):
  #This function doesn't work for a couple of the articles. Need to manually look up the correct link
  list_of_dicts = []
  for wiki_url in wiki_url_list:
    print(wiki_url)
    with urllib.request.urlopen(wiki_url) as url:
        data = url.read().decode('utf-8')
        items_dict = json.loads(data)
    # Create a list of dictionaries.
    list_of_dicts.extend( 
    {
     "project": item["project"],
      "article": item["article"],
     "granularity": item["granularity"],
     "timestamp": item["timestamp"],
     "access": item["access"],
     "agent": item["agent"],
     "views": item["views"]
    } for item in items_dict["items"])
    # Print the list of dictionaries.
  print(json.dumps(list_of_dicts))
  print("finished get_data")
  return list_of_dicts


def format_list_of_dicts(list_of_dicts):
  formatted_list = []
  for timestamp_dict in list_of_dicts:
    # if article is not in formatted list, add a new dictionary to the list and add article and timestamp key-value pairings
    index = -1
    for item in formatted_list: # for dictionary in new list
      if timestamp_dict["article"] in item.values(): # if algorithm is one of the values in that dictionary, set index equal to its index
        index = formatted_list.index(item)
    if index != -1: # if the algorithm is one of the values in the dictionary
        formatted_list[index][timestamp_dict["timestamp"]] = timestamp_dict["views"] # add the key-value pairing for timestamp and views to the dictionary at the given index
    else: 
        formatted_list.append({"article":timestamp_dict["article"],timestamp_dict["timestamp"]:timestamp_dict["views"]}) # add a new dictionary to the list
  print("finished format_list_of_dicts")
  return formatted_list

def append_to_csv(file_name,formatted_list):
  df1 = pd.read_csv(file_name)
  df2 = pd.DataFrame(formatted_list)
  df1.merge(df2).to_csv('final_merged.csv')
  print("finished append_to_csv")


def main():
  #scrape_to_csv("article_titles.csv")
  url_list = get_list_of_urls("article_titles.csv", "url")
  #print(url_list)
  dict_list = get_data(url_list)
  #print(dict_list)
  formatted_dict_list = format_list_of_dicts(dict_list)
  #print(formatted_dict_list)
  append_to_csv("article_titles.csv",formatted_dict_list)
  
if __name__ == "__main__":
    main()