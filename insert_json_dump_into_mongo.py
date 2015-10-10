import os
import json
import pymongo

dump_path = '/home/galtay/Data/WikiData/JsonDumps'
json_dump_file = os.path.join(dump_path, 'wikidata-20151005-all.json')
db_name = '-'.join(os.path.basename(json_dump_file).split('-')[0:2])

client = pymongo.MongoClient()
client.drop_database(db_name)
db = client[db_name]

# insert all rows
with open(json_dump_file, 'r') as fp:
    for iline, line in enumerate(fp):
        if line.startswith('[') or line.startswith(']'):
            continue
        obj = json.loads(line.strip(',\n'))
        db[obj['type']].insert_one(obj)
        if iline%5000 == 0:
            print iline

# index collections on WikiData IDs
db['item'].create_index('id', unique=True)
db['property'].create_index('id', unique=True)

client.close()
