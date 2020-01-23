def Decimal_To_Binary(n):
    result=""
    while n!=0:
        result+=str(n%2)
        n/=2
    print 'tu numero binario es',result[::-1]
def Binary_To_Decimal(m):
    	u=str(m)
	i=len(u)
	result=0
	for element in u:
		z=int(element)
		result=result+int(z*(2**(i-1)))
		i-=1
	print 'tu numero decimal es', result
programa=True
while programa:
    print 'Bienvenido al programa para transformar Decimal y Binario'
    if raw_input("Responde decimal para pasar de decimal a binario o responde binario para pasar de binario a decimal: ")=="decimal":
        Decimal_To_Binary(int(raw_input("Introduzca su numero decimal: ")))
    else:
        Binary_To_Decimal(int(respuesta))
    print 'Gracias por usar el programa :D'
    if raw_input("Desea transformar otro numero(yes para continuar o no para cancelar): ")== 'yes':
        if raw_input("Desea pasar de binario a decimal o de decimal a binario: ")=="decimal":
            Decimal_To_Binary(int(raw_input("Introduzca su numero decimal: ")))
            print "Gracias por usar el programa. Hasta la proxima!"
        else:
            Binary_To_Decimal(int(raw_input("Introduce tu numero binario: ")))
            print "Gracias por usar el programa. Hasta la proxima!"
    else:
        print "Adios, hasta la proxima!"
        programa=False