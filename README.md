# Introduction

This is a repository for playing with the Wikidata free linked database
https://www.wikidata.org/wiki/Wikidata:Main_Page.


# Data Dumps

Full database dumps of Wikidata are available in the JSON format.  The landing
page describing all the full data dumps is,

  - https://www.wikidata.org/wiki/Wikidata:Database_download

The actual dump files are available here,

  - https://dumps.wikimedia.org/wikidatawiki/entities

An example dump file name is ``wikidata-20151005-all.json.gz``
An important piece of information about the JSON dumps is,

    Each entity object (data item or property) is placed on a separate line
    in the JSON file, so the file can be read line by line, and each line can
    be decoded separately as an individual JSON object.

The uncompressed files are tens of gigabytes (for example, the file
``wikidata-20151005-all.json.gz`` is 54G when uncompressed).  A
description of the WikiData data model can be found here,

  - https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer

# Load into MongoDB

The data dumps can be loaded into a mongo data base using the
``insert_data_dump_into_mongo.py``.  The script will make one collection
for ``items`` and one collection for ``properties``.  In addition, it will
index these collections on the ``id`` field (the numeric WikiData ID fields
that begin with a Q for items or a P for properties).  For a full data
dump this process will take several hours.