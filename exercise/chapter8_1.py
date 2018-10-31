#__author:iruyi
#date:2018/10/30
import sys

def housing(r):
    ''' Return the difference between the housing starts and construction contracts in 1983 and in 1984 from reader r.'''

    # The monthly housing starts, in thousands of units.
    starts = []
    # The construction contracts, in millions of dollars.
    contracts = []

    # Read the file, populating the lists.
    for line in r:
        start, contract, rate = line.split()
        starts.append(float(start.strip()))
        contracts.append(float(contract.strip()))

    return (sum(starts[12:24]) - sum(starts[0:12]),
            sum(contracts[12:24]) - sum(contracts[0:12]))

if __name__ == '__main__':
    # input_file = open('C:/WorkspacePython/realestate.txt', 'r')
    input_file = open('../data/realestate.txt', 'r')
    print(housing(input_file))
    input_file.close()