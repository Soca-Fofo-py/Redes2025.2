import sys
Host_default = '127.0.0.1'
Port_default = 20000

print("Argv: ", sys.argv,"Len: ",len(sys.argv))
if len(sys.argv) == 2:
    try:
        host , port = sys.argv[1].split(":")
    except: sys.exit("Entrada invalida, isira IP:PORTA no seguinte formato: 127.0.0.1:23000")
elif len(sys.argv) == 1:
    host , port = Host_default , Port_default
else:
    sys.exit("Entrada invalida, isira IP:PORTA no seguinte formato: 127.0.0.1:23000")
    
print(f"Final, Host: {host}, Porta: {port}")