import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class Covid19:
    def __init__(self):
        pass

    def app(self):
        st.header("Example covid")
        filename = st.file_uploader("Set filename", type="csv")
        if filename is not None:
            data = pd.read_csv(filename)
            st.write(data.head())
            index_col = st.selectbox("Pick up index column in your dataframe", options=data.columns)
            data = data.set_index(index_col)
            st.write(data.index)

            unique_values = data.index.unique()
            default_values = ['KAZ', 'USA']
            for value in default_values:
                if value not in unique_values:
                    unique_values = list(unique_values)
                    unique_values.append(value)

            selected_countries = st.multiselect("Select countries", options=unique_values, default=default_values)
            filtered_data = data[data.index.isin(selected_countries)]

            date_col = st.selectbox("Pick the date column for the X-axis", options=data.columns, index=data.columns.get_loc('date'))
            filtered_data[date_col] = pd.to_datetime(filtered_data[date_col])

            value_col = st.selectbox("Pick the column for the Y-axis", options=data.columns, index=data.columns.get_loc('total_cases'))

            fig, ax = plt.subplots(figsize=(10, 6))
            for country in selected_countries:
                country_data = filtered_data[filtered_data.index == country]
                ax.plot(country_data[date_col], country_data[value_col], label=country)

            ax.set_xlabel("Date")
            ax.set_ylabel("Cases")
            ax.set_title(f"{value_col} Over Time for Selected Countries")
            ax.legend()
            st.pyplot(fig)

Covid19_instance = Covid19()
Covid19_instance.app()