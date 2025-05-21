import pandas as pd
import streamlit as st


df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv")

st.title("Bienvenue sur le site de Nathan")

df = df.fillna("NaN")
tiécar_options = pd.concat([df['pickup_borough'], df['dropoff_borough']]).unique()
tiécar_options = sorted(set(tiécar_options))  # suppression des doublons et tri


if "Staten Island" not in tiécar_options:
    tiécar_options.append("Staten Island")

tiécar = st.selectbox("Indiquez votre arrondissement de récupération", tiécar_options)

st.write(f"Tu as choisi : {tiécar}")


images = {
    "Manhattan": "https://assets3.thrillist.com/v1/image/1660860/1200x630/flatten;crop_down;webp=auto;jpeg_quality=70",
    "Queens": "https://www.nyc.fr/wp-content/uploads/2024/10/vue-aerienne_du_queens-scaled.jpg",
    "Bronx": "https://freedomforallamericans.org/wp-content/uploads/2024/07/Bronx-neighborhood-crime-rates.jpg",
    "Brooklyn": "https://api.time.com/wp-content/uploads/2011/12/r-young-brownsville7560.jpg",
    "Staten Island": "https://s.wsj.net/public/resources/images/OB-VE476_1031st_G_20121031142247.jpg"
}


if tiécar in images:
    st.image(images[tiécar], use_container_width=True)
else:
    st.image("https://fr.web.img6.acsta.net/c_310_420/pictures/23/09/01/18/03/4245127.jpg")
