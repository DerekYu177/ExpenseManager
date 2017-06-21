#!/usr/bin/python

# This should be roughly split into three parts
# 1. Getting the photo. This can take several different forms
# depending on what the format is. The easiest is to wait until all
# the photos have been taken (one photo per receipt)
#
# 2. Once the photos have been imported onto a computer, we apply CV onto each photo.
# Photos which are receipts are indexed and the data should be added to a CSV file.
#
# 3. Duplicate photos are ignored once if their attributes are the same.
# For questionable attributes, the computer will prompt with a image of the text in question.
