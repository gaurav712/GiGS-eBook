# Copyright (c) 2020 Gaurav Kumar Yadav

from urllib3 import PoolManager
from bs4 import BeautifulSoup

# Server to fetch data from
SERVER_URL = 'http://gen.lib.rus.ec/search.php?req=QUERY&column=COLUMN&res=100' # res=100 means 100 results per page

# Entry indexes for each type for metadata
AUTHOR_INDEX = 1
TITLE_INDEX = 2
PUBLICATION_INDEX = 3
PUBLISHED_YEAR_INDEX = 4
PAGES_INDEX = 5
LANGUAGE_INDEX = 6
SIZE_INDEX = 7
EXTENTION_INDEX = 8
DOWNLOAD_LINKS_INDEX = 9 # and onwards

class FetchData:

    # To store the final result
    data = []

    def __init__(self, query, column = 'title'):

        # To store each entry
        self.entry = {
            'title': '',
            'author': '',
            'year': '',
            'publication': '',
            'pages': '',
            'language': '',
            'size': '',
            'extention': '',
            'links': []
        }

        # Get the data
        self.http = PoolManager()
        self.request = self.http.request('GET', SERVER_URL.replace('QUERY', query, 1).replace('COLUMN', column, 1))

        # Parse the HTML and get the main list table
        self.soup = BeautifulSoup(self.request.data, 'lxml')
        self.contents_table = self.soup.find_all('table')[2]
        del self.soup    # to save memory

        # Get only the rows with actual book info
        self.contents_table = self.contents_table.find_all('tr')[1:]

        # Process each entry
        for row in self.contents_table:

            # Split all the data fields
            row = row.find_all('td')
            # print(self.get_rest(str(row[PUBLICATION_INDEX])))
            # self.title.append(self.get_title(str(row[TITLE_INDEX])))
            self.entry.update({'title': self.get_title(str(row[TITLE_INDEX])),
                               'author': self.get_author(str(row[AUTHOR_INDEX])),
                               'publication': self.get_rest(str(row[PUBLICATION_INDEX])),
                               'year': self.get_rest(str(row[PUBLISHED_YEAR_INDEX])),
                               'pages': self.get_rest(str(row[PAGES_INDEX])),
                               'language': self.get_rest(str(row[LANGUAGE_INDEX])),
                               'size': self.get_rest(str(row[SIZE_INDEX])),
                               'extention': self.get_rest(str(row[EXTENTION_INDEX])),
                               'links': self.get_links(row[DOWNLOAD_LINKS_INDEX:])})
            self.data.append(self.entry)
            self.entry = self.entry.copy()
        
        del self.entry  # to free a little memory

    # Methods to extract METADATA
    # this is obviously not the efficient way,
    # but it works! :)

    def get_title(self, td_text):
        return (td_text.split('title="">')[1].split('<')[0].strip())

    def get_author(self, td_text):
        # Split all the authors
        authors = td_text.split('</a>')
        author_text = ''    # to store final text

        # Strip of unnecessary garbage from start
        for author in authors:
            if author.strip() != '</td>':
                author_text = author_text + author.split('author">')[1] + ', '

        return author_text[:-3]
    
    def get_links(self, td_text):
        links = []  # to store all the mirrors

        for link in td_text:
            links.append(str(link).split('"')[1])
        
        return links

    # This method can parse Publication, Language, Size etc. all with single implementation
    def get_rest(self, td_text):
        return (td_text.split('</td>')[0].split('>')[1])