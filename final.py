import pandas as pd
import numpy as np

# from IPython.display import display # Allows the use of display() for DataFrames

# Import supplementary visualizations code visuals.py
# import visuals as vs

# Pretty display for notebooks
# %matplotlib inline

# Load the dataset
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

# Print the first few entries of the RMS Titanic data
#datas= full_data[full_data['Parch']==0]

#print  full_data[full_data['Sex']==].describe()


outcomes = full_data['Survived']
data = full_data.drop('Survived', axis=1)


# Show the new dataset with 'Survived' removed
#print(data.head())


def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """

    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred):

        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean() * 100)

    else:
        return "Number of predictions does not match number of outcomes!"


# Test the 'accuracy_score' function
predictions = pd.Series(np.ones(5, dtype=int))
print accuracy_score(outcomes[:5], predictions)


def predictions_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """

    predictions = []
    for _, passenger in data.iterrows():
        # Predict the survival of 'passenger'
        predictions.append(0)

    # Return our predictions
    return pd.Series(predictions)


# Make the predictions
predictions = predictions_0(data)


def predictions_1(data):
    """ Model with one feature:
            - Predict a passenger survived if they are female. """

    predictions = []
    for _, passenger in data.iterrows():
        # Remove the 'pass' statement below
        # and write your prediction conditions here
        if passenger['Sex']=='female':
            predictions.append(1)
        else:
            predictions.append(0)

    # Return our predictions
    return pd.Series(predictions)


# Make the predictions
predictions1 = predictions_1(data)
print accuracy_score(outcomes, predictions1)


def predictions_2(data):
    """ Model with two features:
            - Predict a passenger survived if they are female.
            - Predict a passenger survived if they are male and younger than 10. """

    predictions = []
    for _, passenger in data.iterrows():
        # Remove the 'pass' statement below
        # and write your prediction conditions here
        if passenger['Sex']=='male':
            if passenger['Age']<10:
                predictions.append(1)
            else:
                predictions.append(0)
        else:
            predictions.append(1)

    # Return our predictions
    return pd.Series(predictions)


# Make the predictions
predictions2 = predictions_2(data)

predictions1 = predictions_1(data)
print accuracy_score(outcomes, predictions2)




def predictions_3(data):
    """ Model with two features:
            - Predict a passenger survived if they are female.
            - Predict a passenger survived if they are male and younger than 10. """

    predictions = []
    for _, passenger in data.iterrows():
        # Remove the 'pass' statement below
        # and write your prediction conditions here
        if passenger['Sex']=='male':
            if passenger['Pclass'] != 3:
                if passenger['Age']<14:
                    predictions.append(1)

                else:
                    predictions.append(0)
            else:
                predictions.append(0)
        else:
            predictions.append(1)

    # Return our predictions
    return pd.Series(predictions)


# Make the predictions
predictions3 = predictions_3(data)

print accuracy_score(outcomes, predictions3)
