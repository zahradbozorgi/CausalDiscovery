# CausalDiscovery
## A/B test with UWV

This repository contains code creating an uplift tree from an event log to discover subgroups in the population for which a certain treatment is useful. 

To install the required packages, use the requirements.txt file provided in the repository by running the following command in your virtual environment.

`pip install -r requirements.txt`

Once all the required packages are installed you can run the script using the following command:

`python causal_discovery.py -f input_df.csv -t treatment_col -y outcome_col` 
