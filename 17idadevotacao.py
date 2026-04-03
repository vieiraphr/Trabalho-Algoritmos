nome = input("Digite seu nome:")
print(f"Bem vindo, {nome}! Para prosseguirmos com seu cadastro para emissão de título de eleitor preciso que me informe:")
idade = int(input("Qual é sua idade: "))
if idade >= 16:
    print("Você pode prosseguir com o cadastro.")
else:
    print("Você ainda não atingiu a idade necessária.")