# Carry-Out

## The Carry-Out Sentence
"You cannot compute the missingness of rows that never made it into the dataset — every diagnostic reads only the survivors and calls them the world."

## Wrong Guess Defeated
"An exploratory data analysis report showing zero missing values and clean distributions guarantees that our dataset is complete and representative."

## Falsifying Case
Three source tables merged on an unstandardized identifier silently dropped 4% of records during an inner join. Because the dropped records never entered the final table, standard EDA reported 0.0% missing cells across 79,400 rows, completely missing the excluded subpopulation.
