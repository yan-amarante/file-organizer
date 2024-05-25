import os

print("informe o caminho de uma pasta a ser organizada \nEx: disco_local pasta1 pasta 2 pasta3")

pasta_src = input("")

pasta_src = pasta_src.replace(" ", ":\\", 1).replace(" ", "\\")

pasta_content = os.listdir(pasta_src)

pasta_extensoes = {"set"}

for i in pasta_content:
    pasta_extensoes.add(os.path.splitext(i)[1])

pasta_extensoes.remove("")
pasta_extensoes.remove("set") 

for i in pasta_extensoes:
    if not(os.path.exists(pasta_src + "\\" + i)):
        os.mkdir(pasta_src + "\\" + i)
    else:
        continue

for i in pasta_content:
    for j in pasta_extensoes:
        if os.path.splitext(i)[1] == j :
            os.replace(pasta_src + "\\" + i, pasta_src + "\\" + j + "\\" + i)
        else:
            continue
    print("arquivos movidos com sucesso") 




    
print(pasta_src)
# ()
