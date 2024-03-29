

import streamlit as st
import pandas as pd

import pip 
#pip.main(["install","matplotlib"])
#pip.main(["install","numpy"])
#pip.main(["install","plotly_express"])
pip.main(['install', 'matplotlib'])
pip.main(['install', 'plotly'])
pip.main(['install', 'plotly_express'])


#pip.main(['install', 'openpyxl'])


#excel=pd.read_excel('APROBADOS.xlsx',engine = 'openpyxl')


#import plotly.express as px

#import matplotlib.pyplot as plt
import numpy as np

st.title("FUNNEL ACTIVACASH 2.0 :sunglasses:")
#df=pd.read_excel('PROCESOS_PIVOTE.xlsx')

#st.write(excel)


#df_2=pd.read_csv('APROBADOS.csv')
#st.write(df_2)

st.markdown(f':cry: Estos socios estan caidos en el proceso, hay que mandarles wattsapp para que terminen:') 

df=pd.read_csv('PROCESOS_PIVOTE.csv',encoding='latin-1')
st.write(df)

#st.markdown(f'*Resultados Disponibles:{numero_resultados}*') 


st.markdown(f':sweat_smile: Estos socios si terminaron el proceso jajaja:') 


df2=pd.read_csv('APROBADOS.csv',encoding='latin-1')
st.write(df2)


st.markdown(f':neutral_face: Estos socios fueron rechazados:') 


df3=pd.read_csv('RECHAZADOS.csv',encoding='latin-1')
st.write(df3)




import pandas as pd

df = pd.DataFrame({
  "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
  "Contestant": ["Alex", "Alex", "Alex", "Jordan", "Jordan", "Jordan"],
  "Number Eaten": [2, 1, 3, 1, 3, 2],
})




# Graph Objects

import plotly.graph_objects as go

fig = go.Figure()
for contestant, group in df.groupby("Contestant"):
    fig.add_trace(go.Bar(x=group["Fruit"], y=group["Number Eaten"], name=contestant,
      hovertemplate="Contestant=%s<br>Fruit=%%{x}<br>Number Eaten=%%{y}<extra></extra>"% contestant))
fig.update_layout(legend_title_text = "Contestant")
fig.update_xaxes(title_text="Fruit")
fig.update_yaxes(title_text="Number Eaten")
fig.show()





import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)



import plotly.express as px
data = dict(
    number=[39, 27.4, 20.6, 11, 2],
    stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])
fig = px.funnel(data, x='number', y='stage')
#fig.show()


st.plotly_chart(fig) # de esta forma se va a mostrar el dataframe en Streamlit






import pandas as pd

df = pd.DataFrame({
  "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
  "Contestant": ["Alex", "Alex", "Alex", "Jordan", "Jordan", "Jordan"],
  "Number Eaten": [2, 1, 3, 1, 3, 2],
})


# Plotly Express

import plotly.express as px

fig_2 = px.bar(df, x="Fruit", y="Number Eaten", color="Contestant", barmode="group")
#fig_2.show()
st.plotly_chart(fig_2)





###########
###########
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))