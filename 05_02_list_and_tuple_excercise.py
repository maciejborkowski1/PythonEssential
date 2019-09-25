marketing = ['loyality program', 'client promotion', 'market reserch']
marketing.append('public relations')
marketing.insert(1,'investor relations')

emailMarketing = marketing.copy()
emailMarketing.sort()

internalEmails = ['internal communication']

emailMarketing.extend(internalEmails)

newTupleList = tuple(emailMarketing)

print(marketing[2])

print(marketing)
print(emailMarketing)
print(internalEmails)
print(newTupleList)
