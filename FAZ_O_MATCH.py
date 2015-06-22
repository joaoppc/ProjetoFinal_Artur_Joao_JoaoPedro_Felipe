# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:52:13 2015

@author: Felipe
"""

import time
from firebase import firebase
import numpy as np
import matplotlib.pyplot as plt
import collections


firebase = firebase.FirebaseApplication('https://insper-match.firebaseio.com', None)
result = firebase.get('/cadastro', None)# retorna um dícionario com os dados do firebase
Esporte = ["Futebol","Futsal","Vôlei","Handebol","Jiu-Jitsu","Judô","Rugby","Natação","Basquete","Tênis de Mesa","Tênis","Xadrez"]
Preferência = ["Balada","Ler um Livro","Role no Shopping","Ficar em Casa","Soneca","Passear no Parque","Concerto","Teatro","Show","Bar","Cinema","Stand-Up"]
Música = ["Eletrônica","Reggae","Rock","Rap","Sertanejo","Samba","Pagode","Clássica","Funk","Jazz","Forró","MPB"]
Instrumentos = ["Percurssão","Saxofone","Violão","Gaita","Piano","Baixo","Banjo","Cavaquinho","Xilofone","Violino","Flauta","Ukulele"]
Entidade= ["Bateria Imperial","Revista Insper Post","Liga de Enpreendendorismo","Sementes Culturais","Diretório Acâdemico","InFinance","AIESEC","Enactus","BemGasto","GAS","Atlética","Insper Jr"]
indi={} # cria o dicionario indi
count = 0# inicializa um contador
new_result = {}
result=collections.OrderedDict(sorted(result.items(), key=lambda t: t[0])) # ordena o dicionario retornado pelo firebase
for key, val in result.items():
        new_result[val[0]] = [key,result[key]]
new_result = collections.OrderedDict(sorted(new_result.items(), key=lambda t: t[0]))

#print(new_result)
#print(new_result['Artur'][1][1])
filtro = input('selecione o nome' )
ultimo = 'z' + filtro
new_result[ultimo] = new_result.pop(filtro)
for j in new_result.keys(): # loop for criado para percorrer todas as chaves do ficionario result, criado pelo firebase
    esporte_ind=[] 
    preferencia_ind=[] 
    instrumento_ind=[] 
    entidade_ind=[]
    musica_ind=[]
    abc = new_result[j] #cria uma variável(do tipo lista) que retorna os valores dos dicionário
                                #0 = nome
                                #1 = check
                                #2 = email
                                #3 = curso                         
                                #4 = Bairro
                                #5 = periodo
                                #6 = Sexo
                                #7 = dia
                                #8 = mes
                                #9 = ano
    
    if (int(time.strftime('%d'))) >= ((int(abc[1][7]))) and (int(time.strftime('%m'))) >= (int(abc[1][8])):#calcula a idade dos alunos
        
        idade =   int(time.strftime('20%y'))-int(abc[1][9])   
    #else:
        #idade = (int(time.strftime('20%y'))-int(abc[9]))-1           #consertar bug!!!
        
    
    #print (abc[0], 'e-mail:',abc[2], 'curso:',abc[3], 'bairro:',abc[4],'periodo:',abc[5],'preferencias:',abc[1],'idade:',idade,'anos')
    for q in abc[1][1]: #loop for para percorrer todos os item check de cada aluno
        if q in Esporte:        #adiciona nas lista de acordo com sua categoria
            esporte_ind.append(q)
        if q in Preferência:
            preferencia_ind.append(q)
        if q in Instrumentos:
            instrumento_ind.append(q)
        if q in Entidade:
            entidade_ind.append(q)
        if q in Música:
            musica_ind.append(q)
        

    
    count+=1    #adiciona 1 ao contador
    match = {}  #cria um dicionario vazio match
    matches = []    #cria uma lista vazia matches
    alunos=[]       #cria uma lista vazia alunos
    #print(esporte_ind,preferencia_ind,musica_ind,entidade_ind,instrumento_ind)
    indi[count]=[abc[1][0]],esporte_ind,preferencia_ind,musica_ind,entidade_ind,instrumento_ind #cria um dicionário na qual a chave é o contador 
    indi=collections.OrderedDict(sorted(indi.items(), key=lambda t: t[0])) #ordena o dicionário indi
    
if count < 2: # condição que garante que tem que háver pelo menos duas pessoas cadastradas
    pass
else:
    for h in indi[count]: #loop for que percorre todos os item dentro do dicionario indi
        for z in h: # loop for que percorre todos as listas que estavam dentro do dicionario
            for y in range(1,len(indi)):    #loop for que coloca em y um número de acordo com o número de pessoas cadastrado
                for v in indi[count-y]: #loop que percorre o dicionario indi na qual a chave é o dicionario anterior -y 
                    
                    for g in v: # loop for que percorre o dicionario indi[count-y] retornando em g os itens selecionado pelo usuário
                        if z == g: # condição que se os itens selecionados pelo usuario 1(z) forem iguais aos selecionados pelo usuario 2(g) execute o resto
                            aluno1=indi[count][0]#coloca em uma variável o nome do cadastrado1
                            aluno2=indi[count-y][0]#coloca em uma variável o nome do segundo cadastrado
                            
                            matches.append(aluno1[0])# pega a lista matches e adiciona o nome do cadastrado 1
                            matches.append(aluno2[0])#pega a lista matches e adiciona o nome do cadastrado2
                            if aluno1 not in alunos:
                                alunos.append(aluno1)# cria uma lista com todos os alunos(usuarios)
                            if aluno2 not in alunos:
                                alunos.append(aluno2)
                            match[aluno1[0],aluno2[0]]=matches.count(aluno2[0])     #pega o dicionario match e em como chave utiliza aluno1 e o aluno2 como chaves e como valor utiliza quantas vezes o aluno 2 apareceu(match)
                            match =result=collections.OrderedDict(sorted(match.items(), key=lambda t: t[0]))# ordena o dicionário match
                            
                            #print(aluno1[0],' e ',aluno2[0],' tiveram ',matches.count(aluno2[0]),' matches ')       
                            print(aluno1[0],aluno2[0],z,g)
                            #print(z,g,aluno1,aluno2)
    #print(aluno1[0],' e ',aluno2[0],' tiveram ',matches.count(aluno2[0]),' matches ')                        #print(matches)
               #print(y)
porc=[]
for t in range(1,len(alunos)):
    porc.append( (match.popitem()[1]/ (len(abc[1][1])))*100)
    

n_groups = len(alunos)-1            #reproduz o gráfico de barras
#print(porc)


    
means_men = (porc)

#std_men = (2, 3, 4)

#means_women = (25, 32, 34, 20, 25)
#std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.1

opacity = 1
#error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='r',
                 label=aluno1[0])



plt.xlabel('Aluno')
plt.ylabel('% afinidade')
plt.title('InsperMatch')
num_label=[]
for b in range(1,len(alunos)):
        num_label.append(alunos[b][0])
        plt.xticks((index + bar_width)-0.020*n_groups,num_label  )

plt.legend()

plt.tight_layout()
plt.show()  