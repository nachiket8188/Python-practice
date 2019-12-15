import os

os.chdir("D:\Songs\Albums\K.K\K.K-Best-Of-Me-Compilation-Vol.1-128Kbps(Songs.PK)")
print(os.getcwd())

# for f in os.listdir():
#     filename, ext = os.path.splitext(f)
#     no, artist, title = filename.split('- ')
#     print(title)
#     # print(f'{no} - {title}')
#     os.rename(f, f'{title}.{ext}')

for f in os.listdir():
    os.rename(f, f'{f}.mp3')

