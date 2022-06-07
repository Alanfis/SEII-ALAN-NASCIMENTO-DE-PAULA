# Automate Parsing and Renaming of Multiple Files

import os

os.chdir('/home/alan/Downloads/My Wife and Kids')

print(os.getcwd())

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    f_title = file_name.split('-')
    #f_title, f_course, f_num = f_name.split('-')
    #f_title = f_title.strip()
    #f_course = f_course.strip()
    #f_num = f_num.strip()[1:].zfill(2)
    #print(f_title)
    print('{}'.format(f_title))
    #print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
    #new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    #os.rename(f, new_name)
    #print(file_name.split('-'))
    #print(f)