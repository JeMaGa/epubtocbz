import click
import os
import shutil
import zipfile
from zipfile import ZipFile, is_zipfile

TMP_PATH = 'tmp/'
IMG_PATH = 'OEBPS/images/'
COVER = 'Cover.jpg'
PAGE_1 = 'page001.jpg'
EPUB = '.epub'
CBZ = '.cbz'


def epubtocbz(file, origin, destination):
    origin_path = origin+'/'+file
    if not zipfile.is_zipfile(origin_path):
        print(f'{{file}} is not a zip file and cannot be processed.')
    else:
        with ZipFile(origin_path) as origin:
            origin.extractall(path=TMP_PATH)
            if os.path.isfile(TMP_PATH + IMG_PATH + COVER):
                os.rename(TMP_PATH+IMG_PATH + COVER,
                          TMP_PATH+IMG_PATH + PAGE_1)
                destination_path = destination+'/' + \
                    file.removesuffix(EPUB)+CBZ
                with ZipFile(destination_path, 'w') as destination_file:
                    for img_file in os.listdir(TMP_PATH+IMG_PATH):
                        destination_file.write(
                            TMP_PATH+IMG_PATH+img_file)
            else:
                print(f'{{COVER}} file not found in file : {{file}}')
            shutil.rmtree('tmp')


@click.command()
@click.argument('origin')
@click.argument('destination')
def main(origin, destination):
    if os.path.isdir(origin):
        origin_files = [f for f in os.listdir(origin) if f.endswith('.epub')]
        if len(origin_files) > 0:
            # destination exists ?
            if not os.path.isdir(destination):
                os.makedirs(destination)
                print(
                    f'The destination path {{destination}} has been created.')
            # make something
            with click.progressbar(origin_files, label='Processing files', length=len(origin_files)) as bar:
                for file in bar:
                    epubtocbz(file, origin, destination)
        else:
            print(f'No .epub file found in {{origin}}. Exiting')
    else:
        print(f'{{origin}} is not a directory. Exiting')


if __name__ == '__main__':
    main()
