import os
import re
import sys
from io import TextIOWrapper
from tkinter import Tk, filedialog

g_count = 0

def date_split(name: str) -> str:
    # r1 - YYYY*MM*DD (asterisk for any non-alphanumeric)
    # r2 - YYYYMMDD
    r1 = re.compile('\d{4,4}\W\d{2,2}\W\d{2,2}')
    r2 = re.compile('\d{8,8}')
    date = None
    body = None

    if (m := r1.match(name)):
        date = m.group()
        date = re.sub(r'\W', '-', date)
        body = r1.split(name)[1]

    elif (m := r2.match(name)):
        date = m.group()
        date = f'{date[:6]}-{date[6:]}'
        date = f'{date[:4]}-{date[4:]}'
        body = r2.split(name)[1]

    if (date or body) is None:
        sys.exit("Error: file(s) selected does not conform to date regex")
    body = re.split(r'\W*', body, 1)[1]
    return date, body

def numbering_split(name: str) -> str:
    # any decimal
    r = re.compile('\d*')
    number = None
    body = None

    if (m := r.match(name)):
        number = m.group()
        number = number.lstrip('0')
        body = r.split(name, 1)[1]
        body = re.split(r'\W*', body, 1)[1]

    return number, body


def rename(f: TextIOWrapper) -> None:
    f.close()
    file = f.name
    # path = dir + filename + ext
    path, ext = os.path.splitext(file)
    dir, filename = path.rsplit('/', 1)

    # vvvv MAIN RENAMING SECTION vvvv
    # uncomment snippet for appropriate scenario

    # YYYY-MM-DD - Body
    # date, body = date_split(filename)
    # print(date, body)

    # 01 - Body
    # numbering, body = numbering_split(filename)
    # numbering = numbering.zfill(2)
    # print(numbering, body)

    # Counter
    # global g_count
    # g_count = g_count + 1
    # count = str(g_count).zfill(2)
    # ^^^^ MAIN RENAMING SECTION ^^^^

    newName = f'template{ext}'
    
    print(f'{filename}{ext}')
    print(f'\t{newName}\n')

    # newFile = f'{dir}/{newName}'
    # os.rename(file, newFile)
        

if __name__ == '__main__':
    Tk().withdraw()
    files = filedialog.askopenfiles()
    for f in files:
        rename(f)
