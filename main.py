import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from get_DB_data import get_data
from cleaner_module import cleaner

################## CHANGE MODELS HERE #####################
# Add/remove list elements as necessary. Facilitates comparison of different models
models = [RandomForestClassifier(),
          LogisticRegression(),
          DecisionTreeClassifier()] 

##### CLEANING DATA #######
DB_path = os.path.join(os.getcwd(), os.path.join('data', 'data.db')) # this should get relative file path
df = cleaner(get_data(DB_path))

#### The axis ####
X_var = df.drop('Value', axis=1)
Y_var = df['Value']

############################# DECLARING SPLIT ON DATA ####################################
# Train test split - the machine learning portion: 70 train 20 test 10 validation
size_for_test_set = 0.2
size_for_validation_set = 0.1

# Test set
X_train, X_test, Y_train, Y_test = train_test_split(X_var, Y_var, test_size=size_for_test_set) # test

# Validation set
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=size_for_validation_set) # validation

#################################### Processsing ####################################
# 'Tagging' of types of varibles to be transformed for model; getting ready for processing
num_vars = [] # numerical variables
cat_vars = [] # categorical variables
ode_vars = [] # ordinal variables

# Into the pipe and transformed
transformed_data = piping(num_vars, cat_vars, ode_vars)

#################################### OUTPUT ####################################
############# Evaluation ###############
generate_output(transformed_data, vars_train, vars_test, vars_val, Is_Scam_train, Is_Scam_test, Is_Scam_val, models)




