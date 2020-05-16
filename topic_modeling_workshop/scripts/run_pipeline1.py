#!/usr/bin/env python3

"""
Topic Modeling with gensim.

This is the main coordination script.
It allows you to set the pipeline parameters.
It allows you to determine which components will be run. 
After setting the right parameters, runs this script! (F5)
"""


# == Imports ==


from os.path import join
from topic_modeling_workshop.scripts import helpers
from topic_modeling_workshop.scripts import preprocessing
from topic_modeling_workshop.scripts import build_corpus
from topic_modeling_workshop.scripts import modeling
from topic_modeling_workshop.scripts import postprocessing
from topic_modeling_workshop.scripts import make_overview


import warnings
warnings.filterwarnings("ignore")




# == Files and folders ==

workdir = ".."            # working directory
dataset = "hkpress"              # dataset name, e.g. "hkpress-test"
identifier = "hkp1"           # model identifier, e.g. "hkp-test-10tp"



# == Parameters ==

numtopics =  15             # number of topics of the model, e.g. 15
passes =   500               # number of iterations when modeling, eg. 500
lang = "en"                 # language of the materials: "en" or "fr"



# == Coordinating function ==

def main(workdir, dataset, identifier, numtopics, passes, lang):
    print("==", "starting", "==", "\n==", helpers.get_time(), "==")   
    helpers.make_dirs(workdir, identifier)
    preprocessing.main(workdir, dataset, identifier, lang)
    build_corpus.main(workdir, identifier)
    modeling.main(workdir, identifier, numtopics, passes)
    postprocessing.main(workdir, dataset, identifier, numtopics)
    make_overview.main(workdir, identifier) 
    
main(workdir, dataset, identifier, numtopics, passes, lang)
