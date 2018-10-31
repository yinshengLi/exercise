#__author:iruyi
#date:2018/10/30
import sys

def read_housing_data(r):
    ''' Read housing data from reader r, returning lists of starts, contracts, and rates.'''
    # The monthly housing starts, in thousands of units.
    starts = []
    # The construction contracts, in millions of dollars.
    contracts = []
    rates = []

    # Read the file, populating the lists.
    for line in r:
        start, contract, rate = line.split()
        starts.append(float(start.strip()))
        contracts.append(float(contract.strip()))
        rates.append(rate.strip())

    return (starts, contracts, rates)

def process_housing_data(starts, contracts):
    '''Return the difference between the housing starts and construction contracts in 1983 and in 1984.'''
    return (sum(starts[12:24]) - sum(starts[0:12]),
     sum(contracts[12:24]) - sum(contracts[0:12]))


if __name__ == '__main__':
    # input_file = open('C:/WorkspacePython/realestate.txt', 'r')
    input_file = open('../data/realestate.txt', 'r')
    starts, contracts, rates = read_housing_data(input_file)
    print(process_housing_data(starts, contracts))
    input_file.close()