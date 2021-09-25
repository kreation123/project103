import pandas as pd
import plotly.express as ex
df = pd.read_csv('Copy+of+data+-+data.csv')
figuer= ex.line(df, x ='date', y='cases' ,color='country' )
figuer.show()