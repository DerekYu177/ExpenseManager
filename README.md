This is be roughly split into three parts: Input, Process, Output

##### Input

Getting the photo. This can take several different forms depending on what the format is. The easiest is to wait until all the photos have been taken (one photo per receipt). 
  1. These photos can be grabbed directly from where they are stored.
  2. This does mean that when they are imported into the Apple Photos app, they need to be exported. Each export group can be automatically tagged with the date, making each export easier

  _Investigation onto Photos naming scheme still needed._

##### Process

We apply CV onto each photo to extract relevant tags and attributes.

  1. Duplicate photos are ignored once if their attributes are the same. (A property if imported photos are automatically deleted)
  2. For questionable attributes, the computer will prompt with a image of the text in question. _(Can ML be used to improve this accuracy?)_
  3. Receipts are then extracted and indexed into another folder. (All receipts which are a month old can be deleted)
  4. Relevant Metadata is also collected from the photo for context.

##### Output

Photos which are receipts are indexed and the data should be added to a CSV file. Technically any format is okay as long as the data exists.
