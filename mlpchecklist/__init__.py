class ChecklistItem:
    
    def __init__(self, text, steps={}, title=None):
        if title is None:
            self.title = ' '.join(text.split(' ')[1:])[:-1]
        else:
            self.title = title
        self.text =  text
        self.steps = ItemCollection(self.title, steps)
        
    def __repr__(self):
        return self.text
    
    def __str__(self):
        return self.text
    
    
class ItemCollection:
    
    def __init__(self, title, items={}):
        self.title = title
        self._items = items
        # self.steps = list(self._items.values())
        self.__dict__.update(items)
    
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
    

 
    
_1_steps = {'_1': ChecklistItem('1. Define the objective in business terms.'),
            '_2': ChecklistItem('2. How will your solution be used?'),
            '_3': ChecklistItem('3. What are the current solutions/workarounds (if any)?'),
            '_4': ChecklistItem('4. How should you frame this problem (supervised/unsupervised, online/offine, etc.)?'),
            '_5': ChecklistItem('5. How should performance be measured?'),
            '_6': ChecklistItem('6. Is the performance measure aligned with the business objective?'),
            '_7': ChecklistItem('7. What would be the minimum performance needed to reach the business objective?'),
            '_8': ChecklistItem('8. What are comparable problems? Can you reuse experience or tools?'),
            '_9': ChecklistItem('9. Is human expertise available?'),
            '_10': ChecklistItem('10. How would you solve the problem manually?'),
            '_11': ChecklistItem('11. List the assumptions you (or others) have made so far.'),
            '_12': ChecklistItem('12. Verify assumptions if possible.')}


_2_steps = {'notes' : ChecklistItem('Note: automate as much as possible so you can easily get fresh data.\n'),
            '_1' : ChecklistItem('1. List the data you need and how much you need.'),
            '_2' : ChecklistItem('2. Find and document where you can get that data.'),
            '_3' : ChecklistItem('3. Check how much space it will take.'),
            '_4' : ChecklistItem('4. Check legal obligations, and get authorization if necessary.'),
            '_5' : ChecklistItem('5. Get access authorizations.'),
            '_6' : ChecklistItem('6. Create a workspace (with enough storage space).'),
            '_7' : ChecklistItem('7. Get the data.'),
            '_8' : ChecklistItem('8. Convert the data to a format you can easily manipulate (without changing the data itself).'),
            '_9' : ChecklistItem('9. Ensure sensitive information is deleted or protected (e.g., annonymized).'),
            '_10' : ChecklistItem('10. Check the size and type of data (time series, sample, geographical, etc.).'),
            '_11' : ChecklistItem('11. Sample a test set, put it aside, and never look at it (no data snooping!).')}

_3_steps = {'notes' : ChecklistItem('Note: try to get insights from a field expert for these steps.\n'),
            '_1' : ChecklistItem('1. Create a copy of the data for exploration (sampling it down to a manageable size if necessary).'),
            '_2' : ChecklistItem('2. Create a Jupyter notebook to keep a record of your data exploration.'),
            '_3' : ChecklistItem("""3. Study each attribute and its characteristics:
            - Name
            - Type (categorical, int/float, bounded/unbounded, text, structured, etc.)
            - % of missing values
            - Noisiness and type of noise (stochastic, outliers, rounding errors, etc.)
            - Usefulness for the task
            - Type of distribution (Gaussian, uniform, logarithmic, etc.)"""),
            '_4' : ChecklistItem('4. For supervised learning tasks, identify the target attribute(s).'),
            '_5' : ChecklistItem('5. Visualize the data.'),
            '_6' : ChecklistItem('6. Study the correlations between attributes.'),
            '_7' : ChecklistItem('7. Study how you would solve the problem manually.'),
            '_8' : ChecklistItem('8. Identify the promising transformations you may want to apply.'),
            '_9' : ChecklistItem('9. Identify the extra data that would be useful (go back to "Get the Data").'),
            '_10' : ChecklistItem('10. Document what you have learned.')}

_4_steps = {'notes': ChecklistItem('''Notes:

            - Work on copies of the data (keep the original dataset intact).
            - Write functions for all data transformations you apply, for five reasons:
                 - So you can easily prepare the data the next time you get a fresh dataset
                 - So you can apply these transformations in future projects
                 - To clean and prepare the test set
                 - To clean and prepare the new data instances once your solution is live
                 - To make it easy to treat your preparation choices as hyperparameters\n'''), 
             '_1': ChecklistItem('''1. Data cleaning:
            - Fix or remove outliers (optional).
            - Fill in missing values (e.g., with zero, mean, median...) or drop their rows (or columns).'''),
             '_2': ChecklistItem('''2. Feature selection (optional):
            - Drop the attributes that provide no useful information for the task.'''),
             '_3': ChecklistItem('''3. Feature engineering, where appropriate:
            - Discretize continuous features.
            - Decompose features (e.g. categorical, date/time, etc.).
            - Add promising transformations of features (e.g., log(x), sqrt(x), x^2, etc.).
            - Aggregate features into promising new features.'''),
             '_4': ChecklistItem('''4. Feature scaling:
            - Standardize or normalize features.''')}

