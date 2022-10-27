import json

if __name__ == "__main__":
    import requests
    from bs4 import BeautifulSoup

    url = 'https://ridibooks.com/category/new-releases/2200'
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    bookservices = soup.select('.title_text')

    my_json_list = []
    for no, book in enumerate(bookservices, 1):
        my_json_list.append({no: book.text.strip()})

    with open('data.json', "w", encoding="UTF-8-sig") as f_write:
        json.dump(my_json_list, f_write, ensure_ascii=False, indent=4)
