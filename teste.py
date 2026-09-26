from datetime import datetime
import webbrowser

hora_marcada = None
compromisso = None

link_steam = "https://store.steampowered.com/"

while True:

    print("\n--- SEXTA-FEIRA ---")
    print("1 = Ligar.")

    opcao = input("Escolha a opção = ")

    if opcao == "1":

        print("\nSEXTA-FEIRA LIGADA!")

        while True:

            print("\nOI, SOU A SEXTA-FEIRA. COMO POSSO AJUDAR?")
            print("1 = Informe a hora.")
            print("2 = Me fale o dia.")
            print("3 = Marcar horário e compromisso.")
            print("4 = Mostrar compromisso marcado.")
            print("5 = Sair.")
            print("6 = Abrir Steam.")

            opcao = input("Escolha a opção = ")

            if opcao == "1":

                hora_atual = datetime.now().strftime("%H:%M:%S")
                print("A hora atual é:", hora_atual)

            elif opcao == "2":

                dia_atual = datetime.now().strftime("%d/%m/%Y")
                print("O dia atual é:", dia_atual)

            elif opcao == "3":

                hora_marcada = input("Digite a hora marcada (HH:MM): ")
                compromisso = input("Qual é o compromisso? ")

                print("\nCOMPROMISSO MARCADO COM SUCESSO!")

            elif opcao == "4":

                if hora_marcada is None:
                    print("\nVocê ainda não possui nenhum compromisso marcado.")
                else:
                    print("\n--- COMPROMISSO MARCADO ---")
                    print("Hora:", hora_marcada)
                    print("Compromisso:", compromisso)

            elif opcao == "5":

                print("\nSEXTA-FEIRA DESLIGADA.")
                break

            elif opcao == "6":

                print("\nABRINDO A STEAM...")
                webbrowser.open(link_steam)

            else:

                print("Opção inválida!")