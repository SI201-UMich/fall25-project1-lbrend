# name: Brendon Lee
# student ID: 47446397
# email: leebrendg@umich.edu
# collaborators: Gen AI
# solo project


import csv
def read_penguin_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

        print("column1: ", data[0].keys(), )
        print("column2: ", data[1].keys(), "\n")
        print("sample row1: ",data[0], "\n")
        
        print("sample row2: ",data[1], "\n")
        print("total rows: ", len(data))
    return data






def main():
    read_penguin_data('penguins.csv')


if __name__ == "__main__":
    main()