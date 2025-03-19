import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Adrian's Dashboard: First Dashboard")
st.sidebar.title('Want to know more:')
section = st.sidebar.radio('Go to:', ['Home', 'Data Table', 'Bar Chart'])
data = pd.DataFrame({'Category': ['A', 'B', 'C', 'D'], 'Values': [23, 17, 35, 29]})
if section == 'Home':
   st.write('Welcome to the dashboard! please select a seciton from the sidebar.')
   st.write('The Next Line')

elif section == 'Data Table':
     st.subheader('Bar Chart')
     fig, ax = plt.subplots()
     ax.bar_xlabel('Category')
     ax.set_ylabel('Values')
     st.plot(fig)

import os
os.system('streamlit run "C:/Shindagha Documents/SEM 2/advance_lytics/adrian_spyder.py"')
import streamlit as st
import pandas as pd

st.title("Adrian's First Dashboard")


data = pd.DataFrame({'Category': ['A', 'B', 'C', 'D'], 'Values': [23, 17, 35, 29]})

tab1, tab2, tab3 = st.tabs(['Home', 'Data Table', 'Bar Chart'])

with tab1: 
    st.write('Welcome to the dashboard! Please select a tab above.')


with tab2:
    st.subheader('Data Table')
    st.write(data)

with tab3:
    st.subheader('Bar Chart')
    st.bar_chart(data.set_index('Category'))