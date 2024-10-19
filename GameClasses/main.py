from GameClasses.specializedClasses import Mago,Guerreiro,Monge,Ninja

print("Bem vindo!")
input("Aperte qualqer botão para iniciar sua aventura\n")

characterName = input("Por favor, digite o nome do seu personagem: \n")
characterAge = input("Por favor, digite a idade do seu personagem: \n")
characterClasses = input(
f"""
olá {characterName}, daqui em diante trilharemos um caminho perigoso!
para seguir em frente você deve escolher entre uma das seguintes profissões:
    Guerreiro [G]
    Mago [MA]
    Monge [MO]
    Ninja [N]
""").upper()

def characterBuilder(classChoice, name, age):
    match classChoice:
        case "G":
            return Guerreiro.Guerreiro(name, age)
        case "MA":
            return Mago.Mago(name, age)
        case "MO":
            return Monge.Monge(name, age)
        case "N":
            return Ninja.Ninja(name, age)
        case _:
            print("Escolha de classe incompatível!")

character = characterBuilder(characterClasses, characterName, characterAge)

print("Finalizamos a criação do seu personagem")

print("="*40)
print(
f""" 
Nome: {character.nome}
Idade: {character.idade}
Classe: {character.__class__.__name__}
""")
print("="*40)
print(character.atacar())
