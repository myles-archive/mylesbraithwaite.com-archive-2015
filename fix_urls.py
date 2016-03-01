import os
import fnmatch

html_files = []

for root, dirname, filenames in os.walk('mylesbraithwaite.com'):
    for filename in fnmatch.filter(filenames, '*.html'):
        html_files.append(os.path.join(root, filename))

for html_file in html_files:
    print(html_file)

    with open(html_file, 'w+') as f:
        contents = f.read()

        contents.replace('//media.mylesbraithwaite.com/', '/media/')
        contents.replace('//static.mylesbraithwaite.com/', '/static/')

        contents.replace('http:/media/', '/media/')
        contents.replace('http:/static/', '/static/')

        contents.replace('https:/media/', '/media/')
        contents.replace('https:/static/', '/static/')

        f.write(contents)
