import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from tennis_regression_analysis import model_these_features

# load and investigate the data here:
data = pd.read_csv('tennis_stats.csv',index_col = [0,1])
tennis = pd.DataFrame(data)
all_features = ['Aces', 'DoubleFaults', 'FirstServe', 'FirstServePointsWon', 'SecondServePointsWon',
            'BreakPointsFaced', 'ServiceGamesPlayed', 'ServiceGamesWon', 'TotalServicePointsWon',
            'FirstServeReturnPointsWon', 'SecondServeReturnPointsWon', 'BreakPointsOpportunities',
                       'BreakPointsSaved', 'BreakPointsConverted', 'ReturnGamesPlayed', 'ReturnGamesWon',
                       'ReturnPointsWon', 'TotalPointsWon']
binary_features = ['FirstServePointsWon','FirstServe','SecondServePointsWon','SecondServeReturnPointsWon',
                    'BreakPointsConverted','BreakPointsSaved','ReturnGamesWon','ReturnPointsWon','ServiceGamesWon',
                    'TotalPointsWon','TotalServicePointsWon']
numeric_features = ['Aces','BreakPointsFaced','BreakPointsOpportunities','ReturnGamesPlayed','DoubleFaults',
                     'ServiceGamesPlayed']
outcomes = ['Wins','Losses','Ranking','Winnings']
# perform exploratory analysis here:
print(tennis.isna().any())
#print(binary_features.columns)


## perform single feature linear regressions here:

## perform two feature linear regressions here:

## perform multiple feature linear regressions here:
print("creating model for predicted winnings using all features:\n")
model_these_features(all_features, tennis, outcomes, 0)
print("creating model for predicted winnings using only binary features:\n")
model_these_features(binary_features, tennis, outcomes, 0)
print("creating model for predicted winnings using only numeric features:\n")
model_these_features(numeric_features, tennis, outcomes, 0)
