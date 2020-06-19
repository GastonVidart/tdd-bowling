pinesTirados=0
def play_bowling(current_score, rolls, pins):
    #modulo para realizar una jugada
    global pinesTirados 
    if current_score==0:
        pinesTirados=0  
    score=current_score
    scoreAux=0
    print(pinesTirados)
    if pinesTirados==0:
        pinesTirados=rolls*pins
        scoreAux=pinesTirados
    else:
        scoreAux=pinesTirados+rolls*pins
        if scoreAux==10:
            scoreAux=rolls*pins+1
        pinesTirados=0 
    score=score+scoreAux
    return score

