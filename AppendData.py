f=open('output.txt','a')
x=int(input('Enter numner of lines you wat to append: '))
for i in range(x):
    y=input("Enter text to write to the file: ")
    f.write(y)
    print('Data successfully appended.')
f.close()
f=open('output.txt')
for i in f.readlines():
    print(i)
f.close()
