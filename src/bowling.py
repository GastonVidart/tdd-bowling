def play_bowling(current_score, rolls, pins):
    # modulo para realizar una jugada
    global pinesTirados, esPrimerTiro, flagSpare, flagStrike
    terminado = True
    if current_score == 0:
        # si es el inicio del juego, se actualizan las variables
        pinesTirados = 0
        esPrimerTiro = True
        flagSpare = False
        flagStrike = 0

    for tiro in range(rolls):
        # para cada tiro
        current_score += pins

        if flagSpare:
            # hay que sumar el bonus de media chuza
            current_score += pins
            flagSpare = False

        if flagStrike != 0:
            current_score += pins
            flagStrike = (flagStrike + 1) % 3

        if esPrimerTiro:
            # del juego actual
            if pins == 10:
                flagStrike = 1
            else:
                esPrimerTiro = False
                pinesTirados = pins
        else:
            # segundo tiro del juego actual
            pinesTirados += pins
            if pinesTirados == 10:
                # tiro todos los pinos
                terminado = False
                flagSpare = True
            pinesTirados = 0
            esPrimerTiro = True

    return current_score, terminado
