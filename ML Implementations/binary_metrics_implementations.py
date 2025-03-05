import numpy as np

def confusion_matrix(y_true, y_pred):
    """Computes the confusion matrix with class percentages."""
    true_positives = np.sum((y_true == 1) & (y_pred == 1))
    true_negatives = np.sum((y_true == 0) & (y_pred == 0))
    false_positives = np.sum((y_true == 0) & (y_pred == 1))
    false_negatives = np.sum((y_true == 1) & (y_pred == 0))

    total_samples = len(y_true)
    total_positives_true = np.sum(y_true == 1)
    total_negatives_true = np.sum(y_true == 0)

    # Calculate percentages
    tp_percent = (true_positives / total_positives_true) * 100 if total_positives_true > 0 else 0
    tn_percent = (true_negatives / total_negatives_true) * 100 if total_negatives_true > 0 else 0
    fp_percent = (false_positives / total_negatives_true) * 100 if total_negatives_true > 0 else 0
    fn_percent = (false_negatives / total_positives_true) * 100 if total_positives_true > 0 else 0

    conf_matrix = np.array([[true_negatives, false_positives],
                             [false_negatives, true_positives]])

    percentages = np.array([[tn_percent, fp_percent],
                            [fn_percent, tp_percent]])

    return conf_matrix, percentages


def accuracy(y_true, y_pred):
    """Computes the accuracy."""
    return np.mean(y_true == y_pred)

def precision(y_true, y_pred):
    """Computes the precision."""
    true_positives = np.sum((y_true == 1) & (y_pred == 1))
    false_positives = np.sum((y_true == 0) & (y_pred == 1))
    if true_positives + false_positives == 0:
        return 0.0 #handle division by zero
    return true_positives / (true_positives + false_positives)

def recall(y_true, y_pred):
    """Computes the recall."""
    true_positives = np.sum((y_true == 1) & (y_pred == 1))
    false_negatives = np.sum((y_true == 1) & (y_pred == 0))
    if true_positives + false_negatives == 0:
        return 0.0 #handle division by zero
    return true_positives / (true_positives + false_negatives)

def f1_score(y_true, y_pred):
    """Computes the F1 score."""
    prec = precision(y_true, y_pred)
    rec = recall(y_true, y_pred)
    if prec + rec == 0:
        return 0.0 #handle division by zero
    return 2 * (prec * rec) / (prec + rec)

# Example usage
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
y_pred = np.array([1, 1, 1, 0, 0, 1, 1, 0, 1, 0])

conf_matrix = confusion_matrix(y_true, y_pred)
acc = accuracy(y_true, y_pred)
prec = precision(y_true, y_pred)
rec = recall(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("Confusion Matrix:\n", conf_matrix)
print("Accuracy:", acc)
print("Precision:", prec)
print("Recall:", rec)
print("F1 Score:", f1)