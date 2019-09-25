countryLeaders={'PL':'Duda','US':'Trump','DE':'Merkel'}
#print(countryLeaders.setdefault('FR','Macron'))

#print(countryLeaders.get('DE'))

newLeaders={'RU':'Putin','DE':'Schulz'}
countryLeaders.update(newLeaders)
print(countryLeaders)
