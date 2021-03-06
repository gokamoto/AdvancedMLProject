__author__ = 'griffin'

import pandas as pd
import numpy as np
from data_processing_update import numpyArrays
from featureEngineering_CategoryReduction import reduceCategories
from featureEngineering_userClustering import userCluster
from featureEngineering_textFeatures import ngram_processing
from featureEngineering_CollaborativeFiltering import addRecommendationScores

def applyFeatures(training_data, test_data, features_list):

    if "Category Reduction" in features_list:
        # Reduce business categories using PCA
        category_col_indices = [col for col in training_data.columns if 'b_categories_' in col]
        training_data, test_data = reduceCategories(training_data, test_data, category_col_indices)
        print "Added Category Reduction"

    if "User Clustering" in features_list:
        # Add in column for user clusters
        training_data, test_data = userCluster(training_data, test_data)
        print "Added User Clustering"

    if "Text Features" in features_list:
        training_data, test_data = ngram_processing(training_data, test_data)
        print "Added Text Features"

    if "Collaborative Filtering" in features_list:
        training_data, test_data = addRecommendationScores(training_data, test_data)
        print "Added Collaborative Filtering"

    training_data.replace([np.inf, -np.inf], np.nan, inplace=True)
    test_data.replace([np.inf, -np.inf], np.nan, inplace=True)

    training_data.fillna(training_data.mean(), inplace=True)
    test_data.fillna(test_data.mean(), inplace=True)
    return training_data, test_data
