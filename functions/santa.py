import random

import create_participants
import shuffle_participants
import check_draw

def santa_list(couples):
    '''
    Generate a Secret Santa list for a given list of couples.
    Args:
        couples (list of tuples): A list of tuples, where each tuple contains the names of two people in a couple.
    Returns:
        None
    '''
    
    participants = create_participants(couples)
    receveurs = shuffle_participants(participants)

    tirage_valide = False

    while tirage_valide == False:
        random.shuffle(receveurs)
        tirage_valide = check_draw(receveurs, participants, couples)

    for donneur, receveur in zip(participants, receveurs):
        print(f'{donneur} offre à {receveur}')