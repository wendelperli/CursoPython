# Manipulando Textos
frase = 'Curso em Vídeo Python'
#print(frase[3]) #Mostra a quarta letra (índice 3)
#print(frase[3:13]) #Mostra o caractere da posiçao 3 até 12
#print(frase[:13]) #Mostra do início até 12
#print(frase[1:15]) #Mostra da posição 1 até 14
#print(frase[1:15:2]) #Mostra da posição 1 até 14 de 2 em 2
#print(frase[::2]) #Mostra do início ao fim de 2 em 2
#print('''Welcome''')
#print(frase.count('o')) #Conta quantas vezes a letra "o" minúsculo aparece no texto
#print(frase.upper().count('O')) #Transforma a frase em maiúsculas e conta quantas vezes a letra "O" aparece no texto
#print(len(frase))#Mostra o comprimento da frase
#print(len(frase.strip()))#Mostra o comprimento da frase removendo os espaços indesejados antes e depis
#print(frase.replace('Python', 'Android')) #Substitui a oalavra "Python" por "Android"
#print(frase[0])#Mostra a letra da posção "0" (zero)
#frase = frase.replace('Python', 'Android') # Substitui a oalavra "Python" por "Android" salvando na variável
#print(frase)
#print('Curso' in frase) #Mostra se a palavra "Curso" está na frase
#print(frase.find('Curso')) #Mostra se existe a palavra "Curso" e mostra que a palavra "Curso começa na posição "0" (zero)
#print(frase.find('Video')) # Vai mostrar o valor "-1" já que a palavra "Video" sem o ascento nãoexiste
#print(frase.lower().find('vídeo')) #Transforma "Vídeo" em minúsculo e encontra "vídeo"
#print(frase.split()) #Cria uma lista com separador de espaços
dividido = frase.split()
#print(dividido[0]) #Mostra apenas o índicice "0" da lista
#print(dividido[2][3]) #Pega a palavra do índice "2" e mostra sua terceira letra