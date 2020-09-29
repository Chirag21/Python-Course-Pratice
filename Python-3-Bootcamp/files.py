from io import open_code


with open('myfile.txt') as myfile:
    contents=myfile.read()

print(contents)

with open('myfile.txt') as myfile,open('myfilecopy.txt',mode='w+') as myfilecopy:
    myfilecopy.write(myfile.read())

with open('myfilecopy.txt') as myfile1:
    contents1=myfile1.read()

print(type(contents1))

print(f'############################\n{contents}')

help(print)