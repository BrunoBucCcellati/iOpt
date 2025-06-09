import numpy as np
import iOpt

import catboost as cb
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def objective(trial):

    data, target = load_breast_cancer(return_X_y=True)
    train_x, valid_x, train_y, valid_y = train_test_split(data,
                                                          target,
                                                          test_size=0.3)

    param = {
        "colsample_bylevel":
        trial.suggest_float("colsample_bylevel", 0.01, 0.1),
        "depth":
        trial.suggest_int("depth", 1, 12),
        "objective":
        trial.suggest_discrete("objective", ["Logloss", "CrossEntropy"]),
        "boosting_type":
        trial.suggest_discrete("boosting_type", ["Ordered", "Plain"]),
        "bootstrap_type":
        trial.suggest_discrete("bootstrap_type",
                               ["Bayesian", "Bernoulli", "MVS"]),
        "used_ram_limit":
        "16gb"
    }

    if param["bootstrap_type"] == "Bayesian":
        param["bagging_temperature"] = trial.suggest_float(
            "bagging_temperature", 0, 10)
    elif param["bootstrap_type"] == "Bernoulli":
        param["subsample"] = trial.suggest_float("subsample", 0.1, 1)

    gbm = cb.CatBoostClassifier(**param)

    gbm.fit(train_x,
            train_y,
            eval_set=[(valid_x, valid_y)],
            verbose=0,
            early_stopping_rounds=100)

    preds = gbm.predict(valid_x)
    pred_labels = np.rint(preds)
    accuracy = accuracy_score(valid_y, pred_labels)
    return accuracy


if __name__ == "__main__":
    study = iOpt.create_study()
    study.optimize(objective=objective,
                   solver_parameters=iOpt.SolverParameters(
                       r=5, eps=0.001, iters_limit=100, refine_solution=True))


    study.best_float_params()
    study.best_discrete_params()
    study.best_values()
