from math import sin,cos,atan,atan2, pi as PI, sqrt

# Constants
Qe = 1.602217653e-19 # Carga del electron o del proton
mp = 1.673e-27 # masa proton 
mn = 1.675e-27 # masa neutron
me = 9.109e-31 # masa electron
m0 = 4 * PI * 1e-7 # T * m / A
g = 9.81

def getFuerzaCableConCorriente(I, l, B, tita):
  return I * l * B * sin(tita)

def getRadioCurvatura(m, v, q, B):
  return m * v / (abs(q) * B)

def getVelAng(v, R):
  return v / R

def degreeToRad(alfa):
  return alfa * PI / 180

def getCampoMagnetico(I, R):
  return m0 * I / (2 * PI * R)

def sumVectorPolar(r1, tita1, r2, tita2):
  r = sqrt(r1**2 + r2**2 + 2*r1*r2*cos(tita2-tita1))
  tita = tita1+atan2(r2*sin(tita2-tita1), r1+r2*cos(tita2-tita1))
  return (r, tita)

"""
# Unidades
 - B se mide en [T]

# Formulas
 - F = q * v x B -> La fuerza sobre una carga q que se mueve con velocidad v en un campo magnetico B
 - F = q.(E + v x B) -> La fuerza sobre una particula cargada que se mueve en una region donde existen campos electrico y magnetico
 - F = I * L * |B| * sin(tita) -> Fuerza sobre todas las cargas en un alambre de longitud l con corriente I
 - F = |q| * v * B -> Fuerza centripeta
 - R = m * v / (|q| * |B|) -> Radio del movimiento circular
 - ω = v / R = |q| * B / m -> Velocidad angular
 - B = m0 * I / (2 * PI * R) -> Campo magnetico de un cable
 
# Cosas a recordar

mili => 1e-3
micro => 1e-6
nano => 1e-9
pico => 1e-12

"""

def ejercicio1():
  print('La de arriba tiene carga positiva, la del medio no tiene carga, la otra tiene carga negativa')
  print('Como? Definicion de producto cruz')

def ejercicio2():
  print('El angulo entre el vector velocidad y el campo magnetico es 0')
  print('Por lo tanto, el producto cruz entre ellos sera 0')
  print('Entonces la particula no experimenta ninguna fuerza, es decir, continua en la misma direccion y sentido que llevaba')

def ejercicio3():
  print('Debe circular de clockwise para que produzca fuerza hacia abajo, y asi, los resortes se estiren')
  k = .5 + .5 # Resortes en paralelo se suman
  dy = 5e-3
  m = 100e-3
  l = 0.5
  B = 1
  P = m * -g
  e = -P / k
  F = -k * (e + dy)
  extra = P - F
  I = extra / (l * B)
  print("I =", I)

def ejercicio4():
  B = 1
  v = 1e6
  R = getRadioCurvatura(me, v, -Qe, B)
  ω = getVelAng(v, R)
  print('Radio curvatura:', R)  
  print('Velocidad angular:', ω) # radianes por segundo
  print('Frecuencia angular de rotacion:', ω/(2*PI))

def ejercicio5():
  d = .1
  l = .1
  I = 1
  diag = sqrt(l**2 + (d/2)**2)
  mB = getCampoMagnetico(I, diag)
  tita1,tita2 = atan(l/(d/2))-PI/2, -atan(l/(d/2))-PI/2
  print("B =", sumVectorPolar(mB,tita1,mB,tita2))

def ejercicio6():
  print('Dibujalo y te das cuenta que el 0 ocurre en el medio')
  print('Usa formula bizarra m0 * I / (2 * PI * R), igualalas, recorda que Ra+Rb=d y listo')
  print('Ra = Ia * d / (Ia + Ib)')

ejercicio5()