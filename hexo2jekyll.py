
'''
After parsing md files from cnblogs' xml file, you may need to add date at the head of each fileName.md for jekyll.
-- this py3 script do:
 - load the markdown post file list
 - open each file and parse out the date
 - add layout
 - build the date-fileName.md


  ref: https://jekyllrb.com/docs/front-matter/
'''

mdFile_folder = 'output'
jekyllposts_dir = 'output_jekyll'

import os
import glob
from os import listdir
from os.path import isfile, join

# create dir for jekyll output
if not os.path.exists(jekyllposts_dir):
    os.mkdir(jekyllposts_dir)

# load the files of hexo
data_folder = mdFile_folder
fileList = [f for f in listdir(data_folder) if isfile(join(data_folder, f))]

new_filesName = []
for post_file in fileList:
    print(post_file)
    with open(mdFile_folder + '/' + post_file, 'r', errors='replace') as postReader:
        content = postReader.readlines()
        if len(content) < 3:   # in case '.DS_Store'
            continue
        else:
            date_str = content[2].split(' ')[1]   # e.g. 2020-01-10
            # insert the second line of content by layout
            content.insert(1, 'layout: post\n')
            content.insert(4, 'category: from_cnblogs\n')
            content[3] = content[3][:-1] + ' +0800' + '\n'   # add time zone info

    postReader.close()
    new_fileName = date_str + '-' + post_file
    # os.rename(mdFile_folder + '/' + post_file, mdFile_folder + '/' + new_fileName)
    new_filesName.append(new_fileName)

    # write
    with open(jekyllposts_dir + '/' + new_fileName, 'w') as file:
        file.writelines(content)
        file.close()

print('done with', len(fileList), 'posts.')
