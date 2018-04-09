
# coding: utf-8

# In[17]:

import pandas as pd
import math

def findmean():
	df=pd.read_csv('/home/somit/elucidata/upload/static/Roundoff_Dataset.csv')
	df.head()


	# In[18]:

	cols=df.columns
	#print cols
	cols=cols[3:]
	#print cols
	#print len(cols)

	df=df[cols]
	#print df.head()
	a=sorted(df['RoundedOffTime'].unique())

	df2=pd.DataFrame(columns=cols)
	for e in a:
	    print e
	    df1=df.loc[df['RoundedOffTime']==e]
	    b={}
	    for c in cols:
	        t=df1[c].mean()
	        b[c]=t
	    print b
	    df2=df2.append(b,ignore_index=True)   
	    
	#print df2.head()


	# In[19]:

	# df2.to_csv("MeanValues.csv",index=False)
	return df2

