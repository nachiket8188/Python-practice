import csv

# with open('new_names.csv','r') as f:
#     csv_reader = csv.reader(f)
    # print(csv_reader)  # this is an iterable object. Hence, the loop below.
    # next(csv_reader)
    # # for line in csv_reader:
    # #     print(line)
    # with open('new_names.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='\t')
    #     for line in csv_reader:
    #         csv_writer.writerow(line)
    # for line in csv_reader:  # no delimiter specified for new file.
    #     print(line)
    # using dictionary reader & writer to operate on CSvs.
with open('names.csv','r') as f:
    csv_reader = csv.DictReader(f)
    for line in csv_reader:
        print(line)
