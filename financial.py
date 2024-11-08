import pickle
import streamlit as st
import numpy as np

# loading the saved model
financial_model = pickle.load(open('C:/Users/tejas/OneDrive/Desktop/financial risk/financial risk/model.sav', 'rb'))

# sidebar for navigation

# Enroachment detection in IOT devices
def home_page():
    st.title("Home Page")
    st.image("financial.jpg")
    st.write("Welcome to the Financial risk forecast analysis based on deep learning considering the data collection from different sources")

def prediction_page():
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Date = st.text_input('Date')

        credit_card = st.text_input('credit_card')

        online_payment = st.text_input('online_payment')

        Stock_price = st.text_input('Stock_price')

        Interest_rate = st.text_input('Interest_rate')

        Exchange_rate = st.text_input('Exchange_rate')

        Economic_Indicator = st.text_input('Economic_Indicator')

    # code for Prediction
    financial_prediction = ''

    # creating a button for Prediction
    if st.button('Financial risk  prediction Result'):
        # Use the user input for model prediction
        # Convert input to a numerical format (e.g., float)
        credit_card = float(credit_card)
        online_payment = float(online_payment)
        Stock_price = float(Stock_price)
        Interest_rate = float(Interest_rate)
        Exchange_rate = float(Exchange_rate)
        Economic_Indicator = float(Economic_Indicator)
        
        # Reshape the input data into a 2D array
        input_data = np.array([credit_card, online_payment, Stock_price, Interest_rate, Exchange_rate, Economic_Indicator]).reshape(1, -1)
        
        # Make prediction using the reshaped input data
        financial_prediction = financial_model.predict(input_data)
        
        # Display the prediction result
        if financial_prediction == 0:
            st.success('No financial risk detected.')
            st.write('Recommendation: Continue monitoring the financial situation.')
        else:
            st.error('Financial risk detected!')
            st.write('Recommendation: Take necessary actions to mitigate the financial risk.')

def about_page():
    st.title("About")
   
    st.write("Welcome to Our Financial risk forecast analysis based on deep learning considering the data collection from different sources Project.")
    st.write("# **About the Project**")
    st.write("""Our project is dedicated to the detection of encroachment in Internet of Things (IoT) devices. We focus on ensuring the security and integrity of IoT networks by identifying and preventing unauthorized access or intrusion attempts.""")
    st.write("# **Key Objectives**")
    st.write("### **Real-time Detection**")
    st.write("""Our primary objective is to develop a system that can detect encroachment or suspicious activities in real-time within IoT devices. This proactive approach enhances the security posture of IoT networks.""")
    st.write("### **Enhance Device Security**")
    st.write("""We aim to enhance the overall security of IoT devices by identifying and mitigating potential threats. This involves analyzing network traffic, monitoring device behavior, and detecting patterns indicative of encroachment.""")
    st.write("### **Utilize Machine Learning**")
    st.write("""By leveraging advanced Machine Learning models, we seek to create a robust encroachment detection system. Machine Learning algorithms allow us to learn from historical data and adapt to emerging threats in the dynamic IoT landscape.""")
    st.write("### **Findings and Impact**")
    st.write("""Our research findings contribute to the field of IoT security by providing effective encroachment detection mechanisms. Detecting and preventing encroachment is crucial for maintaining the confidentiality, integrity, and availability of IoT devices and networks.""")
    st.write("# **Financial Risk Forecast Analysis**")
    st.write("""We also specialize in Financial risk forecast analysis based on deep learning considering the data collection from different sources. Our expertise in this area allows us to provide valuable insights and predictions to help organizations make informed decisions and mitigate financial risks.""")
    st.write("# **Get Involved**")
    st.write("""Excited about the potential of securing IoT devices and analyzing financial risks? Join us on our journey as we explore innovative solutions in encroachment detection and financial risk analysis. Engage with our community, share your expertise, and together, let's build a more secure and resilient future.""")
    st.write("# **Contact Us**")
    st.write("""Have questions or want to learn more about our project? Contact our team at kasarlajhansi07@gmail.com and let's start a conversation about how we can collaborate to drive innovation in IoT security and financial risk analysis.""")


# Replace "your-email@example.com" with the actual email address for contact.

# Streamlit app
def main():
    # Set color and size for the sidebar title
    st.sidebar.markdown("<h1 style='color: blue; font-size: 24px;'>Financial risk forecast analysis based on deep learning considering the data collection from different sources</h1>", unsafe_allow_html=True)

    # Create the radio button
    page = st.sidebar.radio(" ", ["Home", "Prediction Page", "About"])

    if page == "Home":
        home_page()
    elif page == "Prediction Page":
        prediction_page()
    elif page == "About":
        about_page()

if __name__ == "__main__":
    main()
