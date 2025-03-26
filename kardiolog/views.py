from django.shortcuts import render 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score 
import pandas as pd 

def index(request): 
	return render(request, "index.html") 

def predict(request): 
	return render(request, "predict.html")

def kontakt(request):
    return render(request, 'kontakt.html')

def o_nama(request):
    return render(request, 'o_nama.html')

def preventiva(request):
    return render(request, 'preventiva.html') 

def blog(request):
    return render(request, 'blog.html') 


def result(request): 
	dataframe = pd.read_csv("venv/heart_2020_cleaned.csv") 
	dataframe['Smoking']=dataframe['Smoking'].replace({'Yes':1,'No':0})
	dataframe['AlcoholDrinking']=dataframe['AlcoholDrinking'].replace({'Yes':1,'No':0})
	dataframe['Stroke']=dataframe['Stroke'].replace({'Yes':1,'No':0})
	dataframe['DiffWalking']=dataframe['DiffWalking'].replace({'Yes':1,'No':0})
	dataframe['Sex']=dataframe['Sex'].replace({'Male': 1, 
								'Female': 0})
	dataframe['AgeCategory']=dataframe['AgeCategory'].replace({'18-24':0,'25-29':1,'30-34':2,'35-39':3,'40-44':4,'45-49':5,'50-54':6,'55-59':7,'60-64':8,'65-69':9,'70-74':10,'75-79':11,'80 or older':12})
	 
	dataframe['Race']=dataframe['Race'].replace( {'American Indian/Alaskan Native': 0, 'Asian': 1, 'Black': 2, 'Hispanic': 3, 'Other': 4, 'White': 5}) 
	dataframe['Diabetic']=dataframe['Diabetic'].replace({'No':0,'No, borderline diabetes': 0.25,'Yes':0.75,'Yes (during pregnancy)':1})
	dataframe['PhysicalActivity']=dataframe['PhysicalActivity'].replace({'No':1,'Yes':0})
	dataframe['GenHealth']=dataframe['GenHealth'].replace({'Poor':4,'Fair':3,'Good':2,'Very good':1,'Excellent':0})
	dataframe['Asthma']=dataframe['Asthma'].replace({'Yes':1,'No':0})
	dataframe['KidneyDisease']=dataframe['KidneyDisease'].replace({'Yes':1,'No':0})
	dataframe['SkinCancer']=dataframe['SkinCancer'].replace({'Yes':1,'No':0})
	dataframe['HeartDisease']=dataframe['HeartDisease'].replace({'Yes':1,'No':0})
	Y = dataframe["HeartDisease"] 
	X = dataframe.drop(["HeartDisease"], axis=1) 

	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1) 

	model = LogisticRegression(max_iter=1000) 
	model.fit(X_train, Y_train)
	inputs = {
        'n0': float(request.GET['n0']), 
        'n1': 1 if request.GET['n1'] == 'Yes' else 0,
        'n2': 1 if request.GET['n2'] == 'Yes' else 0,
        'n3': 1 if request.GET['n3'] == 'Yes' else 0,
		'n3_1': float(request.GET['n3_1']),
		'n3_2': float(request.GET['n3_2']),
		'n4': 1 if request.GET['n4'] == 'Yes' else 0,
        'n5': 1 if request.GET['n5'] == 'Male' else 0,
        'n6': AgeMapping(request.GET['n6']),  
        'n7': RaceMapping(request.GET['n7']), 
        'n8': DiabetesMapping(request.GET['n8']),  
        'n9': 1 if request.GET['n9'] == 'Yes' else 0,
        'n10': HealthMapping(request.GET['n10']),  
        'n11': float(request.GET['n11']),  
        'n12': 1 if request.GET['n12'] == 'Yes' else 0,
        'n13': 1 if request.GET['n13'] == 'Yes' else 0,
        'n14': 1 if request.GET['n14'] == 'Yes' else 0,
    }

	feature_order = ['n0', 'n1', 'n2', 'n3', 'n3_1', 'n3_2', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13', 'n14']
	input_values = [inputs[feature] for feature in feature_order]
	
	pred = model.predict([input_values]) 

	result1 = "" 
	if pred == [0]: 
		result1 = "Rezultati našeg algoritma ne ukazuju na prisustvo srčanih problema. Međutim, preporučujemo Vam da nastavite sa zdravim životnim navikama i redovnim medicinskim pregledima."
	else: 
		result1 = "Rezultati našeg algoritma ukazuju na moguću prisutnost srčanih problema. Preporučujemo da se obratite ljekaru za detaljniji pregled."

	return render(request, "predict.html", 
				{"result2": result1}) 

def AgeMapping(age_str):
    return {
        '18-24': 0, '25-29': 1, '30-34': 2, '35-39': 3,
        '40-44': 4, '45-49': 5, '50-54': 6, '55-59': 7,
        '60-64': 8, '65-69': 9, '70-74': 10, '75-79': 11,
        '80 or older': 12
    }.get(age_str, 0)  

def RaceMapping(race_str):
    return {
        'White': 5, 'Black': 2, 'Asian': 1,
        'American Indian/Alaskan Native': 0,
        'Other': 4, 'Hispanic': 3
    }.get(race_str, 5) 

def DiabetesMapping(diabetes_str):
    return {
        'No': 0, 'Yes': 0.75, 'No, borderline diabetes': 0.25,
        'Yes (during pregnancy)': 1
    }.get(diabetes_str, 0) 

def HealthMapping(health_str):
    return {
        'Excellent': 0, 'Very good': 1, 'Good': 2,
        'Fair': 3, 'Poor': 4
    }.get(health_str, 2)  