_5_steps = {'notes': ChecklistItem('''Notes:

            - If the data is huge, you may want to sample smaller training sets so you can train many different models in a reasonable time (be aware that this penalizes complex models such as large neural nets or Random Forests).
            - Once again, try to automate these steps as much as possible.\n'''),
            '_1': ChecklistItem('''1. Train many quick-and-dirty models from different categories using standard parameters.
            - e.g., linear, naive Bayes, SVM, Random Forest, neural net, etc.'''),
            '_2': ChecklistItem('''2. Measure and compare their performance.
            - For each model, use N-fold cross-validation and compute the mean and standard deviation of the performance measures on the N folds.'''),
            '_3': ChecklistItem('3. Analyze the most significant variables for each algorithm.'), 
            '_4': ChecklistItem('''4. Analyze the types of errors the models make.
            - What data would a human have used to avoid these errors?'''),
            '_5': ChecklistItem('5. Perform a quick round of feature selection and engineering.'),
            '_6': ChecklistItem('6. Perform one or two more quick iterations of the five previous steps.'),
            '_7': ChecklistItem('7. Shortlist the top three to five most promising models, preferring models that make different types of errors.')}

_6_steps = {'notes': ChecklistItem('''Notes:

            - You will want to use as much data as possible for this step, especially as you move toward the end of fine-tuning.
            - As always, automate what you can.\n'''),
            '_1': ChecklistItem('''1. Fine-tune the hyperparameters using cross-validation:
            - Treat your data transformation choices as hyperparameters, especially when you are not sure about them (e.g., if you're not sure whether to replace missing values with zeros or with the median values, or to just drop the rows).
            - Unless there are very few hyperparameter values to explore, prefer random search over grid search. If training is very long, you may prefer a Bayesian optimization approach (e.g., using Gaussian process priors, as described by Jasper Snoek et al. (https://homl.info/134).'''),
            '_2': ChecklistItem('2. Try Ensemble methods. Combining your best models will often produce better performance than running them individually.'),
            '_3': ChecklistItem('3. Once you are confident about your final model, measure its performance on the test set to estimate the generalization error.'),
            '>': ChecklistItem("> Don\'t tweak your model after measuring the generalization error: you would just start overfitting the test set.")}


_7_steps = {'_1': ChecklistItem('1. Document what you have done.'),
            '_2': ChecklistItem('''2. Create a nice presentation.
            - Make sure you highlight the big picture first.'''),
            '_3': ChecklistItem('3. Explain why your solution achieves the business objective.'),
            '_4': ChecklistItem('''4. Don't forget to present interesting points you noticed along the way.
            - Describe what worked and what did not.
            - List your assumptions and your system's limitations.'''),
            '_5': ChecklistItem('5. Ensure your key findings are communicated through beautiful visualizations or easy-to-remember statements (e.g., "the median income is the number-one predictor of housing prices.").')}    


_8_steps = {'_1': ChecklistItem('1. Get your solutions ready for production (plug into production data inputs, write unit tests, etc.).'),
            '_2': ChecklistItem('''2. Write monitoring code to check your system's live performance at regular intervals and trigger alerts when it drops.
            - Beware of slow degradation: models tend to "rot" as data evolves.
            - Measuring performance may require human pipeline (e.g., via a crowdsourcing service). 
            - Also monitor your inputs' quality (e.g. a malfunctioning sensor sending random values, or another team's output becoming stale). This is particularly important for online learning systems.'''),
            '_3': ChecklistItem('3. Retrain your models on a regular basis on fresh data (automate as much as possible).')}



mlp_main_steps = {'notes': ChecklistItem("This checklist can guide you through your Machine Learning projects. \n\n\tThere are eight main steps:\n"),
                  '_1': ChecklistItem("1. Frame the problem and look at the big picture.", _1_steps),
                  '_2': ChecklistItem("2. Get the data.", _2_steps),
                  '_3': ChecklistItem("3. Explore the data to gain insights.", _3_steps, 'Explore the Data'),
                  '_4': ChecklistItem("4. Prepare the data to better expose the underlying patterns to Machine Learning algorithms.",_4_steps, 'Prepare the Data'),
                  '_5': ChecklistItem("5. Explore many different models and shortlist the best ones.", _5_steps, 'Shortlist Promising Models'),
                  '_6': ChecklistItem("6. Fine-tune your models and combine them into a great solution.", _6_steps, 'Fine-Tune the System'),
                  '_7': ChecklistItem("7. Present your solution.", _7_steps),
                  '_8': ChecklistItem("8. Launch, monitor, and maintain your system.", _8_steps, 'Launch!')}

MLP = ItemCollection('Machine Learning Project Checklist', mlp_main_steps)


    
if __name__ == '__main__':
    
    pass
