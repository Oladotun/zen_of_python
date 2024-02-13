'''
Simple is better than complicated in python suggests than we always go for the most simplistic solutions.
The following example highlights that
'''
# TODO: try with time it
# timeit
# complicated approach
def reverse(myStr):
    if myStr:
        return reverse(myStr[1:]) + myStr[0]
    else:
        return myStr
    
print(reverse("drink water please"))
print("In the above approach, a more complicated approach, " 
      "have been utilized to generate the reverse algorithm")

# more simple using python built-in functionality

def reverse_short(myStr):
    return myStr[::-1]

print(reverse_short("drink water please"))
print("In the above approach, one line of code was used to generate the code" )

# learning continues here: https://www.codeconquest.com/blog/the-zen-of-python-explained-with-examples/