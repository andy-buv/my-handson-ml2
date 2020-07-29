from .itemcollection import ItemCollection

class ChecklistItem:
    
    def __init__(self, text, steps={}, title=None):
        if title is None:
            self.title = ' '.join(text.split(' ')[1:])
            if self.title[:-1] == '.':
                self.title = self.title[:-1]
        else:
            self.title = title
        self.text =  text
        self.steps = ItemCollection(self.title, steps)
        
    def __repr__(self):
        return self.text
    
    def __str__(self):
        return self.text