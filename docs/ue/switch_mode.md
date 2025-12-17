# Carla、虚拟现实、无人机模式之间的切换

Carla 模式主要关注行人和自动驾驶车辆的场景模拟，VR 模式针对智能驾驶舱的行为和交互虚拟现实模拟，AIR 模式重点解决低空无人机的模拟，该页面的文档主要解决它们三者之间的切换问题。



## 使用方法

下载 [链接](https://pan.baidu.com/s/1n2fJvWff4pbtMe97GOqtvQ?pwd=hutb) 中的`software/hutb/hutb_car_vr_air_mujoco.zip`，`CarlaUE4.exe`启动场景的默认游戏模式为 Carla。
使用 [config.py](https://github.com/OpenHUTB/hutb/blob/hutb/PythonAPI/util/config.py) 切换到 [VR 模式](interbehavior.md) ：
```shell
config.py --map Town10HD?GAME=VR
```
切换到无人机模式：
```shell
config.py --map Town10HD?GAME=AIR
```
参数中的`Town10HD`为所要切换的地图名，`GAME=`后面为所需要切到到的游戏模式名，目前支持：CARLA、VR、AIR 三种模式。

## 增加切换游戏模式的实现分析

调用 config.py 切换地图时 Carla 模式的 `--map` 参数不支持游戏模式的切换，为了支持游戏模式的切换，先分析已有实现的调用过程：

1. 脚本 config.py 使用  load_world() 函数实现世界的加载，该功能的实现位于 [PythonAPI\carla\source\libcarla\Client.cpp](https://github.com/OpenHUTB/hutb/blob/f32283bd214907196de92f98b0e7ffe583b45bf4/PythonAPI/carla/source/libcarla/Client.cpp#L227)
```cpp
.def("load_world", CONST_CALL_WITHOUT_GIL_3(cc::Client, LoadWorld, std::string, bool, rpc::MapLayer), (arg("map_name"), arg("reset_settings")=true, arg("map_layers")=rpc::MapLayer::All))
```

