import click
import os
import shutil
import zipfile
from zipfile import ZipFile, is_zipfile

IMG_PATH = 'tmp/OEBPS/images/'


def epubtocbz(file, origin, destination):
    origin_path = origin+'/'+file
    if not zipfile.is_zipfile(origin_path):
        print(f'{{file}} is not a zip file and cannot be processed.')
    else:
        with ZipFile(origin_path) as origin:
            origin.extractall(path='tmp/')
            if os.path.isfile(IMG_PATH + 'Cover.jpg'):
                os.rename(IMG_PATH + 'Cover.jpg',
                          IMG_PATH + 'page001.jpg')
                destination_path = destination+'/' + \
                    file.removesuffix('.epub')+'.cbz'
                with ZipFile(destination_path, 'w') as destination_file:
                    for img_file in os.listdir(IMG_PATH):
                        destination_file.write(
                            IMG_PATH+img_file)
            else:
                print(f'Cover.jpg file not found in file : {{file}}')
            shutil.rmtree('tmp')


@click.command()
@click.argument('origin')
@click.argument('destination')
def main(origin, destination):
    origin_files = [f for f in os.listdir(origin) if f.endswith('.epub')]
    if len(origin_files) > 0:
        # make something
        for file in origin_files:
            epubtocbz(file, origin, destination)
    else:
        print(f'No .epub file found in {{origin}}. Exiting')


if __name__ == '__main__':
    main()
