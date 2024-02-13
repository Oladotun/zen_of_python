## Not beautiful
x = 10
y = 20 

z = x + y if x < y else x - y

print(z)

'''
Apparently the above code is not beautiful because it lacks readability.
To add readability to code, we should break into the following steps below
'''

if x < y:
    z = x + y
else:
    z = x - y

print(z)

'''
The above code is easier to read, even though we use more steps.
The only question I have, is that is this not breaking the nested principle?

So staying flat without being nested
'''