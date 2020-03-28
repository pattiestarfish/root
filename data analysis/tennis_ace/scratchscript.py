#import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as numpy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
numpy.set_printoptions(suppress=True)
import seaborn

#broken funct
def create_player_database(array, coefficients):
    player_database=[]
    player_names=[]
    i=0
    for ele in array:
#        player_names.append(ele)
        player_database.append(ele)
        player_database[i] = str(ele) + str(coefficients[i])
        i += 1
    print(player_database)
    return


# load and investigate the data here:
data = pd.read_csv("tennis_stats.csv", index_col = [0,1])
#redefine index to name (default ints)
tennis = pd.DataFrame(data)
features = tennis[['Aces', 'DoubleFaults', 'FirstServe', 'FirstServePointsWon', 'SecondServePointsWon',
            'BreakPointsFaced', 'ServiceGamesPlayed', 'ServiceGamesWon', 'TotalServicePointsWon',
            'FirstServeReturnPointsWon', 'SecondServeReturnPointsWon', 'BreakPointsOpportunities',
            'BreakPointsConverted', 'ReturnGamesPlayed', 'ReturnGamesWon', 'ReturnPointsWon', 'TotalPointsWon']]
outcomes = tennis[['Wins','Losses','Ranking','Winnings']]
#print(outcomes['Wins'][])


#draws scatter plots for all features vs Outcome: Wins
#draw plots for all outcomes, then create linear regression for all variables, sort by highest R values
for feature in features:
    plt.scatter(tennis[[feature]],tennis[['Ranking']], alpha=0.6)
    plt.xlabel(str(feature)), plt.ylabel('Player World Ranking')
    ranking_regr = LinearRegression()
    x_train, x_test, y_train, y_test = train_test_split(tennis[[feature]], tennis[['Ranking']], train_size=0.8, test_size=0.2, random_state=6)
    ranking_model = ranking_regr.fit(x_train, y_train)
    rank_predict = ranking_regr.predict(x_test)

    #if score between test and actual values are close, model is relatively accurate
    print(ranking_regr.score(x_train,y_train))
    print(ranking_regr.score(x_test,y_test))
    residuals = rank_predict - y_test
    print(residuals)

 #   plt.scatter(tennis[[feature]],tennis[['Winnings']], alpha=0.6)
 #   plt.xlabel(str(feature)), plt.ylabel('Player Total Winnings')

 #   plt.scatter(tennis[[feature]],tennis[['Wins']], alpha=0.6)
  #  plt.xlabel(str(feature)), plt.ylabel('Player Total Wins')


#print(tennis[['BreakPointsOpportunities', 'Winnings']])

# perform exploratory analysis here:


#finding correlation coefficients, assigning them to header variables
mlr = LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(tennis[['BreakPointsOpportunities']],tennis[['Winnings']],train_size = 0.8, test_size = 0.2, random_state = 6)
model = mlr.fit(x_train,y_train)
win_predict = mlr.predict(x_test)
x_coefficients = (numpy.reshape(mlr.coef_, (-1,1)))
#print(x_coefficients[0])

print("Printing correlational coefficients for Player Winnings: ")
create_player_database(tennis[['BreakPointsOpportunities']], x_coefficients)
print(tennis[['Aces']])

#reshape creates vertical columns with 1 element per square
print(type(mlr.coef_))
print(type(tennis))
#tennis_headers = numpy.reshape(tennis, (-1,1))
print(mlr.coef_)


#finding R scores
#print(tennis[['Year']])


print(mlr.score(x_train,y_train))
print(mlr.score(x_test,y_test))
residuals = win_predict - y_test
plt.scatter(win_predict, residuals, alpha = 0.4)
plt.title('Win prediction residuals')
plt.show()
plt.scatter(tennis[['BreakPointsOpportunities']], tennis[['Winnings']])
plt.xlabel("Player Break Points"), plt.ylabel("Playing Winnings: $")
plt.show()
plt.scatter(tennis[['Aces']], tennis[['Wins']])
plt.xlabel("Service Aces"), plt.ylabel("Player wins")
plt.show()

## perform single feature linear regressions here:
#single_reg = LinearRegression()
#single_reg.fit(y, z)
#winnings_predict = single_reg.predict(y)

#plt.plot(y, winnings_predict, 'or')
#plt.show()

## perform two feature linear regressions here:


## perform multiple feature linear regressions here:



















