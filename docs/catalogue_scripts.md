# Scripts 目录

本文档概述了 HUTB Python API 的可用示例 Python 脚本和实用程序。您可以使用这些脚本来学习 HUTB 的 Python API、执行实用功能或进行测试，并以此为基础编写自己的脚本。以下示例脚本位于 HUTB 代码库或软件包的 [PythonAPI/examples](https://github.com/OpenHUTB/hutb/tree/hutb/PythonAPI/examples) 目录中。

* [手动控制](#manual-control)
* [自动控制](#automatic-control)
* [生成交通流](#generate-traffic)
* [逆 AI 交通流](#inverted-ai-traffic)
* [开始记录](#start-recording)
* [开始重放](#start-replaying)
* [Open3D LIDAR](#open3d-lidar)
* [边界框](#bounding-boxes)
* [非渲染模式](#no-rendering-mode)
* [动态天气](#dynamic-weather)
* [LIDAR to camera](#lidar-to-camera)
* [载具画廊](#vehicle-gallery)

---

## 手动控制

* Script filename: `manual_control.py`
* Example usage: `python3 manual_control.py --res 800x600 --sync`

This script allows a user to manually control a vehicle through a CARLA map using the keyboard, with a visualization of sensor output in a Pygame window. It is one of the first scripts new users should experiment with to explore CARLA maps and to understand the behavior of vehicles and sensors. It is also very useful for testing and debugging when changes have been made to core CARLA functionality relating to rendering, physics, traffic or sensing that might affect appearance, driving behavior or sensor output.

The script spawns a vehicle (the ego vehicle) at a randomly selected spawn point in the map and allows manual control of the vehicle through the arrow keys or WASD keys. Other keyboard shortcuts are available to change vehicles, change gears, change sensor type or start recording and many other functions. 

Manual control can be combined with the [generate traffic script](#generate-traffic) to drive a vehicle through traffic. Launch the generate traffic script prior to launching manual control. Do not attempt to run both scripts in synchronous mode, there should only be 1 client running in synchronous mode. By default manual control runs in asynchronous mode and generate traffic runs in synchronous mode, hence they will work together smoothly in their default synchrony configuration. 

### Key commands

| Key | Control |
|-----|---------|
| W, &uarr;    | Throttle |
| S, &darr;    | Brake |
| A/D, &larr;, &rarr; | Steer left/right |
| Q            | Toggle reverse |
| Space        | Hand-brake |
| P            | Toggle autopilot |
| M            | Toggle manual transmission |
| ,/.          | Gear up/down |
| CTRL + W     | Toggle constant velocity mode at 60 km/h |
| L            | Toggle next light type |
| SHIFT + L    | Toggle high beam |
| Z/X          | Toggle right/left blinker |
| I            | Toggle interior light |
| TAB          | Change sensor position |
| ` or N       | Next sensor |
| [1-9]        | Change to sensor [1-9] |
| G            | Toggle radar visualization |
| C            | Change weather (Shift+C reverse) |
| Backspace    | Change vehicle |
| O            | Open/close all doors of vehicle |
| T            | Toggle vehicle's telemetry |
| V            | Select next map layer (Shift+V reverse) |
| B            | Load current selected map layer (Shift+B to unload) |
| R            | Toggle recording images to disk |
| CTRL + R     | Toggle recording of simulation (replacing any previous) |
| CTRL + P     | Start replaying last recorded simulation |
| CTRL + +     | Increments the start time of the replay by 1 second (+SHIFT = 10 seconds) |
| CTRL + -     | Decrements the start time of the replay by 1 second (+SHIFT = 10 seconds) |
| F1           | Toggle HUD |
| H/?          | Toggle help |
| ESC          | Quit |

### 命令行参数

The manual control script has multiple command line arguments for configuration:

| Argument | Short form | Default | Description |
|----------|------------|---------|-------------|
| --verbose | -v | - | Print debug info |
| --host | -h | 127.0.0.1 | Host IP address |
| --port | -p | 2000 | TCP port for CARLA client |
| --autopilot | -a | Not active | Enable autopilot for ego vehicle |
| --res |  | 1280x720 | Pixel resolution of all camera sensors |
| --filter |  | vehicle.* | Filter for vehicle type |
| --generation |  | 2 | Specify vehicle model generation |
| --rolename |  | hero | Rolename assigned to the ego vehicle |
| --gamma |  | 2.2 | Gamma correction of the RGB camera |
| --sync |  | Not active | Activate the script in synchronous mode |

### Script variants

针对不同用途，有多种手动控制脚本版本。它们都使用相同的快捷键和大部分相同的命令行参数，有些版本还包含额外的命令行参数。

#### Chrono

* Script filename: `manual_control_chrono.py`

This script launches manual control with Chrono physics, using the Sedan powertrain parameters found in the `Co-Simulation/Chrono/Vehicles` directory of the CARLA repository/package. 

#### 鱼眼相机

* 脚本文件名：`manual_control_fisheye.py`

此脚本以手动控制的方式启动鱼眼相机模型。此脚本与 [手动控制](#manual-control) 脚本具有相同的快捷键和命令行参数。它还包含一些用于相机模型参数的额外命令行参数：

| 参数                | 简写形式 | 默认                                                                            | 描述                                                                  |
|-------------------|------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------|
| --fov             |  | 90.0                                                                          | 相机视场角(field of view angle)                                          |
| --fov_mask        |  | Not active                                                                    | 视场之外的掩膜像素                                                           |
| --fov_fade_size   |  | 0.0                                                                           | 视场边缘的衰减，给定增宽因子                                                      |
| --model           |  | perspective                                                                   | 相机模型: <br>透视投影 <br>等距投影 <br>等积投影 <br>正射投影 <br>立体投影 <br>kannala-brandt |
| --k0              |  | 0.0831                                                                        | k0 Kannala-Brandt 参数                                                |
| --k1              |  | 0.0111                                                                        | k1 Kannala-Brandt 参数                                         |
| --k2              |  | 0.00858                                                                       | k2 Kannala-Brandt 参数                                         |
| --k3              |  | 0.000854                                                                      | k3 Kannala-Brandt 参数                                         |
| --equirectangular |  | Not active                                                                    | 等距柱状投影                                          |
| --perspective     |  | Not active                                                                    | 透视投影                                              |
| --longitude_shift | 0.0 | 将等距柱状投影模型的视角中心移动一定角度 |

#### Steering wheel

* Script filename: `manual_control_steeringwheel.py`

This script demonstrates how to control CARLA using an external steering wheel through Pygame's Joystick module. 

---

## 自动控制

* Script filename: `automatic_control.py`
* Example usage: `python3 automatic_control.py --agent Basic --loop`

Automatic control makes use of the CARLA Agents library to automatically control a vehicle around a CARLA map. The CARLA agents library contains various simple driving agent implementations intended for demonstrative purposes. A Pygame window visualizes the vehicle's camera view. 

| Argument | Short form | Default | Description |
|----------|------------|---------|-------------|
| --verbose | -v |  | Print debug info |
| --host | -h | 127.0.0.1 | Host IP address |
| --port | -p | 2000 | TCP port for CARLA client |
| --res |  | 1280x720 | Pixel resolution of all camera sensors |
| --filter |  | vehicle.* | Filter for vehicle type |
| --generation |  | 2 | Specify vehicle model generation |
| --sync |  | Not active | Activate the script in synchronous mode |
| --loop | -l | Not active | Sets a new random destination upon reaching the previous one |
| --agent | -a | | Agent type, "Behavior", "Basic" or "Constant" |
| --behavior | -b | | Agent behavior, "cautious", "normal" or "aggressive" |
| --seed| -s |  | Seed for repeat executions |

---

## 生成交通流

* Script filename: `generate_traffic.py`
* Example usage: `python3 generate_traffic.py -n 100`

This script generates traffic of varying density distributed across a chosen CARLA map. Pedestrians are also generated. The density of traffic and pedestrians can be chosen via command line arguments. The generate traffic script can be run in combination with manual control to drive a vehicle around a map populated with traffic, 

### Command line arguments 

| Argument | Short form | Default | Description |
|----------|------------|---------|-------------|
| --number-of-vehicles | -n | 30 | Number of vehicles to spawn |
| --number-of-walkers | -w | 10 | Number of pedestrians to spawn |
| --host | -h | 127.0.0.1 | Host IP address |
| --port | -p | 2000 | TCP port for CARLA client |
| --safe |  |  | Don't spawn vehicles prone to accidents |
| --filterv |  | vehicle.* | Filter vehicle models with string |
| --filterw |  | walker.pedestrian.* | Filter pedestrian models with string |
| --generationv |  | All | Specify vehicle generation, "1", "2" or "All" |
| --generationw |  | All | Specify pedestrian generation, "1", "2" or "All" |
| --tm-port |  | 8000 | Specify TCP port for the TM |
| --asynch |  | Not active | Run the script in synchronous mode |
| --hybrid |  | Not active | Activate hybrid mode for the TM |
| --seed | -s |  | Integer seed for random generation (activates the deterministic mode for the TM) |
| --seedw |  |  | Integer seed for the pedestrian module |
| --car-lights-on | | False | Enable automatic light managment by the TM |
| --hero | | False | Nominate a hero vehicle |
| --respawn | | False | Automatically respawn dormant vehicles in large maps |
| --no-rendering | | Not active | Activate no-rendering mode for the CARLA server |

---

## 逆 AI 交通流

* Script filename: `invertedai_traffic.py`
* Example usage: `python3 invertedai_traffic.py -iai-key <token> --record`

This script demonstrates how to launch a traffic simulation in CARLA driven by [Inverted AI's](https://www.inverted.ai/home) AI traffic engine. You will need to provide an Inverted AI API key, please [register](https://www.inverted.ai/portal/login) on the website to obtain one. 

### Command line arguments 

| Argument | Short form | Default | Description |
|----------|------------|---------|-------------|
| --number-of-vehicles | -n | 30 | Number of vehicles to spawn |
| --number-of-walkers | -w | 10 | Number of pedestrians to spawn |
| --host | -h | 127.0.0.1 | Host IP address |
| --port | -p | 2000 | TCP port for CARLA client |
| --safe |  |  | Don't spawn vehicles prone to accidents |
| --filterv |  | vehicle.* | Filter vehicle models with string |
| --filterw |  | walker.pedestrian.* | Filter pedestrian models with string |
| --generationv |  | All | Specify vehicle generation, "1", "2" or "All" |
| --generationw |  | All | Specify pedestrian generation, "1", "2" or "All" |
| --seed | -s |  | Integer seed for random generation (activates the deterministic mode for the TM) |
| --hero |  | Not active | Set one of the vehicles as a hero |
| --iai-key | | | Inverted AI API key |
| --record | | Not active | Record the simulation using the CARLA recorder |
| --sim-length | | 60 | Simulation length in seconds |
| --location | | carla:Town10HD | IAI formatted map for simulation  |
| --capacity | | 100 | Quadtree leaf split threshold |
| --width | | 250 | Width of area to initialize traffic |
| --height | | 250 | Height of area to initialize traffic |
| --map-center | | -50,20 | Center of the area to initialize |
| --iai-async | | Not active | Call IAI DRIVE asynchronously |
| --api-model | | bI5p | IAI API model version |
| --iai-log | | Not active | Store a log file for the co-simulation |
| --iai-waypoint-distance | | 15 | Distance to next waypoint for IAI agents |
| --iai-waypoint-detection-threshold | | 2 | Distance from waypoint to consider as completed |
| --iai-max-distance-away | | 20 | Max distance away before a new waypoint is set for an agent |

---

## 开始记录

* Script filename: `start_recording.py`
* Example usage: `python3 start_recording.py`

This script demonstrates how to use the CARLA recorder. Some traffic is spawned and the movement is recorded as a log by the [CARLA recorder](foundations.md#recorder). 

| Argument | Short form | Default | Description |
|----------|------------|---------|-------------|
| --host | -h | 127.0.0.1 | Host IP address |
| --port | -p | 2000 | TCP port for CARLA client |
| --number-of-vehicles | -n | 30 | Number of vehicles to spawn |
| --delay | -d | 2.0 | Delay in seconds between spawns |
| --safe |  |  | Don't spawn vehicles prone to accidents |
| --recorder_filename | -f | test1.log | Filename of recorded log |
| --recorder_time | -t | 0 | Recording duration |

---

## 开始重放

* Script filename: `start_recording.py`
* Example usage: `python3 start_recording.py -f carla.log` 

This script demonstrates how to use the CARLA replayer.  

| Argument | Short form | Default | Description |
|----------|------------|---------|-------------|
| --host | -h | 127.0.0.1 | Host IP address |
| --port | -p | 2000 | TCP port for CARLA client |
| --duration | -d | 0.0 | Duration to replay |
| --recorder_filename | -f | test1.log | Filename of recorded log |
| --camera | -c | 0 | Camera follows actor with given integer ID |
| --time-factor | -x | 1.0 | Time multiplier for playback, e.g. 2.0 for double speed |
| --ignore-hero | -i | Not active | Ignore the hero vehicle |
| --move-spectator |  | Not active | Move spectator camera |
| --top-view |  | Not active | Activate top-down birdseye view |
| --spawn-sensors | | Not active | Spawn sensors in the replaying simulation |
| --map-override | -m | | Map name to replace OpenDRIVE in log file |

---

## Open3D LIDAR

* Script filename: `open3d_lidar.py`
* Example usage: `python3 open3d_lidar.py --semantic --points-per-second 100000` 

This script demonstrates the visualization of LIDAR point clouds generated by the CARLA LIDAR sensor and semantic LIDAR sensor. The [Open3D library](https://www.open3d.org) is used for visualization and is recommended by the CARLA development team for performant point-cloud visualization. 

### Command line arguments

| Argument | Short form | Default | Description |
|----------|------------|---------|-------------|
| --host | -h | 127.0.0.1 | Host IP address |
| --port | -p | 2000 | TCP port for CARLA client |
| --no-rendering |  |  | Activate no-rendering mode |
| --semantic |  | Not active | Use semantic LIDAR |
| --no-noise |  | Not active | Don't add noise and dropoff |
| --no-autopilot |  | Not active | Disable's autopilot, vehicle remains motionless |
| --show-axis |  | Not active | Show the Cartesian axes |
| --filter |  | vehicle.* | Filter vehicle models with string |
| --upper-fov |  | 15.0 | LIDAR's upper field of view in degrees |
| --lower-fov |  | -25.0 | LIDAR's lower field of view in degrees |
| --channels |  | 64.0 | Number of LIDAR channels |
| --range |  | 100.0 | LIDAR's max range in meters |
| --points-per-second |  | 500000 | LIDAR points per second |
| -x |  | 0.0 | X-offset of LIDAR sensor |
| -y |  | 0.0 | Y-offset of LIDAR sensor |
| -z |  | 0.0 | Z-offset of LIDAR sensor |

---

## 边界框

* Script filename: `bounding_boxes.py`
* Example usage: `python3 bounding_boxes.py -d 100` 

This script demonstrates how to derive 3D and 2D bounding boxes through the Python API and visualize them projected into a camera viewplane. The script also has the facitlity to record both 3D and 2D bounding boxes in JSON format alongside camera frames in PNG. The bounding boxes are visualized in a Pygame window. The visualization can be switched between the 3D and 2D bounding boxes using the *2* and *3* number keys. A distance threshold can be set as a command line argument, bounding boxes beyond this threshold will not be visualized or recorded.

* **3D bounding boxes**: The 3D bounding box coordinates are given in the vehicle's local coordinate system, centered on the center of the vehicle's bounding box. For visualization the 3D bounding boxes are projected into the camera plane using the camera's intrinsic parameters. They are derived from each actor's `bounding_box` attribute.

* **2D bounding boxes**: The 2D bounding boxes are given in pixel-based image coordinates of the camera's viewplane. The 2D bounding boxes are derived from the instance segmentation image.

### Key commands 

| Key | Control |
|-----|---------|
| R   | Start recording bounding boxes and camera frames  |
| 3 | Visualize 3D bounding boxes |
| 2 | Visualize 2D bounding boxes |
| ESC | Quit |

### Command line arguments

| Argument | Short form | Default | Description |
|----------|------------|---------|-------------|
| --host | -h | 127.0.0.1 | Host IP address |
| --port | -p | 2000 | TCP port for CARLA client |
| --distance | -d | 50 | Distance threshold for bounding boxes |
| --res |  | 1280x720 | Pixel resolution of the camera sensor (including the instance segmentation camera) |

---

## 非渲染模式

* Script filename: `no_rendering_mode.py`
* Example usage: `python3 no_rendering_mode.py --res 800x600 --filter lincoln_mkz_2020`

To use this script effectively, you should launch the CARLA server in no-rendering mode like so:

```sh
./CarlaUE4.sh --no-rendering
```

This script demonstrates how to visualize the map and vehicles when using the no-rendering mode of CARLA, which disables the spectator view, allowing CARLA to run in a higher performance configuration. This enables frame rates at or above 100 FPS. A Pygame window visualizes a top-down 2D representation of the scene with simple bounding boxes and 2D road surfaces. This is useful when using CARLA without sensors for traffic simulation or driving 3rd party renderers.

### Key commands 

| Key | Control |
|-----|---------|
| TAB          | Toggle hero mode |
| Mouse Wheel  | Zoom in / zoom out |
| Mouse Drag   | Move map (map mode only) |
| W, &uarr;    | Throttle |
| S, &darr;    | Brake |
| A/D, &larr;, &rarr; | Steer left/right |
| Q            | Toggle reverse |
| Space        | Hand-brake |
| P            | Toggle autopilot |
| M            | Toggle manual transmission |
| ,/.          | Gear up/down |
| F1           | Toggle HUD |
| I            | Toggle actor ids |
| H/?          | Toggle help |
| ESC          | Quit |

### Command line arguments

| Argument | Short form | Default | Description |
|----------|------------|---------|-------------|
| --verbose | -v |  | Print debug info |
| --host | -h | 127.0.0.1 | Host IP address |
| --port | -p | 2000 | TCP port for CARLA client |
| --res |  | 1280x720 | Pixel resolution of the display window |
| --filter |  | vehicle.* | Filter vehicle models with string |
| --map |  | None | Start a new episode in a given map |
| --no-rendering |  | Not active | Switch off server rendering |
| --show-triggers |  | Not active | Show trigger boxes for traffic lights |
| --show-connections |  | Not active | Show waypoint connections |
| --show-spawn-points |  | Not active | Show recommended spawn points |

---

## 动态天气

* Script filename: `dynamic_weather.py`
* Example usage: `python3 no_rendering_mode.py --res 800x600 --filter lincoln_mkz_2020`

This script demonstrates how to modify the weather settings in CARLA during runtime, enabling changing weather conditions within a simulation. 

### Command line arguments

| Argument | Short form | Default | Description |
|----------|------------|---------|-------------|
| --host | -h | 127.0.0.1 | Host IP address |
| --port | -p | 2000 | TCP port for CARLA client |
| --speed |  | 1.0 | Rate of weather changes |

---

## LIDAR to camera

* Script filename: `lidar_to_camera.py`
* Example usage: `python3 lidar_to_camera.py --res 800x600 --points-per-second 50000`

This script demonstrates how to project a LIDAR pointcloud into the camera plane. The script stores camera frames with the projected LIDAR points in a directory named `_out` in the root directory of the terminal used to run the script.

### Command line arguments

| Argument | Short form | Default | Description |
|----------|------------|---------|-------------|
| --verbose | -v |  | Print debug info |
| --host | -h | 127.0.0.1 | Host IP address |
| --port | -p | 2000 | TCP port for CARLA client |
| --res |  | 1280x720 | Pixel resolution of the display window |
| --frames |  | 500 | Number of frames to record |
| --dot-extent |  | 2 | LIDAR point extent in pixels |
| --no-noise |  | Not active | Don't add noise and dropoff |
| --upper-fov |  | 15.0 | LIDAR's upper field of view in degrees |
| --lower-fov |  | -25.0 | LIDAR's lower field of view in degrees |
| --channels |  | 64.0 | Number of LIDAR channels |
| --range |  | 100.0 | LIDAR's max range in meters |
| --points-per-second |  | 100000 | LIDAR points per second |

---

## 载具画廊

* Script filename: `vehicle_gallery.py`
* Example usage: `python3 vehicle_gallery.py` 

This script gives 360 degree views of all CARLA vehicles in sequence.

