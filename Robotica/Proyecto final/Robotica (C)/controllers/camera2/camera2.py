from controller import Robot, Camera
import numpy as np

# Definición de TIME_STEP
TIME_STEP = 32

# Inicialización básica
robot = Robot()
camera = robot.getDevice("camara2")
camera.enable(TIME_STEP)

emitter = robot.getDevice("emitter2")

prev_image = None

def detect_movement(camera):
    global prev_image
    current_image = camera.getImage()
    if current_image is None:
        return False

    width = camera.getWidth()
    height = camera.getHeight()

    current_image_array = np.frombuffer(current_image, dtype=np.uint8).reshape((height, width, 4))
    if prev_image is None:
        prev_image = current_image_array.copy()
        return False

    diff = np.abs(current_image_array.astype(np.int16) - prev_image.astype(np.int16)).sum()

    prev_image[:] = current_image_array

    return diff > (width * height * 3 * 10)

while robot.step(TIME_STEP) != -1:
    if detect_movement(camera):
        emitter.send(b"movimiento detectado")
