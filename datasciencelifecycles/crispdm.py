from . import ChecklistItem, ItemCollection

_1_steps = {'_1': ChecklistItem('1. Determine business objectives'),
            '_2': ChecklistItem('2. Assess situation'),
            '_3': ChecklistItem('3. Determine data mining goals'),
            '_4': ChecklistItem('4. Produce project plan')}

_2_steps = {'_1': ChecklistItem('1. Collect intial data'),
            '_2': ChecklistItem('2. Describe data'),
            '_3': ChecklistItem('3. Explore data'),
            '_4': ChecklistItem('4. Verify data quality')}

_3_steps = {'_1': ChecklistItem('1. Select data'),
            '_2': ChecklistItem('2. Clean data'),
            '_3': ChecklistItem('3. Construct data'),
            '_4': ChecklistItem('4. Integrate data'),
            '_5': ChecklistItem('5. Format data')}

_4_steps = {'_1': ChecklistItem('1. Select modelling technique'),
            '_2': ChecklistItem('2. Generate test design'),
            '_3': ChecklistItem('3. Build model'),
            '_4': ChecklistItem('4. Assess model')}

_5_steps = {'_1': ChecklistItem('1. Evaluate results'),
            '_2': ChecklistItem('2. Review process'),
            '_3': ChecklistItem('3. Determine next steps')}

_6_steps = {'_1': ChecklistItem('1. Plan deployment'),
            '_2': ChecklistItem('2. Plan monitoring and maintenance'),
            '_3': ChecklistItem('3. Produce final report'),
            '_4': ChecklistItem('4. Review project')}

crispdm_main_steps = {'_1': ChecklistItem('1. Business understanding', _1_steps),
                      '_2': ChecklistItem('2. Data understanding', _2_steps),
                      '_3': ChecklistItem('3. Data preparation', _3_steps),
                      '_4': ChecklistItem('4. Modelling', _4_steps),
                      '_5': ChecklistItem('5. Evaluation', _5_steps),
                      '_6': ChecklistItem('6. Deployment', _6_steps)}

CRISPDM = ItemCollection('CRISP-DM Project Process', crispdm_main_steps, 'CRISP')