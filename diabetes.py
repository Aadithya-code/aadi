import streamlit as st
import pickle 
import os
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Medical Analysis",layout="wide",page_icon="LIFE")

working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(f'{working_dir}/diabetes.pkl','rb'))


NewBMI_Overweight = 0
NewBMI_Underweight = 0
NewBMI_Obesity_1 = 0
NewBMI_Obesity_2 = 0 
NewBMI_Obesity_3 = 0
NewInsulinScore_Normal = 0
NewGlucose_Low = 0
NewGlucose_Normal = 0 
NewGlucose_Overweight = 0 
NewGlucose_Secret = 0 
with st.sidebar:
   selected = option_menu("Medical Analysis",
                ['Diabetes Prediction'
                 ],
                 menu_icon='Medical-fill',
                 icons=['activity' ],
                 default_index=0)

if selected == 'Diabetes Prediction':
   st.title("Diabetes Prediction Using Machine Learning")
   
   col1,col2,col3 = st.columns(3)

   with col1 :
      Pregnancies= st.text_input("Number Of Pregnancies")
   with col2 :
     Glucose = st.text_input("Glucose Level")
   with col3 :
     BloodPressure = st.text_input("BloodPressure Value") 
   with col1:
     SkinThickness = st.text_input("SkinThickness Value")
   with col2:
     Insulin =  st.text_input("Insulin Value")
   with col3:
     BMI = st.text_input("BMI Value")
   with col1:
      DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction Value")
   with col2:
     Age = st.text_input("Age")   
   diabetes_result = ""
   if st.button("Diabetes Test Result"):
      if float(BMI)<=18.5:
         NewBMI_Underweight = 1
      elif 18.5 < float(BMI) <=24.9:
         pass
      elif 24.9<float(BMI)<=29.9:
         NewBMI_Overweight = 1 
      elif 29.9<float(BMI)<=34.9:
        NewBMI_Obesity_1=1
      elif 34.9<float(BMI)<=39.9:
        NewBMI_Obesity_2=1
      elif float(BMI)>39.9:
         NewBMI_Obesity_3=1

      if 16<=float(Insulin)<=166:
         NewInsulinScore_Normal = 1

      if float(Glucose)<=70:
         NewGlucose_Low = 1 
      elif 70<float(Glucose)<=99:
         NewGlucose_Normal = 1
      elif 99<float(Glucose)<=126:
         NewGlucose_Overweight = 1
      elif float(Glucose)>126:
         NewGlucose_Secret = 1         

      user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,
                     NewBMI_Underweight,NewBMI_Overweight , NewBMI_Obesity_1 ,NewBMI_Obesity_2 ,NewBMI_Obesity_3 ,
                 NewInsulinScore_Normal ,NewGlucose_Low ,NewGlucose_Normal , 
                 NewGlucose_Overweight,NewGlucose_Secret ,]
      
      user_input = [float(x) for x in  user_input]
      prediction = diabetes_model.predict([user_input])
      if prediction[0]== 1:
         diabetes_result = "The Person Is Diabetic"
      else:
         diabetes_result = "The Person Is Not Diabetic"
   st.success (diabetes_result )      