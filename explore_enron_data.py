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
import glob
df = pd.DataFrame(enron_data)
#print df.head()
#print df.shape

#define a function that calculates how many persons of interest in enron_data
#def poi():
#    nbr=0
#    for person in enron_data.keys():
#        if enron_data[person]['poi'] == 1:
#            nbr = nbr+1
#    return nbr
#print "there are", poi(), "person of interest"

#define a function that calculates how many persons of interest in /final_project/poi_names.txt and this by reading from the txt_file and calculate the occurences


poi_count=0
import os
folder = 'final_project/'
for txt_file in os.listdir(folder):
    with open (os.path.join(folder, txt_file)) as file:
        for line in file.readlines():
            for word in line.split():
                if word=='(y)':
                    poi_count+=1


print "There are ",poi_count, "POIs"
