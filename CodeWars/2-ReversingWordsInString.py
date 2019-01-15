s = ("Hello World")
a = s.split()
a.reverse()
result = " ".join(a)
print(result)

OR

def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)
