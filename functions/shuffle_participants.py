import random

def shuffle_participants(participants):
    '''
    Shuffle the list of participants to create a random order for the Secret Santa.
    Args:
        participants (list): A list of participants, where each participant is a string representing their name.
    Returns:
        receveurs (list): A list of participants shuffled in a random order.
    '''
    
    receveurs = participants.copy()
    random.shuffle(receveurs)
    return receveurs