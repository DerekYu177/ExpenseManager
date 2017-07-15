This is be roughly split into three parts: Input, Process, Output

## Operation
#### Input

Getting the photo. We wait until the photos have been imported onto the processing computer.
  1. We query the user to determine the relevant folder (_ui still under construction_)
  2. We run over all of the photos to determine which ones are receipts (_can we use ML for this?_)

  _Investigation onto Photos naming scheme still needed._

#### Process

We apply OCR onto each photo to extract relevant tags and attributes.

  1. The extracted data currently is the date-time, and the total amount. (_currently working on the address_)
  2. This extracted data is then compared to the database, where duplicates are ignored. (We have the time attribute so this should be okay). Unique entries are inserted into the relevant line.
  3. For questionable attributes such as the address, the computer will prompt with a image of the text in question. _(Can ML be used to improve this accuracy?)_

#### Output

We log all data into a .csv file.

## Installation Process
### required packages

```
brew install tesseract
pip install Pillow
pip install pytesseract
```

### To get homebrew w/ python2.7 and PyQt4:

```
xcode-select --install
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install cartr/qt4/pyqt
brew install python
```

### Adding to your PYTHONPATH
```
 /usr/local/Cellar/python/2.7.13/Frameworks/Python.Framework/Version/2.7/bin/python2.7
/usr/local/Cellar/pyqt/
```

##### credits
- `robonobodojo` for the excellent guide

> to view markdown in atom, use ctrl-shift-m
