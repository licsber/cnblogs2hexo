import os
import re
from datetime import datetime    

xml_file = 'CNBlogs_BlogBackup_1_201707_202002.xml'
out_dir = 'output'

xml_file = open(xml_file).read()
if xml_file[0] == '\ufeff':
    xml_file = xml_file[1:]

if not os.path.exists(out_dir):
    os.mkdir(out_dir)

items = re.findall(r'CDATA\[([\s\S]*?)\]\]>', xml_file)
titles = re.findall(r'item><title>([\s\S]*?)</title', xml_file)
dates = re.findall(r'author><pubDate>([\s\S]*?)</pubDate><guid', xml_file)

assert(len(items) == len(titles))
assert(len(items) == len(dates))

def get_date(date):
    date = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')
    return date

for i in range(len(items)):
    with open(out_dir + '/'+ titles[i] + '.md', 'w') as file:
        file.write('---\n')
        file.write('title: \'' + titles[i])
        file.write('\'\ndate: ' + str(get_date(dates[i])))
        file.write('\n---\n')
        file.write(items[i])
        file.close()