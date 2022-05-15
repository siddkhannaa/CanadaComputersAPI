from flask import request, jsonify
from bs4 import BeautifulSoup

from urllib.request import urlopen
from urllib.parse import quote_plus

import re

generate_search_url = lambda s, page: f'https://www.canadacomputers.com/search/results_details.php?language=en&keywords={s}&page_num={page}'

def product_search(search_string, low, high):
    output = {'products': []}

    # price range param: "pr=" + quote_plus(quote_plus(f"${low}+-+${high}"))

    page = 0

    while 1:
        search = quote_plus(search_string)
        page_str = quote_plus(str(page))
        url = generate_search_url(search, page_str)

        if (low is not None) and (high is not None):
            url += "&pr=" + quote_plus(quote_plus(f"${low}") + "+-+" + quote_plus(f"${high}"))

        print(url)
        data = urlopen(url).read().decode()

        soup = BeautifulSoup(data, 'html.parser')

        no_results = soup.find('div', class_='col-12 mt-5 mb-1')

        if no_results:
            break

        products = soup.findAll('div', class_='productTemplate')

        for product in products:
            title_elem = product.find('span', class_='productTemplate_title')
            title = title_elem.text.strip()
            link = title_elem.find('a')['href']
            price = product.find('span', class_='pq-hdr-product_price').text.strip()
            try:
                item_code = re.findall(r'Item Code: ([A-Z]{5}[0-9]{5})', str(product))[0]
            except IndexError:
                item_code = 'No Code'
            
            try:
                online_availability = product.find('small', class_='pq-hdr-bolder').text.strip()
                if "Online" not in online_availability:
                    online_availability = 'Not Available online'
                    
            except AttributeError:
                online_availability = 'unknown'
                
            try:
                instore_availability = product.find('small', class_='pq-hdr-bolder').text.strip()
                if "In Store" not in instore_availability:
                    instore_availabiltiy = 'Not Available in store'
                    
            except AttributeError:
                instore_availability = 'unknown'
                    
            
            item = {
                'title': title,
                'price': price,
                'item_code': item_code,
                'online_availability': online_availability,
                'instore_availability': instore_availability,
                'link': link
            }

            output['products'].append(item)

            page += 1

    return output