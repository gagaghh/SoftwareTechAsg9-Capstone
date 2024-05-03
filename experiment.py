import tkinter as tk
from machinelearning import funcPrediction



mlmodel = tk.Tk()
mlmodel.title("Predict Gold Prices")
    

def quitter():
    quit()

tk.Button(mlmodel,text="Continue").grid(row=4)
tk.Button(mlmodel,text="Exit",command=quitter).grid(row=4, column=1)

def perform_prediction():
    try:
        input_value = float(input_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number!")
        return
    
    prediction_result = funcPrediction(input_value)

    result_label.config(text=f"Prediction: {prediction_result[0]}")

input_label = tk.Label(mlmodel, text="Input Value:")
input_label.grid(row=3, column=0)
input_entry = tk.Entry(mlmodel)
input_entry.grid(row=3, column=1)

prediction_button = tk.Button(mlmodel, text="Predict", command=perform_prediction)
prediction_button.grid(row=4, column=1)

result_label = tk.Label(mlmodel, text="")
result_label.grid(row=5, columnspan=2)

mlmodel.mainloop()