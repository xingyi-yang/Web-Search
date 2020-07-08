def search4vowels(word:str) -> set:
    """ Display any vowels found in an asked-for word"""
    vowels =  set('ariou')
    return vowels.intersection(set(word))

def search4letters(phrase:str, letters:str) ->set:
    """ Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
