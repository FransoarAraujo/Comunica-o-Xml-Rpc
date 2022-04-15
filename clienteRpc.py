import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
num1 = float(input('Digite um número: \n'))
num2 = float(input('Digite outro numero \n'))

print("A Soma de:(",num1,"+",num2,") é:", s.add(num1,num2))
print("A Multiplicação de:(",num1,"X",num2,") é:", s.mul(num1,num2))
print("A Divisão de:(",num1,"/",num2,") é:", s.div(num1,num2))
print("A Subtração de:(",num1,"-",num2,") é:", s.sub(num1,num2))