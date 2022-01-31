import ipywidgets as widgets
from ipywidgets import interact

global answer2a
    
def task1b():
    print("Which of the features contains most missing values")
    rb=widgets.RadioButtons(
        options=[('No selection', -1),
                 ('There are no missing values', 0),
                 ('Province/State', 1), 
                 ('Country/Region', 2),
                 ('Lat', 3),
                 ('Lon', 4),
                 ('1/22/20', 5),
                 ('1/23/20', 6)],
        #value='None',
        description='Select feature:'
        #disabled=False
    )
    return rb
    
def task1c():
    rb=widgets.RadioButtons(
        options=['No selection', 
        'Drop columns',
        'Drop rows',
        'Imputation',
        'None'],
        description='Strategy:',
        disabled=False
    )
    return rb


