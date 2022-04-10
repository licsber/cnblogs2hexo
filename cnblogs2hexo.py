import os
import re
from datetime import datetime

'''
  replace the / in title with the _ for fileName.md saving
'''

xml_file = 'CNBlogs_BlogBackup_131_201301_202106.xml'
out_dir = 'output'

xml_file = open(xml_file, 'r', encoding='UTF-8').read()
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
    if '/' in titles[i]:
        print('path with slash:', titles[i])
        title_legal = titles[i].replace('/', '_')
    else:
        title_legal = titles[i]

    with open(out_dir + '/'+ title_legal + '.md', 'w', encoding='utf-8') as file:
        file.write('---\n')
        if '\'' in titles[i] and '\"' not in titles[i]:
            file.write('title: \"' + titles[i])
            file.write('\"\ndate: ' + str(get_date(dates[i])))
        elif '\"' in titles[i] and '\'' not in titles[i] :
            file.write('title: \'' + titles[i])
            file.write('\'\ndate: ' + str(get_date(dates[i])))
        elif '\"' in titles[i] and '\'' in titles[i]:
            file.write('title: \'' + titles[i])
            file.write('\'\ndate: ' + str(get_date(dates[i])))
            print('warning! the \' and \" are in frontmatter of file:', titles[i])
        else:
            file.write('title: \'' + titles[i])
            file.write('\'\ndate: ' + str(get_date(dates[i])))

        file.write('\n---\n')
        file.write(items[i])
        file.close()
