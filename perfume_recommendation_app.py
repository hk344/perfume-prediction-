import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics.pairwise import euclidean_distances
import joblib

# Load the model and label encoder
model = joblib.load('perfume_prediction_model.pkl')
le = joblib.load('label_encoder.pkl')

# Define a function to compute the distance between the user input and each perfume
def compute_distances(user_input):
    # Encode the user input
    encoded_input = le.transform([user_input])
    
    # Compute the distance between the user input and each perfume in the dataset
    distances = euclidean_distances(encoded_input.reshape(1, -1), model.feature_importances_.reshape(1, -1))
    
    return distances

def recommend_perfume(user_input):
    # Compute the distances between the user input and each perfume in the dataset
    distances = compute_distances(user_input)
    
    # Get the index of the closest perfume
    closest_index = distances.argmin()
    
    # Get the predicted perfume name
    predicted_perfume = le.inverse_transform([closest_index])[0]
    
    return predicted_perfume

# Create a dictionary to map the input values to their respective feature names
input_features = {
    'Gender': ['Male', 'Female'],
    'Frequency': ['Subtle', 'Balanced', 'Strong'],
    'Fragrance': ['Leathery', 'Fresh', 'Floral', 'Fruity', 'Sweet', 'Woody', 'Aromatic', 'Oriental']
}

# Create the web application using Streamlit
def main():
    st.title('Perfume Recommendation')
    st.write('Please provide your preferences below:')
    
    # Create input fields for gender, frequency, and fragrance
    gender = st.selectbox('Gender', input_features['Gender'])
    frequency = st.selectbox('Frequency', input_features['Frequency'])
    fragrance = st.selectbox('Fragrance', input_features['Fragrance'])
    
    # Create a button to generate perfume recommendation
    if st.button('Generate Recommendation'):
        user_input = f"{gender}-{frequency}-{fragrance}"
        predicted_perfume = recommend_perfume(user_input)
        
        st.write('Based on your inputs, we recommend trying this perfume:')
        st.write(predicted_perfume)

if __name__ == '__main__':
    main()
