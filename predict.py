import pickle
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
​
​
def load_the_model():
    model = keras.models.load_model('/Users/christophersparrow/code/keir20/book-woofer/API/model3')
    with open('/Users/christophersparrow/code/keir20/book-woofer/API/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    print ('model loaded')
    return model, tokenizer
  
    
def predict(sentence):
    model, tokenizer = load_the_model()
    sentence_lst=[]
    sentence_lst.append(sentence)
    sentence_seq=tokenizer.texts_to_sequences(sentence_lst)
    sentence_padded=pad_sequences(sentence_seq,maxlen=1000,padding='post')
    ans=model.predict(sentence_padded)
    print("The emotion predicted is",ans)
    
if __name__=="__main__":
    #model, tokenizer = load_the_model()
    #predict('Hi there this is a nheew test sentence and it is scary, model, tokenizer', model, tokenizer)
    predict(str(input('Enter a sentence : ')))