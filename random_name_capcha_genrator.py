
# coding: utf-8

# In[ ]:


import string,random


# In[ ]:


letter=""
def name(a):
    temp=[]
    for i in a:
        if i=="vo":
            temp.append(random.choice(vovels))
        elif i=='co':
            temp.append(random.choice(consonent))
        elif i=='nu':
            temp.append(str(random.randint(0,9)))
        else:
            temp.append(i)
    return temp
        


# In[ ]:


vovels="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"


# In[ ]:


user_input=list(input("""To genrate a random capcha or name please follow these steps.
1. Please enter "vo" for "Vovels" "co" for "Consonents" and "nu" for "number".
2. Plese enter the values space saperated.
3. If You enter the value of ur chose just enter it as u have entered "vo","co","nu"
4. And Do not Enter "nu" in case of name because common sence.
5. After u have enterded last digit press enter do not give space after it.""").split(" "))


# In[ ]:


atempts=int(input("How many time u wana genrate the capcha or name"))


# In[ ]:


for i in range(atempts):
    print("".join(name(x)))

