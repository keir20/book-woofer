import streamlit as st
import streamlit.components.v1 as components

st.markdown('Hope all goes well!')

components.html(
    '''
        <iframe src="https://open.spotify.com/embed/playlist/7xOHp3ZlSBJNJOgsQwF85S" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
    ''',
    height=600
)