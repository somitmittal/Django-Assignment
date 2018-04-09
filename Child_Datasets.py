
# coding: utf-8

# In[108]:

import pandas as pd


def child_dataset():
	df=pd.read_csv('/home/somit/elucidata/upload/static/mass_spec_data.csv')
	df.head()


	# In[107]:

	#print list(df.columns.values)


	# In[117]:

	i=0


	pc=pd.DataFrame(columns=list(df.columns.values))
	lpc=pd.DataFrame(columns=list(df.columns.values))
	plasma=pd.DataFrame(columns=list(df.columns.values))
	# print pc

	#print df['Accepted Compound ID'].isnull().sum()
	# print df['Accepted Compound ID'].describe()

	#print df['Accepted Compound ID'].isnull().sum()
	#df=df['Accepted Compound ID'].fillna("A")



	while i<df.shape[0]:
	    cmp_id=df.iloc[i]['Accepted Compound ID']   
	    cmp_id=str(cmp_id)
	    l=len(cmp_id)
	    if l>=2 and cmp_id[l-2:l]=='PC' and cmp_id[l-3:l]!='LPC':
	        pc=pc.append(df.iloc[i],ignore_index=True)
	    elif len >=3 and cmp_id[l-3:l]=='LPC':  
	        lpc=lpc.append(df.iloc[i],ignore_index=True)
	    elif l>=11 and cmp_id[l-len("plasmalogen"):l]=="plasmalogen":
	        plasma=plasma.append(df.iloc[i],ignore_index=True)  
	    i+=1

	# print pc.shape
	# print lpc.shape
	# print plasma.shape



	# In[118]:

	pc.to_csv("PC_Compound.csv",index=True)
	lpc.to_csv("LPC_Compound.csv",index=True)
	plasma.to_csv("Plasmalogen_Compound.csv",index=True)

	return pc,lpc,plasma

