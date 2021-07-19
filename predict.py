import numpy as np
import pickle

def predict(pregnancies, glucose, bloodpressure, skinthikness, insulin,bmi,dpfunc,age,model_name):
    filename = model_name+".sav"
    #Loading the model from local storage
    model = pickle.load(open(filename,"rb"))
    y_pred= model.predict(
        np.array([
            [
                pregnancies, 
                glucose, 
                bloodpressure, 
                skinthikness, 
                insulin,
                bmi,
                dpfunc,
                age]]))
    
    return y_pred[0]