import streamlit as st

def recommend_perfume():
    st.title("Perfume Recommendation App")
    
    gender = st.selectbox("Select your gender", ["Male", "Female"])
    frequency = st.selectbox("Select the frequency of use", ["Subtle", "Balanced", "Strong"])
    fragrance = st.selectbox("Select your fragrance preference", ["Leathery", "Fresh", "Floral", "Fruity", "Sweet", "Woody", "Aromatic", "Oriental"])

    if st.button("Get Perfume Recommendation"):
        # Perform your perfume prediction based on the user inputs
        # You can use the existing code for perfume prediction here
        
        # Display the recommended perfume
        st.success("Based on your inputs, we recommend trying this perfume: [Perfume Name]")
        
# Run the perfume recommendation app
if __name__ == "__main__":
    recommend_perfume()
