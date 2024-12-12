import streamlit as st
from streamlit_lottie import st_lottie

class Home:
    def __int__(self):
        pass
    def app(self):
        with st.container():
            lottie_animation = "https://lottie.host/91be4f3b-2f30-4b1f-bb78-5acfb14060f7/4P4uMo4mp1.json"
            st.subheader('Hi, my name is Aikyn')
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.write("##")
                st.write("I make music and you can find my song in all platforms")
                st.write(
                        """
                        My favorite artists is:
                        - Ken Carson
                        - Destroy Lonely
                        - Playboi Carti
                        - Travis Scott
                        - Che
                        """
                )
                st.write("and more opium songs")
                st.write("[My Spotify](https://open.spotify.com/artist/6M7tZTg2MGpXU4mtVWo4CU)")
            with right_column:
                st_lottie(lottie_animation, height=300, key="coding")
                st.image("img/usa.png")
