import pickle 
import streamlit as st
model1=pickle.load(open('titanic2.pkl','rb'))

def myf1():
    st.title("Survival Prediction on Titanic Dataset")
    pclass=st.number_input("Enter class of the passenger(1,2,3)", min_value=1, max_value=3, step=1)
    age=st.number_input("Enter age of the passenger", min_value=0.0)
    gender=st.number_input("Enter 1 if Male, Enter 0 if Female", min_value=0, max_value=1, step=1)
    pred=st.button("Predict")
    if pred:
        op=model1.predict([[pclass,age,gender]])
        if op[0]==1:
            st.write("The Passenger is :green['Survived']")
        else:
            st.write("The Passenger is :red['Not Survived']")
    else:
            st.error("Please fill out all fields correctly before predicting..")
    
myf1()