
# coding: utf-8

# This is a Project i made to incrypt a string by using key this program took the user input in form of string and then uses the user key to perform encrypting operation on that string for eg. if u enter string "Hello" and key 20 you will get out put as "Byffi".This program only encrypt A-Z a-z and 0-9 only.

# In[15]:


User_input=input()
d=list(User_input)
key=int(input())
z=[]


# In[16]:


for i in d:
    z.append(ord(i))


# In[17]:


temp=[]
for i in z:
    if i>96 and i<123:
        if (i + key%26)>122:
            temp.append(i-26+key%26)
        else:
            temp.append(i+key%26)
    elif i>64 and i<91:
        if (i + key%26)>90:
            temp.append(i-26+key%26)
        else:
            temp.append(i+key%26)
    elif i>47 and i<58:
        if (i + key%10)>57:
            temp.append(i-10+key%10)
        else:
            temp.append(i+key%10)
    else:
        temp.append(i)


# In[18]:


output=[]
for i in temp:
    output.append(chr(i))


# In[19]:


result=""
result="".join(output)


# In[20]:


print(result)

