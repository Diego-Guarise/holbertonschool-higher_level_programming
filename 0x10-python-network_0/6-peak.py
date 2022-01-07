#!/usr/bin/python3
""" Test function find_peak """


def find_peak(list_of_integers):
    if list_of_integers:
        return max(list_of_integers)
    else:
        return None