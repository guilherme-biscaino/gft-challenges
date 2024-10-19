from bdb import effective

while True:
    questionInput = input("Deseja fazer novas consultas: S/N? \n").upper()
    if questionInput == "S":

        try:
            matchesWon:int = int(input("Digite a wantidade de vitórias\n"))

            matchesLost:int = int(input("Digite a wantidade de derrotas\n"))

            def matchesValuator(wins):

                match wins:
                    case _ if wins < 0:
                        raise ValueError

                    case _ if wins < 10:
                        return "Ferro"

                    case _ if wins <= 20:
                        return "Bronze"

                    case _ if wins <= 50:
                        return "Prata"

                    case _ if wins <= 80:
                        return "Ouro"

                    case _ if wins <= 90:
                        return "Platina"

                    case _ if wins <= 100:
                        return "Ascendente"

                    case _ if wins >= 101:
                        return "Imortal"


            def heroStats(win, loses):
                totalMatches = win + loses
                matchBalance = win - loses
                winrate = (matchesWon / totalMatches) * 100

                rank = matchesValuator(win)
                return {"vitorias": matchBalance, "winrate": winrate, "rank": rank}

            heroRank = heroStats(matchesWon, matchesLost)

            print("="*30)
            print(f"O herói tem saldo de {heroRank['vitorias']} vitorias. \nEstando no rank {heroRank['rank']}! "
                  f"\nTendo {heroRank['winrate']:.2f}% de taxa de vitórias.")
            print("="*30)


        except ValueError:
            print("A quantidade de jogos inseridos é invalida!")
        except:
            print("Houve um erro inesperado!")

    elif questionInput == "N":
            break
    else:
        print("Opção inválida!")