import streamlit as st
import plotly.express as px
from controller import get_data

st.title("Next Days Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}.")

if place:
    try:
        # Call the api to get the data based  on the type chosen
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure= px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        elif option == "Sky":
            images = {"Clear": "resources/clear.png" , "Clouds": "resources/cloud.png" ,
                    "Rain": "resources/rain.png", "Snow": "resources/clear.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115 )


            # images = {"Clear": "resources/clear.png" , "Clouds": "resources/cloud.png" ,
            #         "Rain": "resources/rain.png", "Snow": "resources/clear.png"}
            # sky_conditions = [dict["weather"][0]["description"] for dict in filtered_data]
            # # image_paths = [images[condition] for condition in sky_conditions]
            # if "clear" in sky_conditions:
            #     st.image(images["Clear"])
            # elif "clouds" in sky_conditions:
            #     st.image(images["Clouds"])
            # elif "snow" in sky_conditions:
            #     st.image(images["Snow"])
            # elif "rain" in sky_conditions:
            #     st.image(images["Rain"])
    except KeyError:
        st.write("Sorry, the city name you entered is not valid, please either correct its spelling or use a valid city name.")
