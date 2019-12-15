# file objects - reading & writing to files
# f = open('test.txt', 'r')
# print(f.name)
# print(f.mode)
# f.close()
# opening the file using a context manager - the recommended way
# with open('test.txt', 'r') as f:
    # f_contents = f.read()
    # f_contents = f.readlines()
    # f_contents = f.readline()
    # print(f_contents, end='')
    # f_contents = f.readline()
    # print(f_contents)
    # for line in f:
    #     print(line, end='')  # in terms of memory, this is preferred over f.readlines() or
        # f.read() because this one prints one line at a time. So there's only one line in the memory at a time.
    # f_contents = f.read(100)
    # print(f_contents)
    # f_contents = f.read(100)  # 100 is the no. of chars.
    # print(f_contents)
    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')
    # f.seek(0)
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')

    # print(f.tell())

    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)

# print(f.name)
# print(f.mode)
# print(f.closed)
# print(f.read())  # returns error

# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

# with open('test.txt','r') as rf:
#     with open('test.copy', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# with open('Cap Shield.jpg','rb') as rf:
#     with open('Cap Shield copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

with open('Cap Shield.jpg','rb') as rf:
    with open('Cap Shield copy.jpg', 'wb') as wf:
        chunk_size = 1500
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
            