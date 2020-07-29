from . import ChecklistItem, ItemCollection


_1_steps = {'notes': ChecklistItem('')}

_2_steps = {'notes': ChecklistItem('')}

_3_steps = {'notes': ChecklistItem('')}

_4_steps = {'notes': ChecklistItem('')}

_5_steps = {'notes': ChecklistItem('')}

ccemd_main_steps = {'_1': ChecklistItem('1. Collection', _1_steps),
                    '_2': ChecklistItem('2. Cleaning', _2_steps), 
                    '_3': ChecklistItem('3. Exploratory Data Analysis', _3_steps),
                    '_4': ChecklistItem('4. Model Building', _4_steps),
                    '_5': ChecklistItem('5. Model Deployment', _5_steps)}

CCEMD = ItemCollection('Data Science Life Cycle', ccemd_main_steps)