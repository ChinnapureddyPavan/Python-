def index_rigth_side(string,check_string):
    i=len(string)-len(check_string)
    for j in range(i,-1,-1):
        if string[j:j+len(check_string)]==check_string:
            return j
            break
string="pavankumarvan"
check_string="rv"
print(index_rigth_side(string,check_string))
