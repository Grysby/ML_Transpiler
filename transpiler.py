from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import joblib

def train_and_save():
    iris = load_iris()
    X = iris.data[:, :2]
    y = (iris.target != 0 ) * 1

    model = LinearRegression() # construction d'un objet de Régression logistique
    model.fit(X, y) # Entrainement du modèle
    
    joblib.dump(model, "model_lin_iris.joblib")

def transpile(path : str, test_pred):
  model = joblib.load(path)

  str_theta = "{ "
  thetas = []
  thetas.append(model.intercept_)
  for i in model.coef_:
    thetas.append(i)
  for i in range(len(thetas) - 1):
    str_theta += str(thetas[i]) + ", "
  str_theta += str(thetas[-1]) + " }"

  str_test_pred = "{ "
  for i in range(len(test_pred) - 1):
    str_test_pred += str(test_pred[i]) + ", "
  str_test_pred += str(test_pred[-1]) + " }"

  
  code =  f"""#include <stdio.h>

float thetas[] = {str_theta};

float linear_regression_prediction(float *features, int n_features) {{\n
    float res = {thetas[0]};
    
    for (int i = 0; i < n_features; i++) {{
        res += features[i] * thetas[i + 1];
    }}
    
    return res;
}}

int main() {{
    float to_pred[] = {str_test_pred};
    printf("Prediction: %lf\\n", linear_regression_prediction(to_pred, 2));
}}
"""
  print("Code generated")
  f = open("linear_reg.c", "w")
  f.write(code)
  print("Use gcc linear_reg.c")
  print("Use ./a.out")
