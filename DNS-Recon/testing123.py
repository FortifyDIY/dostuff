import os.path

name = 'filename'

var1 = '1'
var2 = '2'
var3 = '3'

list = ['a', 'b', 'c']


def switch(i):
    switcher = {
        'a': var1,
        'b': var2,
        'c': var3
    }
    return switcher.get(i)


for value in list:
    if os.path.isfile(name + '.' + value):
        pass
    else:
        f = open(name + '.' + value, "w+")
        f.close()

    with open(name + '.' + value, "r+") as file:
        for line in file:
            # Read next line
            line = file.readline()
            # check line is not empty
            if value in line:
                break
        else:
            print(value)
            file.write("\n")
            file.write(value)  # append missing data
            file.close()