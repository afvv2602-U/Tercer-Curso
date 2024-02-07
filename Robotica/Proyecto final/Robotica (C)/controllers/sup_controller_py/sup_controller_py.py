from controller import Supervisor

TIME_STEP = 32

# Inicia el supervisor
supervisor = Supervisor()

# Obtiene el Receiver para recibir mensajes
receiver = supervisor.getDevice("receiver")
receiver.enable(TIME_STEP)

def spawn_robot():
    # Esta función crea un nuevo robot en la simulación
    robot_def = """DEF MY_ROBOT Robot { 
                      translation 0 0 0 
                      rotation 0 1 0 0 
                      children [ 
                        Shape {
                          appearance Appearance {
                            material Material {
                            }
                          }
                          geometry Box {
                            size 1 1 1
                          }
                        } 
                      ] 
                    }"""
    root_node = supervisor.getRoot()
    children_field = root_node.getField('children')
    children_field.importMFNodeFromString(-1, robot_def)

# Bucle principal del supervisor
while supervisor.step(TIME_STEP) != -1:
    # Verifica si hay mensajes recibidos
    while receiver.getQueueLength() > 0:
        message = receiver.getData().decode('utf-8')
        print(f"Mensaje recibido: {message}")
        
        # Si el mensaje indica movimiento, spawnea un nuevo robot
        if message == "movimiento detectado":
            print("Spawneando un nuevo robot debido a la detección de movimiento.")
            spawn_robot()

        receiver.nextPacket()
