
# coding: utf-8

# In[26]:

import pandas as pd
import math

def roundoff():
	df=pd.read_csv('/home/somit/elucidata/upload/static/mass_spec_data.csv')
	df.head()


	i=0

	a=[]

	while i<df.shape[0]:
	    t=df.iloc[i]['Retention time (min)']
	    t+=0.5
	    t=math.floor(t)
	    a.append(t)
	    i+=1
	    
	#print a    
	df['RoundedOffTime']=a

	#print df.iloc[0]
	print df.shape


	# In[28]:

	#df.to_csv("NewDataset.csv",index=False)
	return df

