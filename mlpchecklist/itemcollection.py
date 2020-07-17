class ItemCollection:
    
    def __init__(self, title, items={}, author=None):
        self.title = title
        self._items = items
        # self.steps = list(self._items.values())
        self.__dict__.update(items)
        self.author = author
    
    def __repr__(self):
        
        str_items = '\n\t'.join([str(item) + '\n' for item in self._items.values()])
        
        
        return f"""
        {self.title.upper()}
        {"=" * len(self.title)}\n
        {str_items}\n"""
    
    def __str__(self):
        
        str_items = '\n\t'.join([str(item) + '\n' for item in self._items.values()])
        
        
        return f"""
        {self.title.upper()}
        {"=" * len(self.title)}\n
        {str_items}\n"""
    
    def detailed(self):
        
        all_steps = '\n'.join([str(item.steps) for item in self._items.values()])
        
        print(f"""
    {self}
    {all_steps}""")