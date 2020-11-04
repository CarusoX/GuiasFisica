from math import pi as PI, sin, cos, sqrt

# Constants
eps0 = 8.854e-12
K = 1 / (4 * PI * eps0)
Qe = 1.602217653e-19 # Carga del electron o del proton
mp = 1.673e-27 # masa proton 
mn = 1.675e-27 # masa neutron
me = 9.109e-31 # masa electron
g = 9.81

def getEnergyFromQandD(q, d):
  return abs(K * q / d**2)

def getForceFromQandE(q, E):
  return abs(q * E)

def getPotencialFromQandD(q, d):
  return K * q / d

def degreeToRad(alfa):
  return alfa * PI / 180

"""
# Unidades
- E se mide en [N / C]
- F se mide en [N]
- Q se mide en [C]
- V se mide en [N * m / C] o en [J / C]
- W se mide en [J]

# Formulas
 - |F| = m a
 - |F| = Q |E|
 - |E| = K * |Q| / d**2
 - V = K * Q / d
 - Psi = Qenc / eps0 = oint_ E dA (Integrar sobre el area del cuerpo que encierra teniendo en cuenta el vector energia)

# Cosas a recordar
De la energia, solo sabemos el modulo, dibujar para saber la direccion

De la fuerza, solo sabemos el modulo, dibujar y recordar que si `q` es negativo, cambia el sentido

El potencial electrico tiene signo

Los resultados funcionan si trabajas con C, N y m. Asi que saca al pingo los micrones y esas cosas

Tablita de la suerte

mili => 1e-3
micro => 1e-6
nano => 1e-9
pico => 1e-12

"""

def ejercicio1():
  E = getEnergyFromQandD(-4*10**-9, .12)
  F = getForceFromQandE(Qe, E)
  print(E, F)

def ejercicio2():
  Q1 = 1e-6
  Q2 = -2e-6
  Q3 = 3e-6
  D = .5
  E1 = getEnergyFromQandD(Q2, D) - getEnergyFromQandD(Q3, 2*D)
  E2 = getEnergyFromQandD(Q1, D) - getEnergyFromQandD(Q3, D)
  E3 = getEnergyFromQandD(Q1, 2*D) - getEnergyFromQandD(Q2, D)
  F1 = getForceFromQandE(Q1, E1)
  F2 = getForceFromQandE(Q2, E2)
  F3 = getForceFromQandE(Q3, E3)
  V1 = getPotencialFromQandD(Q2, D) + getPotencialFromQandD(Q3, 2*D)
  V2 = getPotencialFromQandD(Q1, D) + getPotencialFromQandD(Q3, D)
  V3 = getPotencialFromQandD(Q1, 2*D) + getPotencialFromQandD(Q2, D)
  print('|F| =', F1, F2, F3)
  print('|E| =', E1, E2, E3)
  print('V =', V1, V2, V3)

def ejercicio3():
  L = .15
  m = 3e-2
  tita = degreeToRad(5)
  a = sin(tita) * L
  P = m * g
  Px = sin(tita) * P
  F = Px / cos(tita)
  Q = sqrt(F * (2*a)**2 / K)
  print(Q)

def ejercicio4():
  Q = 3e-6
  L = .25
  diagonal = sqrt(L**2+L**2)
  Ex = getEnergyFromQandD(Q, diagonal / 2) + getEnergyFromQandD(Q, diagonal / 2)
  Ey = getEnergyFromQandD(Q, diagonal / 2) + getEnergyFromQandD(Q, diagonal / 2)
  print('E (con ejes rotados 45) = ', [Ex, Ey])
  print('E (sin rotar)', [sqrt(Ex**2+Ey**2), 0])
  print('Una carga positiva se moveria hacia la derecha con una fuerza:', sqrt(Ex**2+Ey**2)*Q)
  print('La energia en el punto medio deja de ser horizontal')


def ejercicio5():

  # Esta es la forma posta
  def getEnergy(Q1, Q2, a, b, alfa, beta, r1, r2):
    alfa, beta = degreeToRad(alfa), degreeToRad(beta)
    E1 = getEnergyFromQandD(Q1, r1)
    E1x, E1y = E1 * cos(alfa), E1 * sin(alfa)
    E2 = getEnergyFromQandD(Q2, r2)
    E2x, E2y = E2 * cos(beta), - E2 * sin(beta)
    return E1x + E2x, E1y - E2y
  
  # Si a == b entonces r1 == r2 y ademas alfa = beta
  # Por lo tanto E1y == E2y, E2x == E2y
  # Entonces el resultado es
  print("E = [2 * getEnergyFromQandD(Q, r1) * cos(alfa), 0]")

def ejercicio6():
  Q = 3.2e-19
  m = 6.68e-30 # kg
  T = 2e-6 # segundos
  D = .05 # metros
  # El campo electrico es contante, por lo tanto tenemos aceleracion constante -> formulita x0 + v0 * t + 1/2 * accel * t**2
  accel = 2 * D / T**2 # m / s**2
  F = m * accel
  E = F / Q # F = Q * E
  print('E =', [E, 0])
  print('W =', F * D)
  print('V =', - F * D / Q)

def ejercicio7():
  v = 3e6
  E = 200
  h = 0.015
  L = .1
  F = -Qe * E
  a = F / me # F = m * a
  # Como la velocidad es vertical, x0 = v0 = 0
  tiempo_hasta_el_piso = sqrt(-h / a * 2)
  dis_hor = tiempo_hasta_el_piso * v
  if(dis_hor >= L): print('La particula escapa')
  else: print('La particula choca en:', dis_hor)

def ejercicio8():
  print('Cuek')

def ejercicio9():
  Q = 1.5e-8
  V = 30
  d = K * Q / V
  print('Radio con 30V:', d)
  d1 = d * K * Q / (d + K * Q)
  d2 = d1 * K * Q / (d1 + K * Q)
  print('Notar que las distancias', [d, d1, d2], "producen:")
  print([getPotencialFromQandD(Q, d), getPotencialFromQandD(Q, d1), getPotencialFromQandD(Q, d2)])
  print('Pero d - d1 =', d - d1, '!=', d1 - d2, '= d1 - d2')
  print('Respuesta, no :)')

def ejercicio10():
  dv = 1 / 4 # Cuentitas faciles
  de = 1 / (1 + sqrt(3))
  print('V = 0 en', dv)
  print('E = 0 en', de)

def ejercicio11():
  print('Carga puntual rodeada por cordon => E = Q / (eps0 * 2 * PI * r)')
  print('Carga puntual rodeada por cascaron 3D => E = Q / (eps0 * 4 * PI * r**2)')
  print('Cascaron esferico delgado y conductor de radio R y carga uniforme Q => E = Q / (eps0 * 4 * PI * r**2)')
  print('Linea infinita de carga con densidad lineal lambda => E = lambda / (2 * PI * eps0 * r) ')
  print('Plano infinito de carga con densidad superficial lambda => E = lambda / (2 * eps0) ')
  
  
def ejercicio12():
  print('Flujo en S1 = (Q - 2Q) / eps0')
  print('Flujo en S2 = (Q - Q) / eps0')
  print('Flujo en S3 = (Q - Q - 2Q) / eps0')
  print('Flujo en S4 = (0) / eps0')

def ejercicio13():
  pass

def ejercicio14():
  pass

ejercicio9()

