class Item():
    def __init__(self, name, description):
        self.name = name 
        self.description = description
       

    # function that print the name and description of x item 
    # to be printed in adv.py
    def __str__(self):
        return(f"{self.name}: {self.description}")