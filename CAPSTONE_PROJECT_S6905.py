#!/usr/bin/env python
# coding: utf-8

# # INSTALLATION PART

# In[5]:


pip install pymysql


# In[6]:


import pymysql


# In[7]:


pip install pandas


# In[4]:


pip install mysql-connector


# In[8]:


pip install matplotlib


# In[6]:


pip install seaborn


# # CONNECTION PART:

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql
import mysql.connector


# In[10]:


connection = pymysql.connect(
    host ="localhost",
    user="root",
    password="#Sunder7502",
    database="crime"
)


# In[11]:


cursor = connection.cursor()


# # BASIC STATISTICS ON THE DATASET

# In[12]:


cursor.execute("select * from crime_data")
rows = cursor.fetchall()

for row in rows:
    print(row)


# In[34]:


sql_vic = cursor.execute('select Vict_Age, count(*) as crime_count from crime_data group by Vict_Age;')
rows = cursor.fetchall()
for row in rows:
    print(row)


# In[13]:


df = pd.read_csv('crime_data.csv')


# In[14]:


df.head()


# In[37]:


df.shape


# In[38]:


df.info()


# In[39]:


df.describe()


# # ANALYSIS PART 
# QUESTIONS:

# # 1. Spatial Analysis:
#   Question:
#   1.Where are the geographical hotspots for reported crimes?

# In[15]:


Q1= ('select LAT, LON, count(*) as Number_of_crime from crime_data group by LAT, LON order by Number_of_crime desc;')


# In[96]:


cursor.execute(Q1)


# In[17]:


df1 = pd.read_sql_query(Q1, connection)


# In[18]:


df1.head()


# In[20]:


plt.figure(figsize=(10,5))
sns.scatterplot(x='LON', y='LAT', data =df1,label=map)
plt.title('GEOGRAPHICAL CRIME HOTSPOT')
plt.legend()
plt.show()


# # 2. VICTIM DEMOGRAPHICS:
#     QUESTION -Victim Demographics:
# 
# What is the distribution of victim ages in reported crimes?
# 
# Is there a significant difference in crime rates between male and female victims?

# In[16]:


q2=('select Vict_Age, count(*) as crime_count from crime_data group by Vict_Age order by Crime_count_Reported desc limit 10;')


# In[56]:


cursor.execute(q2)


# In[100]:


df2= pd.read_sql_query(q2, connection)


# In[61]:


type(df2)


# In[101]:


df2.head()


# In[102]:


sns.barplot(x="Vict_Age", y="crime_count", data =df2)
plt.title("AGE DISTRIBUTION")
plt.show()


# # 2B.Is there a significant difference in crime rates between male and female victims?
# 

# In[21]:


Q3 =('select Vict_Sex AS GENDER, count(*) AS Crime_count, count(*) * 100.0 / sum(count(*)) OVER() AS Crime_rate_percentage from crime_data group by Vict_Sex;')


# In[22]:


cursor.execute(Q3)


# In[23]:


df3= pd.read_sql_query(Q3, connection)


# In[116]:


sns.barplot(x="GENDER", y="Crime_count", data = df3,hue="Crime_rate_percentage")
plt.title('Crime Rate between Male and Female')
plt.show()


# # 3. Location Based Analysis
# Location Analysis:
# 
# Where do most crimes occur based on the "Location" column?

# In[81]:


Q4=('select Location, count(*) as Most_Crime_no from crime_data group by Location order by Most_Crime_no desc limit 10;')


# In[82]:


cursor.execute(Q4)


# In[83]:


df4 = pd.read_sql_query(Q4, connection)


# In[84]:


df4


# In[85]:


plt.figure(figsize=(18,5))
sns.barplot(x="Location", y="Most_Crime_no", data =df4)
plt.title('LOCATION BASED CRIME')
plt.show()


# # 4.Crime Code Analysis:
# 
# What is the distribution of reported crimes based on Crime Code?

# In[86]:


Q5 =('select Crm_cd, count(Crm_cd) as Reported_Crime from crime_data group by Crm_Cd order by Reported_Crime desc limit 10;')


# In[87]:


cursor.execute(Q5)


# In[89]:


df5 = pd.read_sql_query(Q5, connection)


# In[90]:


df5


# In[92]:


plt.figure(figsize=(5, 15))
plt.pie(df5["Reported_Crime"], labels=df5["Crm_cd"], autopct ='%1.1f%%', startangle=90)
plt.title("CRIME DISTRIBUTION")
plt.show()


# # END
