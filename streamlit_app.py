import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Visualisasi Dataset dengan Pilihan Grafik")

# Input untuk mengunggah file dataset
uploaded_file = st.file_uploader("https://raw.githubusercontent.com/ffzs/dataset/refs/heads/master/insurance.csv", type=["csv"])

# Memeriksa apakah file telah diunggah
if uploaded_file is not None:
    # Membaca dataset
    df = pd.read_csv(uploaded_file)

    # Menampilkan dataset
    st.write("Dataset:")
    st.dataframe(df)

    # Pilihan grafik
    chart_type = st.selectbox(
        "Pilih jenis grafik", 
        ["Line Chart", "Bar Chart", "Area Chart"]
    )

    # Checkbox untuk memilih kolom yang ingin ditampilkan
    columns = df.columns.tolist()
    selected_columns = []
    
    st.write("Pilih kolom yang ingin ditampilkan:")
    for column in columns:
        if st.checkbox(column):
            selected_columns.append(column)

    # Menampilkan grafik untuk setiap kolom yang dipilih
    if selected_columns:
        for column in selected_columns:
            st.subheader(f"Grafik untuk kolom: {column}")
            
            if chart_type == "Line Chart":
                st.line_chart(df[column])
            elif chart_type == "Bar Chart":
                st.bar_chart(df[column])
            elif chart_type == "Area Chart":
                st.area_chart(df[column])

else:
    st.write("Silakan unggah file dataset untuk memulai.")
