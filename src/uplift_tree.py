import pandas as pd
from causalml.inference.tree import UpliftTreeClassifier
from causalml.inference.tree import uplift_tree_string, uplift_tree_plot


def build_uplift_tree(df, t, y):

    treatment = t
    outcome = y

    df[treatment]=df[treatment].astype(str)

    controllables = []
    uncontrollables = []

    features = df
    for col in [treatment, outcome]:
        features = features.drop(col, axis=1)

    # Train uplift tree
    uplift_model = UpliftTreeClassifier(max_depth=5, min_samples_leaf=200, min_samples_treatment=50,
                                        n_reg=100, evaluationFunction='KL', control_name='0')
    uplift_model.fit(features.values, treatment=df[treatment].values, y=df[outcome].values)


    # Print uplift tree as a string
    result = uplift_tree_string(uplift_model.fitted_uplift_tree, features.columns.values.tolist())

    # save uplift tree as png
    graph = uplift_tree_plot(uplift_model.fitted_uplift_tree, features.columns.values.tolist())
    with open("UpliftTree.png", "wb") as png:
        png.write(graph.create_png())


