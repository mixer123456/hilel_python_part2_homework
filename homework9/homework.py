import csv
import json

factory = {
    'It department': 100,
    'Sales dep': 100,
    'Production dep': 100,
    'Law dep': 100,
    'Construction dep': 100,
}


def save_data():
    '''
    save data json and csv
    :return:
    '''
    global factory
    with open('data.json', mode='w', encoding='utf-8') as file:
        json.dump(factory, file, sort_keys=True, skipkeys=True, indent=4)

    with open('data.csv', mode='w', encoding='utf-8') as file:
        ob_csv = csv.DictWriter(file, fieldnames=factory.keys(), lineterminator='\n')
        ob_csv.writeheader()
        ob_csv.writerows([factory])


def read_data_json():
    '''
    read data json
    :return: data from json file
    '''
    with open('data.json', mode='r', encoding='utf-8') as file:
        return file.read()


def read_data_csv():
    '''
    read data csv
    :return: read data from csv file
    '''
    with open('data.csv', mode='r', encoding='utf-8') as file:
        dict_data = csv.DictReader(file)
        return next(dict_data)


factory.update({'Law dep': 50})

factory['Finance dep'] = 100

factory.pop('Finance dep')
print(factory)
save_data()

staff = read_data_json()

print(f'''json data
{staff}''')



# count_staff = staff.values()
# print(sum(count_staff))

staff = read_data_csv()

print(f'''
csv data
{staff}''')

count_staff = staff.values()
print(sum(count_staff))
