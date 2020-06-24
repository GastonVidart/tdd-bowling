def play_bowling(current_score, rolls, pins):
    # modulo para realizar una jugada
    global pinesTirados, esPrimerTiro, flagSpare, flagStrike, rondaActual, rondaFinal, strikeActivos
    terminado = True
    if current_score == -1:
        # si es el inicio del juego, se actualizan las variables
        pinesTirados = 0
        esPrimerTiro = True
        # Es primer tiro de la ronda
        flagSpare = False
        flagStrike = 0
        rondaActual = 1
        rondaFinal = False
        current_score = 0
        strikeActivos = 0

    for tiro in range(rolls):
        # para cada tiro
        rondaFinal = rondaActual == 11
        # la ronda final se computa de manera diferente a las demas
        if flagSpare:
            # hay que sumar el bonus de media chuza
            current_score += pins
            flagSpare = False

        if flagStrike != 0:
            # Si tiene bonus de chuza
            current_score += pins * strikeActivos
            # reinicia el flag cada 2 rondas
            flagStrike = (flagStrike + 1) % 3
            if strikeActivos > 1:
                strikeActivos -= 1
            elif flagStrike == 0:
                strikeActivos == 0

        if not rondaFinal:
            # juego normal
            current_score += pins
            if esPrimerTiro:
                # de la ronda actual
                if pins == 10:
                    flagStrike = 1
                    rondaActual += 1
                    strikeActivos += 1
                    # La ronda avanza porque se hizo una chuza
                else:
                    esPrimerTiro = False
                    pinesTirados = pins
            else:
                # segundo tiro de la ronda actual
                pinesTirados += pins
                if pinesTirados == 10:
                    # completo media chuza
                    terminado = False
                    flagSpare = True
                elif pinesTirados > 10:
                    print("Tiro incorrecto Fin del Juego!")
                pinesTirados = 0
                esPrimerTiro = True
                rondaActual += 1

    return current_score, terminado
