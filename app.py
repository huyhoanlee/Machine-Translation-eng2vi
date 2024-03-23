import streamlit as st
import requests
import http.client

# Streamlit UI
st.title("Machine Translation with FastAPI")

text = st.text_input('Enter text: ', 'Hello')

if text is not None:
    # Display the uploaded image
    st.write(text)

    host = "127.0.0.1"
    port = 8000
    # Set up the connection
    conn = http.client.HTTPConnection(host, port)

    # Set the headers
    headers = {'Content-type': 'text/plain'}
    if st.button('Translate'): 
        # Send a POST request to the /text endpoint
        try:
            conn.request("GET", "/text", body=text, headers=headers)
            
            # Get the response
            response = conn.getresponse()
            ans = response.read().decode()
            st.success(ans)

        except Exception as e:
            print(f"Error sending request: {str(e)}")
        finally:
            # Close the connection
            conn.close()


# import streamlit as st
# import requests

# # Streamlit UI
# st.title("Machine Translation with FastAPI")

# # Text input field
# text = st.text_input('Enter text:', 'Hello')

# if st.button('Translate'):  # Button to trigger translation
#     # Make a request to the FastAPI endpoint for translation
#     url = "http://127.0.0.1:8000/translator/"  # Make sure FastAPI is running on port 8000
#     data = {"text": text}  # Send text as a form field
#     response = requests.post(url, data=data)
#     st.write(response)
#     if response.status_code == 200:
#         result = response.json()
#         translated_text = result
#         st.success(f"Translated: {translated_text}")
#     else:
#         st.error("Translation failed. Please try again.")
