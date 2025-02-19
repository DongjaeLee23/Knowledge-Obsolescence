import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import PercentFormatter

def load_and_process_data(file_paths):
    dataframes = []
    for file_path in file_paths:
        df = pd.read_csv(file_path, usecols=['epoch', 'train_acc', 'test_acc_2021-10-01', 'test_acc_11-2021'])
        df['epoch'] += 1  # Increment epochs to range between 1 and 10
        if 'bert_2021-4_log.csv' in file_path or 'bert_11-2020_log.csv' in file_path or 'bert_12-2020_log.csv' in file_path:
            df['test_acc_2021-10-01'] = 1 - df['test_acc_2021-10-01']  # Invert test accuracy for better visualization
            df['test_acc_11-2021'] = 1 - df['test_acc_11-2021']  # Invert test accuracy for better visualization
        dataframes.append(df)
    return dataframes

def plot_accuracy(df_list, y_col, y_label, title, y_lim):
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="darkgrid")

    markers = ['o', 's', '^', 'p']
    colors = ['b', 'g', 'purple', 'r']
    marker_face_colors = ['orange', 'red', 'yellow', 'black']
    
    for df, marker, color, mfc in zip(df_list, markers, colors, marker_face_colors):
        plt.plot(df['epoch'], df[y_col], linestyle='-', marker=marker, color=color, markersize=8, linewidth=2, 
                 markerfacecolor=mfc, markeredgewidth=2)
    
    plt.xlabel('Epochs', fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.title(title, fontsize=16)
    plt.xticks(range(1, 11), fontsize=12)
    plt.yticks(fontsize=12)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.xlim(0.8, 10.2)
    plt.ylim(y_lim)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(['Old FNC 2021-4', 'Old FNC 2021-5', 'NELA 2020-11', 'NELA 2020-12'], fontsize=12)
    plt.show()

def compute_means(df_list):
    means = []
    for df in df_list:
        means.append(df[['train_acc', 'test_acc_2021-10-01', 'test_acc_11-2021']].mean().tolist())
    return means

def plot_boxplot(data):
    myBoxPlot = pd.DataFrame(data)
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=myBoxPlot["dataset"], y=myBoxPlot["average_acc"])
    plt.xlabel('Dataset', fontsize=14)
    plt.ylabel('Average Test and Train Accuracies', fontsize=14)
    plt.title('Box Plot of Accuracies', fontsize=16)
    plt.show()

# Load and process data
file_paths = ['bert_2021-4_log.csv', 'bert_2021-5_log.csv', 'bert_11-2020_log.csv', 'bert_12-2020_log.csv']
df_list = load_and_process_data(file_paths)

# Plot training accuracy
plot_accuracy(df_list, 'train_acc', 'Training Accuracy', 'Training Accuracy Between All NELA and Old FNC Datasets', (0.7, 1.0))

# Plot testing accuracy with New FNC 10-2021
plot_accuracy(df_list, 'test_acc_2021-10-01', 'Testing Accuracy with New FNC 10-2021', 'Testing Accuracy on First New FNC, 10-2021', (0.4, 0.7))

# Plot testing accuracy with New FNC 11-2021
plot_accuracy(df_list, 'test_acc_11-2021', 'Testing Accuracy with New FNC 11-2021', 'Testing Accuracy on Second New FNC, 11-2021', (0.5, 0.8))

# Compute means
means = compute_means(df_list)

data = {
    'dataset': ['Old FNC 2021-4', 'Old FNC 2021-4', 'Old FNC 2021-4', 
                'Old FNC 2021-5', 'Old FNC 2021-5', 'Old FNC 2021-5', 
                'NELA 2020-11', 'NELA 2020-11', 'NELA 2020-11', 
                'NELA 2020-12', 'NELA 2020-12', 'NELA 2020-12'],
    'average_acc': sum(means, [])
}

# Plot boxplot
plot_boxplot(data)