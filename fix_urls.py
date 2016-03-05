import os
import fnmatch

html_files = []

for root, dirname, filenames in os.walk('mylesbraithwaite.com'):
    for filename in fnmatch.filter(filenames, '*.html'):
        html_files.append(os.path.join(root, filename))

for html_file in html_files:
    print(html_file)

    with open(html_file, 'r') as f:
        contents = f.read()

    with open(html_file, 'w+') as f:
        contents = contents.replace('//media.mylesbraithwaite.com/', '/media/')
        contents = contents.replace('//static.mylesbraithwaite.com/', '/static/')

        contents = contents.replace('http:/media/', '/media/')
        contents = contents.replace('http:/static/', '/static/')

        contents = contents.replace('https:/media/', '/media/')
        contents = contents.replace('https:/static/', '/static/')

        f.write(contents)
