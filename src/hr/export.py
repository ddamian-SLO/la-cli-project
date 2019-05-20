import json, csv

def format_json(json_list, outfile):
    outfile.write(json.dumps(json_list, sort_keys=True, indent=4))
    outfile.close()

def format_csv(csv_list, outfile):
    outfile.write('name,id,home,shell\n')
    writer = csv.writer(outfile)
    rows =  [[csv_list['name'], csv_list['id'], csv_list['home'], csv_list['shell']] for user in csv_list]

    writer.writerows(rows)
    outfile.close()
