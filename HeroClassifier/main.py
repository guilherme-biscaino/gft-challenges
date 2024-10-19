while True:
    questionInput = input("Deseja fazer novas consultas: S/N? \n").upper()
    if questionInput == "S":
        HeroName: str = input("Digite o nome do seu herói: \n")

        try:
            HeroExperience = int(input("Digite a quantidade de experiência do seu heroi: \n").replace(".", ""))


            def rankmatcher(experience):
                match experience:
                    case _ if experience < 0:
                        raise ValueError
                    case _ if experience < 1000:
                        return "Ferro"
                    case _ if experience <= 2000:
                        return "Bronze"
                    case _ if experience <= 5000:
                        return "Prata"
                    case _ if experience <= 7000:
                        return "Ouro"
                    case _ if experience <= 8000:
                        return "Platina"
                    case _ if experience <= 9000:
                        return "Ascendente"
                    case _ if experience <= 10000:
                        return "Imortal"
                    case _ if  experience > 10001:
                        return "Radiante"

            heroRank = rankmatcher(HeroExperience)

            print(f"O Herói de nome: {HeroName} \nEstá no nível de: {heroRank}")
        except ValueError:
            print("A quantidade de xp inserida é invalida!")
        except NameError:
            print("O nome do Herói está invalido!")

    elif questionInput == "N":
            break
    else:
        print("Opção inválida!")