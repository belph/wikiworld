# Introduction

This is a repository for playing with the Wikidata free linked database
https://www.wikidata.org/wiki/Wikidata:Main_Page.

# Data Dumps

Full database dumps of Wikidata are available in the JSON format.  The landing
page describing all the full data dumps is
https://www.wikidata.org/wiki/Wikidata:Database_download.
The actual dump files are available here
https://dumps.wikimedia.org/wikidatawiki/entities/.
An example dump file name is ``wikidata-20151005-all.json.gz``

## Pre-process

An important piece of information about the JSON dumps is,

    Each entity object (data item or property) is placed on a separate line
	in the JSON file, so the file can be read line by line, and each line can
	be decoded separately as an individual JSON object.

When uncompressed this file is 54G.  A nice first step is to break the
uncompressed file into smaller files using the ``split`` command,

    split --numeric-suffixes --suffix-length 4 --lines 100000 --verbose --additional-suffix=.json wikidata-20151005-all.json wikidata-20151005-

This will split the main file up into smaller files with 100,000 lines each
using numeric suffixes with 4 digits and appending the .json extension.  The
downside is that the files will not be the same size.  There is a --number
flag for split, that will produce files of equal size, but it will break
lines between files.

As a final step we will remove the first line of the first file and the
last line of the last file as they are just square brackets enclosing the
whole data dump.  After all these operations we will be left with a number
of files in which all lines are strings which can be parsed into JSON
objects with minimal processing.
