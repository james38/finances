"""
Question types to ask users.
"""

def ask_binary_qx(qx):
    ans = ""
    while ((ans == "a") | (ans == "b")) is not True:
        ans = input(qx)
        if ans == "a":
            pass
        elif ans == "b":
            pass
        else:
            print("Please enter either a or b")
    return ans
