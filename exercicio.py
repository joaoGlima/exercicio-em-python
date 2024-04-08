nome = input ('Digite seu nome: ')
idade = input ('Digite sua idade: ')

if nome and idade: 
    print('seu nome é:', nome)
    print ('seu nome invertido é:', nome[::-1])
    print('seu nome contém ou (não) espaço:', ' ' in nome)
    print('seu nome tem:', len( nome))
    print ('a primeira letra do seu nme é:', nome [0])
    print ('a ultima letra do seu nome é:', nome [-1])
    print ('o primeiro numero da sua idade é:', idade [0])
else:
    print ("Desculpe, você deixou campos vazios.")