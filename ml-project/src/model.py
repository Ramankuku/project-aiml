import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib


def build_model(X_train, X_test, y_train, y_test):

    rf = RandomForestClassifier(random_state=42)

    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20, 25],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2]
    }

    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=5,
        scoring='accuracy',
        n_jobs=-1
    )

    mlflow.set_experiment("Random_Forest_GridSearch")

    with mlflow.start_run():

        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_
        y_pred = best_model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        mlflow.log_params(grid_search.best_params_)

        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)


        # 7. Log model
        mlflow.sklearn.log_model(best_model, "random_forest_model")
        #joblib
        joblib.dump(best_model, 'RandomForest.joblib')

        print("Best Parameters:", grid_search.best_params_)
        print("Accuracy:", accuracy)

    return best_model
