Because of some data shortages, we adopt three different ways to manipulate the data. 
Three models are trained with different dataset. Details are written as follow:


1. Exclude loan_status "Current" and "In Grace Period". Also drop the following features: out_prncp, total_pymnt, total_rec_prncp, total_rec_int
Because we think it is a pre_loan model and it is difficult to distinguish those status from 'bad' and 'good'.
This model is in the '1.Project 3-Logistic Regression' file.

2. Keep all loan_status and features, but did not adopt SMOTE to balance samples, we separate 36 months loans from 60 months loans.
These two models are in '2.Project 3-Logistic Regression-36months' and '3.Project 3-Logistic Regression-60months' files.

3. Keep all loan_status and features  and adopt module SMOTE to handle sample imbalance.
This model is in the '4. Project 3-Dealing with unbalanced sample' file.


, 