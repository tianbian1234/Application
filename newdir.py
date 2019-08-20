import requests
import lxml.html
import csv

url = 'https://search.damai.cn/search.htm?ctl=演唱会&order=1'
source = requests.get(url).content
print(source)
selecter = lxml.html.fromstring(source)
print(selecter)
item_list = selecter.xpath('//div[@class="search__itemlist"]/div[@class="item__main"]/div[@class="item__box"]/div')
print(item_list)
item_dict_list = []
for item in item_list:
    print(item)
    show_name = item.xpath('//div[@class="item__text"]/div[@class="item__text__title"]/a/text()')
    show_url = item.xpath('//div[@class="item__text"]/div[@class="item__text__title"]/a/@href')
    show_time = item.xpath('//div[@class="item__text"]/div[@class="item__text__time"]/text()')

    item_dict = {'show_name': show_name[0] if show_name else '',
                 'show_url': 'https' + show_url[0] if show_url else '',
                 'show_time': show_time[0].strip() if show_time else ''}
    item_dict_list.append(item_dict)

with open('result.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames = ['show_name', 'show_url', 'show_time'])



    writer.writeheader()
    writer.writerows(item_dict_list)

