# import statements
import os
import csv
import pandas as pds

def create_list_of_file_names(folder_path):
    list_of_file_names = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            #print(filename)
            list_of_file_names.append(filename)
    #print(list_of_file_names)
    return list_of_file_names

def create_list_of_cells(list_of_file_names, directory):
    os.chdir(directory)
    list_of_cells = []
    for file in list_of_file_names:
        with open(file) as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for row in reader: 
                for cell in row:
                    list_of_cells.append(cell)
                    #print(cell)
    #print(list_of_cells)
    return list_of_cells


def create_list_of_links(list_of_cells):
    list_of_links = []
    for cell in list_of_cells:
        if ("http://" in cell or "https://" in cell) & (cell not in list_of_links):
            link = cell.split(' ')[0]
            list_of_links.append(link)
            #print(link)
    print(list_of_links)
    return list_of_links

def create_links_csv(list_of_links, file_name, directory):
    os.chdir(directory)
    with open(file_name, 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["links"])
        for link in list_of_links:
            writer.writerow([link])

def main():
    list_of_file_names = create_list_of_file_names("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/authors/google_sheet_pages_test")
    list_of_cells = create_list_of_cells(list_of_file_names, "/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/authors/google_sheet_pages_test")
    list_of_links = create_list_of_links(list_of_cells)
    create_links_csv(list_of_links, "links.csv", "/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/authors")


if __name__ == "__main__":
    main()