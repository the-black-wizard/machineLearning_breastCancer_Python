#!/usr/bin/env python3

	#####################################################
	##    WISCONSIN BREAST CANCER MACHINE LEARNING     ##
	#####################################################

# Project by Raul Eulogio

# Project found at: https://www.inertia7.com/projects/3


"""
Model Evaluation
"""
# Import Packages ----------------------------
import matplotlib.pyplot as plt
from helper_functions import test_class_set
import random_forest as rf
import knn
import neural_networks as nn
from terminaltables import AsciiTable
from sklearn.metrics import classification_report

# Calling up metrics from the model scripts
# KNN ---------------------------------------
metrics_knn = knn.return_knn()
fpr = metrics_knn['fpr']
tpr = metrics_knn['tpr']
auc_knn = metrics_knn['auc']
predictions = metrics_knn['predictions']
test_error_rate = metrics_knn['test_error']

# RF ----------------------------------------
metrics_rf = rf.return_rf()
fpr2 = metrics_rf['fpr']
tpr2 = metrics_rf['tpr']
auc_rf = metrics_rf['auc']
predictions_rf = metrics_rf['predictions']
test_error_rate_rf = metrics_rf['test_error']

# NN ----------------------------------------
metrics_rf = nn.return_nn()
fpr3 = metrics_rf['fpr']
tpr3 = metrics_rf['tpr']
auc_nn = metrics_rf['auc']
predictions_nn = metrics_rf['predictions']
test_error_rate_nn = metrics_rf['test_error']

# Main --------------------------------------
if __name__ == '__main__':
	# Populate list for human readable table from terminal line
	table_data = [[ 'Model/Algorithm', 'Test Error Rate',
		'False Negative for Test Set', 'Area under the Curve for ROC',
		'Cross Validation Score'],
		['Kth Nearest Neighbor',  round(test_error_rate, 3), 5,
		round(auc_knn, 3), "Accuracy: {0: 0.3f} (+/- {1: 0.3f})"\
				.format(knn.mean_cv_knn, knn.std_error_knn)],
		[ 'Random Forest', round(test_error_rate_rf, 3), 3,
		round(auc_rf, 3), "Accuracy: {0: 0.3f} (+/- {1: 0.3f})"\
				.format(rf.mean_cv_rf, rf.std_error_rf)],
		[ 'Neural Networks' ,  round(test_error_rate_nn, 3),  1,
		round(auc_nn, 3), "Accuracy: {0: 0.3f} (+/- {1: 0.3f})"\
				.format(nn.mean_cv_nn, nn.std_error_nn)]]

	# convert to AsciiTable from terminaltables package
	table = AsciiTable(table_data)

	target_names = ['Benign', 'Malignant']

	print('Classification Report for Kth Nearest Neighbor:')
	print(classification_report(predictions,
		test_class_set,
		target_names = target_names))

	print('Classification Report for Random Forest:')
	print(classification_report(predictions_rf,
		test_class_set,
		target_names = target_names))

	print('Classification Report for Neural Networks:')
	print(classification_report(predictions_nn,
		test_class_set,
		target_names = target_names))

	print("Comparison of different logistics relating to model evaluation:")
	print(table.table)

	# Plotting ROC Curves
	f, ax = plt.subplots(figsize=(10, 10))

	plt.plot(fpr, tpr, label='Kth Nearest Neighbor ROC Curve (area = {0: .3f})'\
		.format(auc_knn),
         	color = 'deeppink',
         	linewidth=1)
	plt.plot(fpr2, tpr2,label='Random Forest ROC Curve (area = {0: .3f})'\
		.format(auc_rf),
         	color = 'red',
         	linestyle=':',
         	linewidth=2)
	plt.plot(fpr3, tpr3,label='Neural Networks ROC Curve (area = {0: .3f})'\
		.format(auc_nn),
         	color = 'purple',
         	linestyle=':',
         	linewidth=3)

	ax.set_axis_bgcolor('#fafafa')
	plt.plot([0, 1], [0, 1], 'k--', lw=2)
	plt.plot([0, 0], [1, 0], 'k--', lw=2, color = 'black')
	plt.plot([1, 0], [1, 1], 'k--', lw=2, color = 'black')
	plt.xlim([-0.01, 1.0])
	plt.ylim([0.0, 1.05])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title('ROC Curve Comparison For All Models')
	plt.legend(loc="lower right")
	plt.show()

	# Zoomed in
	f, ax = plt.subplots(figsize=(10, 10))
	plt.plot(fpr, tpr, label='Kth Nearest Neighbor ROC Curve  (area = {0: .3f})'\
		.format(auc_knn),
         	color = 'deeppink',
         	linewidth=1)
	plt.plot(fpr2, tpr2,label='Random Forest ROC Curve  (area = {0: .3f})'\
		.format(auc_rf),
         	color = 'red',
         	linestyle=':',
         	linewidth=3)
	plt.plot(fpr3, tpr3,label='Neural Networks ROC Curve  (area = {0: .3f})'\
		.format(auc_nn),
         	color = 'purple',
         	linestyle=':',
         	linewidth=3)

	ax.set_axis_bgcolor('#fafafa')
	plt.plot([0, 1], [0, 1], 'k--', lw=2) # Add Diagonal line
	plt.plot([0, 0], [1, 0], 'k--', lw=2, color = 'black')
	plt.plot([1, 0], [1, 1], 'k--', lw=2, color = 'black')
	plt.xlim([-0.001, 0.2])
	plt.ylim([0.7, 1.05])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title('ROC Curve Comparison For All Models (Zoomed)')
	plt.legend(loc="lower right")
	plt.show()

	print('fin \n:)')
