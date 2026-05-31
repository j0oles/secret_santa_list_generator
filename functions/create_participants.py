def create_participants(couples):
    '''
    Create a list of participants from a list of couples.
    Args:
        couples (list of tuples): A list of tuples, where each tuple contains the names of two people in a couple.
    Returns:
        participants (list): A list of participants, where each participant is a string representing their name.
    '''
    
    participants=[]
    for couple in couples:
        for person in couple:
            participants.append(person)
    return participants
