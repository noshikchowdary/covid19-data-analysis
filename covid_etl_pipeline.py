import requests 
import pandas as pd 

url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)
data= response.json()

df=pd.DataFrame(data)


#transform 
columns_needed=['country','cases','deaths','recovered','active','population']
# After sorting or cleaning, reset the index

df_clean=df[columns_needed]
df_sorted= df_clean.sort_values(by='cases',ascending=False)
df_sorted = df_sorted.reset_index(drop=True)


df_sorted['cases_per_million']=(df_sorted['cases']/ df_sorted['population'])*1_000_000
df_sorted['death_rate']=(df_sorted['deaths']/df_sorted['cases'])*100
df_sorted['recovery_rate']=(df_sorted['recovered']/df_sorted['cases']*100)
top_cases=df_sorted.sort_values('cases_per_million',ascending=False).head(10)
top_deaths=df_sorted.sort_values('death_rate', ascending=False).head(10)
top_recovery_rate=df_sorted.sort_values('recovery_rate',ascending=False).head(10)
 
import matplotlib.pyplot as plt 

plt.figure(figsize=(10,6))
plt.bar(top_cases['country'],top_cases['cases_per_million'], color='skyblue')
plt.title('Top 10 Countries by COVID-19 Cases per Million People')
plt.xlabel('country')
plt.ylabel('cases per million')
plt.xticks(rotation=45)
plt.tight_layout()


plt.figure(figsize=(8,8))
plt.pie(
    top_deaths['death_rate'], 
    labels=top_deaths['country'], 
    autopct='%1.1f%%', 
    startangle=140,
    colors=plt.cm.Reds(range(50, 50 + len(top_deaths)*10, 10))
)
plt.title('Top 10 Countries by COVID-19 Death Rate')
plt.tight_layout()
plt.show()


