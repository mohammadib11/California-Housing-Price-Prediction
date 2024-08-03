def GetPrediction(model, inputs : list) :
    PredictionResult = model.predict([inputs])
    return PredictionResult