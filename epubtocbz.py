import zipfile
from zipfile import ZipFile
import os

print(zipfile.is_zipfile("origin/alienated.epub"))
with ZipFile("origin/alienated.epub") as origin:
    origin.extractall(path='tmp/origin')

os.rename('tmp/origin/OEBPS/images/Cover.jpg',
          'tmp/origin/OEBPS/images/page001.jpg')

with ZipFile('destination/alienated.cbz', 'w') as destination:
    for file in os.listdir('tmp/origin/OEBPS/images'):
        destination.write('tmp/origin/OEBPS/images/'+file)
