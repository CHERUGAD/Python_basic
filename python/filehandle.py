#File writing and reading
with open('test.txt', 'w') as f:
    f.write('Hello, World!')
with open('test.txt', 'r') as f:
    print(f.read())
#file reading line by line
with open('test.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write('Hello, World!\n')
    f.write('Hello, World!\n')
with open('test.txt', 'r') as f:
    for line in f:
        print(line)
