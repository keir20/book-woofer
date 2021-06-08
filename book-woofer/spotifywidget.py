import streamlit as st
import streamlit.components.v1 as components

st.title('hello world')

def select_and_play(feeling):
    happy = 'https://open.spotify.com/playlist/556ICk4gRzDknRfWGeQ3x1?si=317b09e2dc4b45f3'
    sad = 'https://open.spotify.com/playlist/0dRxDrR1PfZMlVbfnuBRbR?si=1c1095aff5cf4b24'
    anger = 'https://open.spotify.com/playlist/7FjP7MbRgFYFdv5avuhiBI?si=4289f7bbaa1243af'
    enthusiasm = 'https://open.spotify.com/playlist/4JsAKbWk4AoBcfpSs2afOM?si=d578284db05845ca'
    empty = 'https://open.spotify.com/playlist/77OpFLSdLy3nC9huQIXlxk?si=205fa8c2b1d24e8d'
    boredom = 'https://open.spotify.com/playlist/2rA0wLILuvNuLhAacn4kth?si=9ec06d60f5b14c53'
    worry = 'https://open.spotify.com/playlist/5Dt93qIXccZvZbU6r3oIbs?si=061a1e6b521b422f'
    love = 'https://open.spotify.com/playlist/73KuPUAtOecLDAetRn80TW?si=dda2764abcde4498'
    surprise = 'https://open.spotify.com/playlist/0BaRZECQEqp4zDd0Njzlj1?si=d943c1a27fec45df'
    fun = 'https://open.spotify.com/playlist/7HwdXmzNKXBzTAisOKYVsJ?si=6f73860860db49d1'
    relief = 'https://open.spotify.com/playlist/2zaAFRdI6lEaX8Esc11XPZ?si=b4ea70e95eca4506'
    hate = 'https://open.spotify.com/playlist/6vdOF3ZRqiYimqEm4lk98V?si=eb11df3e48b44e4e'
    neutral = 'https://open.spotify.com/playlist/5pSdjjPHbXpbqFJGf31Ksn?si=8a2e9c4bf0e04ef5'

    d= {'happy':happy, 'sad':sad, 'worry':worry, 'love':love, 
        'anger':anger, 'fun':fun, 'relief': relief, 'empty':empty,
        'hate':hate, 'enthusiasm':enthusiasm, 'surprise':surprise,
        'boredom':boredom, 'neutral':neutral
       }
    
    mood = d[feeling]

    return components.html(
            f'<iframe src={mood} width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>',
            height=600
            )

# components.html(
#     '''
#         <iframe src="https://open.spotify.com/embed/playlist/7xOHp3ZlSBJNJOgsQwF85S" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
#     ''',
#     height=600
# )