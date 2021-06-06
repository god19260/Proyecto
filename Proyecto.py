# Proyecto de simulación
# Dipolos y polarización
# Teoría Electromagnética 1

# Jefry Carrasco - 19387
# Gerardo Fuentes - 19389
# Fredy Godoy - 19260

#import matplotlib.pyplot as plt
import numpy as np
# Valores para constantes:
q = '3e-9'
d = '10e-9'
pi = '3.1416'
Ep = '8.85e-12'

# Equivalentes coordenadas esfericas y cartesianas
cosT = 'z/(sqrt(x^2+y^2+z^2))' # Coseno de Theta
sinT = 'x*sqrt(1+y^2/x^2)/(sqrt(x^2+y^2+z^2))' #Seno de Theta

cosP = '1/sqrt(1+y^2/x^2)'  # Coseno de Phi     
sinP = '(x/y)/sqrt(1+y^2/x^2)'  # Seno de Phi

r = 'sqrt(x^2+y^2+z^2)' 

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-* Ingresar Funciones -*-*-*-*-*-*-*-*-*-*

# Dipolos sobre eje z
# Campo
Funcion_r_z = '('+cosT+'*'+'2'+')'+'/'+'('+r+'^'+'3'+')'          # Función coordenada en r de esfericas  
Funcion_t_z = '('+sinT+')'+'/'+'('+r+'^'+'3'+')'                  # Función coordenada en theta de esfericas
Funcion_p_z =  '0'                                                # Función coordenada en phi de esfericas

# Dipolos sobre eje y
# Campo
Funcion_r_y = '('+sinP+'*'+sinT+'*'+'2'+')'+'/'+'('+r+'^'+'3'+')' # Función coordenada en r de esfericas  
Funcion_t_y = '('+'-'+sinP+'*'+cosT+')'+'/'+'('+r+'^'+'3'+')'     # Función coordenada en theta de esfericas
Funcion_p_y = '('+'-'+cosP+')'+'/'+'('+r+'^'+'3'+')'              # Función coordenada en phi de esfericas

# Dipolos sobre eje x
# Campo
Funcion_r_x = '('+sinT+'*'+cosP+'*'+'2'+')'+'/'+'('+r+'^'+'3'+')' # Función coordenada en r de esfericas  
Funcion_t_x = '('+'-'+cosP+'*'+cosT+')'+'/'+'('+r+'^'+'3'+')'     # Función coordenada en theta de esfericas
Funcion_p_x = '('+sinP+')'+'/'+'('+r+'^'+'3'+')'                  # Función coordenada en phi de esfericas

# Dipolos sobre eje z angulo alpha
# Campo
Funcion_r_a = '('+'('+cosT+'+'+sinP+'*'+sinT+'+'+cosP+'*'+sinT+')'+'*'+'sqrt(2)'+')'+'/'+'('+r+'^'+'3'+')'   # Función coordenada en r de esfericas  
Funcion_t_a = 'sqrt(2)'+'/2'+'('+sinT+'-'+cosT+'*'+sinP+'-'+cosT+'*'+cosP+')'+'/'+'('+r+'^'+'3'+')'          # Función coordenada en theta de esfericas
Funcion_p_a = 'sqrt(2)'+'/2'+'('+'-'+cosT+'/'+sinT+'-'+cosT+'+'+sinP+')'+'/'+'('+r+'^'+'3'+')'               # Función coordenada en phi de esfericas

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Dipolos sobre eje z
# Campo
Funcion_r_i_z = Funcion_r_z + '(x/sqrt(x^2+y^2+z^2))'
Funcion_r_j_z = Funcion_r_z + '(y/sqrt(x^2+y^2+z^2))'
Funcion_r_k_z = Funcion_r_z + '(z/sqrt(x^2+y^2+z^2))'

Funcion_t_i_z = Funcion_t_z + '(z/(sqrt(x^2+y^2+z^2)sqrt(1+y^2/x^2)))'
Funcion_t_j_z = Funcion_t_z + '((z*y/x)/(sqrt(x^2+y^2+z^2)sqrt(1+y^2/x^2)))'
Funcion_t_k_z = Funcion_t_z + '(-x*sqrt(1+y^2/x^2)/sqrt(x^2+y^2+z^2))'

Funcion_p_i_z = Funcion_p_z + '(-(y/x)/sqrt(1+y^2/x^2))'
Funcion_p_j_z = Funcion_p_z + '(1/sqrt(1+y^2/x^2))'
Funcion_p_k_z = Funcion_p_z + '(0)'

# Dipolos sobre eje y
# Campo
Funcion_r_i_y = Funcion_r_y + '(x/sqrt(x^2+y^2+z^2))'
Funcion_r_j_y = Funcion_r_y + '(y/sqrt(x^2+y^2+z^2))'
Funcion_r_k_y = Funcion_r_y + '(z/sqrt(x^2+y^2+z^2))'

Funcion_t_i_y = Funcion_t_y + '(z/(sqrt(x^2+y^2+z^2)sqrt(1+y^2/x^2)))'
Funcion_t_j_y = Funcion_t_y + '((z*y/x)/(sqrt(x^2+y^2+z^2)sqrt(1+y^2/x^2)))'
Funcion_t_k_y = Funcion_t_y + '(-x*sqrt(1+y^2/x^2)/sqrt(x^2+y^2+z^2))'

Funcion_p_i_y = Funcion_p_y + '(-(y/x)/sqrt(1+y^2/x^2))'
Funcion_p_j_y = Funcion_p_y + '(1/sqrt(1+y^2/x^2))'
Funcion_p_k_y = Funcion_p_y + '(0)'

