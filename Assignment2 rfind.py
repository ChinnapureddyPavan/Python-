def index_rigth_side(string,check_string):
    i=len(string)-len(check_string)
    for j in range(i,-1,-1):
        if string[j:j+len(check_string)]==check_string:
            return j
    return -1
string="pavankumarvan"
check_string="rvaa"
print(index_rigth_side(string,check_string))
