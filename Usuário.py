#Nome Da Pessoa
print("Insira seu nome:")
nome= str(input())

#Ano de Nascimento 
dataCorreta = False
while dataCorreta == False:

    print("Insira o ano do seu de nascimento")
    try:
        data= int(input())
        idade= 2022 - data
        if data <=2021 and data>=1922:
            dataCorreta== True
            print(f"Seu nome é {nome}, você possui ou completará {idade} anos ")
        else:
            print("A data escolhida está fora da margem de ano")
    except:
        print("O ano de nascimento é inválido")
