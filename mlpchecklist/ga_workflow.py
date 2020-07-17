from . import ItemCollection, ChecklistItem

_1_steps = {'_1': ChecklistItem('1. Identify business/product objectives'),
            '_2': ChecklistItem('2. Identify and hypothesize goals and criteria for success'),
            '_3': ChecklistItem('3. Create a set of questions for identifying correct data set')}

_2_steps = {'_1': ChecklistItem('1. Identify the "right" data set(s)'),
            '_2': ChecklistItem('2. Import data and set up local or remote data structre'),
            '_3': ChecklistItem('3. Determine most appropriate tools to work with data')}

_3_steps = {'_1': ChecklistItem('1. Read any documentation provided with the data'),
            '_2': ChecklistItem('2. Perform exploratory data analysis'),
            '_3': ChecklistItem('3. Verify the quality of the data')}

_4_steps = {'_1': ChecklistItem('1. Determine sampling methodology and sample data'),
            '_2': ChecklistItem('2. Format, clean, slice and combine data in Python'),
            '_3': ChecklistItem('3. Create necessary derived columns from the data (new data)')}

_5_steps = {'_1': ChecklistItem('1. Identify trends and outliers'),
            '_2': ChecklistItem('2. Apply descriptive and inferential statistics'),
            '_3': ChecklistItem('3. Document and transform data')}

_6_steps = {'_1': ChecklistItem('1. Select appropriate model'),
            '_2': ChecklistItem('2. Build model'),
            '_3': ChecklistItem('3. Evaluate and refine model')}

_7_steps = {'_1': ChecklistItem('1. Summarize findings with narrative, storytelling techniques'),
            '_2': ChecklistItem('2. Present limitations and assumptions of your analysis'),
            '_3': ChecklistItem('3. Identify follow up problems and questions for future analysis')}

dsw_main_steps = {'_1': ChecklistItem("1. Identify the Problem", _1_steps),
                  '_2': ChecklistItem("2. Acquire the Data", _2_steps),
                  '_3': ChecklistItem("3. Parse the Data", _3_steps),
                  '_4': ChecklistItem("4. Mine the Data", _4_steps),
                  '_5': ChecklistItem("5. Refine the Data", _5_steps),
                  '_6': ChecklistItem("6. Build a Data Model", _6_steps),
                  '_7': ChecklistItem("7. Present the Results", _7_steps)}

DSW = ItemCollection('Data Science Workflow', dsw_main_steps,'General Assembly Slides')