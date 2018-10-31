#__author:iruyi
#date:2018/10/30
from urllib import request
# read local file
# input_file = open('C:/WorkspacePython/te.txt','r')
# for line in input_file:
#     line = line.strip()
#     print(line)
# input_file.close()

# optimize
def process_file(name):
    ''' read file and print content'''
    input_file = open(name, 'r')
    for line in input_file:
        line = line.strip()
        print(line)
    input_file.close()

# read remote file
def process_remote_file(url):
    ''' process remote file and print content'''
    web_page = request.urlopen(url)
    for line in web_page:
        line = line.strip()
        print(line)
    web_page.close()


def process_file_common(reader):
    ''' Reader and print contents both local file and remote file'''
    for line in reader:
        print(line)

def skip_header(reader):
    ''' skip header'''
    line = reader.readline()
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()
    return line

def process_skip_file(r):
    ''' Read and print open reader r.Skip unvalid line. Every line has one digital value in valid line'''
    line = skip_header(r).strip()
    list = []
    print(line)
    if line != '-':
        list.append(float(line))

    # Read the rest of the data
    for line in r:
        line = line.strip()
        print(line)
        if line != '-': # 判断缺失值
            list.append(float(line))
    return list

def process_skip_file2(r):
    ''' Read and print open reader r. Every line have mulitiple values and every value ends with full stop'''
    line = skip_header(r).strip()
    list = []
    print(line)
    values = line.split()
    for value in values:
        value = value.strip().replace('.', '')
        # value = value.strip()[:-1]
        if value != '-':  # 判断缺失值
            list.append(float(value))

    # Read the rest of the data
    for line in r:
        line = line.strip()
        print(line)
        values = line.split()
        for value in values:
            value = value.strip().replace('.', '')
            if value != '-':  # 判断缺失值
                list.append(float(value))
    return list

if __name__ == '__main__':
    # process_file('C:/WorkspacePython/te.txt')
    tt = process_remote_file("https://www.baidu.com/")
    print(tt)
    # input_file = open('../data/test_data.txt','r')
    # process_file_common(input_file)
    # list = process_skip_file(input_file)
    # list = process_skip_file2(input_file)
    # input_file.close()
    # print('result:', list)
    # print('smallest:', min(list))




