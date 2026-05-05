from gtts import gTTS
import streamlit as st
import queue
#membuat visualisasi queue dari 
st.title("antrian klinik sederhana")
st.write("ini adalah aplikasi antrian klinik sederhana")

#inisialisasi state untuk menyimpan data 
if  "antrian" not in st.session_state:
    st.session_state.antrian = queue.Queue()
#contoh penggunaan GTTS
text = "selamat datang di kelas a"
tts = gtts.gTTS(text=text, lang="id")
tts.save("output.mp3")


#contoh play
playsound.playsound("output.mp3")

if antrian 