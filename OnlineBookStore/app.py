import streamlit as st
from create import create
from read import read
from update import update
from delete import delete
from database import create_table, close

def main():
    st.title("eBike App")
    menu = ["Insert XML data","View all tables","Update","Delete"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Insert XML data":
        st.subheader("Enter Dealer Details:")
        create()

    elif choice == "View all tables":
        st.subheader("View all tables")
        read()

    elif choice == "Update":
        st.subheader("Update created tasks")
        update()

    elif choice == "Delete":
        st.subheader("Delete created tasks")
        delete()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
    



