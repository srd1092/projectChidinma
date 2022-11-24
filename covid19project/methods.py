import matplotlib.pyplot as plt
import pandas as pd


def read_data(file_name, column_name):
    print("Reading data from csv file")

    df = pd.read_csv(file_name)
    df[column_name] = pd.to_numeric(df[column_name])
    iso_codes = []
    dates = []
    values = []

    for i, row in df[['iso_code', 'date', column_name]].iterrows():
        current_iso = row['iso_code']
        current_date = row['date']

        if pd.notnull(row[column_name]):
            current_value = row[column_name]
        else:
            current_value = 0

        iso_codes.append(current_iso)
        dates.append(current_date)
        values.append(current_value)

    return iso_codes, dates, values


def generate_bar_graph(file_name, column_name):
    data = read_data(file_name, column_name)
    plt.bar(data[0], data[2])
    plt.show()


def min_max(file_name, column_name):
    data = read_data(file_name, column_name)
    minimum_value = min(data[2])
    maximum_value = max(data[2])
    print(f'The minimum value for {column_name} is {"{:,}".format(minimum_value)}')
    print(f'The maximum value for {column_name} is {"{:,}".format(maximum_value)}')


def average_value(file_name, column_name):
    data = read_data(file_name, column_name)
    total_sum = sum(data[2])
    length = len(data[2])
    avg = round(total_sum/length, 3)
    formatted_avg = "{:,}".format(avg)
    print(f'The average value for {column_name} is {formatted_avg}')


def filter_with_iso_code(file_name, column_name, iso_code):
    data = read_data(file_name, column_name)
    # print(f'The {column_name} for {iso_code} are:')
    print(data[0])
    for _ in data[0]:
        if _ == iso_code:
            print(_)

# match the list items as per the row number and display with each iso code
# check for a way to count the number unique items in a list
