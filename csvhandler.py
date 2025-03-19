import csv

def write_to_csv(filename, header, data):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

def append_to_csv(filename, data):
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

def read_from_csv(filename):
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  
        return [row for row in reader]