
# Constants
eps0 = 8.854e-12
K = 1 # Aire, ...

def genCapacitanciaSerie(c1, *c2):
  C = c1 * c2[0] / (c1 + c2[0])
  if(len(c2) > 1): return genCapacitanciaSerie(C, *c2[1:])
  return C

def genCapacitanciaParalela(c1, *c2): 
  C = c1 + c2[0]
  if(len(c2) > 1): return genCapacitanciaParalela(C, *c2[1:])
  return C

def getVoltage(q, c):
  return q / c

def getCarga(c, v):
  return c * v

def genResistenciaSerie(c1, *c2):
  C = c1 + c2[0]
  if(len(c2) > 1): return genResistenciaSerie(C, *c2[1:])
  return C

def genResistenciaParalela(c1, *c2):
  C = c1 * c2[0] / (c1 + c2[0])
  if(len(c2) > 1): return genResistenciaParalela(C, *c2[1:])
  return C

def getVoltageR(r, i):
  return r * i

def getCorriente(v, r):
  return v / r

def getPotencia(v=None,i=None,r=None):
  if(v and i):
    return v * i
  if(i and r):
    return r * i**2
  if(v and r):
    return v**2 / r
  raise Exception


"""
# Unidades
 - Q se mide en [C]
 - C se mide en [F]
 - V se mide en [V]
 - R se mide en [Ω]
 - I se mide en [A]
 - P se mide en [W]

# Formulas
 - Q = C * V
 - E = C * V * V / 2 = Q**2 / (2 * C)
 - C = Area * eps0 * K / d --> Capacitancia de placa con un area. K depende del material
 - V = R * I
 - P = V * I = R * I**2 = V**2 / R

# Cosas a recordar

Capacitores en serie: se mantiene Q

Capacitores en paralelo: se mantiene V

Resistencias en serie: se mantiene I

Resistencias en paralelo: se mantiene V

Los resultados funcionan si trabajas con C, N y m. Asi que saca al pingo los micrones y esas cosas

Tablita de la suerte

mili => 1e-3
micro => 1e-6
nano => 1e-9
pico => 1e-12

"""

def ejercicio1():
  print('Cuek')

def ejercicio2():
  V = 90
  Cs1 = genCapacitanciaSerie(3e-6, 6e-6)
  Cs2 = genCapacitanciaSerie(2e-6, 4e-6)
  C = genCapacitanciaParalela(Cs1, Cs2)
  print('Capacidad del sistema', C)
  Qs1 = getCarga(Cs1, V)
  Qs2 = getCarga(Cs2, V)
  V1 = getVoltage(Qs1, 3e-6)
  V2 = getVoltage(Qs1, 6e-6)
  V3 = getVoltage(Qs2, 2e-6)
  V4 = getVoltage(Qs2, 4e-6)
  print("V =", V1, V2, V3, V4)
  print("Q =", Qs1,Qs1,Qs2,Qs2)
  E = C * V * V / 2
  print("Energia total", E)

def ejercicio3():
  A = 0.00075
  d = 0.00119
  V = 12
  C = 2 * A * eps0 * K / d
  print('La capacitancia del sistema P1, P2, P3 es', genCapacitanciaParalela(C, C))
  Q = getCarga(genCapacitanciaParalela(C, C), V)
  print('La carga en P2 es', Q)
  print('La capacitancia del sistema P1, P2, P3, P4 es', genCapacitanciaParalela(C, C, C))
  print('La carga en P4 es', getCarga(C, V))

def ejercicio4():
  C1 = 10e-6
  C2 = 5e-6
  C3 = 4e-6

  C1C2 = genCapacitanciaParalela(C1, C2)
  C1C2C3 = genCapacitanciaSerie(C1C2, C3)

  Q = getCarga(C1C2C3, 100)
  V12 = getVoltage(Q, C1C2)
  Q1 = getCarga(C1, V12)
  Q2 = getCarga(C2, V12)
  V3 = getVoltage(Q, C3)
  print('Q =', Q1, Q2, Q)
  print('V =', V12, V12, V3)

  print('===============')

  C1C2 = genCapacitanciaSerie(C1, C2)
  C1C2C3 = genCapacitanciaParalela(C1C2, C3)

  Q = getCarga(C1C2C3, 100)
  Q12 = getCarga(C1C2, 100)
  Q3 = getCarga(C3, 100)
  V1 = getVoltage(Q12, C1)
  V2 = getVoltage(Q12, C2)
  print('Q =', Q12, Q12, Q3)  
  print('V =', V1, V2, 100)

def ejercicio5():
  R2 = 2
  I1 = 5
  I2 = 4
  # V = (R1 + R2) * I2
  # V = (R1) * I1
  R1 = I2 * R2 / (I1 - I2)
  print('El valor de la resistencia original es', R1)

def ejercicio6():
  R1, R2, R3, R4 = 1, 2, 3, 4
  V = 18

  R13 = genResistenciaParalela(R1, R3)
  R1234 = genResistenciaSerie(R13, R2, R4)
  I1234 = getCorriente(V, R1234)
  V13 = getVoltageR(R13, I1234)
  I1 = getCorriente(V13, R1)
  I3 = getCorriente(V13, R3)

  print('Resistencia equivalente', R1234)
  print('I =', I1, I1234, I3, I1234)
  print('P =', getPotencia(i=I1,r=R1), getPotencia(i=I1234,r=R2), getPotencia(i=I3,r=R3), getPotencia(i=I1234,r=R4))
  print('Potencial total =', getPotencia(i=I1234, r=R1234))

  print('(1+C)/C =', getPotencia(i=I1234, r=R1234) / V**2, '\b, Absurdo para C no negativo!')

def ejercicio7():
  print('Carusito, acordate que la carga se conserva')
  print('Ergo, Q0 = QC(t) + Q3C(t)')
  print('Tambien acordate que en el equilibrio, los voltajes son iguales')
  print('Ergo, VC = V3C')
  print('Hace cuentas magicas dividiendo y multiplicando por C esas ecuaciones')
  print('Recorda que la energia en el resistor es la energia inicial (Q0**2/(2*C)) - las energias finales en los capacitores')

def ejercicio8():
  C1, C2 = 3e-6, 6e-6
  R1, Ri = 5, 1
  V = 12
  Cs = genCapacitanciaSerie(C1, C2)
  Rt = genResistenciaSerie(R1, Ri)
  print('Constante de tiempo = ', Rt * Cs)
  print('La medida de rapidez con que se carga / descarga un capacitor')
  Qs = getCarga(Cs, V)
  V2 = getVoltage(Qs, C2)
  print('Voltaje del capacitor de 6e-6F =', V2)

  print('============')
  Ct = genCapacitanciaParalela(C1, C2)
  print('Constante de tiempo = ', Rt * Ct)
  print('Voltaje del capacitor de 6e-6F =', V)

ejercicio8()