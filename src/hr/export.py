import json, csv

def format_json(json_list, outfile):
    outfile.write(json.dumps(json_list, sort_keys=True, indent=4))
    outfile.close()

def format_csv(csv_list, outfile):
    outfile.write('name,id,home,shell\n')
    writer = csv.writer(outfile)

    for user in csv_list:
        rows =  [[user['name'], user['id'], user['home'], user['shell']]] 
        writer.writerows(rows)

    outfile.close()
