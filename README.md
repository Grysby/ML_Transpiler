# ML_Transpiler
Transpiler of a linear reg from python to C

#Install

Use 

```
pip install joblib
pip install scikit-learn
```

# How to use it

- We can use the function ***train_and_save*** to train and save the model on
a joblib file. This model can only be train on the iris dataset.
- Now just use the ***transpile*** function and specify the path of the
  joblibfile and the values you want to predict. Here it would be :

```
  transpile(path/to/file.joblib, [2.5, 5.5])
``` 

