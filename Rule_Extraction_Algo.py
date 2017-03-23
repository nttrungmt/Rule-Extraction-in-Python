import pandas as pd
import numpy as np

class RuleFinder():

    def __init__(self, dat_file, rule_length=-1):
        self.rule_length = rule_length
        self.dat_file = dat_file

    def parse_file(self, header=None, cols=None):
        self.data = pd.read_csv(self.dat_file, header=header)
        return self.data


    def divideset(self,rows,column,value):
        split_function=None
        if isinstance(value, int) or isinstance(value,float):
            split_function = lambda x: x > value
        else:
            split_function = lambda x: x == value

        self.set1=rows[rows[column].apply(split_function)]
        self.set2=rows[~rows[column].apply(split_function)]
        return (self.set1, self.set2)


    def entropy(self,rows, column):
        log2 = lambda x: np.log(x)/np.log(2)
        counts = rows[column].value_counts()
        count_freq = counts/len(rows)
        return count_freq.apply(log2)

    def fit(self,rows,column, scoring=entropy):

        current_score = scoring(rows,column)

        best_gain = 0.0
        best_criteria = None
        best_sets = None

        classes = df[column].value_counts()
        var_cols = df.drop(column, axis=1).columns.values
        for col in var_cols:
            counts = rows[col].value_counts()
            print counts

            for value in counts.values():
                print value


Lung_dataset = RuleFinder("Lung_Cancer.csv", 3)
data = Lung_dataset.parse_file(header=None)
print data.head()
print data[0].value_counts()
print Lung_dataset.entropy(data, 0)
sub_1, sub_2 = Lung_dataset.divideset(data, 0, 1)
print sub_1[2].value_counts()
