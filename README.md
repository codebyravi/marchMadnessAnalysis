# March Madness 2019 Analysis

A Machine Learning solution take data from this data (https://www.kaggle.com/c/mens-machine-learning-competition-2019).

The project provides a solution to both Stage 1 and Stage 2 of the Kaggle competition, predicting the winner of historical fixtures and predicting the winners of all possible March Madness 2019 matchups respectively.

The submission files for these solutions can be found in 'SubmissionStage1.csv' and 'SolutionStage2.csv' respectively. The project predicts the probability that the first team specified will beat the second team specified for each matchup listed in the Sample Submission file for both Stage 1 and Stage 2.

The project also creates a predicted bracket for the 2019 NCAA Men's March Madness basketball tournament based on the predictions made in Stage 2, and uses the tournament seedings and slots. This bracket can be found in the file 'output.png'.

### Required Dependencies

- Numpy
  pip install numpy
- Pandas
  pip install pandas
- Matplotlib
  pip install matplotlib
- Pickle
  It's a standard library in Python
- Random
  It's a standard library in Python
- Ski Kit Learn
  pip install scikit-learn
- Keras
  pip install keras
- Bracketeer
  pip install bracketeer

### Execution Instructions

1. Create dataset that holds details for each team for every season.

```
python createTeamDetails.py
```

2. Create dataset that contains details about every past matchup, which is used as the training dataset.

```
python createTrainingDataset.py
```

3. Create predictive models that can be used to predict the outcomes of future fixtures.

```
python createPredictionModel.py
```

4. Create dataset that holds the data used by the model for matchups that must be predicted in the Stage 1 submission.

```
python createStage1PredictionsDataset.py
```

5. Use the most accurate model created to create Stage 1 predictions, and write these to a submission file.

```
python createStage1Predictions.py
```

6. Submit the Stage 1 predictions to the Kaggle competition (requires setting up of the Kaggle library and Kaggle API).

```
kaggle competitions submit -c mens-machine-learning-competition-2019 -f SubmissionStage1.csv -m "My Stage 1 submission"
```

7. Create dataset that holds the data used by the model for matchups that must be predicted in the Stage 2 submission.

```
python createStage2PredictionsDataset.py
```

8. Use the most accurate model created to create Stage 2 predictions, and write these to a submission file.

```
python createStage2Predictions.py
```

9. Create a visual representation of the predictions made for the 2019 tournament.

```
python createBracket.py
```

10. Submit the Stage 2 predictions to the Kaggle competition (requires setting up of the Kaggle library and Kaggle API).

```
kaggle competitions submit -c mens-machine-learning-competition-2019 -f SubmissionStage2.csv -m "My Stage 2 submission"
```

### File Details

Other files included or created in this repository include (in order of creation/access):

- _data/RegularSeasonDetailedResults.csv_: Holds data from NCAA Regular Season matchups since 1985.
- _data/NCAATourneyDetailedResults.csv_: Holds data from NCAA March Madness matchups since 2003.
- _data/TeamConferences.csv_: Holds data regarding the team ID's of each team part of the dataset for each year.
- _data/all_teamData.csv_: Holds per-season data for each NCAA team since 2003.
- _data/2019_teamData.csv_: Holds regular season data for 2019 NCAA teams.
- _data/all_dataset.csv_: Holds data for all NCAA matchups since 2003 in a format suitable for use as training data.
- _scaler.save_: Holds the scaler that is used to preprocess data before it is used for predictions.
- _predictor.pkl_: Holds the most accurate classifier created during the training phase.
- _data/stage1_dataset.csv_: Holds data for matchups identified in Stage 1 in a format suitable for making predictions with.
- _data/stage2_dataset.csv_: Holds data for matchups identified in Stage 2 in a format suitable for making predictions with.
- _SampleSubmissionStage1.csv_: Holds details regarding which matchups should be predicted for Stage 1.
- _SampleSubmissionStage2.csv_: Holds details regarding which matchups should be predicted for Stage 2.
- _SubmissionStage1.csv_: Holds the submissions for Stage 1 of the Kaggle competition, as it stores the matchup predictions.
- _SubmissionStage2.csv_: Holds the submissions for Stage 2 of the Kaggle competition, as it stores the matchup predictions.
- _data/Teams.csv_: Holds data regarding the team name of each team based on their team ID.
- _data/NCAATourneySeeds.csv_: Holds data regarding the NCAA seed of each team.
- _data/NCAATourneySlots.csv_: Holds data regarding the NCAA slot of each team.
- _bracket.png_: Holds a visual representation of the predictions made in the form of a bracket for the 2019 tournament.

### Predictor Details

The features in an input instance for this model are:

- 0: Team 1 Home or Away (1: Home, 0: Neutral, -1: Away)
- 1: Team 1 Points per game - Team 2 Points per game
- 2: Team 1 Points Allowed per game - Team 2 Points Allowed per game
- 3: Team 1 Field Goals Made per game - Team 2 Field Goals Made per game
- 4: Team 1 Field Goals Attempted per game - Team 2 Field Goals Attempted per game
- 5: Team 1 3-Pointers Made per game - Team 2 3-Pointers Attempted per game
- 6: Team 1 Free-Throws Made per game - Team 2 Free-Throws Attempted per game
- 7: Team 1 Offensive Rebounds per game - Team 2 Offensive Rebounds per game
- 8: Team 1 Defensive Rebounds per game - Team 2 Defensive Rebounds per game
- 9: Team 1 Assists per game - Team 2 Assists per game
- 10: Team 1 Turnovers per game - Team 2 Turnovers per game
- 11: Team 1 Steals per game - Team 2 Steals per game
- 12: Team 1 Blocks per game - Team 2 Blocks per game
- 13: Team 1 Personal Fouls per game - Team 2 Personal Fouls per game

The output for an input instance for this model is the probability that Team 1 wins.

### NCAA 2019 Tournament Predictions

<img src = "bracket.png"/>

### Reflection on the competition

I will post this once the NCAA Competition completes on April 8th 2019.
