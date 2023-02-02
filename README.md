# Batch Rename Script
A script to help rename batches of files using a template. The script works best in scenerios where files need to follow some format.

## Usage
```
python rename.py
```
A file dialogue will let you select files you want to rename. The console will print the original file name and the renamed file indented below.
```
original_file.txt
    renamed_file.txt
```
This script needs to be manually edited in order to work. In the function `rename()`, you format your new file name with the line `newFile = f'template{ext}'`.

There is some code commented out in a block above that grants you access to relevant variables for templating. These variables let you preserve important data from the original file.

If you are happy with the output name, uncomment the final lines of code `os.rename()` and run again.

## Template Variables

### Date
Date variable is pulled from the beginning of the file name. Body is the remaining portion.
```
<date>      <body>
YYYYMMDD    filename.txt
YYYY-MM-DD  filename.txt
YYYY.MM.DD  filename.txt
```
Any date pulled will automatically be formatted to YYYY-MM-DD to match with [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). Any punctuation after the date is ignored.

### Numbering
Numbering variable is pulled from the beginning of the file name. Body is the remaining portion.
```
<number>    <body>
01.         filename.txt
02 -        filename.txt
03          filename.txt
```
Any punctuation after the first number is ignored.

### Counter
Counter lets you increment independent of existing file name if you're trying to re-establish an ordering.
```
file_01.txt
file_02.txt
file_03.txt
```