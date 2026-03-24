#!/usr/bin/env python
# coding: utf-8

# 场景下载：https://huggingface.co/datasets/SimWorld-AI/SimWorld/blob/main/Base20260201/Windows.zip


### UE 命令测试
import sys
import time
from pathlib import Path
sys.path.append(str(Path().resolve().parent))
from simworld.communicator.unrealcv import UnrealCV
from simworld.communicator.communicator import Communicator
from simworld.agent.humanoid import Humanoid
from simworld.agent.scooter import Scooter
from simworld.utils.vector import Vector


# Play in UE first
ucv = UnrealCV()
communicator = Communicator(ucv)


ucv.get_objects()


# ## 相机测试
ucv.get_cameras()


# #### 生成机器狗
robot_dog_name = "Demo_Robot"
robot_dog_asset = "/Game/Robot_Dog/Blueprint/BP_SpotRobot.BP_SpotRobot_C"
ucv.spawn_bp_asset(robot_dog_asset, robot_dog_name)
ucv.set_location((0, 0, 20), robot_dog_name)
ucv.enable_controller(robot_dog_name, True)


print(ucv.get_camera_location(1))
print(ucv.get_camera_rotation(1))
print(ucv.get_camera_fov(1))
print(ucv.get_camera_resolution(1))
ucv.show_img(ucv.get_image(1, 'lit'))


ucv.set_camera_location(1, (0, 0, 0))
ucv.set_camera_rotation(1, (0, 0, 0))
ucv.set_camera_fov(1, 90)
ucv.set_camera_resolution(1, (320, 240))


print(ucv.get_camera_location(1))
print(ucv.get_camera_rotation(1))
print(ucv.get_camera_fov(1))
print(ucv.get_camera_resolution(1))
ucv.show_img(ucv.get_image(1, 'lit'))


ucv.show_img(ucv.get_image(1, 'lit'))


# ## 动作测试

# ### 机器狗测试

# #### Look up

ucv.dog_look_up(robot_dog_name)


# #### look down

ucv.dog_look_down(robot_dog_name)


# #### transition

#### 向前移动
speed = 200
duration = 1
direction = 0
move_parameter = [speed, duration, direction]
ucv.dog_move(robot_dog_name, move_parameter)
time.sleep(duration)

#### 向后移
direction = 1
move_parameter = [speed, duration, direction]
ucv.dog_move(robot_dog_name, move_parameter)
time.sleep(duration)

#### 向左移
direction = 2
move_parameter = [speed, duration, direction]
ucv.dog_move(robot_dog_name, move_parameter)
time.sleep(duration)

#### 向右移
direction = 3
move_parameter = [speed, duration, direction]
ucv.dog_move(robot_dog_name, move_parameter)
time.sleep(duration)


# #### 旋转

#### 向右转
angle = 90
duration = 0.7
clockwise = 1
rotate_parameter = [duration, angle, clockwise]
ucv.dog_rotate(robot_dog_name, rotate_parameter)
time.sleep(duration)

#### Turn left
angle = -90
counter_clockwise = -1
rotate_parameter = [duration, angle, counter_clockwise]
ucv.dog_rotate(robot_dog_name, rotate_parameter)
time.sleep(duration)


# #### destory



ucv.destroy(robot_dog_name)


# ### Humanoid avatar test 

# #### Spawn humanoid

humanoid_1 = Humanoid(Vector(0, 0), Vector(1, 0))
# humanoid_path = '/Game/TrafficSystem/Pedestrian/Base_User_Agent.Base_User_Agent_C'
humanoid_path = '/Game/Human_Avatar/DefaultCharacter/Blueprint/BP_Default_Character.BP_Default_Character_C'
humanoid_name = 'GEN_BP_Humanoid_0'


communicator.spawn_agent(agent=humanoid_1, name=humanoid_name, model_path=humanoid_path)


# #### Interaction



ucv.get_objects()



# arguing
ucv.humanoid_argue(humanoid_name, 0)




ucv.humanoid_stop_current_action(humanoid_name)




# discuss
ucv.humanoid_discuss(humanoid_name, 0)




ucv.humanoid_stop_current_action(humanoid_name)



# listen
ucv.humanoid_listen(humanoid_name)



ucv.humanoid_stop_current_action(humanoid_name)



# directing
ucv.humanoid_directing_path(humanoid_name)




# wave to dog
ucv.humanoid_wave_to_dog(humanoid_name)



ucv.humanoid_stop_current_action(humanoid_name)



# pick up light object
communicator.spawn_object('BP_Mug_C_1', '/Game/InteractableAsset/Cup/BP_Mug.BP_Mug_C', (290, -110, 0), (0, 0, 0))




ucv.humanoid_pick_up_object(humanoid_name, "BP_Mug_C_1")




# drop off object
ucv.humanoid_drop_object(humanoid_name)




ucv.destroy('BP_Mug_C_1')




communicator.spawn_object('BP_Interactable_Box_C_1', '/Game/InteractableAsset/Box/BP_Interactable_Box.BP_Interactable_Box_C', (290, -110, 0), (0, 0, 0))




# pick up heavy object
ucv.humanoid_pick_up_object(humanoid_name, "BP_Interactable_Box_C_1")




# drop off object
ucv.humanoid_drop_object(humanoid_name)




ucv.destroy('BP_Interactable_Box_C_1')


 


# enter and exit vehicle
communicator.spawn_object('BP_VehicleBase_Destruction_C_1', '/Game/Interactable_Vehicle/Blueprint/BP_VehicleBase_Destruction.BP_VehicleBase_Destruction_C', (100, 200, 0), (0, 0, 0))


 


ucv.humanoid_enter_vehicle(humanoid_name, "BP_VehicleBase_Destruction_C_1")


 


ucv.humanoid_exit_vehicle(humanoid_name, "BP_VehicleBase_Destruction_C_1")


 


ucv.destroy('BP_VehicleBase_Destruction_C_1')


 


ucv.destroy('GEN_BP_Humanoid_0')


 


ucv.clean_garbage()


# #### Scooter

 


agent_path = '/Game/TrafficSystem/Pedestrian/Base_User_Agent.Base_User_Agent_C'
scooter_path = '/Game/ScooterAssets/Blueprints/BP_Scooter_Pawn.BP_Scooter_Pawn_C'


 


agent = Humanoid(Vector(0, 0), Vector(0, 1))
scooter = Scooter(Vector(100, 0), Vector(0, 1))


 


communicator.spawn_agent(agent, agent_path)
communicator.spawn_scooter(scooter, scooter_path)


 


communicator.humanoid_get_on_scooter(agent.id)
agent.scooter_id = scooter.id


 


communicator.set_scooter_attributes(agent.scooter_id, 0, 0, 0)


 


communicator.humanoid_get_off_scooter(agent.id, scooter.id)


 


communicator.humanoid_step_forward(agent.id, 2)


 


communicator.humanoid_rotate(agent.id, 90, 'left')


 


communicator.disconnect()

