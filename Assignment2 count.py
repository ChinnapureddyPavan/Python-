def count_substring(string,sub):
    count=0
    sub_len=len(sub)
    
    for i in range(len(string)-sub_len+1):
        if string[i:i+sub_len]==sub:
            count+=1
    return count
string="pavanpavankumar"
sub="pavan"
print(count_substring(string,sub))
