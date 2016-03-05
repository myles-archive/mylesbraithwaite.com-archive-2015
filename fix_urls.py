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
        contents = f.read()

        contentes = contents.replace('//media.mylesbraithwaite.com/', '/media/')
        contentes = contents.replace('//static.mylesbraithwaite.com/', '/static/')

        contentes = contents.replace('http:/media/', '/media/')
        contentes = contents.replace('http:/static/', '/static/')

        contentes = contents.replace('https:/media/', '/media/')
        contentes = contents.replace('https:/static/', '/static/')

        f.write(contents)
