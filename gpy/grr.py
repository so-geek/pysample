# 参考サイト
# http://statmodeling.hatenablog.com/entry/how-to-use-GPy

# %%
import GPy
import numpy as np
import matplotlib.pyplot as plt

# %% 訓練データ作成
np.random.seed(seed=123)
N = 50
X = np.random.uniform(-3., 3., (N, 2))
Y = np.sin(X[:, 0:1]) * np.sin(X[:, 1:2]) + np.random.randn(N, 1)*0.05

# %% モデル学習
kernel = GPy.kern.Matern52(2, ARD=True)
model = GPy.models.GPRegression(X, Y, kernel)
model.optimize(messages=True, max_iters=1e5)

# %% モデル可視化 等高線で三次元描写する場合
model.plot()

# %% モデル可視化 x[0] = -1.0 の場合
model.plot(fixed_inputs=[(0, -1.0)], plot_data=False)

# %% 予測
x_pred = np.array([np.linspace(-3, 3, 100), np.linspace(3, -3, 100)]).T
y_qua_pred = model.predict_quantiles(x_pred, quantiles=(2.5, 50, 97.5))[0]
