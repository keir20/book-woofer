import streamlit as st
import tensorflow as tf
from book_woofer.predict import *

st.title('books and woofers')

# imported = load_model('../models/model3')
# model = keras.models.load_model('../models/model3/saved_model.pb')
#------------------------------------------------------
#   functions 
#------------------------------------------------------

model, tokenizer = load_the_model()

user_input = st.text_input('Enter a sentence : ')

predict(str(user_input))

#------------------------------------------------------
#   streamlit 
#------------------------------------------------------

#------------------------------------------------------

#------------------------------------------------------
#   models
#------------------------------------------------------

#------------------------------------------------------

# predict(str(input('Enter a sentence : ')))

# if __name__=="__main__":
    
    #predict('Hi there this is a nheew test sentence and it is scary, model, tokenizer', model, tokenizer)
    