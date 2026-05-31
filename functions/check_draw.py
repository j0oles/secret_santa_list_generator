def check_draw(receveurs, participants, couples):
    '''
    Check if the Secret Santa draw is valid.
    Args:
        receveurs (list): A list of participants shuffled in a random order.
        participants (list): A list of participants, where each participant is a string representing their name.
        couples (list of tuples): A list of tuples, where each tuple contains the names of two people in a couple.
    Returns:
        bool: True if the draw is valid, False otherwise.
    '''
    
    for donneur, receveur in zip(participants, receveurs):
        if donneur == receveur:
            return False

        for couple in couples:
            if donneur in couple and receveur in couple:
                return False
    return True