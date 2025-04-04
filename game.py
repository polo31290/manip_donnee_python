def game (): 
    """
    lance le jeu qui vas se dérouler comme ceci :
        le joueur va tout le temps commencer
        deplace une premiere piece : 
            verifier quelle piece est selectionner et verifier si le deplacement souhaiter par le joueur est possible (si il n'y a aucune piece qui interfere ou si
            il n'y a aucune de ses propre piece a l'endroit ou il veut se deplacer, si la piece choisi n'est pas en clouage donc si elle protege pas d'un echec ou simplement 
            si c'est le bon deplacement pour la piece selectionner)
                si tout est bon alors deplacer la piece et continuer la pârtie
                sinon le laisser reessayer (redemarer la demande) afficher un texte "attention {nom de la piece} ne peux se deplacer comme ça"

        verifier si une piece a etait attaquer (ou si une piece est sur la trajectoire de deplacement d'une autre piece) ?
            si oui laquelle ?
                roi : est-qu'il peut s'echapper ou est-ce qu'une piece peut intervenir ?
                    si oui la partie continue en obligeant le joueur a deplacer son roi ou a le protéger avec une autre piece :
                        si le joueur essaye de deplacer une autre piece un message d'erreur s'affiche comme quoi il faut deplacer le roi ou le proteger
                        si le joueur deplace bien la piece ou le roi alors la partie continue
                    si non fin de la partie qui est gagner par la couleur oppose au roi en echec
                autre piece : la partie continue
            si non la partie continue
        si aucune piece n'est attaquer alors la partie continue
        
    """