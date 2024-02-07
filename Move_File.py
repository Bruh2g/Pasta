import os
import shutil
inicio="C:/Users/Servidor VIVO/Desktop/Programação/102"
fim="C:/Users/Servidor VIVO/Desktop/Pasta"
lista=os.listdir(inicio)
for file_name in lista:
    name,ext=os.path.splitext(file_name)
    if ext=="":
        continue
    if ext in[".pdf"]:
        pasta1=inicio+"/"+file_name
        pasta2=fim+"/"+"documentos"
        pasta3=fim+"/"+"documentos"+"/"+file_name
        if os.path.exists(pasta2):
            print("movendo")
            shutil.move(pasta1,pasta3)
        else:
            os.makedirs(pasta2)
            print("movendo")
            shutil.move(pasta1,pasta2)