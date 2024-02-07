#include <webots/robot.h>
#include <webots/camera.h>
#include <webots/supervisor.h>
#include <stdlib.h>

#define TIME_STEP 32

// Variables globales para las cámaras
WbDeviceTag camera_1;
WbDeviceTag camera_2;

void initialize_cameras() {
    WbDeviceTag camera_1 = wb_robot_get_device("camara1");
    WbDeviceTag camera_2 = wb_robot_get_device("camara2");

    wb_camera_enable(camera_1, TIME_STEP);
    wb_camera_enable(camera_2, TIME_STEP);
}


bool detect_movement(WbDeviceTag camera) {
    static const unsigned char *prev_image = NULL;
    const unsigned char *current_image = wb_camera_get_image(camera);

    if (prev_image == NULL) {
        prev_image = current_image; // La primera vez, solo guarda la imagen actual
        return false;
    }

    int width = wb_camera_get_width(camera);
    int height = wb_camera_get_height(camera);
    long long sum_diff = 0;

    // Compara la imagen actual con la anterior
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            int index = (y * width + x) * 3; // 3 bytes por píxel (RGB)
            sum_diff += abs(current_image[index] - prev_image[index]); // Diferencia en el canal rojo
            sum_diff += abs(current_image[index+1] - prev_image[index+1]); // Diferencia en el canal verde
            sum_diff += abs(current_image[index+2] - prev_image[index+2]); // Diferencia en el canal azul
        }
    }

    prev_image = current_image; // Actualiza la imagen previa

    // Considera que hay movimiento si la diferencia supera un umbral
    return sum_diff > (width * height * 3 * 10); // Ajusta el umbral según sea necesario
}

void spawn_robot() {
    // Define el string de la definición del robot que quieres spawnear
    const char *robot_def = "DEF MY_ROBOT Robot { translation 0 0 0 rotation 0 1 0 0 children [ Robot { ... } ] }";

    // Obtiene el nodo raíz de la simulación
    WbNodeRef root_node = wb_supervisor_node_get_root();
    WbFieldRef children_field = wb_supervisor_node_get_field(root_node, "children");

    // Importa el nuevo nodo robot
    wb_supervisor_field_import_mf_node_from_string(children_field, -1, robot_def);
}



int main(int argc, char **argv) {
    wb_robot_init();

    initialize_cameras();

    while (wb_robot_step(TIME_STEP) != -1) {
        if (detect_movement(camera_1) || detect_movement(camera_2)) {
            spawn_robot();
        }
    }

    wb_robot_cleanup();
    return 0;
}


