import numpy as np
import matplotlib.pyplot as plt

class LinearRegression():
    def __init__(self):
        self.J_history = []

    def computecost(self,X, y):
        J = 0
        m = max(y.shape)
        #X = np.concatenate((np.ones((m,1)), X), axis=1)
        prediction = np.dot(X,self.theta)
        sq_error = (prediction - y)**2
        J = 1/(2*m) * np.sum(sq_error)
        return J

    def fit(self,X, y, alpha=0.01, iterations=1500, return_prams=False):
        m = max(y.shape)
        X = np.concatenate((np.ones((m,1)), X), axis=1)
        n = min(X.shape)
        self.theta = np.zeros((n,1))
        #J_history = []
        for i in range(0, iterations):
            error = np.dot(X, self.theta) - y
            self.theta = self.theta - ((alpha/m) * np.dot(X.T, error))
            J = self.computecost(X, y)
            self.J_history.append(J)

        self.J_history = np.asarray(self.J_history)
        self.J_history = self.J_history.reshape(iterations, 1)
        #print(self.J_history.shape)
        if return_prams ==True:
            return self.J_history, self.theta


    def plotdata(self, X, y,title="Title", X_label="X-axis", y_label="Y-axis"):
        plt.scatter(X, y, color = 'red')
        plt.title(title)
        plt.xlabel(X_label)
        plt.ylabel(y_label)
        plt.show()

    def plotregressor(self, X, y,title="Title", X_label="X-axis", y_label="Y-axis"):
        m = max(y.shape)
        x = X
        X = np.concatenate((np.ones((m,1)), X), axis=1)
        plt.scatter(x, y, color = 'red')
        plt.plot(x, np.dot(X, self.theta), color = 'blue')
        plt.title(title)
        plt.xlabel(X_label)
        plt.ylabel(y_label)
        plt.show()

    def plotcost(self):
        random = np.asarray(list(range(0, max(self.J_history.shape))))
        plt.plot(random, self.J_history, color = 'blue')
        plt.title("cost function")
        plt.xlabel("Iterations")
        plt.ylabel("Cost value")
        plt.show()


