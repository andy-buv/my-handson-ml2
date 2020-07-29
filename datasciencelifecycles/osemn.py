from . import ChecklistItem, ItemCollection


_0_steps = {'notes': ChecklistItem('')}

_1_steps = {'notes': ChecklistItem('')}

_2_steps = {'notes': ChecklistItem('')}

_3_steps = {'notes': ChecklistItem('')}

_4_steps = {'notes': ChecklistItem('')}

_5_steps = {'notes': ChecklistItem('')}



osemn_main_steps = {'_0': ChecklistItem('0. Business Question ', _0_steps),
                    '_1': ChecklistItem('1. Obtain', _1_steps),
                    '_2': ChecklistItem('2. Scrub', _2_steps),
                    '_3': ChecklistItem('3. Explore', _3_steps),
                    '_4': ChecklistItem('4. Models', _4_steps),
                    '_5': ChecklistItem('5. iNterpret', _5_steps)}

OSEMN = ItemCollection('OSEMN Framework', osemn_main_steps, 'Hilary Mason and Chris Wiggins')