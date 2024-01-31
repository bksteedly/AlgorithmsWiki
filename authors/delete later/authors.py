import pandas as pd
import requests
import datetime


def scrape_details(DOI):
    print(DOI)
    authors = []
    num_authors = 0
    title = ''
    date = None
    year = None
    url = ''
    link = 'https://api.crossref.org/works/' + str(DOI)
    response = requests.get(link)
    if response.status_code == 200:
        data = response.json()
        #print(data)
        if 'author' in data['message']:
            for author in data['message']['author']:
                if 'given' in author and 'family' in author:
                    authors.append(author['given'] + ' ' + author['family'])
                elif 'family' in author:
                    authors.append(author['family'])
                elif 'given' in author:
                    authors.append(author['given'])
                num_authors = len(authors)
                #print(num_authors)
                title = data['message']['title']
                #print(title)
                if 'published' in data['message']:
                    date = data['message']['published']['date-parts'][0]
                else:
                    date = data['message']['created']['date-parts'][0]
                year = date[0]
                #print(date)
                url = data['message']['resource']['primary']['URL']
                #print(URL)
        elif 'editor' in data['message']:
            for author in data['message']['editor']:
                #print(author)
                authors.append(author['given'] + ' ' + author['family'])
                #print(authors)
                num_authors = len(authors)
                #print(num_authors)
                title = data['message']['title']
                #print(title)
                date = data['message']['created']['date-parts'][0]
                year = date[0]
                month = date[1]
                day = date[2]
                date = datetime.date(int(year), int(month), int(day)).strftime('%m/%d/%Y')
                #print(date)
                url = data['message']['resource']['primary']['URL']
                #print(URL)
    print(authors, num_authors, title, year, url)
    return authors, num_authors, title, year, url

def read_csv(infile):
    df = pd.read_csv(infile)
    for index, row in df.iterrows():
        df[['Authors', 'Number of Authors', 'Title', 'Date', 'URL']] = df['DOI'].apply(scrape_details).apply(pd.Series)
    return df

def main():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/authors/authors_dataset_with_titles.xlsx - Sheet1-2.csv')
    new_list_dict = []
    for index, row in df.iterrows():
        doi = row['DOI']
        algorithm = row['name']
        authors, num_authors, title, year, url = scrape_details(doi)
        
        # Append the scraped details to the new DataFrame
        new_list_dict.append({
            'Algorithm': algorithm,
            'DOI': doi,
            'Authors': authors,
            'Number of Authors': num_authors,
            'Title': title,
            'Year': year,
            'URL': url
        })
    # Save the new DataFrame to a CSV file
    new_df = pd.DataFrame(new_list_dict)
    new_df.to_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/authors/output.csv', index=False)

if __name__ == "__main__":
    main()