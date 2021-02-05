import os
import sys
from pathlib import Path

categories = {
    'images':   ('JPEG', 'PNG', 'JPG', 'SVG',),
    'videos':   ('AVI', 'MP4', 'MOV', 'MKV',),
    'documents':('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX',),
    'musics':   ('MP3', 'OGG', 'WAV', 'AMR',),
    'archives':   ('ZIP', 'GZ', 'TAR',),
    'others':   ()
    }

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
#path = "/home/ievgenii/Pictures"
p = Path(path)

# for i in p.iterdir():
#     print(Path(str(i)).is_dir())
# #print(f"Start in {path}")

def get_files_from_dir_recursive(dir):
    files = []
    for i in dir.iterdir():
        if Path(str(i)).is_dir():
            files.extend(get_files_from_dir_recursive(Path(str(i))))              
        else:
            files.append(str(i))
    return files


# files - это список имен файлов и папок в path.
files = get_files_from_dir_recursive(p)

out_put = {}

def fill_dict(cat,file,out_put):
          
    try:       
        l = out_put[cat]   
    except KeyError :
        out_put[cat] = [file]       
    else:
        if not l:
            out_put[cat] = [file]
        else:  
            out_put[cat].append(file) 
    return out_put

def get_file_ext(file_name):
    return  str(file_name.split('.')[-1]).upper()  
  

for file in files:
    if "." in file:
        ext = get_file_ext(file)
       
        if  ext in categories['images']:
            out_put = fill_dict('images', file, out_put)            

        elif  ext in categories['videos']:
            out_put = fill_dict('videos', file, out_put)

        elif  ext in categories['documents']:
            out_put = fill_dict('documents', file, out_put)         

        elif  ext in categories['musics']:
            out_put = fill_dict('musics', file, out_put)

        elif  ext in categories['archives']:
            out_put = fill_dict('archives', file, out_put)

        else:
            out_put = fill_dict('others',file, out_put)

list_other_ext = []

# Список файлов в каждой категории (музыка, видео, фото и пр.)
print("Список файлов в каждой категории (музыка, видео, фото и пр.):")

for cat, fs in out_put.items():
    list_file = "\n".join(fs)
    list_ext = map(get_file_ext,fs)
    if cat == 'others':
        list_other_ext.extend(map(get_file_ext,fs))      


    print(f'Category {cat} has {len(fs)} files')
    print(f'{list_file}')
    print()
    # Список всех расширений, которые встречаются в целевой папке.
    print("Список всех расширений, которые встречаются в целевой папке.:")
    print(" ".join(list(set(list_ext))))
    print()

# Перечень всех расширений, которые скрипту неизвестны.
print("Перечень всех расширений, которые скрипту неизвестны.:")
print(" ".join(list(set(list_other_ext))))


