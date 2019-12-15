import csv

html_output = ''
names = []
with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)
    # We don't want headers or first line of data.
    next(csv_data)  # One can use this next() method on a generator to skip one iteration.
    next(csv_data)
    for line in csv_data:
        # print(line)
        if line[0] == 'No Reward':
            break
        names.append(str(f'{line[0]} {line[1]}'))

# for name in names:
#     print(name)

html_output += f"<p>There are currently {len(names)} public contributors. Thanks !</p>"
# print(html_output)
html_output += '\n<ul>'

for name in names:
    html_output += f"\n\t<li>{name}</li>"

html_output += "\n/<ul>"
print(html_output)

#  this same thing can be achieved using DictReader from csv module too.
