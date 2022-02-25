# -*- coding: utf-8 -*-
"""
Applying Text Similarity Functions
data stitching using text similarity.

problem:
We will have multiple tables in the database, and sometimes there won’t
be a common “ID” or “KEY” to join them – scenarios like the following:
• Customer information scattered across multiple tables and systems.
• No global key to link them all together.
• A lot of variations in names and addresses.

Solution:
This can be solved by applying text similarity functions on the
demographic’s columns like the first name, last name, address, etc. And
based on the similarity score on a few common columns, we can decide
either the record pair is a match or not a match.    
"""
# Deduplication in the same table
import recordlinkage

# import dataset
from recordlinkage.datasets import load_febrl1

df = load_febrl1()
df.head()

# Blocking Technique
"""
Standard blocking
    > Single column
    > Multiple columns
    
Sorted neighborhood
Q-gram : fuzzy blocking
LSH
Canopy clustering
"""

indexer = recordlinkage.BlockIndex(on = 'given_name')
pairs = indexer.index(df)
print(len(pairs))


"""
Similarity matching and scoring
Here we compute the similarity scores on the columns like given name,
surname, and address between the record pairs generated in the previous
step. For columns like date of birth, suburb, and state, we are using the
exact match as it is important for this column to possess exact records.
We are using jarowinkler
"""
compare_cl = recordlinkage.Compare()

compare_cl.string('given_name', 'given_name', method = 'jarowinkler',
                  label='given_name')

compare_cl.string('surname', 'surname', method = 'jarowinkler',
                  label='surname')

compare_cl.string('address_1', 'address_1', method = 'jarowinkler',
                  label='address_1')

compare_cl.exact('date_of_birth','date_of_birth', label = 'date_of_birth')

compare_cl.exact('suburb','suburb', label = 'suburb')

compare_cl.exact('state','state', label = 'state')

features = compare_cl.compute(pairs, df)

features.sample(5)

# Predicting records match or do not match using ECM - classifier
# select all the features except for given_name since its our blocking key

features1 = features[['suburb','state','surname','date_of_birth','address_1']]

# Unsupervised learning - probabilistic
ecm = recordlinkage.ECMClassifier()

result_ecm = ecm.learn((features1).astype(int), return_type='series')

result_ecm

# Records of same customers from multiple tables

from recordlinkage.datasets import load_febrl4
df1, df2 = load_febrl4()
df1.head()
df2.head()

# Blocking - to reduce the comparison window and creating record pairs
indexer = recordlinkage.BlockIndex(on = 'given_name')
pairs = indexer.index(df1,df2)

# Similarity matching
compare_cl1 = recordlinkage.Compare()
compare_cl1.string('given_name', 'given_name', method = 'jarowinkler',
                   label='given_name')

compare_cl1.string('surname', 'surname', method = 'jarowinkler',
                  label='surname')

compare_cl1.string('address_1', 'address_1', method = 'jarowinkler',
                  label='address_1')

compare_cl1.exact('date_of_birth','date_of_birth', label = 'date_of_birth')

compare_cl1.exact('suburb','suburb', label = 'suburb')

compare_cl1.exact('state','state', label = 'state')

features2 = compare_cl1.compute(pairs, df1,df2)
features2.head(12)



# Predicting records match or do not match using ECM – classifier
#Here is an unsupervised learning method to calculate the probability that
# the record is a match.
# select all the features except for given_name since its our blocking key

features1 = features[['suburb','state','surname','date_of_birth','address_1']]
# unsupervised learning - probablistic
ecm = recordlinkage.ECMClassifier()
result_ecm = ecm.learn((features1).astype(int),return_type = 'series')

result_ecm



























