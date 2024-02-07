#include <webots/robot.h>
#include <webots/motor.h>
#include <webots/distance_sensor.h>

#define TIME_STEP 64
#define MAX_SPEED 6.28

int main(int argc, char **argv) {
  wb_robot_init();

  WbDeviceTag ds[2];
  ds[0] = wb_robot_get_device("ds_right");
  ds[1] = wb_robot_get_device("ds_left");
  wb_distance_sensor_enable(ds[0], TIME_STEP);
  wb_distance_sensor_enable(ds[1], TIME_STEP);

  WbDeviceTag wheels[4];
  wheels[0] = wb_robot_get_device("wheel1");
  wheels[1] = wb_robot_get_device("wheel2");
  wheels[2] = wb_robot_get_device("wheel3");
  wheels[3] = wb_robot_get_device("wheel4");
  for (int i = 0; i < 4; ++i) {
    wb_motor_set_position(wheels[i], INFINITY);
    wb_motor_set_velocity(wheels[i], 0.0);
  }

  int avoidObstacleCounter = 0;
  while (wb_robot_step(TIME_STEP) != -1) {
    double leftSpeed = 1.0;
    double rightSpeed = 1.0;
    if (avoidObstacleCounter > 0) {
      avoidObstacleCounter--;
      leftSpeed = 1.0;
      rightSpeed = -1.0;
    } else {
      for (int i = 0; i < 2; ++i) {
        if (wb_distance_sensor_get_value(ds[i]) < 950.0) {
          avoidObstacleCounter = 100;
        }
      }
    }
    wb_motor_set_velocity(wheels[0], leftSpeed * MAX_SPEED);
    wb_motor_set_velocity(wheels[1], rightSpeed * MAX_SPEED);
    wb_motor_set_velocity(wheels[2], leftSpeed * MAX_SPEED);
    wb_motor_set_velocity(wheels[3], rightSpeed * MAX_SPEED);
  }

  wb_robot_cleanup();
  return 0;
}
