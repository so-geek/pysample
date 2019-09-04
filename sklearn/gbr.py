# 参考サイト
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
# http://techtipshoge.blogspot.com/2015/07/scikit-learn5-gradient-boosting.html
# https://qiita.com/flystaslingan40/items/439a463f018239a98be6
# https://opendatagroup.github.io/Knowledge%20Center/Tutorials/Gradient%20Boosting%20Regressor/

# %% ボストンの住宅価格読込
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt

data = load_boston()
x = data['data']
y = data['target']
train_x, test_x, train_y, test_y = train_test_split(x, y)

# %% 学習
model = GradientBoostingRegressor()

parameters = {
    'learning_rate': [0.13, 0.1, 0.07, 0.05],
    'max_depth': [4, 6, 8],
    'min_samples_leaf': [3, 5, 9],
    'max_features': [1.0, 0.5, 0.3]
}

grid_search_cv = GridSearchCV(
    model,
    parameters,
    verbose=10,
    n_jobs=-1,
    cv=4
)
grid_search_cv.fit(train_x, train_y)

print("best index=", grid_search_cv.best_index_)
print("best score=", grid_search_cv.best_score_)
print("best params=", grid_search_cv.best_params_)
print("best estimator=", grid_search_cv.best_estimator_)

# %% 推定
estimator = grid_search_cv.best_estimator_
estimated_y = estimator.predict(test_x)

fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(range(test_y.size), test_y, label="test_y")
ax.scatter(range(estimated_y.size), estimated_y, label="estimated_y")
ax.legend()
