import os
import sys


categories = {
    'images':   ('JPEG', 'PNG', 'JPG',),
    'videos':   ('AVI', 'MP4', 'MOV',),
    'documents':('DOC', 'DOCX', 'TXT',),
    'musics':   ('MP3', 'OGG', 'WAV', 'AMR',),
    'others':   ()
    }

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
#path = "/home/ievgenii/Downloads"
#print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)

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

        else:
            out_put = fill_dict('others',file, out_put)


for cat, fs in out_put.items():
    list_file = "\n".join(fs)
    list_ext = map(get_file_ext,fs)   

    # Список файлов в каждой категории (музыка, видео, фото и пр.)
    print()
    print(f'Category {cat} has {len(fs)} files')
    print(f'{list_file}')
    print()
    # Список всех расширений, которые встречаются в целевой папке.
    print(set(list_ext))
    print()
    
