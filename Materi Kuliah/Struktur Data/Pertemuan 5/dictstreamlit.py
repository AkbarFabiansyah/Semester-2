<<<<<<< HEAD
import streamlit as st

st.title("📊 Aplikasi Dictionary")
st.subheader("🔄️ Hitung Kata dalam Paragraf")

textInput = st.text_area("Masukkan Paragraf", height=200)

if st.button("Hitung Analisis"):
    words = textInput.lower().split()
    count = {}

    for word in words:
        count[word] = count.get(word, 0) + 1

    st.subheader("Hasil Analisis")
    st.write(count)
=======
import streamlit as st

st.title("📊 Aplikasi Dictionary")
st.subheader("🔄️ Hitung Kata dalam Paragraf")

textInput = st.text_area("Masukkan Paragraf", height=200)

if st.button("Hitung Analisis"):
    words = textInput.lower().split()
    count = {}

    for word in words:
        count[word] = count.get(word, 0) + 1

    st.subheader("Hasil Analisis")
    st.write(count)
>>>>>>> 825fc310cdea392d93ae14421ae3cc8c573059d0
    st.bar_chart(count)