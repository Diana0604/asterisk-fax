global_var = "global hello"

def local():
    local_var = "local hello"

    print(local_var)
    print(global_var)
    global_var = "new global hello"

local()

print(global_var)