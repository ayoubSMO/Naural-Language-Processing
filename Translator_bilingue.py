import gzip
import io

import tqdm
import os
import walkdir

class TranslatorBilingue :

    # Constructeur de notre machine de traduction
    # en deffinissent les fichiers des deux langues
    def __init__(self ,pathLang1 ,pathLang2 ,lang1 ,lang2):
        self.set_embedded_lang1(pathLang1)
        self.set_embedded_lang2(pathLang2)
        self.lang1 = lang1
        self.lang2 = lang2
        print("___ j'ai bien fait la construction !")



    def set_embedded_lang1(self, pathLang1):
        self.pathLang1 = pathLang1

    def set_embedded_lang2(self, pathLang2):
        self.pathLang2 = pathLang2


    # Construction des matrices d’embeddings X,Y d'aprés les vecteurs d'embeddings
    def embedded_Matrix(self):
        try:

            gz_file = gzip.open("cc.ar.300.vec.gz" ,"rb") ; ar_words = gz_file.read() ; print(ar_words)
        except Exception:
            print("You have file1 exception !!")

        try:
            gz_file = gzip.open("cc.en.300.vec.gz" ,"rb") ; en_words = gz_file.read() ; print(en_words)
        except Exception:
            print("You have file2 exception !!")

        return [ar_words ,en_words]


    def load_vectors(self):
       fin = io.open(self.pathLang1 ,encoding='utf-8' ,newline='\n',errors='ignore')
       print("file is open !")
       n ,d = map(int ,fin.readline().split())
       data = {}

       print("loop section !")
       for line in tqdm.tqdm(fin):
           tokens = line.rstrip().split(' ')
           data[tokens[0]] = map(float,tokens[1:])


       return data




