def opcion1():
print('Opcion 1 seleccionada')
def conectar_db():
 try:
 conexion = psycopg2.conenect()
def cerrar_conexion(conexion):
 if conexion:
 conexion.close()
def opcion1():
 conn=conectar_bd()
