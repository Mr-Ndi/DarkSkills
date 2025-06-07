from bs4 import BeautifulSoup

with open('courses.html', 'r') as html_file :
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    tag = soup.find_all('h5')
    print(tag)
