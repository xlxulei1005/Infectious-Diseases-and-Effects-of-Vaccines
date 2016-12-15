'''
This module contains user defined errors for handling exceptions.
    DigitError
    InvalidDisease
Created on Nov 21, 2016
'''

class DigitError(Exception):
    '''
    Handling meaningless digit Input
    '''
    def __str__(self):
        return 'Only string disease name are valid for Heatmap!'


class InvalidDisease(Exception):
    '''
    Handling invalid input for Heatmap plot
    '''
    def __str__(self):
        return 'This is not a valid disease for heatmap plot!'  