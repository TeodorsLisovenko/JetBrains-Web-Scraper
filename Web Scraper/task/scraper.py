import os
import string

import requests
from bs4 import BeautifulSoup


def file_saver(file_title, file_content):
    file_to_save = open(file_title + '.txt', 'w', encoding='utf-8')
    file_to_save.write(file_content)
    file_to_save.close()


page_range = int(input())
topic_to_search = input()

# Creating all page folders
try:
    for page_number in range(1, page_range + 1):
        os.mkdir(f'Page_{page_number}')
except FileExistsError:
    pass

for page_number in range(1, page_range + 1):

    r = requests.get(f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={page_number}")
    os.chdir(f"Page_{page_number}")
    if r.status_code == 200:

        soup = BeautifulSoup(r.content, 'html.parser')
        main = soup.find('div', attrs={'class': 'position-relative z-index-1'})
        section_of_articles = main.find('section', attrs={'class': 'u-mb-48 u-mt-48'})
        article_container = section_of_articles.find('div', attrs={'class': 'u-container'})
        block_of_articles = article_container.find('ul', attrs={'class': 'app-article-list-row'})
        list_of_articles = block_of_articles.findAll('li', attrs={'class': 'app-article-list-row__item'})

        for article in list_of_articles:
            wrapper_of_article = article.find('div', attrs={'class': 'u-full-height'})
            content_of_article = wrapper_of_article.find('article',
                                                         attrs={'class': 'u-full-height c-card c-card--flush'})

            # Check topic category
            section_of_topic = content_of_article.find('div', attrs={'class': 'c-card__section c-meta'})
            topic = section_of_topic.find('span', attrs={'class': 'c-meta__type'})
            y = topic.text

            if topic.text == topic_to_search:
                # Getting title
                title = content_of_article.find('h3', attrs={'class': 'c-card__title'})

                # Modifying clean title for file name
                clean_punctuation = title.text.translate(str.maketrans('', '', string.punctuation))
                replace_whitespace = clean_punctuation.replace(" ", "_")
                title_for_filename = replace_whitespace.replace("\n", "")

                # Getting article link from title
                link_of_title = title.find('a', href=True)
                fetch_article = requests.get('https://www.nature.com' + link_of_title['href'])
                soup_article = BeautifulSoup(fetch_article.content, 'html.parser')

                # Getting articles content
                article_main = soup_article.find('div', attrs={'role': 'main'})
                article_wrapper_one = article_main.find('article', attrs={
                    'class': 'article-item'})
                article_wrapper_three = article_wrapper_one.find('div', attrs={
                    'class': 'container cleared container-type-article'})
                article_wrapper_four = article_wrapper_three.find('div', attrs={'data-component': 'article-container'})

                # Research Highlight are bit different form others so if the line below fails we reset article_body with one that is present in Research Highlight ones.
                article_body = article_wrapper_four.find('div', attrs={'class': 'align-left'})

                if article_body is None:
                    article_body = article_wrapper_four.find('div', attrs={'class': 'article__copy'})
                    article_section = article_body.find('div', attrs={'class': 'article-item__body'})
                else:
                    article_section = article_body.find('div', attrs={'class': 'article__body cleared'})

                # Getting paragraphs
                article_paragraphs = article_section.findAll('p')

                content = ""
                for paragraph in article_paragraphs:
                    content += paragraph.text

                # Saving in file
                file_saver(title_for_filename, content)

        os.chdir('..')
    else:
        print("Request failed!")
