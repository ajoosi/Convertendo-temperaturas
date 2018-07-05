c = int(input(' Informe a temperatura em °C:'))
f = ((9*c)/5) + 32
print('A temperatura de {} °C corresponde a {} °F!'.format(c,f))


print ('.')
print ('.')
print ('.')

fa = int(input(' Informe a temperatura em °F:'))
ce = ((fa-32)*5) /9
print('A temperatura de {} °F corresponde a {:.1f} °C!'.format(fa,ce))


