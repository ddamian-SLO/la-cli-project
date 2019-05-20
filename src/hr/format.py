import json, csv, sys

def format_json(json_list, outfile=sys.stdout):
    outfile.write(json.dumps(json_list, sort_keys=True, indent=4))
    outfile.close()

def format_csv()