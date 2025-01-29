def replace_substring(original,old,new):
    result=""
    i=0
    while i<len(original):
        if original[i:i+len(old)]==old:
            result=result+new
            i=i+len(old)
        else:
            result=result+original[i]
            i=i+1
    return result
original="pavankumar"
old="pavan"
new="kumar"
print(replace_substring(original,old,new))
