#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a_dictionary={v:k for k,v in a_dictionary.items()}
    return a_dictionary[max(a_dictionary)]