# Dipolos sobre eje x
# Campo
Funcion_r_i_x = Funcion_r_x + '(x/sqrt(x^2+y^2+z^2))'
Funcion_r_j_x = Funcion_r_x + '(y/sqrt(x^2+y^2+z^2))'
Funcion_r_k_x = Funcion_r_x + '(z/sqrt(x^2+y^2+z^2))'

Funcion_t_i_x = Funcion_t_x + '(z/(sqrt(x^2+y^2+z^2)sqrt(1+y^2/x^2)))'
Funcion_t_j_x = Funcion_t_x + '((z*y/x)/(sqrt(x^2+y^2+z^2)sqrt(1+y^2/x^2)))'
Funcion_t_k_x = Funcion_t_x + '(-x*sqrt(1+y^2/x^2)/sqrt(x^2+y^2+z^2))'

Funcion_p_i_x = Funcion_p_x + '(-(y/x)/sqrt(1+y^2/x^2))'
Funcion_p_j_x = Funcion_p_x + '(1/sqrt(1+y^2/x^2))'
Funcion_p_k_x = Funcion_p_x + '(0)'

# Dipolos sobre eje z angulo alpha
# Campo
Funcion_r_i_a = Funcion_r_a + '(x/sqrt(x^2+y^2+z^2))'
Funcion_r_j_a = Funcion_r_a + '(y/sqrt(x^2+y^2+z^2))'
Funcion_r_k_a = Funcion_r_a + '(z/sqrt(x^2+y^2+z^2))'

Funcion_t_i_a = Funcion_t_a + '(z/(sqrt(x^2+y^2+z^2)sqrt(1+y^2/x^2)))'
Funcion_t_j_a = Funcion_t_a + '((z*y/x)/(sqrt(x^2+y^2+z^2)sqrt(1+y^2/x^2)))'
Funcion_t_k_a = Funcion_t_a + '(-x*sqrt(1+y^2/x^2)/sqrt(x^2+y^2+z^2))'

Funcion_p_i_a = Funcion_p_a + '(-(y/x)/sqrt(1+y^2/x^2))'
Funcion_p_j_a = Funcion_p_a + '(1/sqrt(1+y^2/x^2))'
Funcion_p_k_a = Funcion_p_a + '(0)'
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* Resultado final *-*-*-*-*-*-*-*-*-*-*
# Dipolos sobre eje z
# Campo
i_z = Funcion_r_i_z + '+' + Funcion_t_i_z + '+' + Funcion_p_i_z
j_z = Funcion_r_j_z + '+' + Funcion_t_j_z + '+' + Funcion_p_j_z
k_z = Funcion_r_k_z + '+' + Funcion_t_k_z + '+' + Funcion_p_k_z
# Dipolos sobre eje y
# Campo
i_y = Funcion_r_i_y + '+' + Funcion_t_i_y + '+' + Funcion_p_i_y
j_y = Funcion_r_j_y + '+' + Funcion_t_j_y + '+' + Funcion_p_j_y
k_y = Funcion_r_k_y + '+' + Funcion_t_k_y + '+' + Funcion_p_k_y
# Dipolos sobre eje x
# Campo
i_x = Funcion_r_i_x + '+' + Funcion_t_i_x + '+' + Funcion_p_i_x
j_x = Funcion_r_j_x + '+' + Funcion_t_j_x + '+' + Funcion_p_j_x
k_x = Funcion_r_k_x + '+' + Funcion_t_k_x + '+' + Funcion_p_k_x
# Dipolos sobre eje z angulo alpha
# Campo
i_a = Funcion_r_i_a + '+' + Funcion_t_i_a + '+' + Funcion_p_i_a
j_a = Funcion_r_j_a + '+' + Funcion_t_j_a + '+' + Funcion_p_j_a
k_a = Funcion_r_k_a + '+' + Funcion_t_k_a + '+' + Funcion_p_k_a

# Resultados Finales
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
# Dipolos sobre eje z
print('Funcion en r: ' + Funcion_r_z)
print('Funcion en theta: ' + Funcion_t_z)
print('Funcion en phi: ' + Funcion_p_z)
print('Campo electrico de dipolo orientado sobre el eje z:')
print('-Coordenada i: ' +i_z); # Devuelve la funcion en cartesianas
print('-Coordenada j: ' +j_z); # Devuelve la funcion en cartesianas
print('-Coordenada k: ' +k_z); # Devuelve la funcion en cartesianas
print('\n')
# Dipolos sobre eje y
print('Campo electrico de dipolo orientado sobre el eje y:')
print('-Coordenada i: ' +i_y); # Devuelve la funcion en cartesianas
print('-Coordenada j: ' +j_y); # Devuelve la funcion en cartesianas
print('-Coordenada k: ' +k_y); # Devuelve la funcion en cartesianas
print('\n')
# Dipolos sobre eje x
print('Campo electrico de dipolo orientado sobre el eje x:')
print('-Coordenada i: ' +i_x); # Devuelve la funcion en cartesianas
print('-Coordenada j: ' +j_x); # Devuelve la funcion en cartesianas
print('-Coordenada k: ' +k_x); # Devuelve la funcion en cartesianas
print('\n')
# Dipolos sobre eje z angulo alpha
print('Campo electrico de dipolo orientado sobre el eje z angulo alpha:')
print('-Coordenada i: ' +i_a); # Devuelve la funcion en cartesianas
print('-Coordenada j: ' +j_a); # Devuelve la funcion en cartesianas
print('-Coordenada k: ' +k_a); # Devuelve la funcion en cartesianas
print('\n')
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')