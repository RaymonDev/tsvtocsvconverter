# TSV to CSV converter
This program written in Python converts any TSV file to CSV. If your file is really big, the program will go slower, but it will work.

## How it works

This program uses Pandas to replace all the tabs with commas. It succesfully converts a TSV file into a CSV file that can be interpreted by the machine. 


### Requisites:
- Tkinter
- Pandas (https://github.com/pandas-dev/pandas)
- PyNotifier (https://pypi.org/project/py-notifier/)
- OS

 ```
pip install pandas
 ```
 
 ```
pip install py-notifier
 ```

### Installing and executing

- Download or clone the repository.
- Install the required libraries (specified in the Requisites section)
- If you have more than one version of python in your computer, make sure you are installing the libraries on the correct version (the version that you are going to use)
- Execute the Python file (with the launcher or through any other prefered method). The lanucher only works for sure on Windows 10
- Press the "Choose file" button and select the file that you want to convert
- Press "Convert"
- The program will start converting the file. Take into account that if the file is large, the program will take a little bit longer to convert it
- A new CSV file should be created in the same path as the python file.

### Works for sure on:

- Windows 10 with Python 3.9
