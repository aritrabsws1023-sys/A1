try:
    f=open("sample.txt")
    l=f.readlines()
    for i in range(len(l)):
        print(f'Line {i+1}: {l[i]}')
    f.close()
except:
    print('Error: The file sample.txt was not found.')

