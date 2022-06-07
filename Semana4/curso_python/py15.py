# CSV Module: How to Read, Parse, and Write CSV Files

import csv 

# with open('new_names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')

#     for line in csv_reader:
#         print(line)

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line['email'])


# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     #next(csv_reader)

    with open('new_names2.csv', 'w') as new_file:
        fielnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fielnames,  delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            #print(line[2])
            #del line['email']
            csv_writer.writerow(line)