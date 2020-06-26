def play_bowling(current_score, rolls, pins):
    # modulo para realizar una jugada
    global pinesTirados, esPrimerTiro, flagSpare, flagStrike, rondaActual, rondaFinal, strikeActivos    
    if current_score == -1:
        # si es el inicio del juego, se reinician las variables
        pinesTirados = 0
        esPrimerTiro = True     # Es primer tiro de la ronda
        flagSpare = False
        flagStrike = 0
        rondaActual = 1
        rondaFinal = False
        current_score = 0
        strikeActivos = 0
    elif current_score > 300 or current_score < -2:
        # se verifica un puntaje válido
        print("Puntaje ingresado inválido")
        return -2, False

    if pins > 10 or pins < 0:
        # se verifica que no se tiren mas de 10 pines o un valor negativo
        print("Pines tirados inválido")
        return -2, False

    if rolls < 0:
        print("Se ingresó un tiro inválido")
        return -2, False

    i = 0
    while i < rolls:
        # para cada tiro
        rondaFinal = rondaActual == 11
        if rondaFinal and not flagSpare and not flagStrike:
            #  se verifica que el tiro se pueda realizar
            #  si esta en la ronda final, y no hay flags activos, debe terminar el juego
            print("Se a hecho un juego inváldio, se jugaron mas rondas de las permitidas")
            return -2, False

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
                    flagSpare = True
                elif pinesTirados > 10:
                    # no se pueden acumular mas de 10 pines tirados
                    print("La cantidad de pines tirados es incorrecta")
                    return -2, False
                pinesTirados = 0
                esPrimerTiro = True
                rondaActual += 1
        i += 1

    return current_score, True
