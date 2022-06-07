# File Objects: Reading and Writing to Files

with open('test.txt', 'r') as f: 
    #f_contents = f.read()
    #for line in f:
        #print(line, end='')
    #f_contents = f.readline()
    #print(f_contents, end='')

    #f_contents = f.readline()
    #print(f_contents, end='')
    size_to_read = 100
    #f_contents = f.read(size_to_read)
    #print(f_contents, end='')

    #f_contents = f.read(size_to_read)
    #print(f_contents, end='')

    #while len(f_contents) > 0:
    #    print(f_contents, end='')
    #    f_contents = f.read(size_to_read)
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)
    #print(f.tell())

#f = open('test.txt', 'r')

#with open('test2.txt', 'w') as f:
#   f.write('Test')
#   f.seek(0)
#   f.write('R')

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('img.jpg', 'rb') as rf:
    with open('img_copy.jpg', 'wb') as wf:
         #for line in rf:
         #   wf.write(line)
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

print(f.name)
print(f.mode)
print(f.close)
#print(f.read())

f.close()