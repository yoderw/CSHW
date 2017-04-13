### MACHINE LEARNING ###
'''
-- problems with turing test: ask to multiply eg. 347598672384 * 172892346
-- chinese room; early algorithms worked like this (ie. lookup tables)
-- ML is not trying to pass the turing test
    -- take some data, generalize some non-programmed rules (using stats)

supervised learning:= labelled data points as input; labels for new data points as output

|O X   X  X X
| O  X  O  X
|O  O  ?   X X
| O   O  X X
|______________

    -- e.g. using linear (or other) regression: outcome = a*age + b*weight
    regularization:= preference for simple classifiers
    (e.g. specifiy how straight the boundary line can be bt. O's and X's)

Minority Report using data science (or is that just psychopass...)

unsupervised learning:= nonlabelled data points as input
    -- clustering:= "drawing circles" around groups of data points
       (can reason about the world better with use of categories)

       k-means:= 1 pick centers
                 2 put in point in cluster w/ nearest center
                 3 recalculate centers
                 4 repeat 2-3
                 (will not loop infinitely)

       hierarchical:= 1 start with cluster for every point
                      2 merge the two closest clusters into one
                      3 repeat 2 until desired # of clusters is reached
                      (can represent as a tree,
                       to show optimum clustering for an aribitrary # of clusters)
                       -- can be used to show evolutionary tree of DNA sequences,
                          languages, etc.
'''
