from datetime import datetime
import webbrowser
import urllib.parse
import subprocess


chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def abrir_chrome(url):
    try:
        subprocess.Popen([chrome, url])
    except FileNotFoundError:
        print("SEXTA-FEIRA: Google Chrome não foi encontrado.")
        

hora_marcada = None
compromisso = None

print("SEXTA-FEIRA INICIADA!")
print("Digite 'sair' para desligar.\n")


while True:

    comando = input("Você: ").lower().strip()

    # ==========================================
    # SAIR / DESLIGAR
    # ==========================================

    if comando == "sair" or comando == "desligar":

        print("\nSEXTA-FEIRA DESLIGADA.")
        break

    # ==========================================
    # HORA
    # ==========================================

    elif "hora" in comando:

        hora_atual = datetime.now().strftime("%H:%M:%S")

        print(f"SEXTA-FEIRA: A hora atual é {hora_atual}.")

    # ==========================================
    # DATA / DIA
    # ==========================================

    elif "dia" in comando or "data" in comando:

        dia_atual = datetime.now().strftime("%d/%m/%Y")

        print(f"SEXTA-FEIRA: Hoje é {dia_atual}.")

    # ==========================================
    # STEAM / ABRIR STEAM
    # ==========================================

    elif comando == "steam" or comando == "abrir steam":

        print("SEXTA-FEIRA: Abrindo a Steam...")

        webbrowser.open("steam://open/main")

    # ==========================================
    # ABRIR YOUTUBE
    # COM OU SEM CANAL
    # ==========================================

    elif comando.startswith("abrir youtube"):

        canal = comando.replace(
            "abrir youtube",
            "",
            1
        ).strip()

        # --------------------------------------
        # SEM CANAL
        # --------------------------------------

        if not canal:

            print("SEXTA-FEIRA: Abrindo o YouTube...")

            webbrowser.open(
                "https://www.youtube.com/"
            )

        # --------------------------------------
        # COM CANAL
        # --------------------------------------

        else:

            print(
                f'SEXTA-FEIRA: Procurando "{canal}" no YouTube...'
            )

            canal_url = urllib.parse.quote(canal)

            url_youtube = (
                f"https://www.youtube.com/results?search_query={canal_url}"
            )

            webbrowser.open(url_youtube)

    # ==========================================
    # CANAL DO YOUTUBE
    # PESQUISA NO PRÓPRIO YOUTUBE
    # ==========================================

    elif (
        comando.startswith("canal ")
        or comando.startswith("canal do ")
        or comando.startswith("youtube canal ")
        or comando.startswith("youtube do ")
    ):

        if comando.startswith("canal do "):

            canal = comando.replace(
                "canal do ",
                "",
                1
            ).strip()

        elif comando.startswith("canal "):

            canal = comando.replace(
                "canal ",
                "",
                1
            ).strip()

        elif comando.startswith("youtube canal "):

            canal = comando.replace(
                "youtube canal ",
                "",
                1
            ).strip()

        else:

            canal = comando.replace(
                "youtube do ",
                "",
                1
            ).strip()

        if canal:

            print(
                f'SEXTA-FEIRA: Procurando o canal "{canal}" no YouTube...'
            )

            canal_url = urllib.parse.quote(canal)

            url_youtube = (
                f"https://www.youtube.com/results?search_query={canal_url}"
            )

            webbrowser.open(url_youtube)

        else:

            print(
                "SEXTA-FEIRA: Qual canal do YouTube você deseja acessar?"
            )

    # ==========================================
    # YOUTUBE / YT
    # PESQUISA ATRAVÉS DO GOOGLE
    # ==========================================

    elif (
        comando.startswith("youtube ")
        or comando.startswith("yt ")
    ):

        if comando.startswith("youtube "):

            pesquisa = comando.replace(
                "youtube ",
                "",
                1
            ).strip()

        else:

            pesquisa = comando.replace(
                "yt ",
                "",
                1
            ).strip()

        if pesquisa:

            pesquisa_completa = "YouTube " + pesquisa

            print(
                f'SEXTA-FEIRA: Pesquisando '
                f'"{pesquisa_completa}" no Google...'
            )

            pesquisa_url = urllib.parse.quote(
                pesquisa_completa
            )

            url_google = (
                f"https://www.google.com/search?q={pesquisa_url}"
            )

            webbrowser.open(url_google)

        else:

            print(
                "SEXTA-FEIRA: O que você deseja pesquisar no YouTube?"
            )

    # ==========================================
    # ABRIR / PESQUISAR / ENTRAR / ABRA
    # TUDO PASSA PELO GOOGLE
    # ==========================================

    elif (
        comando.startswith("abrir ")
        or comando.startswith("pesquisar ")
        or comando.startswith("entrar ")
        or comando.startswith("abra ")
    ):

        if comando.startswith("abrir "):

            pesquisa = comando.replace(
                "abrir ",
                "",
                1
            ).strip()

        elif comando.startswith("pesquisar "):

            pesquisa = comando.replace(
                "pesquisar ",
                "",
                1
            ).strip()

        elif comando.startswith("entrar "):

            pesquisa = comando.replace(
                "entrar ",
                "",
                1
            ).strip()

        else:

            pesquisa = comando.replace(
                "abra ",
                "",
                1
            ).strip()

        if pesquisa:

            print(
                f'SEXTA-FEIRA: Pesquisando '
                f'"{pesquisa}" no Google...'
            )

            pesquisa_google = urllib.parse.quote(
                pesquisa
            )

            url_google = (
                f"https://www.google.com/search?q={pesquisa_google}"
            )

            webbrowser.open(url_google)

        else:

            print(
                "SEXTA-FEIRA: O que você deseja que eu abra?"
            )

    # ==========================================
    # MOSTRAR COMPROMISSO
    # ==========================================

    elif (
        "compromisso" in comando
        or "compromissos" in comando
    ):

        if hora_marcada is None:

            print(
                "SEXTA-FEIRA: "
                "Você ainda não possui nenhum compromisso marcado."
            )

        else:

            print("\n--- COMPROMISSO ---")
            print("Horário:", hora_marcada)
            print("Compromisso:", compromisso)

    # ==========================================
    # MARCAR / AGENDAR COMPROMISSO
    # ==========================================

    elif (
        "marcar" in comando
        or "agendar" in comando
    ):

        print(
            "SEXTA-FEIRA: Certo. Qual é o horário?"
        )

        hora_marcada = input("Você: ").strip()

        print(
            "SEXTA-FEIRA: E qual é o compromisso?"
        )

        compromisso = input("Você: ").strip()

        print(
            "\nSEXTA-FEIRA: "
            "Compromisso marcado com sucesso!"
        )

    # ==========================================
    # SAUDAÇÃO
    # ==========================================

    elif (
        "oi" in comando
        or "olá" in comando
        or "ola" in comando
    ):

        print(
            "SEXTA-FEIRA: Olá. Como posso ajudar?"
        )

    # ==========================================
    # COMANDO DESCONHECIDO
    # ==========================================

    else:

        print(
            "SEXTA-FEIRA: Não entendi o comando."
        )

        