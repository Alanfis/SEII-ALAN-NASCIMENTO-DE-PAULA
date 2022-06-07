# Real Word Example: Parsing Names From a CSV to an HTML List

import csv

html_outuput = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # for item in csv_data:
    #     print(item)
    # We don't want headers or first line of bad data
    #print(csv_data)

    next(csv_data)
    for line in csv_data:
        #print(list(csv_data))
        #print(line)
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_outuput += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_outuput += '\n<ul>'

for name in names:
    html_outuput += f'\n\t<li>{name}</li>'

html_outuput += '\n</ul>'

print(html_outuput)

# for name in names:
#     print(name)