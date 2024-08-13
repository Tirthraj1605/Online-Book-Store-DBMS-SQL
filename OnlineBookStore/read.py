import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data


def read():
    result = view_all_data()
    # st.write(result)
    df_books = pd.DataFrame(result, columns=['BookId','Title','Author','Price','Quantity'])
    df_carts = pd.DataFrame(result, columns=['Cartid','UserId','BookId','Quantity'])
    df_users = pd.DataFrame(result, columns=['UserId','Username','Password'])
    with st.expander("books"):
        st.dataframe(df_books)
    with st.expander("users"):
        st.dataframe(df_users)
    with st.expander("carts"):
        st.dataframe(df_carts)
