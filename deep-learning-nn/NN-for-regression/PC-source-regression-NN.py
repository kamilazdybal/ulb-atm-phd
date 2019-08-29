"""
This function performs Deep Neural Network regression of PC-source terms in the space of Principal Components.

PC-score-1 and PC-score-2 are the predictors.
PC-source-1 and PC-source-2 are the regressors.
"""
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import center_and_scale as cas
from plot_regression_results import plot_regression
import quality_of_reconstruction as qor

nrmse_collected = []
scal_crit = 'pareto'

for st in range(0,2):

    # Load full csv data:
    Output = pd.read_csv('Data/PC_sources_all_species_c_mean_s_' + scal_crit + '.csv', sep = ',', header=None, usecols=[st])
    Input = pd.read_csv('Data/PC_scores_all_species_c_mean_s_' + scal_crit + '.csv', sep = ',', header=None, usecols=[0,1])
    idx_sampled = pd.read_csv('Data/idx_sampled.csv', sep = ',', header=None, usecols=[0])

    # Change DataFrames to numpy arrays:
    Output = Output.to_numpy()
    Input = Input.to_numpy()
    (n_obs, n_pcs) = np.shape(Input)
    Input_s = np.zeros([n_obs, n_pcs])
    Output = np.reshape(Output, (n_obs,1))
    idx_sampled = idx_sampled.to_numpy() - 1 # minus one is to change from Matlab to Python indexing

    # Scale data to be in range -1 to 1:
    Input_s[:,0] = cas.minus_one_one(Input[:,0])
    Input_s[:,1] = cas.minus_one_one(Input[:,1])
    Output_s = cas.minus_one_one(Output)

    # Sample using pre-defined pool:
    (n_samples, _) = np.shape(idx_sampled)
    idx_sampled = np.reshape(idx_sampled, (n_samples))
    Input_sampled = Input_s[idx_sampled]
    Output_sampled = Output_s[idx_sampled]

    # Neural Networks Sequential model -----------------------------------------
    val_split = 0.2

    # Create Sequential model:
    model = Sequential([
    Dense(5, input_dim=2, activation='tanh'),
    Dense(10, activation='tanh'),
    Dense(20, activation='tanh'),
    Dense(10, activation='tanh'),
    Dense(5, activation='tanh'),
    Dense(1, activation='linear')
    ])

    model.compile(Adam(lr=0.001), loss='mean_squared_error', metrics=['accuracy'])
    model.fit(Input_sampled, Output_sampled, batch_size=250, epochs=800, validation_split=val_split, verbose=0)

    Output_regressed = model.predict(Input_s, verbose=0)

    # --------------------------------------------------------------------------

    # Compute NRMSE:
    nrmse = qor.nrmse(Output_s, Output_regressed)
    nrmse_collected.append(nrmse)

    # Print info on the data set size:
    print('-----------------------------------------------------------')
    print('Regressing variable number ' + str(st+1) + '.')
    print('\nMin scaled Predictor-1:\t' + str(round(np.min(Input_s[:,0]), 5)) + '\tMax scaled Predictor-1:\t' + str(round(np.max(Input_s[:,0]), 5)))
    print('Min scaled Predictor-2:\t' + str(round(np.min(Input_s[:,1]), 5)) + '\tMax scaled Predictor-2:\t' + str(round(np.max(Input_s[:,1]), 5)))
    print('Min scaled Regressor:\t' + str(round(np.min(Output_s), 5)) + '\tMax scaled Regressor:\t' + str(round(np.max(Output_s), 5)) + '\n')

    print('Percentage of the data used for training: %.3f' % (np.size(Output_sampled)/np.size(Output) * 100))
    print('NRMSE for the reconstruction is: %.3f' % (np.round(nrmse, 5)))
    print('-----------------------------------------------------------')

    # Save the regression results in .csv:
    Output_regressed = cas.uu_minus_one_one(Output_regressed, Output)
    filename = 'source_term_' + str(st+1) + '_regression_results_s_' + scal_crit + '.csv'
    np.savetxt(filename, (Output_regressed), delimiter=',')

    # Plotting:
    filename = 'DWGs/PC-source-NN-NRMSE-results-1-ST-Z' + str(st+1) + '-regression.png'
    plot_labels = ['PC-1', 'PC-2', 'PC-source term ' + str(st+1)]
    plot_regression(Input, Output, Output_regressed, plot_labels, filename)
