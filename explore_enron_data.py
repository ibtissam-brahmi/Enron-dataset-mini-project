#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
#import the dataset
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#get how many many data points our dataset have
print "The Enron dataset contains",len(enron_data), "people"

#convert the dictionary to a dataframe
import pandas as pd
df = pd.DataFrame(enron_data)
print df.head()
print df.shape
