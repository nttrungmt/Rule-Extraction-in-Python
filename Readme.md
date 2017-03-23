### Rule Extraction Systems

Rule Extraction systems are a family of inductive learning techniques that build a predictive model based on a dataset. It uses separate and conquer to directly induce rules from a given training set and build a knowledge repository to aid in decision making.

We want to make a system that takes a dataset as input and returns a set of rules to differentiate the dataset into Rules that best split the dataset across the defined label using the descriptive features.

Lets say we input a dataset that has as features the sociodemographic variables of each data-point and we want to have a set of rules that tell us the sociodemographic makeup of people that are visited our homepage vs people that did not. Our Dataset looks like:

| AgeBracket | IncomeBracket | Gender | Visited Home Page |
| :--------: | :-----------: | :----: | :---------------: |
|     3      |       1       |   F    |         1         |
|     2      |       2       |   M    |         0         |
|     2      |       3       |   F    |         0         |



We want to know which combination of features influences the propensity of a user to visit the homepage vs the alternative. This is very similar to training a decision tree classifier on the dataset. However there are specific differences in Decision Trees and Rule Extraction Classifiers. Let us define a few terms to better motivate our description:

Lets say our rule is 		$(\text{Gender} = F) \rightarrow \text{Visited Home Page} = 1 $

with LHS and RHS being $(\text{Gender} = F)$ and  $\text{Visited Home Page} = 1 $ respectively. Now we can define the quality indicators of this rule:

- Coverage: Fraction of records that satisfy the antecedent of a rule, or the LHS

  ​

  ​						$Coverage = \frac{LHS}{\text{Total number of samples}}$	

  ​

- Accuracy: Fraction of records covered by the rule when it holds



​							$Accuracy = \frac{\text{LHS } \cap \text{ RHS}}{LHS}$



For the above rule, Coverage = 2/3 = 66.7% and Accuracy = 1/2 = 50%



There are two ways in which we can extract rules from the dataset. One is to ask for a set of rules based on metrics of maximizing coverage and accuracy. The other is to already give a part of the rule, like gender==female and ask for complementary rules that best specialize the rule set.



Methodology:

Generate rule that maximizes the rules accuracy. Choosing the best attribute to split on, and choosing the best value to split the attribute on. Here the difference from a decision tree lies in the fact that a decision tree would try to maximize a node's purity.

![Capture](D:\Users\jassandh1\Desktop\Capture.PNG)







|           Covering Algorithms            |              Decision Tree               |
| :--------------------------------------: | :--------------------------------------: |
| **Covering Approach** where at each stage a rule a identified that covers some of the examples, which are then skipped while considering the next rules | **Sequential Approach** where we conduct a step-wise search for the best rules guided by evaluation measures |
| Flexibility in choosing for better coverage/accuracy or a combination of both | Rules become more complex as we move downwards in a tree |
|    More readable than decision trees     | A new set of rules requires reshaping the entire tree |
| Empirically proven to be better than decision trees | Rule obtained without decision trees are more compact and accurate |
| Easier to analyze and modify, do not have an order | Rules have an implied order in which the splitting is performed |
| More flexibility and more combinations of rules given that they all don't grow recursively out of a single root node |                                          |



### Covering Algorithms

| Covering Algorithm |          Rule Extraction Method          |
| :----------------: | :--------------------------------------: |
|       Prism        |                                          |
|       RIPPER       |                                          |
|        LEM2        |                                          |
|         AQ         |                                          |
|        CN2         |                                          |
|       MODLEM       |                                          |
|         1R         | Learns one rule to split the dataset based on one single attribute, minimizes error rate |



### Methods for Sequential Learning One Rule algorithm

```python
def Sequential Convering (K Class, A attributes, D data, T acceptance threshold):
    R = [] #previous set of rules
    r = learn_one_rule(Y Class, A attributes, D data)
    for i in range(0,n):
        if evaluate(r, D) > T:
            R.append(r)
            D = D[R == True]
            r = learn_one_rule(K Class, A attributes, D data)
   	return R
```



```python
def R_1(C Classes, A Attributes, D Data):
    R = []
    for Att in A:
        R_a = []
      for v in Att:
          if isdigit(Att) == False: #Categorical features
            D_a_v = D[Att==v]
            Class_v = D[C].value_counts().index[0] #Take most occuring class
            R_a.append([Att=v->class=C_i])
          elif isdigit(Att) == True: #Continuous numerical features
              D_a_v = D[Att>=v]
              ...
      R_a =	get_lowest_error_value_split(R_a)
    R = get_lowest_error_attribute(R_a)
    return R
```

### Prism Covering Algorithm

```python
def get_rules(C Classes, A Attributes, D Data):
    for c_i in C:
        D_sub = D
        p = True
        R_ci = [if p then C=c_i]
        for each Att in A:
            accuracy = {}
            for v in Att:
                accuracy[(Att, v)] = (D_sub[Att==v, Classes = c_i])/D_sub[Att==v]
        accuracy_max_v = take max_acc key #break ties with size of D_sub[Att==v]
        R_ci.append(if Att_best=v_best then C=c_i)
        #repeat above with D[Att_best=v_best] to refine the rule
        #Remove all instances covered by R and do same process on remaining dataset 
     return R_c1, R_c2..
```



### Decision Tree Algorithms

Flowcharts that aid in the decision making process. Different kinds of Decision Tree algorithms in practice which a top down, recursive, divide and conquer approach to decision tree induction:

| ID3 (Iterative Dichotomiser) | C4.5 | CART |
| :--------------------------: | :--: | :--: |
|    Precursor in the C4.5     |      |      |
|                              |      |      |
|                              |      |      |
|                              |      |      |