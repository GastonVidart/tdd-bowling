def play_bowling(current_score, rolls, pins):
    # modulo para realizar una jugada
    global pinesTirados, esPrimerTiro, flagSpare, flagStrike, rondaActual, rondaFinal
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

    for tiro in range(rolls):
        # para cada tiro

        rondaFinal = rondaActual == 11
        if rondaFinal:
            #la ronda final se computa de manera diferente a las demas
            current_score += ronda10(pins)
        else:
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
                # Detecta si es el primer tiro de la ultima ronda
                if pins == 10:
                    flagStrike = 1
                    rondaActual += 1
                    # La ronda se termina porque hizo una chuza
                else:
                    esPrimerTiro = False
                    pinesTirados = pins
            else:
                # segundo tiro del juego actual
                pinesTirados += pins
                if pinesTirados == 10:
                    # completo media chuza
                    terminado = False
                    flagSpare = True
                pinesTirados = 0
                esPrimerTiro = True
                rondaActual += 1

    return current_score, terminado


def ronda10(pins):
    # modulo que se encarga de computar los ultimos 2 tiros
    global pinesTirados, esPrimerTiro, flagSpare, flagStrike, rondaActual, rondaFinal
    if flagSpare:
        score = pins
        flagSpare = False

    if flagStrike != 0:
        score = pins
        flagStrike = (flagStrike + 1) % 3

    aux = pinesTirados+pins
    if aux > 10:
        #si esta haciendo una media chuza, se controla que no supere el limite
        print("Error en cant pines", pinesTirados)
    elif pins < 10:
        #si no es chuza
        pinesTirados = aux

    return score
