# [具身人模拟](https://github.com/google-deepmind/mujoco/network/dependents)

<!-- 共5k+个仓库，
更新到的页面： 
https://github.com/google-deepmind/mujoco/network/dependents?dependents_before=NDgxMzAyMjMxNTE
-->

<!-- 更新到最新的仓库： 
https://github.com/mcx/robosuite
-->

- [__人__](#humanoid)
    - [人的建模](#humanoid_model)
- [__Mujoco__](#Mujoco)
    - [人形机器人](#humanoid_robot)
    - [双足机器人](#bipedal)
    - [灵巧手](#hand)
    - [比赛](#tournament)
- [__ROS__](#ros)
- [__强化学习__](#rl)
    - [DQN](#dqn)
    - [AC](#ac)
    - [PPO](#ppo)
    - [多智能体](#multi_agent)
    - [模仿学习](#imitation)
    - [分层强化学习](#hierarchy)
    - [分布式强化学习](#distributed)
    - [离线强化学习](#off_line_rl)
    - [逆强化学习](#inverse_rl)
    - [元强化学习](#meta_rl)
- [__感知__](#perception)
    - [触觉](#tactile)
- [__规划__](#planning)
- [__控制__](#control)
- [__测试__](#test)
- [__数据__](#data)
- [__世界模型__](#world_model)
- [__大模型__](#llm)
- [__建模__](#modelling)
- [__研究__](#research)
- [__竞赛__](#contest)
- [__教程__](#tutorial)
- [__学习__](#learning)
- [__任务__](#task)
    - [无人机](#UAV)
- [__平台__](#platform)
- [__工具__](#tool)
- [__杂项__](#misc)


## 肌肉骨骼人 <span id="humanoid"></span>

[使用 MuJoCo 物理引擎模拟的肌肉骨骼模型要解决的环境](https://github.com/MyoHub/myosuite) - 包含在 OpenAI gym API 中

[将 opensim 4.0+ MSK 模型转换为 MuJoCo 格式的工具](https://github.com/MyoHub/myoconverter) - 具有优化的肌肉运动学和动力学

[使用“双 DQN 强化学习”来解决肌肉骨骼任务](https://github.com/victor369basu/MyosuiteDDQN) 

[比赛ENG-ME951-MyoChallenge2023](https://github.com/renaik/ENG-ME951-MyoChallenge2023) - 即DEP-RL：过度驱动和肌肉骨骼系统中强化学习的具体探索

[计算出遵循约束条件的最可能路径](https://github.com/rimao-uni/Frame-interpolation-by-OM-theory)

[在MuJoCo中建模和模拟人机交互任务](https://github.com/User-in-the-Box/user-in-the-box) - 用户采用具有感知能力（例如自我中心视觉）的肌肉驱动生物力学模型进行建模，并通过强化学习进行训练以解决交互任务

[仿生机器人测试平台](https://github.com/Co-Evolve/brt)

[用户采用具有感知能力（例如自我中心视觉）的肌肉驱动生物力学模型进行建模，并通过强化学习进行训练以解决交互任务](https://github.com/Koyle1/cmhci-uitb-code) - [其他](https://github.com/Koyle1/RL_2025_UITB_REG)

[具身智能体的脑-身同步探索](https://github.com/yangsizhe/bbsea)

[利用肌肉学习：拟人化任务中数据效率和鲁棒性的优势](https://github.com/martius-lab/learningwithmuscles)

[基于强化学习的运动模仿，实现生理上合理的肌肉骨骼运动控制](https://github.com/amathislab/Kinesis)

[利用强化学习模拟双足站立和平衡](https://github.com/Ardiegon/ReinforcementHumanoidBalancing)

[在 MUJOCO 和 Isaac Gym 中模拟 SMPL/SMPLX 人形机器人](https://github.com/ZhengyiLuo/SMPLSim)

[支持 PDP 论文中的扰动恢复任务](https://github.com/Stanford-TML/PDP)

[从任意跌倒状态起身](https://github.com/tianxintao/get_up_control) - [其他](https://github.com/sumanth-tangirala/get-up-control-trajectories)

[MyoChallenge 保定球策略分析](https://github.com/amathislab/MyoChallengeAnalysis)

[具有内部复杂性的网络模型架起了人工智能与神经科学的桥梁](https://github.com/helx-20/complexity)

[LocoMuJoCo是一个专门针对运动的模仿学习基准。它涵盖了多种环境，包括四足动物、两足动物和肌肉骨骼人体模型](https://github.com/Harry-maximum/loco-mujoco)

[训练和比较人形 AI 代理完成1v1 近战](https://github.com/rodSiry/bagarreio)

[使用 MuJoCo 和 Gym 重新实现的 DeepMimic 控制框架](https://github.com/sah4jpatel/DeepMimic_Revisited)

[行走](https://github.com/scott-yj-yang/brax_rodent_walk)

[探索与行为相关的神经网络](https://github.com/danielcson/dsc_capstone_q1) - 模仿行为来模拟大脑

[sin-cassie-rl-python](https://github.com/cwjwudi/sin-cassie-rl-python)

[使用 Brax 和 MJX 实现啮齿动物模仿学习的 VNL 实现](https://github.com/talmolab/VNL-Brax-Imitation)

[双足步行者的Gym环境](https://github.com/cameronpm1/bpwgym)

[PACER：行人动画控制器](https://github.com/nv-tlabs/pacer)

[MIMo是一个用于研究婴儿认知发展的平台](https://github.com/ZhendongL/MIMo_Original) - 使用MuJoCo进行物理模拟的 gym 环境以及多个可产生视觉、触觉、本体感觉和前庭系统模拟感官输入的模块组成。[其他](https://github.com/Pitohui202/MiMo)

[机器人学习的模块化仿真框架和基准](https://github.com/ARISE-Initiative/robosuite) - 包括人形机器人

[使用 mujoco 和类人神经机械模型（而非人形机器人）实现 DeepMimic](https://github.com/DanielCastillo03/DeepMimic_Research)

[带有通用规划器的 H-GAP 人形控制代码发布](https://github.com/facebookresearch/hgap)

[仿生机器人](https://github.com/MHaqui/Biomecanical_project)

[构建意识与决策机制](https://github.com/oyako-li/TPG)

[单变量径向基函数层：受大脑启发的低维输入深度神经层](https://github.com/bkpcoding/urbf)

[用于机器人、深度强化学习和神经科学研究的 Python 工具](https://github.com/shandilya1998/neurorobotics)



### 人的建模 <span id="humanoid_model"></span>

[OpenSim 肌肉骨骼模型转到 MuJoCo](https://github.com/MyoHub/myoconverter)

[用于 mujoco 模拟的机器人模型集合](https://github.com/anupamkaul/mujoco_menagerie)

[模和模拟人机交互任务的源代码](https://github.com/BaiYunpeng1949/heads-up-multitasker)

[人外骨骼步态模型集成](https://github.com/kekellyu/legsim)

[一种可微分符号建模方法，用于人体运动模拟](https://github.com/Baikalfische/Human-SymPy-model)

[使用肌肉骨骼模型创建 x2 外骨骼模型（模拟人类佩戴外骨骼的真实情况）](https://github.com/NuCapybara/x2_myosuite)

[MyoSuite是使用MuJoCo物理引擎模拟的肌肉骨骼环境和任务的集合](https://github.com/myo-manipulation/AlBornoLab-myosuite)

[用于研究婴儿认知发展的平台](https://github.com/trieschlab/MIMo) - 可产生视觉、触觉、本体感觉和前庭系统模拟感官输入的模块组成

[用于分析人手样本钳式抓握执行情况的机器人测试台的设计和实现](https://github.com/NikonPic/PhoenixHand)

[伯克利人形机器人精简版](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)

[使用 ODE、PhysX 或 MuJoCo 后端的肌肉骨骼建模系统](https://github.com/wol101/GaitSym5)

[为 OpenManipulator-X 绘制机器人代码](https://github.com/EndeavoringYoon/Drawing-Robot-with-OpenManipulator-X)

[MorphVSR：基于体素的软机器人模拟与协同进化框架](https://github.com/Hadi-Khan-Projects/VoxelSoftRobots)

[Menagerie是MuJoCo物理引擎的高质量模型集合](https://github.com/hridey622/menagerie)

[自适应膝关节动力学模拟](https://github.com/pr0tos/adaptive_knee)

[Menagerie：MuJoCo物理引擎高质量模型集合](https://github.com/google-deepmind/mujoco_menagerie)


## Mujoco 机器人 <span id="Mujoco"></span>

[官方的移动任务实现](https://github.com/google-deepmind/dm_control/tree/main/dm_control/locomotion)

[层次世界模型实现人形全身控制](https://github.com/nicklashansen/puppeteer)

[模仿学习基准专注于使用 MuJoCo 执行复杂的运动任务](https://github.com/robfiras/loco-mujoco)

[全身控制的层次世界模型](https://github.com/nicklashansen/puppeteer)

[MyoSuite](https://github.com/MyoHub/myosuite) - 使用 MuJoCo 物理引擎模拟的肌肉骨骼模型要解决的环境/任务的集合，并包含在 OpenAI gym API 中

[将机器人送入家庭并收集数据](https://github.com/AlexanderKhazatsky/household_robots)

[使用预测控制，通过 MuJoCo 进行实时行为合成](https://github.com/google-deepmind/mujoco_mpc)

[dm_robotics：为机器人研究创建和使用的库、工具和任务](https://github.com/google-deepmind/dm_robotics)

[通过将人体运动数据传输到机器人模型（Unitree H1），并应用逆运动学 (IK) 和潜在的强化学习 (RL) 等先进技术进行实时自适应，使机器人能够执行动态且自然的类人运动](https://github.com/Noora-Alhajeri/sport-motion-retargeting)




### 人形机器人 <span id="humanoid_robot"></span>

[HumanoidBench：用于全身运动和操控的模拟人形基准](https://github.com/carlosferrazza/humanoid-bench) - [其他1](https://github.com/Woodwardbr/16831-project) 、 [其他2](https://github.com/JiyunJang-24/HumanoidBench-PbRL) 、[其他3](https://github.com/Shuhanl/hro_reinforcement_learning)

[Humanoid-Gym：基于零样本 Sim2Real 迁移的人形机器人强化学习](https://github.com/toonasinensis/humanoid_gym) - [其他](https://github.com/davidmao829/rl_series) 、[其他2](https://github.com/LQ0212/humanoid_gym)

[即插即用的机器人部署框架](https://github.com/HansZ8/RoboJuDo)

[人形策略学习中的对抗性运动和运动模仿](https://github.com/TeleHuman/ALMI-Open)

[用于人形机器人运动和操作的强化学习训练库。基于 MuJoCo 和 JAX 构建](https://github.com/mshicom/ksim)

[用于类人运动和操控的强化学习训练库](https://github.com/mshicom/ksim)

[ASAP：结合模拟和现实世界的物理来学习敏捷的人形机器人全身技能](https://github.com/LeCAR-Lab/ASAP)

[将人体运动捕捉数据转换为平滑且运动学上可行的人形机器人轨迹](https://github.com/YiyangShao2003/SmoothMoCapRetarget)

[FALCON：学习力自适应人形机器人位置操纵](https://github.com/LeCAR-Lab/FALCON)

[OKAMI：通过单一视频模仿教授人形机器人操作技能](https://github.com/UT-Austin-RPL/OKAMI)

[首先用于机器人和人体模板相匹配，同样，训练用于教师网络和学生网络的调整](https://github.com/Ethereal1679/H2O_Sim_Real_reshuffle)

[人形机器人“h1”右臂任务空间控制](https://github.com/parsa25b/robot_task_space_control)

[ASAP：将仿真与现实世界的物理学相结合，以学习敏捷的人形机器人全身技能](https://github.com/LeCAR-Lab/ASAP)

[包含 IsaacLab 扩展，用于训练人形机器人的神经全身控制器](https://github.com/forerunnerai/HOVER)

[基于强化学习的仿人机器人上肢遥操作研究](https://github.com/Hahalim2022y/Teleoperation-of-Humanoid-Robot)

[基于isaacgym的人形机器人强化学习训练](https://github.com/Kong-Huiyang/ti5_isaacgym)

[AgiBot X1使用的强化学习训练代码](https://github.com/wttdlz/wl)

[AMO：超灵巧人形机器人全身控制的自适应运动优化](https://github.com/100-rab/AMO)

[使用强化学习的人形机器人运动控制](https://github.com/Q-M-D/rl-humanoid-locomotion)

[（类人）机器人操作的模仿学习 (IL)、强化学习 (RL) 和从演示中学习 (LfD)](https://github.com/Skylark0924/Rofunc)

[包含 IsaacLab 扩展，用于训练人形机器人的神经全身控制器](https://github.com/NVlabs/HOVER)

[使用运动捕捉数据和 PyBullet 物理模拟实现人形角色的模仿学习](https://github.com/MayankD409/Humanoid_gait_generation)

[在 isaac gym 和 sim-to-sim 到 mujoco 下训练人形机器人的管道](https://github.com/xwpwzzz/humanoid_gym_custom)

[套入自己的人形机器人，同时加入gazebo仿真程序](https://github.com/Yibming/yihumanoid-gym)

[从人体网格描述（SMPL、SMPL-X 等）重新定位到人形姿势](https://github.com/song-siqi/retarget2humanoid)

[AgiBot X1是 AgiBot 自主研发并开源的一款模块化高自由度人形机器人](https://github.com/Vertax42/humanoid-gym)

[具有行为克隆和微调的人形机器人离线强化学习](https://github.com/fmdazhar/demonstration_bc_rl)

[通用且灵巧的人对人全身远程操作和学习](https://github.com/huanyuqingming/omnih2o)

[通过 Reachy2 的（假）sdk 在 mujoco 中与 Reachy2 进行交互](https://github.com/pollen-robotics/reachy2_mujoco)

[人形舞者](https://github.com/DRL-Tsinghua/humanoid-dancer)

[利用 Unitree G1 人形机器人平台开展视觉-语言-动作 (VLA) 技术的研究](https://github.com/cyfarwydd-tian/omnih2o-learn)

[采用了Unitree RL Gym及其 H1_2 机器人模型，并选择了快速运动适应 (RMA)方法](https://github.com/wyy603/isr_project)

[用于收集人形机器人平台身体模式模拟和评估脚本的存储库](https://github.com/event-driven-robotics/neuromorphic_body_schema)

[生成预测控制：动态且难以演示的任务的流匹配策略](https://github.com/vincekurtz/gpc)

[以教会 Mujoco 人形机器人使用Stable Baselines 3站立](https://github.com/rutmehta/assignment3)

[HumEnv 是一个基于 SMPL 人形机器人的环境，旨在进行可重复的人形机器人控制研究](https://github.com/facebookresearch/humenv)

[人形机器人运动捕捉重定向库](https://github.com/RumblingTurtle/recap)

[Unitree H1机器人行走应用](https://github.com/ZhangXG001/unitree_h1_humanoid-gym)

[实时模拟人形的永久人形控制](https://github.com/hosseinfeiz/PHC)

[人形动作捕捉追踪](https://github.com/robo-Bellone/mujoco-MPC-bipedal)

[学习人与人之间的实时全身远程操作](https://github.com/LeCAR-Lab/human2humanoid)



[使用 Genesis 模拟器为两个机器人（KBot 和 ZBot）构建训练环境](https://github.com/chloeji8888/Humanoid-Walking)

[在Mujoco模拟环境中对人形模型进行控制器实验](https://github.com/WilliamZhang20/Humanoid-Mujoco)

[使用Unitree Robots进行强化学习的简单示例，包括Unitree Go2、H1、H1_2、G1](https://github.com/xiaotangtang-s/unitree_rl_gym_xiaotang) - [其他1](https://github.com/myoooofall/BVI_rl_control) 、[其他2](https://github.com/RamseyPengTianhu/Unitree_gym_test) 、 [其他3](https://github.com/Wujieling0624/spibot_RL) 、[其他4](https://github.com/Zhuz0123/unitree_rl) 、[其他5](https://github.com/duohetangshui11/single-leg-probing)

[具有仿真环境的参数化控制器套件，用于人形机器人的协同设计](https://github.com/ami-iit/comodo)

[HumanDIL：全身类人自然运动的解耦模仿](https://github.com/shaosb/hit_omniverse)

[使用JAX和 MuJoCo MJX在 GPU 上进行基于采样的模型预测控制](https://github.com/vincekurtz/hydrax)

[基于Unitree机器人的强化学习实现的仓库，支持Unitree Go2、H1、H1_2、G1](https://github.com/unitreerobotics/unitree_rl_gym) - [其他](https://github.com/RamseyPengTianhu/Unitree_gym)

[AgiBot X1是 AgiBot 自主研发并开源的一款模块化高自由度人形机器人](https://github.com/git6688/tms1)

[跌倒恢复和站立特工](https://github.com/Rhoban/frasa)

[利用强化学习让类人模型行走的小实验](https://github.com/ziyingsk/Humanoid_experiment)

[MuJoCo 模拟用于训练人形机器人](https://github.com/mcgill-robotics/Humanoid-MuJoCo)

[MoCapAct：用于模拟人形控制的多任务数据集](https://github.com/tmitta31/mocapact_test1)

[基础环境legged_robot构建了一个崎岖地形运动任务](https://github.com/HBUTHUANGPX/livelybot_rl_control)

[演示驱动的移动双手操作基准](https://github.com/chernyadev/bigym)

[Humanoid-Gym：基于零样本 Sim2Real 迁移的人形机器人强化学习](https://github.com/thuuzi/bipedv5_gym) - [其他1](https://github.com/2253209/humanoid_gym_2) 、 [其他2](https://github.com/2253209/h1_xdjy) 、 [其他3](https://github.com/roboterax/humanoid-gym)

[Robust Gymnasium：稳健强化学习的统一模块化基准](https://github.com/SafeRL-Lab/Robust-Gymnasium)

[使用四足机器人 Unitree Go1 进行强化学习](https://github.com/DavidDema/DeepRL-quadruped-robot)

[学习人形行走](https://github.com/Sujgaik2003/Nao-robot-pideal-walking-using-RL-)

[使用 Convex MPC 实现双足动物在崎岖和正弦地形上携带有效载荷行走](https://github.com/nithin127/biped_walking)

[3D 双足机器人](https://github.com/mughalfrazk/humanoid-applied-ai)

[离线强化学习作为一个大序列建模问题](https://github.com/danieljnt8/citylearn_transformer)

[用于人形机器人导航的量子深度强化学习](https://github.com/romerik/Quantum_Deep_Reinforcement)

[全身控制](https://github.com/einstein8612/bio-humanoid)

[Humanoid-Gym-Modified 是对humanoid-gym框架的修改，它增加了Pandaman的开源模型，并引入了对 Gazebo 模拟环境中机器人 sim-to-sim 测试的支持](https://github.com/roboman-ly/humanoid-gym-modified)

[在 Stompy（由 K-Scale Labs 开发的人形机器人）上训练和测试强化学习策略的简单方法](https://github.com/michael-lutz/stompy-sandbox)

[跑步者：无需动作捕捉的类人跑步强化学习](https://github.com/dancing-amigo/Runner)

[通过单视频模仿教授人形机器人操作技能](https://github.com/UT-Austin-RPL/OKAMI)

[学习力适应型人形机器人移动操控](https://github.com/LeCAR-Lab/FALCON)

[专家接近度作为单次演示模仿学习的替代奖励](https://github.com/stanl1y/tdil)


### 双足机器人 <span id="bipedal"></span>

[在 BipedalWalker-v3 环境中使用近端策略优化 (PPO) 算法进行智能体训练](https://github.com/canoksuzoglu1/BipedalWalker-RL)

[双足平衡机器人的论文，该机器人采用强化学习中的PPO算法](https://github.com/hoag-nuye/simular_bipebal_robot_Thesis)

[双足机器人简单全技能堆栈](https://github.com/Alexhuge1/fftai_alexbotmini)

[由伺服电机驱动的 ESP32 + Python 控制的双足机器人](https://github.com/AsterisCrack/BipedRobot)

[FootStepNet Envs：用于快速在线双足行走规划和预测的行走规划强化学习环境](https://github.com/Rhoban/footstepnet_envs)

[使用行为克隆（BC）和近端策略优化（PPO）训练被动步行者的综合强化学习](https://github.com/yunusdanabas/passive_walker_rl)

[双足机器人简单全技能栈 alexbotmini](https://github.com/Alexhuge1/Alexbotmini_deploy)

[ZBot 环境：双足机器人训练环境](https://github.com/nicolasztan/Humanoid-Walking)

[VMTS：双足机器人多地形运动的视觉辅助师生强化学习](https://github.com/chenfu-user/VMTS)

[基于 NVIDIA Isaac Gym 的强化学习环境。对于 HighTorque Robotics 的 Pi 人形机器人](https://github.com/HighTorque-Robotics/livelybot_pi_rl_baseline)

[轮式双足机器人仿真与训练](https://github.com/ojferro/Theatrum)

[为双足智能体构建了模拟到真实的强化学习流程](https://github.com/khuntikaran/bipedal-rl)

[FD双足下肢系统](https://github.com/YooTion/fdhumanoid_S2R)

[Performance](https://github.com/lupusorina/robot_learning)

[具有深度强化学习的双足机器人情绪感知社交导航](https://github.com/GTLIDAR/emobipednav)

[基于JAX+MJX的数值逆运动学求解器](https://github.com/based-robotics/mjinx)

[学习一个世界模型，该模型从高级像素图像中捕捉潜在动态](https://github.com/KurtDCD/Dreamer)

[使用双足机器人执行复杂控制任务的各种策略](https://github.com/MMahdiSetak/WalkerRL)


### 手臂 <span id="hand"></span>

[使用逆运动学实现 Unitree G1 人形机器人的基本手部运动](https://github.com/yediong/IK-humanoid)

[对使用机械手进行强化学习的探索](https://github.com/Autobots-Visman/reinforcement-learning)

[GCRL_UR10e 是一个用于 UR10e 机械臂的仿真到实战强化学习框架](https://github.com/cherylwang20/GCRL_UR10e)

[RoboTwin：具有生成数字孪生的双臂机器人基准](https://github.com/Tengbo-Yu/robotwin)


### 比赛 <span id="tournament"></span>

[足球射门、乒乓球对打](https://sites.google.com/view/myosuite/myochallenge/myochallenge-2025) 

[网球环境下的多智能体DDPG](https://github.com/m-fili/Tennis_MADDPG)



## ROS  <span id="ros"></span>

[乐聚机器人控制](https://github.com/LejuRobotics/kuavo-ros-opensource) - 包含 Mujoco 仿真环境

[ROS 的人体模型](https://github.com/shafaghkey/human_model)

[将 ROS 与 MuJoCo 结合使用的封装器、工具和附加 API](https://github.com/ubi-agni/mujoco_ros_pkgs) - 支持 Noetic，- 其他 [mujoco_ros2_control](https://github.com/moveit/mujoco_ros2_control) 

[车道跟随器与强化学习](https://github.com/3N4N/ros-rl)

[Linkerhand ROS2 SDK](https://github.com/linker-bot/linkerhand-ros2-sdk)

[通过 ROS2 使用Dynamixel电机控制机械手](https://github.com/RiccardoBianco/robotic-hand-rwr)

[用于机器人强化学习端到端开发的工具](https://github.com/Zolkin1/robot_rl)

[Aria 的 ROS2](https://github.com/Dhruv2012/projectaria-ros2)

[使用 franka_ros2 和 mink 对 franka fr3 进行遥控（用于逆运动学）](https://github.com/jvdutt/teleop_fr3_ros2)

[只需从 ROS 2 发送目标关节角度即可在 Genesis 中控制机器人](https://github.com/tototototototo07/simple_ros2_genesis_sim)

[基于 ROS2 的户外 SLAM 和自主导航](https://github.com/adeeb10abbas/outdoor_ros2)

[使用 Docker 构建 ROS2 运行环境](https://github.com/cpx0/ros2_docker)

[用于 AR4 机械手的 ROS 2 软件堆栈](https://github.com/Ekumen-OS/ar4)

[基于单刚体模型的四足机器人模型预测控制器](https://github.com/iit-DLSLab/Quadruped-PyMPC)

[利用深度强化学习实现仓库机器人导航](https://github.com/AnirudhJ3/warehouse_nav_rl)

[MuJoCo 的高性能 LiDAR 模拟](https://github.com/TATP-233/MuJoCo-LiDAR)

[基于单刚体模型并用Python编写的模型预测控制器](https://github.com/njayboehme/ME_531_Proj)

[unitree_mpc](https://github.com/sm-1z/unitree_mpc)

[基于 ROS 的功能包，主要围绕 Piper机械臂以及 Orbbec 深度相机等硬件的应用展开](https://github.com/HustWolfzzb/EmbodiedAIOS)

[利用 ROS2 MoveIt 任务构造器来控制 MuJoCo 中的 UR5e 机械臂和 Robotiq 2F-85 夹持器](https://github.com/nimeshaTJ/Nimesha_Jayatunge_Thesis)

[online_hdif_ws](https://github.com/mateoguaman/online_hdif_ws)

[FTN 上开发的与 Solo 相关的所有内容的存储库](https://github.com/ajsmilutin/ftn_solo)

[Faur 手控制](https://github.com/MihneaToader/RWR_control)

[绳索和电缆操纵规划的拓扑表示](https://github.com/UM-ARM-Lab/mjregrasping)

[适用于 ROS 机器人的 FastRLAP 实现、相关的 Gazebo 环境，以及用于越野驾驶的 MuJoCo 环境](https://github.com/kylestach/fastrlap-release)

[一款一体化 ROS 软件包 RoTools](https://github.com/DrawZeroPoint/RoTools) - 用于高级机器人任务调度、视觉感知、路径规划、仿真以及直接/远程操控。它利用 BehaviorTree 实现快速的任务构建和协调，并提供各种实用程序来弥合真实/模拟机器人与高级任务调度程序之间的差距。


## 世界模型  <span id="world_model"></span>

[解耦世界模型：学习从干扰视频中迁移语义知识以进行强化学习](https://github.com/qiwang067/DisWM)

[克服知识障碍：通过预训练世界模型进行观察的在线模仿学习](https://github.com/argmax-ai/aime-v2)

[克服知识障碍：利用预训练世界模型进行视觉观察的在线模仿学习](https://github.com/IcarusWizard/AIME-NoB)

[分层世界模型能够实现跨多个时间尺度的推理](https://github.com/CognitiveModeling/THICK)

[一种基于视觉模型的强化算法 Dreamer](https://github.com/adityabingi/Dreamer) - 它学习一个世界模型，该模型从高级像素图像中捕捉潜在动态，并完全在从学习到的世界模型中想象的部署中训练控制代理

[去噪 MDP：比世界本身更好地学习世界模型](https://github.com/facebookresearch/denoised_mdp)

[研究世界模型中时空信息的理解](https://github.com/hironona/world-language-grounding)

[预训练以机器人为中心的世界模型以实现高效的视觉控制](https://github.com/robo-centric-wm/robo-centric-world-model)

[用机械可解释性研究 OthelloGPT 世界模型学习](https://github.com/Jim-Maar/interpretability)

[个人实验工作场所，用于研究世界建模理念](https://github.com/elilaird/dino_wm)

[通过最大化证据进行行动推断：通过世界模型进行观察的零样本模仿](https://github.com/Zoefia/Zoefia-aime-extrapolation) - [其他]((https://github.com/argmax-ai/aime))


## 强化学习 <span id="rl"></span>

[利用强化学习改进膝关节生物力学建模的新方法](https://github.com/NikonPic/DynamicOpt)

[使用 OpenAI Gym 环境的 xArm6 机器人强化学习框架](https://github.com/julio-design/xArm6-Gym-Env) - 该模型使用深度确定性策略梯度(DDPG) 进行连续动作，并使用后见之明经验回放(HER)

[OGBench 是一个基准测试，旨在促进离线目标条件强化学习 (RL)、离线无监督强化学习和离线强化学习中的算法研究](https://github.com/devinluo27/ogbench_cpdfu_release) - [其他1](https://github.com/qasim-ali0/ModelBasedContrastiveRL)

[基于双视野模型的策略优化 (DHMBPO)](https://github.com/4kubo/erl_lib)

[四足动物-斯坦福小狗文档和训练学习者](https://github.com/Prakyathkantharaju/Quadruped)

[强化学习算法的最小实现及其他强化学习相关实验](https://github.com/PierreLaur/rl_experiments)

[ActSafe：强化学习中具有安全约束的主动探索](https://github.com/yardenas/actsafe)

[RL 控制和预测方法的实现（PyTorch 中的 DRL）](https://github.com/MythraV/rl_lib)

[基于技能的基于模型的强化学习](https://github.com/clvrai/skimo)

[gym上强化学习的一些实现](https://github.com/paoyw/RL_gym)

[基于运动原语的 RL 算法的测试设置](https://github.com/freiberg-roman/mp-rl)

[新兴合作伙伴模型](https://github.com/ruaridhmon/emergent_partner_modelling)

[使用 Openai-gym 进行强化学习](https://github.com/ashiskb/RL-workspace)

[基于因果模型的强化学习工具包](https://github.com/polixir/causal-mbrl)

[从头开始实现 rl2](https://github.com/neverparadise/RL2_from_scratch)

[不同 RL 和轨迹优化算法的实现](https://github.com/Daniellayeghi/Mujoco_Python_Sandbox)

[在 OpenAI Gym 环境中为超级马里奥兄弟实现强化学习](https://github.com/sampadk04/openai-super-mario-bros) - 使用近端策略优化 (PPO) 算法

[基于模型的连续强化学习中的随机值梯度](https://github.com/facebookresearch/svg)

[RL-Project](https://github.com/AntonFlorey/RL-Project)

[基于状态扰动的无模型强化学习探索](https://github.com/Curiouskid0423/rho_exploration)

[强化学习](https://github.com/murataliev/reinforcement_learning)

[RL_project_2022](https://github.com/oselin/RL_project_2022)

[16831_RL_trading](https://github.com/quantingxie/16831_RL_trading)

[rl_project](https://github.com/fabioscap/rl_project)

[不同深度 Q 网络的有效性研究](https://github.com/00ber/Deep-Q-Networks)

[使用 Policy-Gradient 方法在 OpenAI-Gym 中训练代理](https://github.com/till2/policy-gradient-methods)

[CQL_AWAC_ICQL](https://github.com/bvanbuskirk/CQL_AWAC_ICQL)

[基于 DDPG Keras实现示例的 TD3](https://github.com/jnachyla/usd-proj)

[基于 PyTorch 构建的强化学习算法的实现](https://github.com/kartik2309/RLPack) - 它已针对高负载工作负载进行了优化，后端支持 CUDA 和 OpenMP（取决于硬件可用性）

[模块化单文件强化学习算法库](https://github.com/sdpkjc/abcdrl)

[rl](https://github.com/meinczinger/rl)

[保守 Q 学习 (CQL)](https://github.com/Songlm3/CQL)

[Pytorch 实现的 MuZero 用于 Gym 环境](https://github.com/DHDev0/Muzero) - 支持动作空间和观察空间的任何离散、Box 和 Box2D 配置

[基于 Tensorflow 的 DDPG 实现](https://github.com/alexsandercaac/DDPG-Tensorflow) - 使用 DVC 跟踪管道进行实验

[极限 Q 学习：无熵的最大熵强化学习](https://github.com/Div99/XQL)

[利用奖励序列分布进行视觉强化学习的泛化](https://github.com/MIRALab-USTC/RL-CRESP)

[用于稳健深度强化学习的状态对抗性 PPO](https://github.com/Aortz/SA-PPO)

[使用 PPO 训练 SNS](https://github.com/DrYogurt/SNS-PPO)

[OpenAI Gym 环境的强化学习代理](https://github.com/prestonyun/GymnasiumAgents)

[rl](https://github.com/rishiagarwal2000/rl)

[使用深度 Q 学习训练一个代理，让它在一个大的方形环境中收集尽可能多的黄色香蕉](https://github.com/m-fili/DeepQLearning)

[使用基于策略的方法解决 CartPole 问题](https://github.com/m-fili/CartPole_HillClimbing)

[使用交叉熵的连续山地车](https://github.com/m-fili/CrossEntropy)

[强化学习算法的清晰框架和实现](https://github.com/wzcai99/XuanCE-Tiny)

[强化学习 RAINBOW 算法的部分（重新）实现](https://github.com/Dzirik/RAINBOW)

[使用 REINFORCE 算法解决 CartPole](https://github.com/m-fili/reinforce_cartpole)

[探索无模型等变强化学习在运动中的应用](https://github.com/chengh-wang/BBQ)

[基于图像的循环强化学习](https://github.com/CRosero/imgrerl)

[PPOimplementation](https://github.com/Porthoos/PPOimplementation)

[一种解决reacher环境的DDPG算法](https://github.com/m-fili/Reacher_DDPG)

[Q 值函数作为障碍函数](https://github.com/dtch1997/ql_clbf)

[模块化可扩展强化学习](https://github.com/Catwork-LLC/clowder)

[Transformer 作为深度强化学习的骨干](https://github.com/maohangyu/TIT_open_source)

[学徒强化第二阶段](https://github.com/CafeKrem/internship_DL_project)

[使用 Gymnasium 简单实现 PPO](https://github.com/KJaebye/ppo-mujoco)

[TD3](https://github.com/LTBach/TD3)

[reinforcement_learning_dataframe_matching](https://github.com/lhcnetop/reinforcement_learning_dataframe_matching)

[基础设施目标条件强化学习者](https://github.com/spyroot/igc)

[基于OpenAI Spinning Up和Stable-Baseline3的 PPO 实现](https://github.com/realwenlongwang/PPO-Single-File-Notebook-Implementation)

[多目标最大后验策略优化](https://github.com/ToooooooT/MOMPO)

[一种基于弱奖励信号进行奖励设计的方法](https://github.com/abukharin3/HERON)

[强化学习项目](https://github.com/JereKnuutinen/Reinforcement_learning_project)

[使用强化学习方法扩展状态空间控制方法](https://github.com/RX-00/ext_ctrl)

[Reaching_RL](https://github.com/TejoramV/Reaching_RL)

[离散扩散 Q 学习](https://github.com/dxwhood/honours-thesis)

[通过基于强化学习的调度实现安全高效的多系统神经控制器](通过基于强化学习的调度实现安全高效的多系统神经控制器)

[通过自适应策略正则化实现高效的现实世界强化学习，实现腿部运动](https://github.com/realquantumcookie/APRL)

[通过情景控制进行安全强化学习](https://github.com/lizhuo-1994/saferl-ec)

[通过随机模拟进行强化学习](https://github.com/famura/SimuRLacra)

[基于模型的 RL 算法 PlaNet 的 PyTorch 实现](https://github.com/smmislam/pytorch-planet)

[基于模型的强化学习跳跃者](https://github.com/caiopetruccirosa/hopper-walker-model-based-rl)

[少样本离域动态强化学习中的迁移保守方法](https://github.com/PaulDaoudi/FOOD)

[在 MuJoCo 中实现的开源强化学习环境与 Franka 机械臂](https://github.com/learningLogisticsLab/franka_mujoco)

[用于样本有效目标条件强化学习的度量残差网络](https://github.com/Cranial-XIX/metric-residual-network)

### DQN  <span id="dqn"></span>

[扩展深度 Q 网络模型以支持多模态输入](https://github.com/alexbaekey/DeepRL-multimodal)

[将各种改进与强化学习算法相结合](https://github.com/Deonixlive/modulated-DQN) - 试图遵循三个关键原则：数据效率、可扩展性和更快的训练速度

[基于深度 Q 网络的 TensorFlow 2 强化学习实现](https://github.com/metr0jw/DeepRL-TF2-DQN-implementation-for-TensorFlow-2)

[Atari 2600 游戏深度 Q 网络算法的重新实现及对比分析](https://github.com/rullo16/DRLAtari)

[在不同的环境下研究（深度）Q 学习算法并测量我们代理的性能](https://github.com/yasirbarlas/tabular-deep-reinforcement-learning)

[隐式 Q 学习泛化能力评估](https://github.com/Juan5713/CSE3000)

[麦克劳林扩展极限 Q 学习 (MXQL)](https://github.com/motokiomura/MXQL)

[双重和决斗 Q 学习，结合优先经验回放缓冲区和内在好奇心模块，用于 Atari 游戏的强化学习](https://github.com/JvanZyl1/AtariRL)

[基于视觉的端到端机器人抓取，使用 DQN 在 mujoco 环境中进行训练](https://github.com/AvalonGuo/grasprl)

[PyTorch 中的隐式 Q 学习 (IQL)](https://github.com/lihaomin1010/data-expert)

[在 lunarlander 和 bipedalwalker 上测试的 DQN 和 DDPG 的 PyTorch 实现](https://github.com/YingXu-swim/lunarlander-bipedalwalker)

[targeted-double-q-learning](https://github.com/alishiraliGit/targeted-double-q-learning)

[Q学习在二十一点中的应用](https://github.com/mishonenchev/BlackJackAI)

[重症监护应用的多准则深度 Q 学习](https://github.com/alishiraliGit/multi-criteria-deep-q-learning)

[面向重症监护应用的安全领域知识辅助深度强化学习](https://github.com/notY0rick/multi_criteria_dqn)

[dqn-探索-集成](https://github.com/pranavkrishnamoorthi/dqn-exploration-ensemble)

[targeted-double-q-learning](https://github.com/alishiraliGit/targeted-double-q-learning)

[使用 OpenAI gym 环境训练 DQN 的简单脚本](https://github.com/eyalhagai12/simple_dqn)

[DQN_AC](https://github.com/bvanbuskirk/DQN_AC)

### AC <span id="ac"></span>

[软动作者-评论家：基于随机动作者的离线策略最大熵深度强化学习](https://github.com/DSSC-projects/soft-actor-critic)

[用于机器人环境交互任务的演员-评论家模型预测力控制器的实验验证](https://github.com/unisa-acg/actor-critic-model-predictive-force-controller)

[SAC](https://github.com/LTBach/SAC)

[使用Pytorch实现优化的SAC算法](https://github.com/nvan21/Optimized-SAC)

[使用 mypy 输入软行动者-评论家 (SAC) 算法](https://github.com/biegunk/soft-actor-critic-pytorch)

[对安全强化学习的软演员-评论家 (SAC) 算法的修改，结合概率推理来强制执行安全约束，同时保持有效的探索](https://github.com/PabloLah/Probabilistic-Inference-for-Safe-RL)

[强化学习软演员评论家算法教程](https://github.com/khhandrea/python-RL-SAC)

[JSAC 是一个基于软演员-评论 (SAC) 的强化学习 (RL) 系统，旨在实现高性能且稳定的图像学习](https://github.com/fahimfss/JSAC)

[质量-多样性行动者-评论家：通过价值和后继特征评论家学习高性能和多样化行为](https://github.com/adaptive-intelligent-robotics/QDAC)

[UE5 SAC](https://github.com/ryutyke/Learning-To-Get-Up)

[针对 CS285 的深度 Q 学习、Actor Critic 和 Soft Actor Critics 算法的实现](https://github.com/phongtheha/Reinforcement-Learning)

[自软演员-评论家的 SAC 的确定性变体：具有随机演员的离线策略最大熵深度强化学习](https://github.com/pvd6048/DA221M-Course-Project-in-Reinforcement-Learning)

[实施监督 Actor-Critic 策略提炼作为其他迁移学习 RL 方法的基础](https://github.com/andbalch/policy-distillation)

[实现的主要算法是 Soft Actor-Critic (SAC)](https://github.com/tomaskak/neural)

[强化学习的数学基础项目 03 - 连续控制](https://github.com/radajakub/soft-actor-critic)

### PPO <span id="ppo"></span>

[ppo-mujoco](https://github.com/hyln/ppo-mujoco)

[为 Cassie 机器人重新实现 PPO 算法](https://github.com/alhussein-jamil/CassieRobot)

[RNN + PPO pytorch 实现](https://github.com/Amaranth819/RecurrentPPO)

[人工生命模拟器](https://github.com/Limonka11/ArtificialLifeSimulator) - 结合了 PPO 和进化算法

[训练 PPO 代理学习Cart Pole 游戏](https://github.com/seba2390/ProximalPolicyOptimization)

[在 OpenAI gym 中从 Ant-v4 环境衍生的自定义环境中实现 PPO，以学习穿越模板障碍](https://github.com/Ketan13294/PPO-ant)

### 多智能体 <span id="multi_agent"></span>

[个别奖励扶助的多智能体强化学习](https://github.com/MDrW/ICML2022-IRAT)

[多任务参与者评论家学习](https://github.com/anzeliu/multitask_actor_critic_learning)

[JAX 中的分布式多智能体强化学习](https://github.com/instadeepai/Mava)

[用于合作多智能体强化学习的 E3-等变演员-评论家方法](https://github.com/dchen48/E3AC)

[基于噪声分布分解的多智能体分布式强化学习](https://github.com/gengwei479/NoiseDistributionDecomposition)

[学习多智能体强化学习的最佳任务分解](https://github.com/thomasychen/LOTaD)

[利用合作多智能体强化学习进行工厂操作](https://github.com/nkirschi/Factory-MARL)

[合成奖励机器用于合作多智能体强化学习](https://github.com/giovannivarr/MARM-JAIR-code)

[多智能体竞赛](https://github.com/KJaebye/Multiagent-Race)

[INS：交互感知合成，增强离线多智能体强化学习](https://github.com/fyqqyf/INS)

[MARIE - 多智能体自回归想象高效学习](https://github.com/breez3young/MARIE)

[通过智能信息聚合实现可扩展（且强大？）的多智能体强化学习](https://github.com/huiwenn/RobustMARL)

[DoF：用于离线多智能体决策的扩散因子分解框架](https://github.com/xmu-rl-3dv/DoF)

[多智能体扩散模型](https://github.com/dayiethan/CTDE_Diffusion)

[使用 JAX 进行多智能体强化学习](https://github.com/FLAIROx/JaxMARL)

[学习多智能体强化学习的最佳任务分解](https://github.com/thomasychen/base-multi-rm)

[多智能体合作过程中通过潜在想象的心理理论](https://github.com/Davidt98/R2I_ToM_MAPPO)

[多智能体强化学习算法](https://github.com/RahulBoipai/MADDPG-pettingzoo-pytorch)

[MADiff：基于扩散模型的离线多智能体学习](https://github.com/zbzhu99/madiff)

[PyTorch 和 Ray 用于分布式 RL](https://github.com/fatcatZF/rayrl-atari)



### 模仿学习 <span id="imitation"></span>

[7 自由度机械臂拾取和放置，具有模仿学习功能](https://github.com/Himanshu12328/7DOF_Robotic_Manipulation_IL)

[通过语境翻译进行观察模仿](https://github.com/medric49/imitation-from-observation) - 一种基于演示训练代理模仿专家的算法

[多任务模仿学习](https://github.com/chanb/mtil)

[从人类示范中学习操纵技能](https://github.com/aai4r/aai4r-pouring-skill)

[通过精确标记的人类演示进行模仿学习](https://github.com/yilongsong/action_extractor)

[TamedPUMA：利用几何织物进行安全稳定的模仿学习](https://github.com/tud-amr/pumafabrics)

[250美元机械臂的模仿学习](https://github.com/Ryan-GRY/ACT_lcb)

[通过人类远程操作实现人形机器人的深度模仿学习](https://github.com/UT-Austin-RPL/TRILL)

[通用模仿学习的进化策略](https://github.com/SilviaSapora/evil)

[模仿引导强化学习](https://github.com/hengyuan-hu/ibrl)

[扩散状态和匹配分数：模仿学习的新框架](https://github.com/ziqian2000/SMILING)

[JAM：使用 TM12 机械臂进行模仿学习](https://github.com/atticus453/Robot-Magic-TM12)

[KOI：通过混合关键状态指导加速在线模仿学习](https://github.com/GeWu-Lab/Keystate_Online_Imitation)

[使机械臂模仿另一只手臂的方向](https://github.com/Kisfodi/MimicArm)

[JAM：使用 TM12 机械臂进行模仿学习](https://github.com/kevin20021214/Robot-Magic-TM12)

[AdaFlow：基于方差自适应流策略的模仿学习](https://github.com/hxixixh/AdaFlow)

[使用基于 iPhone 的低成本机械臂远程操作进行模仿学习](https://github.com/trzy/robot-arm)

[通过模仿行为来理解大脑](https://github.com/jimzers/DSC180B-A08)

[Milo 是一个 Python 库，旨在简化强化学习 (RL) 和模仿学习 (IL) 任务](https://github.com/jacr13/Milo)

[利用扩散模型作为高表达性的策略类别，用于行为克隆和策略正则化](https://github.com/ep-infosec/21_twitter_diffusion-rl)

[模仿预训练](https://github.com/davidbrandfonbrener/imitation_pretraining)

[模仿学习](https://github.com/scottsus/imitation_learning)

[柔性机器人非线性模型预测控制的安全模仿学习](https://github.com/shamilmamedov/flexible_arm)

[Imitation-Learning](https://github.com/vsreyas/Imitation-Learning)

[graph_offline_imitation](https://github.com/Kavka1/graph_offline_imitation)

[易于运行的模仿学习和强化学习框架](https://github.com/Ericonaldo/ILSwiss)

[四足动物行为克隆实验](https://github.com/dtch1997/quadruped-bc)

[通过行为学习进行观察模仿](https://github.com/medric49/ifobl)

### 分层强化学习 <span id="hierarchy"></span>

[使用 Pytorch、OpenAI Gym 和 Mujoco 进行机器人分层强化学习](https://github.com/mrernst/hrl_robotics_research)

[hierarchy_Reinforcement_Learning](https://github.com/yourlucky/hierarchy_Reinforcement_Learning)

[分层强化学习](https://github.com/yourlucky/Picker-Hierarchical-RL)

[使用 Kinova 臂进行分层 RL，在桌面上解决汉诺塔问题](https://github.com/tuftsrchuff/robosuite_kinova_HRL)

[修改为支持带有步骤（动作，目标）的分层学习](https://github.com/kavuturuyeswanth/Gynasium-RoboticsModified)

[分层元强化学习](https://github.com/Mgineer117/himeta)

[Grid World中的分层强化学习 (HRL)方法](https://github.com/Mgineer117/WINTER)

[通过分层强化学习重新思考决策转换器](https://github.com/mamengyiyi/Autotuned-Decision-Transformer)

[通过逆向优化实现离线分层强化学习（OHIO）的正式实现](https://github.com/carolinssc/OHIO)

[通过关键节点调整子目标以实现离线分层强化学习](https://github.com/qortmdgh4141/ASK)

[分层隐式 Q 学习](https://github.com/skylooop/GOTIL)

[测试稳定比例微分控制器中 mujoco 的 SPD 实现](https://github.com/rohit-kumar-j/SPD_Controller_Mujoco)

### 分布式强化学习  <span id="distributed"></span>

[学习竞赛：分布式强化学习与优化](https://github.com/BrandonBian/l2r-distributed)

[强化学习的高性能分布式训练框架](https://github.com/PaddlePaddle/PARL)

[Stellaris：基于无服务器计算的陈旧感知分布式强化学习](https://github.com/IntelliSys-Lab/Stellaris-SC24)

[RIZE：通过分布式强化学习进行正则化模仿学习](https://github.com/adibka/RIZE)

[在 Hadoop 集群中使用 Ray 和 RLlib 进行分发的预部署](https://github.com/UnaiLaconcha/Distributed-RL)

[具有重要性加权参与者-学习者架构的可扩展分布式深度强化学习](https://github.com/KSB21ST/IMPALA_memory_maze)


### 离线强化学习 <span id="off_line_rl"></span>

[离线强化学习算法](https://github.com/stanford-iris-lab/d5rl) - [其他1](https://github.com/d5rlrepo/d5rl) 、[其他2](https://github.com/d5rl/d5rl) 、 [其他3](https://github.com/d5rlbenchmark/d5rl)

[从完全离线策略数据中学习](https://github.com/dldnxks12/Offline-RL)

[使用新颖的 Hyena 连续卷积核作为 Transformer 的替代方案，以便在离线强化学习中高效地捕捉长距离依赖关系](https://github.com/andrewliu2001/hpml-project)

[使用 Transformer 模型的离线训练在元学习环境中执行上下文强化学习](https://github.com/ethanabrooks/in-context-rl)

[Unifloral：统一离线强化学习](https://github.com/EmptyJackson/unifloral)

[通过 Tsallis 正则化进行离线强化学习](https://github.com/lingweizhu/tsallis_regularization)

[可行区域自限制：离线强化学习中策略优化的新方法](https://github.com/zhushi-math/OPVP3)

[基于扩散模型的离线强化学习约束策略搜索](https://github.com/felix-thu/DiffCPS)

[基于可行性引导扩散模型的安全离线强化学习](https://github.com/kevvvvin21/CSE537ProgressReport)

[OGBench：离线目标条件强化学习基准测试](https://github.com/ShadowNinja10/HIQL_pushT)

[离线目标条件强化学习基准测试](https://github.com/seohongpark/ogbench)

[利用离线强化学习算法解决三指任务的实现](https://github.com/splendidsummer/Trifinger_Offline_RL)

[离线强化学习的扩散策略](https://github.com/Zhendong-Wang/Diffusion-Policies-for-Offline-RL)

[保守离线策略评估的幻觉控制](https://github.com/tobiabir/hambo)

[离线强化学习作为一个大序列建模问题的代码发布](https://github.com/eduruiz00/sadrl-project)

[HIQL：以潜在状态为行动的离线目标条件强化学习](https://github.com/seohongpark/HIQL)

[符合道德规范的 rl](https://github.com/MasonN808/ethically-compliant-rl)

[使用封闭式策略改进算子的离线强化学习](https://github.com/cfpi-icml23/cfpi)

[离线深度强化学习中的数据集审计](https://github.com/link-zju/ORL-Auditor)

[Soft Actor-Critic 中的 SAC：基于随机参与者的离线策略最大熵深度强化学习](https://github.com/d3ac/sac)

### 逆强化学习 <span id="inverse_rl"></span>

[通过贝叶斯心理理论进行稳健逆强化学习](https://github.com/ran-weii/btom_irl)

[机器人手部操作任务的逆向强化学习](https://github.com/saqib1707/RL-Robot-Manipulation)

[利用逆向强化学习简化约束推理](https://github.com/ahugs/simple-icrl)

[CleanIL 是一个深度模拟和逆向强化学习库](https://github.com/ran-weii/cleanil)

[包含逆向强化学习算法的 JAX 实现](https://github.com/FLAIROx/jaxirl)

[Inverse_RL](https://github.com/werkaaa/Inverse_RL)


### 元强化学习 <span id="meta_rl"></span>

[评估复杂任务分布中的元强化学习算法](https://github.com/mhelabd/Meta-RL)

[解决元强化学习中的上下文解耦问题](https://github.com/FrankTianTT/INTACT)

[约束元强化学习，用于可微分凸规划的自适应安全保障](https://github.com/Mgineer117/Meta-CPO)

[人人皆可学习的元学习](https://github.com/ChoiDae1/Meta-learning-Study)

[元学习是一种可进化的编码发展](https://github.com/miltonllera/meta-evolved-dev)

[PAC-贝叶斯离线元强化学习](https://github.com/outshine-J/PAC-Bayesian-Offline-Meta-Reinforcement-Learning)

[模型不可知元学习（MAML）应用于强化学习](https://github.com/GuillaumeEng/easy_maml)

[Meta QLearning 实验优化机器人步行模式](https://github.com/gokulp01/meta-qlearning-humanoid)

[Meta-World 是一个开源的元强化学习和多任务学习模拟基准，包含 50 个不同的机器人操作任务](https://github.com/bmcmahan2016/metaworld)

[利用潜在动力学进行元强化学习的任务信念相似性学习](https://github.com/mlzhang-pr/SimBelief)

[利用概率推理和元学习解决持续长期规划问题](利用概率推理和元学习解决持续长期规划问题)

[Meta-World 是一个开源基准，用于开发和评估用于连续控制机器人操作环境的多任务和元强化学习算法](https://github.com/Farama-Foundation/Metaworld) - [其他1](https://github.com/fcas/Metaworld)

[基于技能的领域转移元强化学习](https://github.com/GarlicWang/RL_2023_Fall)

[元强化学习的进化储层](https://github.com/corentinlger/ER-MRL)

[具有稳健分布在线任务自适应的成本感知离线安全元强化学习](https://github.com/ApocalypseX/COSTA)

[元学习好奇心算法](https://github.com/Ziksby/MetaLearnCuriosity)

[Optm-MetaRL](https://github.com/LucienJi/OptmMeta-RL)

[分布式分层元强化学习器](https://github.com/spyroot/DH-MAML)


## 感知 <span id="perception"></span>

[肌肉骨骼轨迹追踪](https://github.com/17arhaan/Movement_Tracking_Mujoco)

[物体检测与追踪](https://github.com/GUVENAli/yolov5-object-detection-tracking)

[双手操作的人类视觉](https://github.com/ian-chuang/human-vision?tab=readme-ov-file)

[利用物理运动定律从二维标签学习单目三维物体定位](https://github.com/KieDani/Towards_3D_Object_Localization)

[利用“任何事物分割”模型进行通用视觉强化学习](https://github.com/wadiuvatzy/SAM-G)

[盲文识别](https://github.com/takaya-hirano-hayashibeLabo/braille-recognition)

[探索双手机器人操作中的主动视觉](https://github.com/Soltanilara/av-aloha)

[SmoothMoCapRetarget 将人体运动捕捉数据转换为人形机器人流畅且运动学上可行的轨迹](https://github.com/YiyangShao2003/SmoothMoCapRetarget)

[在 Atari Pong 游戏上使用各种视觉模式训练和评估不同的深度强化学习代理](https://github.com/andresnowak/pong_vision_master)

[动作捕捉环境](https://github.com/hartikainen/mocap-environments)

[模拟具身智能体同时发展眼部形态和神经处理的环境，揭示了视觉系统进化的复杂过程](https://github.com/cambrian-org/ACI)

### 触觉 <span id="tactile"></span>

[证明在抓取的软捕获阶段使用触觉传感器的重要性](https://github.com/baha2r/Soft_Capture_Tactile)

[配备视觉和触觉感知的 MuJoCo 机器人环境集合](https://github.com/carlosferrazza/tactile_envs)

[通过技能库和触觉表征进行语义-几何-物理驱动的机器人操作技能转移](https://github.com/MingchaoQi/skill_transfer)

[通过在触摸传感器之间进行跨模态预测](https://github.com/MMintLab/touch2touch)

[通过虚拟手与可变形物体进行交互和抓取，以增强手术模拟效果](https://github.com/Carlo1109/Soft-Touch)

[M2VTP 是一个专为视觉-触觉融合而设计的预训练网络](https://github.com/LQTS/Pretraining_for_M2VTP)

[基于胡须的触觉导航系统](https://github.com/SVDouble/RatteChan)

[基于指尖接触感知采样的抓取生成器](https://github.com/W567/FSG)

[VTDexManip：用于视觉触觉预训练和基于强化学习的灵巧操作的数据集和基准](https://github.com/LQTS/VTDexManip)

[训练 Shadow Hand 机器人在 MuJoCo 模拟中操控笔](https://github.com/br23aay/shadowhand-dexterity-ppo)

[使用 NeuroMechFly v2 模拟果蝇具体感觉运动控制](https://github.com/NeLy-EPFL/flygym) - 包括生嗅觉、腿部粘附等

[通过触觉反馈遥操作系统双手机器人的几个演示来学习变量柔顺控制](https://github.com/omron-sinicx/CompACT)

[通过 ROS 集成，在 MuJoCo 中对 DexRobot 手进行触觉模拟](https://github.com/DexRobot/dexrobot_mujoco) - 支持 MuJoCo 原生触摸传感器和 TaShan 11 维触觉传感器，有视频效果

[一个关于连接触觉设备、VR 耳机和物理模拟以模拟可变形物体的实时触摸的研究项目](https://github.com/SkytAsul/DeformableSimulation)


## 规划 <span id="planning"></span>


[使用基于激光的感知在 MuJoCo 环境中实现人机感知移动机器人导航的强化学习框架](https://github.com/otr-ebla/MuJoCo_HumanAware_MobileRobot_RLNavigation)

[外展机器人学习决策](https://github.com/chrisyrniu/neurips22_outreach_robot_learning_for_decision_making)

[使人工智能能够像处理人类语言一样解释和规划机器人行为](https://github.com/yhbcode000/soft-rob-embedding)

[CIST-GCN：可解释的人体运动预测](https://github.com/QualityMinds/cistgcn)

[MoCapAct和dm_control的扩展，用于避障任务](https://github.com/Team-Zircon/ZirconProject)

[使用 Graph Transformer 规划装配序列](https://github.com/AIR-DISCOVER/ICRA_ASP)

[虚拟工厂环境中的自主Transpalet导航项目](https://github.com/erdnj/Robotics)

[通过物理模拟实现手与物体交互的稳定姿态估计](https://github.com/rongakowang/DeepSimHO)

[风险感知深度强化学习在机器人群体导航中的应用](https://github.com/QZhSSLab/RADR)

[动作稳健决策transformer](https://github.com/afonsosamarques/action-robust-decision-transformer)

[通过对不确定道路系统进行持续数据收集来进行路线优化](https://github.com/BroknLogic/dmaProject) - 包裹递送算法，使其能够在更新道路系统信息的同时安排递送。

[用于欠驱动机器人手的硬件/软件协同优化](https://github.com/adikulkarni11/Underactuated-Robotic-Hands)


## 控制 <span id="control"></span>

[基于对比示例的控制](https://github.com/khatch31/laeo)

[机器人蛇形运动](https://github.com/alexandrubalotescu/Robot-Snake-Locomotion)

[MPC_MBPO](https://github.com/bvanbuskirk/MPC_MBPO)

[为 Franka Emica Panda 机械手实施的模型预测控制](https://github.com/tomasz-naklicki/Panda_MJ_MPC)

[用于微调底层机器人动作的DPO](https://github.com/kenma8/dpo_robotics)

[基于强化学习的双轮足平衡机器人控制](https://github.com/aa4cc/sk8o-rl)

[基于 RL 的 6 自由度机械臂逆运动学控制](https://github.com/Pranav-Malpure/B-Tech-Project)

[眼动视觉伺服系统](https://github.com/ColeDewis/Eyetracker-Visual-Servoing)

[连续控制算法的基本实现](https://github.com/Bowen-He/Bowen-Implementation-DDPG-TD3-SAC)

[学习使用 2-DoF 夹持器进行力控制](https://github.com/llach/learning_fc)

[通过在连接每条腿的两个连杆和躯干的八个铰链上施加扭矩来协调四条腿向前移动](https://github.com/ake1999/TD3_Ant_v4)

[探索关节空间中潜在地标](https://github.com/dtch1997/latent-landmarks)

[用于调试应用于 mujoco 模型的控制器实现](https://github.com/peterdavidfagan/mujoco_controllers)

[简化 Mujoco 中机械手的设置和控制](https://github.com/ian-chuang/Manipulator-Mujoco)

[CMU 16-831 机器人学习简介的作业](https://github.com/dhanvi97/16831_RL)

[带手掌的四轴控制器，包括 RL 控制器和 IK 控制器](https://github.com/Prakyathkantharaju/test_walking_with_palm)

[ Kinova Gen3 机器人控制](https://github.com/jerrywrx/kinova_control)

[如何更改加载模型中指定的执行器](https://github.com/lvjonok/mujoco-actuators-types)

[为 Allegro Hand（一款拥有 16 个独立可控关节的机械手）实现了比例积分微分 (PID) 控制器](https://github.com/premtc/Human_Robot_Hand_Grasping_Mujoco)

[利用强化学习和 VAE 控制千足虫](https://github.com/savanagrawal/Millipede-Control-with-Reinforcement-Learning-and-VAEs)

[刚体操作](https://github.com/barikata1984/rigid-body-manipulation)

[倒立摆](https://github.com/dhruvthanki/mj_InvertedPendulum) - 使用基于优化的操作空间控制来跟踪双摆的末端执行器位置


## 测试 <span id="test"></span>

[评估了 RL 领域的特征提取](https://github.com/clement-chupin/BenchNeuralNework)

[l2r 基准测试](https://github.com/arav-agarwal2/l2r-benchmarks)

[Mujoco测试平台](https://github.com/AIRLABkhu/MujocoTestbed)

[用于测试/评估 mujoco 物理模拟器的沙盒](https://github.com/implementedrobotics/mujoco-sandbox)

[创建 Kinfer 文件以测试 Kscale 机器人功能](https://github.com/kscalelabs/kinfer-unit-tests)

[将Humanoid-gym框架评估其他人形机器人（以H1为例）](https://github.com/Chenhui98/Apply-humanoid-gym-to-other-robots)

[offline_rl_benchmark_by_argo](https://github.com/hjcwuhuqifei/offline_rl_benchmark_by_argo)

[验证gymnasium_roboticsmujoco 环境的 MuJoCo 模型变化](https://github.com/Kallinteris-Andreas/gym-mjc-v5-model-validation) - [其他](https://github.com/Kallinteris-Andreas/gymnasium-mujuco-v5-envs-validation)

[rl-test](https://github.com/Oyveloper/rl-test)

[CQL，PDQN，离线RL评估](https://github.com/zhuhxi/DriverOrderOfflineRL)

[使用来自 4 个种子的 Mujoco Benchmark 结果对 SAC、TD3 和 TD7 进行 pytorch 实现](https://github.com/seungju-k1m/sac-td3-td7)

[PPO-Wipe-Excercise](https://github.com/AbhinavPeri/PPO-Wipe-Excercise)

[TSP 或基于地形的切换](https://github.com/ShreelekhaR/TerrainBasedSwitching)

[USD](https://github.com/nkvch/USD)

[用于 RL 实验的模块化基准测试程序](https://github.com/athkand/Benches)

[视觉泛化的强化学习基准](https://github.com/gemcollector/RL-ViGen)

[专注于使用稳定基线 3方法和Gymnasium界面进行目标条件强化学习](https://github.com/Scilab-RL/Scilab-RL) - [其他](https://github.com/meppe/Scilab-rl)

[GUARD ：通用统一安全强化学习开发基准](https://github.com/intelligent-control-lab/guard)

[d4rl-slim-benchmark](https://github.com/dtch1997/d4rl-slim-benchmark)

[mujoco_test](https://github.com/Geryyy/mujoco_test)

[TEST](https://github.com/amine0el/TEST)

[Safety-Gymnasium：统一的安全强化学习基准](https://github.com/PKU-Alignment/safety-gymnasium)

[机器人优化基准](https://github.com/dawsonc/robotics_optimization_benchmarks)

[RLXBench](https://github.com/oladayosolomon/RLXBench)

[mujoco-motoman-test](https://github.com/DanManN/mujoco-motoman-test)

[BenchSuite](https://github.com/LeoIV/BenchSuite)

[使用 PyTorch 的 functorch 的稳定基线](https://github.com/functorch/sbft)

[l2r 基准测试](https://github.com/learn-to-race/l2r-lab)

[针对机器人操作的基准测试集](https://github.com/xiangyanfei212/RMBench-2022)

## 数据 <span id="data"></span>

[用于模拟人形控制的多任务数据集](https://github.com/microsoft/MoCapAct)

[使用 MuJoCo 生成的数据集的 NeRF 的 Pytorch 实现](https://github.com/volunt4s/mujoNeRF)

[包含 Machines in Motion 实验室中使用的机器人描述](https://github.com/machines-in-motion/mim_robots)

[R2D2：住宅机器人演示数据集](https://github.com/zehanma/r2d2_autolab)

[域随机化示例](https://github.com/ugo-nama-kun/domain_randomization)

[MimicGen：使用人类演示的可扩展机器人学习的数据生成系统](https://github.com/NVlabs/mimicgen)

[用于离线强化学习的组合合成数据生成](https://github.com/spatank/compositional-rl-synth-data)

[结果分享](https://github.com/ykh6581394/resultshare)

[训练或发展可控且多样化的级别生成器](https://github.com/smearle/control-pcgrl)

[可变形物体操控沙盒](https://github.com/nicholasprayogo/dom_sandbox)




## 大模型 <span id="llm"></span>


[利用言语纠正来提升机器人在执行复杂的长期任务时的表现](https://github.com/yay-robot/yay_robot)

[利用人类反馈实现大型语言模型的奖励进化](https://github.com/RishiHazra/Revolve)

[通用机器人和具体化人工智能学习的生成世界](https://github.com/Genesis-Embodied-AI/Genesis)


[基于迭代策略细化的大型语言模型感觉运动控制](https://github.com/jtyska/llm-robotics-article)

[优化视觉-语言-动作模型：提升速度和成功率](https://github.com/hanyangclarence/openvla-oft)

[面向长远强化学习的 LLM 分解和奖励设计](https://github.com/tjvitchutripop/sds685-llm-long-horizon-rl)

[探究在定制机器人形态上进行微调时视觉-语言-动作模型的约束](https://github.com/andomeder/vla-finetuning-investigation)

[TinyVLA：机器人的视觉-语言-动作模型](https://github.com/HanshangZhu/vla-vlm-test)

[RoboMoRe：基于 LLM 的机器人协同设计，通过形态和奖励的联合优化](https://github.com/morphing-matter-lab/RoboMoRe)

[VLA-Cache：通过机器人操作中的自适应令牌缓存实现高效的视觉-语言-动作模型](https://github.com/siyuhsu/vla-cache)

[一种人辅助动作策略优化（HAPO）方法，以纠正交互失败并实现视觉-语言-动作（VLA）模型的稳定优化](https://github.com/bytedance/human_assisted_preference_optimization)

[用大型语言模型 (LLM) 进行感知、规划和动作生成](https://github.com/pbanavara/modular_vla_pipeline)

[微调视觉-语言-行动模型：优化速度和成功率](https://github.com/Lilins1/Openvla-opt) - [其他](https://github.com/hanyangclarence/openvla-oft)

[BadVLA：通过目标解耦优化对视觉-语言-动作模型进行后门攻击](https://github.com/Zxy-MLlab/BadVLA)

[具有内在空间推理的视觉-语言-行动模型](https://github.com/InspireVLA/Inspire-FAST)

[反射规划：多阶段长视界机器人操作的视觉语言模型](https://github.com/ggs2ggs/reflect-vlm)

[评估视觉-语言-动作（VLA）模型的泛化能力](https://github.com/qnoens/EvalGenCapVLA)

[OneTwoVLA：具有自适应推理的统一视觉-语言-动作模型](https://github.com/Fanqi-Lin/OneTwoVLA)

[使用了 langchain 与 ROS2（or TCP），基于提示工程对机器人操作方面的提示词内容进行了设计](https://github.com/GloamingBlue/robochain)

[微调视觉-语言-行动模型：优化速度和成功率](https://github.com/YY-GX/openvla-oft)

[使用 Robomimic 进行 LLM 引导拾放](https://github.com/prasadpr09/Reinforcement-learning--PickPlace)

[使用大型语言模型进行模仿学习的模拟数据集生成](https://github.com/TNA001-AI/SimPoser)

[VLA-RL：通过可扩展强化学习实现精通通用的机器人操作](https://github.com/GuanxingLu/vlarl)

[反馈就是你所需要的一切吗？在目标条件强化学习中利用自然语言反馈](https://github.com/uoe-agents/feedback-dt)

[基于流的扩散视觉-语言-动作模型](https://github.com/qingh097/openpi_fork)

[ImagineBench：通过大型语言模型评估强化学习](https://github.com/LAMDA-RL/ImagineBench)

[通过 Q 学习为 LLM 代理提供零样本最优决策能力](https://github.com/laq2024/MLAQ)

[TeaMs-RL：通过强化学习教授 LLM 生成更好的指令数据集](https://github.com/SafeRL-Lab/TeaMs-RL)

[TinyVLA：面向机器人操作的快速、数据高效的视觉-语言-动作模型](https://github.com/liyaxuanliyaxuan/TinyVLA)

[LAVIS——语言视觉智能库](https://github.com/zahraborghei/Master_Thesis)

[利用大型语言模型促进机器人的运动控制](https://github.com/CaiwuChen/TSE6156)

[多 LLM 重复采样可有效扩展测试时间计算](https://github.com/JianhaoChen-nju/ModelSwitch)

[用于协调双手机器人的大型语言模型](https://github.com/Kchu/LABOR-Agent)

[释放预训练语言模型的力量，实现离线强化学习](https://github.com/srzer/LaMo-2023)

[视觉语言行动模型](https://github.com/saivishwak/VLA)

[基于 LLM 的自主机器人导航控制](https://github.com/rahulk-99/LLM_Prompt_Robot_Walk)

[Text2Reward：利用语言模型进行强化学习的奖励塑造](https://github.com/Yy12136/text2reward-eureka) - [其他](https://github.com/Yy12136/eureka_in_maniskill)

[Dita：用于通用视觉-语言-行动策略的缩放扩散变换器](https://github.com/RoboDita/Dita)

[基于 13 亿 3D 点云的语言-视觉运动策略](https://github.com/horipse01/3d-foundation-policy)

[DexVLA：带有插件扩散专家的视觉语言模型，用于视觉运动策略学习](https://github.com/huaihailv/AgilexDexVLA)

[InCLET：大型语言模型上下文学习可以提高具体指令遵循能力](https://github.com/yuanyaaa/InCLET)

[利用自然语言反馈进行强化学习](https://github.com/TanayGahlot/LearnFromNaturalLanguageFeedback)

[实现 RoCo：具有人类参与的大型语言模型的辩证多机器人协作 (HITL)](https://github.com/avnishkanungo/roco-reprompting) - [其他](https://github.com/awd1779/LLM-Hackathon-Group)

[可使用设备上的 Whisper 和 Llama 语音控制机械臂](https://github.com/fracapuano/llami)

[潜在奖励：情景强化学习中的 LLM 赋能信用分配](https://github.com/thu-rllab/LaRe)

[使用大型语言模型和强化学习对 Mastermind 奖励函数进行进化优化](https://github.com/Wisaacj/Mastermind)

[教授具身强化学习代理：语言使用的信息性和多样性](https://github.com/sled-group/Teachable_RL)

[将 ChatGPT 集成到机器人控制过程中，以实现零样本规划和控制](https://github.com/andrei-calin-dragomir/gpt-controller)

[使用 3GPP 文件微调不同的 LLM](https://github.com/hang-zou/LLM_FT_3GPP)

[大型语言模型项目想法](https://github.com/abdalrahmenyousifMohamed/LLM)

[为 ChatGPT 提供工具以使其具备空间推理能力](https://github.com/thomas-gale/chatgpt-physics-plugin)

[使用大型语言模型提示机器人行走](https://github.com/HybridRobotics/prompt2walk)

[机器人技能合成的语言到奖励](https://github.com/google-deepmind/language_to_reward_2023)

[RoCo：具有大型语言模型的辩证多机器人协作](https://github.com/Sunlighted/multi-agent-robots) - [其他](https://github.com/1mather/dece_roco)

[扩大规模并精简：语言引导的机器人技能习得](https://github.com/real-stanford/scalingup)


## 建模 <span id="modelling"></span>

[iGibson：在大型真实互动场景中训练机器人的模拟环境](https://github.com/S-CHOI-S/Gibson-Env)

[支持 Humanoid-v5 MuJoCo 环境](https://github.com/p1m0/GIST-RL-Project)



[获取机器人 URDF](https://github.com/Engineering-Geek/robot_arm)

[Human-Robot Gym 是一个用于安全人机协作的训练环境](https://github.com/TUMcps/human-robot-gym)

[Menagerie是MuJoCo物理引擎的高质量模型集合](https://github.com/kyokochi/mujoco-model)

[捕获机器人的点云](https://github.com/Velythyl/MJCF2O3D)

[利用通用强化学习算法，在给定环境中教导和控制机器人完成给定任务](https://github.com/CIMBIBOY/GenReL-World)

[包含用于MuJoCo模拟的Andino MJCF模型](https://github.com/Ekumen-OS/andino_mujoco)

[复杂高保真环境中的高效机器人模拟](https://github.com/liuskywalkerjskd/AIR_SIM)

[为 Atlas 机器人提供了 mujoco 和 URDF 模型](https://github.com/lvjonok/atlas-mujoco)

[SPEAR：用于逼真的具身人工智能研究的模拟器](https://github.com/spear-sim/spear)

[humanoidgym 适用于 alexbotmini 并适用于 alexbotmini_sim2real](https://github.com/Alexhuge1/Alexbotmini_gait)

[Mujoco Gym 四足运动环境](https://github.com/iit-DLSLab/gym-quadruped)

[MuJoCo 的 3x3x3 拼图立方体模型](https://github.com/kevinzakka/mujoco_cube)

[主动视觉强化学习的环境集合](https://github.com/elicassion/active-gym)

[通过可微分因果发现缩小模拟与现实之间的差距](https://github.com/XilunZhangRobo/COMPASS-Sim2Real)

[仿生鼠机器人跨越多种地形工作](https://github.com/GrumpySloths/ForCode)

[跳跃机器人 使用MuJoCo研究跳跃机器人腿部机构设计](https://github.com/changqiy/robot)

[包含 Solo-12 四足动物的完整 MuJoCo 模型，包括高保真视觉效果](https://github.com/rkourdis/solo12_mujoco)

[使用MuJoCo研究跳跃机器人腿部机构设计](https://github.com/yinfanyi/hopper)

[模拟机器人环境，用于评估对基本物体重新排列的物体操作方法](https://github.com/mohammad200h/rearrangement_benchmark)

[使用变分自编码器 (VAE) 和生成对抗网络 (GAN) 等深度学习人工智能算法，可以使用训练数据集自动创建新的游戏内容](https://github.com/RusherRG/RLGymBoost)

[利用 Franka Manipulator 在 MuJoCo 中实现的开源强化学习环境](https://github.com/zichunxx/panda_mujoco_gym)

[用于 RL 的生成细胞自动机类学习环境](https://github.com/smearle/autoverse)

[用于评估强化学习代理的适应和探索的环境](https://github.com/izkula/adaptgym)

[CoLeCT 项目的 MuJoCo 模拟环境](https://github.com/lbusellato/CoLeCT_sim)

[IsaacGym 环境示例 KukaTwoArms](https://github.com/intelligent-control-lab/guardX)

[CathSim：一种用于血管内介入的开源模拟器](https://github.com/airvlab/cathsim)

[使用 Kinova Gen3 机器人学习简单任务](https://github.com/Learning-in-robotics/kinova_learning)

[扩展控制器环境](https://github.com/RX-00/ext_ctrl_envs) - 包括推车上的倒立摆、弹簧加载倒立摆

[可以前进、后退、跳跃和绕自身旋转的立方体](https://github.com/seanmoyal/LaasPybulletMujoco)

[固定在矢状平面中的 MuJoCo 和 URDF 模型，用于研究腿式机器人的算法](https://github.com/lvjonok/mujoco-sagital-legged)

[使用 V-HACD 将凹网格分解为凸包来创建 MJCF 模型](https://github.com/tudorjnu/stl2mjcf)

[使用随机生成的障碍物训练机器人](https://github.com/FabioRaff/RL-Dyn-Env)

[基于深度强化学习的 Next-Best-View 方法，用于未知对象重建](https://github.com/MingFengHill/RL-NBV)

[用于训练四足机器人的gym](https://github.com/dtch1997/gymnasium-quadruped)

[建筑物内的测试环境的 3D 模型](https://github.com/AIMotionLab-SZTAKI/AIMotionLab-Virtual)

## 研究 <span id="research"></span>

[开发考虑人类偏好的机器人系统](https://github.com/joonhyung-lee/gov-prj-etri-llm-robotics)

[在机器学习机制可解释性方面的工作](https://github.com/danibalcells/mech-interp-notebooks)

[低质量数据的零样本强化学习](https://github.com/enjeeneer/zero-shot-rl)

[一个策略运行所有策略：多体现运动的端到端学习方法](https://github.com/nico-bohlinger/one_policy_to_run_them_all)

[交互信息技能学习的分析与要素](https://github.com/jens321/csf) - [其他](https://github.com/Princeton-RL/contrastive-successor-features)

[扩散引导是一种可控策略改进算子](https://github.com/kvfrans/cfgrl)

[DIME：基于扩散的最大熵强化学习](https://github.com/ALRhub/DIME)

[3D扩散策略：基于简单3D表示的可泛化视觉运动策略学习](https://github.com/Wushr-Lance/Multi-task-3D-Diffusion-Policy)

[谷歌研究库](https://github.com/google-research/google-research)

[通过强化学习和域随机化实现 Hopper 控制的模拟到现实迁移](https://github.com/alexscavo/Sim-to-Real-Transfer-Project-RL)

[基于相位减少的六足机器人步态转换的中央模式发生器网络](https://github.com/Norihisa-Namura/CPG-network-for-gait-transition-in-hexapod-robots)

[意识浮现](https://github.com/Simsreal/simsreal)

[可解释强化学习的策略梯度方法与决策树的比较](https://github.com/itshannonk/InterpretableRL)

[可扩展持续强化学习的自组合策略](https://github.com/mikelma/componet)

[DeGuV：深度引导的视觉强化学习，用于操作中的泛化和可解释性](https://github.com/tiencapham/DeGuV)

[基于能量的正则化流的最大熵强化学习](https://github.com/ChienFeng-hub/meow)

[CompetEvo：从竞争走向形态进化](https://github.com/KJaebye/CompetEvo)

[利用信息素实现机器人自组织行为](https://github.com/Masashi-Lateolabrax/ICAP)

[学习执行长视界移动操作任务对于推动家庭和工作场所机器人技术的发展至关重要](https://github.com/h2r/LAMBDA)

[混合可微分模拟：通过数据改进实际部署](https://github.com/dcsteinhauser/HDS)

[对称强化学习损失用于不同任务和模型尺度上的稳健学习](https://github.com/shashacks/Symmetric_RL)

[通过熵最大化实现域随机化](https://github.com/gabrieletiboni/doraemon)

[通过因果知识提高任务无关探索的效率](https://github.com/CMACH508/CausalExploration)

[信念状态编码器/解码器](https://github.com/lucidrains/anymal-belief-state-encoder-decoder-pytorch) - 似乎产生了一种可与波士顿动力手工算法（四足动物 Spot）相媲美的策略

[包含SoftGym环境的基准算法](https://github.com/ducphuE10/equiRL)

[使用随机模拟部署保证机器人系统性能](https://github.com/StanfordMSL/performance_guarantees)

[用轨迹解释 RL 决策](https://github.com/karim-abdel/Explaining-RL-Decisions-with-Trajectories)

[进化机器人 Python——脑体协同优化框架](https://github.com/Co-Evolve/erpy)

[通过自适应情境感知策略实现强化学习中的动态泛化](https://github.com/Michael-Beukman/DecisionAdapter)

[基于模型的状态扩散器，用于样本高效在线强化学习](https://github.com/ryanliu30/StateDiffusion)

[通过人类反馈实现高置信度策略改进](https://github.com/httse9/HCPI-HF)

[强化学习中技能转移的分层启动源代码](https://github.com/SSHAY007/MiniHackThePlanet)

[Jax 中改进离线策略优化的宽松平稳分布校正估计](https://github.com/ku-dmlab/PORelDICE)

[描述符条件强化学习 MAP-Elites](https://github.com/adaptive-intelligent-robotics/DCRL-MAP-Elites)

[OPTIMUS：利用视觉运动变换器进行模拟任务和运动规划](https://github.com/NVlabs/Optimus)

[从不平衡演示中进行半监督模仿学习](https://github.com/tRNAoO/Ess-InfoGAIL)

[按复杂性和关节数量的递增顺序训练 MuJoCo 环境（Hopper、Half-Cheetah 和 Ant）的模型](https://github.com/Panjete/mujocoagents)

[METRA：具有度量感知抽象的可扩展无监督强化学习](https://github.com/seohongpark/METRA)

[从示例对象轨迹和预抓取中学习灵巧操作](https://github.com/ishaanshah15/TCDMdev)

[解决情境强化学习的新方法](https://github.com/rpanackal/rl-msc-pro)

[对于 safe_exploration 任务，既需要数据多样性，又需要在线训练安全保障](https://github.com/JackQin007/Safe_Exploration)

[PyTorch 机器人运动学](https://github.com/UM-ARM-Lab/pytorch_kinematics)

[用于模仿学习的记忆一致神经网络](https://github.com/kaustubhsridhar/MCNN) - [其他1](https://github.com/mem-net/MCNN)

[TimewarpVAE：同时进行时间扭曲和轨迹表征学习](https://github.com/anonymousauthor913/iclr2024submission)

[PyTorch 中时间对称数据增强（TSDA）的实现](https://github.com/CLeARoboticsLab/tsymRL)

[JAX 中的在线策略梯度算法](https://github.com/Matt00n/PolicyGradientsJax)

[好奇探索中的目标条件离线规划](https://github.com/martius-lab/gcopfce)

[基于像素观测的状态安全强化学习](https://github.com/SimonZhan-code/Step-Wise_SafeRL_Pixel)

[带有注意力缓存和批量束搜索的轨迹变换器实现](https://github.com/Howuhh/faster-trajectory-transformer)

[深海宝藏问题中采用帕累托主导策略的多目标强化学习](https://github.com/GiovaniCenta/cityflowpql)

[TimewarpVAE：同时进行时间扭曲和轨迹表示学习](https://github.com/travers-rhodes/TimewarpVAE)

[实验机器人操作代理的PLEX 架构的代码和说明](https://github.com/microsoft/PLEX)

[任意跌倒状态起身](https://github.com/TeshShin/UE5-GetupControl) - UE5

[等距运动流形基元](https://github.com/Gabe-YHLee/IMMP-public)

[用于离线策略评估的状态-动作相似性表示代码](https://github.com/Badger-RL/ROPE)

[基于注意力的排列不变神经网络框架 的官方 PyTorch 实现](https://github.com/ethanabrooks/adpp)

[专为 Fanuc Robotiq 机械手设计的创新机械臂操控解决方案](https://github.com/baha2r/Fanuc_Robotiq_Grasp)

[对比学习作为目标条件强化学习](https://github.com/mishmish66/contrastive_rl)

[多智能体质量多样性](https://github.com/YGLY4/Multi-Agent-Quality-Diversity)

[执行 器退化适应Transformer](https://github.com/WentDong/Adapt)

[根据给定轨迹数据推断动态模型的动态参数](https://github.com/lvjonok/f23-pmldl-project)

[强化学习中的硬阈值与进化策略相结合](https://github.com/glorgao/NES-HT)

[反馈就是你所需要的一切吗？在目标条件强化学习中利用自然语言反馈](https://github.com/maxtaylordavies/feedback-DT)

[从多任务演示中学习共享安全约束](https://github.com/konwook/mticl)

[DeFog: 随机丢帧下的决策变换器](https://github.com/hukz18/DeFog)

[通过准度量学习实现最优目标达成强化学习](https://github.com/quasimetric-learning/quasimetric-rl)

[基于 DeepMind Control Suite 实现的具有对称性的 MDP 集合](https://github.com/sahandrez/symmetry_RL)

[研究 Transformers 1 层 Transformer 模型如何收敛到简单统计推断问题的贝叶斯最优解](https://github.com/alejoacelas/bayesian-transformers)

[利用多源工作负载知识促进指数顾问学习](https://github.com/XMUDM/BALANCE)

[引入基于评论家估计的不确定性抽样](https://github.com/juliusott/uncertainty-buffer)

[提升 AI 对齐研究工程技能的资源](https://github.com/callummcdougall/ARENA_2.0) - [其他](https://github.com/alejoacelas/ARENA_2.0_Exhibit) 、[arena-problem-sets](https://github.com/jcmustin/arena-problem-sets) 、 [3.0](https://github.com/callummcdougall/ARENA_3.0)

[自适应强化学习的表征学习](https://github.com/stevenabreu7/adaptiveRL2) - 使用可微分可塑性、状态空间模型和深度强化学习

[具有大型语言模型的辩证多机器人协作](https://github.com/MandiZhao/robot-collab)

[通过多任务策略提炼解决任务干扰](https://github.com/AndreiLix/mutlitask_policy_distillation)

[使用去噪扩散概率模型的轨迹生成、控制和安全性](https://github.com/nicob15/Trajectory-Generation-Control-and-Safety-with-Denoising-Diffusion-Probabilistic-Models)

[策略转移终身RL](https://github.com/zhouzypaul/policy-transfer-lifelong-rl)

[基于幻觉输入偏好的强化学习](https://github.com/calvincbzhang/hip-rl)

[对比贝叶斯自适应深度强化学习](https://github.com/ec2604/ContraBAR)

[可控性感知的无监督技能发现](https://github.com/seohongpark/CSD-locomotion)

[深度方差加权（DVW）的官方实现](https://github.com/matsuolab/Deep-Variance-Weighting-MinAtar)

[合成经验回放 (SynthER) 是一种基于扩散的方法](https://github.com/conglu1997/SynthER) - 可以对强化学习 (RL) 代理收集的经验进行任意上采样，从而大幅提升采样效率和扩展优势

[受控的多样性与偏好：迈向学习多样化的所需技能](https://github.com/HussonnoisMaxence/CDP)

[SNS-Toolbox 方法论文中关于不同类型优化的代码](https://github.com/DrYogurt/SNS-Toolbox-Optimization)

[从受限专家演示中学习软约束](https://github.com/ashishgaurav13/ICL)

[通过中间目标的监督学习进行强化学习](https://github.com/StanfordAI4HI/waypoint-transformer)

[用于测试概念或尝试重现孤立问题的简单区域](https://github.com/EricCousineau-TRI/repro)

[通过扩散概率模型进行强化学习的策略表示](https://github.com/BellmanTimeHut/DIPO)

[突破强化学习中重放率障碍，实现连续控制](https://github.com/proceduralia/high_replay_ratio_continuous_control)

[可控性感知的无监督技能发现](https://github.com/seohongpark/CSD-manipulation)

[解决 OpenAI Gym 中的神经元中间算法遗传算法的问题](https://github.com/DouglasDacchille/GA-InvertedPendulum)

[从梦想到控制：通过潜在想象力学习行为，在 PyTorch 中实现](https://github.com/juliusfrost/dreamer-pytorch)

[预测模型延迟校正强化学习](https://github.com/CAV-Research-Lab/Predictive-Model-Delay-Correction)

[最佳评估成本跟踪](https://github.com/JudithEtxebarrieta/OPTECOT)

[等变模型在潜在对称域中的惊人有效性](https://github.com/pointW/extrinsic_equi)

[基于目标的随机优化替代方法](https://github.com/WilderLavington/Target-Based-Surrogates-For-Stochastic-Optimization)

[利用进化策略进化人工神经网络实现虚拟机器人控制](https://github.com/kenjiroono/NEAT-for-robotic-control)

[机器人环境的安全迁移学习](https://github.com/f-krone/SafeTransferLearningInChangingEnvironments)

[SIMCSUM](https://github.com/timkolber/mtl_sum)

[研究基于模型的强化学习中的不确定性量化](https://github.com/aidanscannell/unc-mbrl)

[通过压缩学习选项](https://github.com/yidingjiang/love)

[NaturalNets](https://github.com/neuroevolution-ai/NaturalNets)

[深度强化学习中的首因偏差](https://github.com/evgenii-nikishin/rl_with_resets) - 深度强化学习代理的 JAX 实现，带有重置功能

[基于近似模型的安全强化学习屏蔽](https://github.com/sacktock/AMBS)

[利用扩散模型作为高表达性的策略类别](https://github.com/twitter/diffusion-rl) - 用于行为克隆和策略正则化

[构建目标驱动的具身化大脑模型](https://github.com/ccnmaastricht/angorapy)

[稳定神经近似的逆向经验重放](https://github.com/google-research/look-back-when-surprised) - [其他](https://github.com/llv22/google-research-forward)


### 奖励

[规律性作为自由游戏的内在奖励](https://github.com/martius-lab/rair-mbrl)

[基于 DeepMind Control Suite 实现的具有变化奖励和动态的上下文 MDP](https://github.com/SAIC-MONTREAL/contextual-control-suite)

[用示例代替奖励：通过递归分类进行基于示例的策略搜索 的 pytorch 实现](https://github.com/Ricky-Zhu/RCE)


## 毕业论文 <span id="contest"></span>

[利用 MARL 技术分解大动作空间来加速学习](https://github.com/QuimMarset/TFM)

[硕士论文的所有脚本](https://github.com/CrushHour/MA)


## 教程 <span id="tutorial"></span>

[MuJoCo 模拟平台入门教程](https://github.com/tayalmanan28/MuJoCo-Tutorial)

[Open AI Gym 基础教程](https://github.com/mahen2-cmd/Open-AI-Gym-Basic-Tutorial)

[介绍机器人系统（主要为全驱动系统）控制的入门课程](https://github.com/simeon-ned/forc)

[适合所有人的人工智能书籍](https://github.com/YeonwooSung/ai_book)

[控制和安全高效的 RL](https://github.com/aai-institute/tfl-training-rl)

[学习-强化学习](https://github.com/ayton-zhang/Learning-Reinforcement-Learning)

[具身人工智能入门课程资料库](https://github.com/wannabeyourfriend/PKU-EECS-EAI-2025spring)

[强化学习的深入讲解](https://github.com/rogerwater/Reinforcement-Learning)

[原始源代码 Michael Hu 撰写的《强化学习的艺术》](https://github.com/Apress/art-of-reinforcement-learning)

[强化学习教程](https://github.com/weiminn/reinforcement_learning_tutorials)


## 学习 <span id="learning"></span>

[伯克利 CS 285的作业：深度强化学习、决策和控制](https://github.com/Roger-Li/ucb_cs285_homework_fall2023) - [其他1](https://github.com/LuK2019/DeepRL) 、[其他2](https://github.com/aayushg55/cs285_hw1_dagger) 、[其他3](https://github.com/berkeleydeeprlcourse/homework_fall2023) 、[其他4](https://github.com/carola-niu/RL_cs285) 、 [其他5](https://github.com/Manaro-Alpha/CS285_DeepRL_hw_sols) 、[其他6](https://github.com/Hoponga/cs285) 、 [其他7](https://github.com/anna-ssi/UCBerkley-CS285-homework-2021) 、[其他8](https://github.com/anna-ssi/UCBerkley-CS285-homework-2021) 、[其他9](https://github.com/Applewonder/CS285-2022) 、[其他10](https://github.com/Arenaa/CS-285) 、[其他11](https://github.com/brunonishimoto/cs285-drl) 、 [其他12](https://github.com/ElPescadoPerezoso1291/cs285-hw3) 、 [其他13](https://github.com/dylan-goetting/RL285) 、 [其他14](https://github.com/nikhil-pitta/CS285Hw) 、[其他15](https://github.com/prestonmccrary/temp) 、 [其他16](https://github.com/jnzhao3/Behavior-Cloning-with-MuJoCo) 、[其他17](https://github.com/levje/cs285_fall2023) 、[其他18](https://github.com/prestonmccrary/garbage) 、[其他19](https://github.com/WangYCheng23/rl_cs285_hw) 、[其他20](https://github.com/nicholaschenai/cs285_2022_soln) 、

[采样策略梯度扩展](https://github.com/BharathRajM/Sampled-Policy-Gradient-and-variants)

[基于Genesis的强化学习示例](https://github.com/TokyoRobotics/torobo_genesis)

[一个专门用于学习使用 Half Cheetah 模型进行强化学习的存储库](https://github.com/GustavoSanches55/HalfCheetah)

[面向初学者的深度学习资料](https://github.com/KEIO-ALS/Lecture_DeepLearning)

[学习走路](https://github.com/kenma8/LearningToWalk)

[用于试验模拟器以举办第二届人工智能大奖赛的存储库](https://github.com/FT-Autonomous/ft_grandprix)

[CMU 16-831 机器人学习简介的作业](https://github.com/shriishwaryaa/Introduction-to-Robot-Learning)

[使用 JAX 实现各种学习算法的练习代码](https://github.com/TheUnsolvedDev/JaxStormer)

[cs285](https://github.com/johnviljoen/cs285)

[由阿尔托大学 Joni Pajarinen 教授主讲的强化学习课](https://github.com/amiiiza/reinforcement_learning)

[CS 285 最终项目：基于连续时间模型的强化学习中的动态学习的神经常微分方程](https://github.com/ZekaiWang04/cs285_proj)

[交互式机器人学习课程项目](https://github.com/LeonardoWjq/NP-RAM)

[CS285 最终项目](https://github.com/skrider/draftsman)

[CS285](https://github.com/ayton-zhang/CS285)

[CS 285 作业](https://github.com/LeslieTrue/cs285_fall22_hw_sol)

[机器人相关课程](https://github.com/waris8/courses)

[通过传统的机器学习方法和强化学习解决课程作业任务](https://github.com/RabbltMan/MachineLearningCoursework)

[CMU 16-831 机器人学习简介的作业](https://github.com/chaitanya1chawla/16831_F23_HW)

[自己实现的深度强化学习算法](https://github.com/minghongx/deeprl)

[CS 285 最终项目：双人不完美信息合作博弈的强化学习](https://github.com/edwardneo/collaboration-strategy)

[实用机器学习与深度学习](https://github.com/dinarayaryeva/pml-dl)

[CS285-proj](https://github.com/KaushikKunal/CS285-proj)

[symmetry-cs285](https://github.com/YasinSonmez/symmetry-cs285)

[利用 MuJoCo 进行深度强化学习](https://github.com/danimatasd/MUJOCO-AIDL)

[大学强化学习考试（9 CFU）材料的组成部分](https://github.com/ProjectoOfficial/ReinforcementLearningProject)

[2022 年高级机器学习 (AML) 课程项目的最终代码](https://github.com/marcopra/RL-vision-based)

[CSCE-642：深度强化学习的作业](https://github.com/Pi-Star-Lab/csce642-deepRL)

[CS285-Final-Project](https://github.com/JophiArcana/CS285-Final-Project)


[CMU 16-831 机器人学习简介的作业](https://github.com/ImNotPrepared/hw2)

[深度强化学习@伯克利（CS 285）](https://github.com/changboyen1018/CS285_Deep-Reinforcement-Learning_Berkeley)


[RL 课程的最终项目](https://github.com/kortukov/the_copilots)

[关于课程作业的一些解决方案](https://github.com/RbingChen/GoodGoodStudy)

[DeepRL课程](https://github.com/ElliottP-13/DeepRL-Course)

[cs285_hw1](https://github.com/RichZhou1999/cs285_hw1)

[2023年夏令营](https://github.com/Swiss-AI-Safety/swiss-summer-camp-23)

[关于 dm_control 的 AI 原理强化学习项目](https://github.com/Otsuts/SAC-GAARA)

[RL相关项目](https://github.com/Pippo809/rl_projects) - 模仿学习、策略梯度

[用于强化学习研究的快速且可定制的gym兼容零售店环境](https://github.com/kenminglee/COMP579-FinalProject)

[本课程包括建模不确定性、马尔可夫决策过程、基于模型的强化学习、无模型强化学习函数近似、策略梯度、部分可观察的马尔可夫决策过程](https://github.com/SpringNuance/Reinforcement-Learning)

[使用 Gymnasium 和 Mujoco 构建强化学习的示例](https://github.com/ramonlins/rlmj)


[cs285深度强化学习](https://github.com/notY0rick/cs285_deep_reinforcement_learning)

[解决Gym问题和其他机器学习实践](https://github.com/qio1112/GymSolutions)

[人工智能中心 2023 年春季项目的存储库](https://github.com/xiaoxiaoshikui/Machine-Learning-Project-for-ETH-AI-Center)

[加州大学伯克利分校 CS285 深度强化学习 2022 年秋季](https://github.com/xd00099/CS285-DeepReinforcementLearning-Berkeley)

[fa22-cs285-project](https://github.com/inferee/fa22-cs285-project)

[一些流行的深度强化学习算法的实现](https://github.com/Manaro-Alpha/RL_Algos)

[DeepRL-CS285](https://github.com/minyonggo/DeepRL-CS285)

[一些训练和微调决策转换器的实验](https://github.com/bhaveshgawri/decision-transformer-transfer-learning)

[学习强化学习的笔记](https://github.com/asuzukosi/reinforcement-learning-study-notes)

[强化学习](https://github.com/MarcoDiFrancesco/reinforcement-learning)

[cs285hw](https://github.com/Grant-Tao/cs285hw)

[CS 285 佳乐的作业](https://github.com/JialeZhaAcademic/UCB-CS-285)

[XAI611项目提案](https://github.com/tlatjddnd101/xai611_project_proposal_2023)

[dm_control 的 AI 原理强化学习项目](https://github.com/Otsuts/SAC-GAARA)

[关于机器学习和控制的笔记本](https://github.com/alefram/notebooks)

[伯克利 CS 285的作业：深度强化学习、决策和控制](https://github.com/rsha256/CS285_HW)

[加州大学伯克利分校 cs 285 课程作业](https://github.com/smoteval/reinforcement_learning_berkeley_assignments)

[伯克利 CS 285的作业：深度强化学习、决策和控制](https://github.com/safooray/rl_berkeley)

[伯克利 CS 285的作业：深度强化学习、决策和控制](https://github.com/A-Abdinur/RLHomeWorkTutorials)

[CS234 最终项目](https://github.com/chuanqichen/CS234_Final_Project)

[强化学习课程练习的实现](https://github.com/juuso-oskari/ReinforcementLearning)

[强化学习练习](https://github.com/taehwanHH/prac_Reinforcement-Learning/tree/main/ReinforcementLearningAtoZ-master)

[伯克利 CS 285的作业：深度强化学习、决策和控制](https://github.com/jongwoolee127/cs285-homework)

[伯克利 CS 285的作业：深度强化学习、决策和控制](https://github.com/akashanand93/rl)

[伯克利 CS 285的作业：深度强化学习、决策和控制](https://github.com/NewGamezzz/cs285-DeepRL-Fall2022)

[USD-22Z-Projekt](https://github.com/olek123456789/USD-22Z-Projekt)

[CS 285 深度强化学习课程材料](https://github.com/Curiouskid0423/deeprl)

[IASD 硕士深度强化学习课程的作业](https://github.com/webalorn/DRL_assignements) - 基于课程Berkeley CS 285：深度强化学习、决策和控制

[伯克利 CS 285的作业：深度强化学习、决策和控制](https://github.com/chengwym/CS285)

[学习CS285时做的作业](https://github.com/lijunxian111/CS285)

[cs285HW](https://github.com/YuquanDeng/cs285HW)

[CS839-最终项目](https://github.com/CohenQU/CS839-FinalProject)

[831project](https://github.com/miao3210/831project)

[强化学习课程的练习和项目代码](https://github.com/ChristianMontecchiani/RL_course)

[伯克利 CS 285的作业：深度强化学习、决策和控制](https://github.com/kiran-ganeshan/cs285)

[cmu_rob831_fall](https://github.com/AsrarH/cmu_rob831_fall)

[高级机器学习（AML）课程项目启动代码](https://github.com/gabrieletiboni/aml22-rl)

[数据分析与人工智能课程考试项目起始代码](https://github.com/gabrieletiboni/daai22-rl)

[毕业论文](https://github.com/Balssh/Thesis)

[CS285 的最终项目代码库：加州大学伯克利分校的深度强化学习](https://github.com/chirag-sharma-00/CS285-Project)

[CS285-Research-Project](https://github.com/aaggarw99/CS285-Research-Project)

[HPC_3](https://github.com/LBatov/HPC_3)

[使用 KNN 算法根据观察结果预测动作](https://github.com/abhayrcodes/cs285knn)

[一个利用强化学习、线性代数和机器人技术概念的实践项目](https://github.com/virajbshah/rl-inator)

[2022/2023 自主代理课程练习](https://github.com/lucalazzaroni/Autonomous-Agents)

[CS 285 家庭作业：深度强化学习](https://github.com/reecehuff/CS285_Homeworks)

[CIFAR-10-练习](https://github.com/RETELLIGENCE-IWEN/CIFAR-10-Practice)

[CS285 - 深度强化学习资料](https://github.com/Naghipourfar/cs285)

[伯克利 CS 285的作业：深度强化学习、决策和控制](https://github.com/GeoffNN/c285-HW)

[策略梯度](https://github.com/bvanbuskirk/PolicyGradient/tree/main/hw2)

[ELEC-E812课程作业](https://github.com/johnson-li/ELEC-E8125)

[用于 CS 391R 课程项目的击球机器人](https://github.com/jbonyun/cs391r)

[ÚFAL 课程 NPFL122](https://github.com/ufal/npfl122)

[伯克利 CS 285的作业：深度强化学习、决策和控制](https://github.com/berkeleydeeprlcourse/homework_fall2022)

## 任务 <span id="task"></span>

[基于物理的乒乓球](https://github.com/AayushSabharwal/physics-pong)

[训练一个通用策略来控制灵巧的机械手演奏任何歌曲](https://github.com/sNiper-Qian/pianomime)

[具有软腕部分可观测性的机器人装配的对称感知强化学习](https://github.com/omron-sinicx/symmetry-aware-pomdp)

[使用深度强化学习训练守门员](https://github.com/magnum094/kicker-praktika)

[足球机器人](https://github.com/utra-robosoccer/soccerbot)

[清理厨房](https://github.com/arhanjain/clean-up-the-kitchen)

[使用强化学习来优化交通信号灯操作以最大化吞吐量](https://github.com/rankun203/traffic_light_ml)

[一个吉他演奏模拟系统，能够读取指法谱，并在训练后引导机械手弹奏吉他](https://github.com/MRXuanL/GPS-GuitarPlaySimulation)

[RoboCasa：通用机器人日常任务的大规模模拟](https://github.com/robocasa/robocasa)

[在 Carla 中实现了原始的 td-mpc2 算法](https://github.com/adeebislam8/carla-tdmpc2)

[DexFG通过少量演示学习多指手的类人功能抓握](https://github.com/DexGraspOpt/DexGraspSyn)

[使用深度强化学习训练桌上足球代理](https://github.com/kitaird/FoosballRL) - [其他](https://github.com/kitaird/ProtoFoosballRL)

[在现实世界中学习弹钢琴](https://github.com/lasr-lab/learning-to-play-piano)

[EHoI：基于事件相机的任务导向手物交互识别基准](https://github.com/turbohiro/EHOI_benchmark)

[OGMP：Oracle 引导的多模式策略，实现敏捷、多功能机器人控制](https://github.com/DRCL-USC/ogmp)

[使用基于脉冲神经网络的架构教四足机器人行走](https://github.com/tganamur/RL-SNN-Quadrupeds)

[基于多智能体强化学习的分布式自主交叉路口管理方法](https://github.com/mcederle99/MAD4QN-PS)

[基于 MuJoCo 的自主飞艇控制模拟环境，具有全面的域随机化支持](https://github.com/Airborne-Robotic/BlimpGymEnvironment)

[空气曲棍球挑战赛](https://github.com/AirHockeyChallenge/air_hockey_challenge) 、[其他](https://github.com/thomasbonenfant/air_hockey_challenge) 、[其他2](https://github.com/Elizabeth-Palacios/Curriculum) 、[其他3](https://github.com/hzm2016/sea_robot_sim)

[2023年空气曲棍球挑战赛](https://github.com/verma-rishabh/air_hockey_qualifying) - [其他](https://github.com/SCNU-SAILOR/air_hockey_challenge_demo)

[可用于开发机器人 3D 装箱问题的求解器的gym环境](https://github.com/floriankagerer/bed-bpp-env)

[实现 DDPG 进行简单的倒水](https://github.com/yashas-salankimatt/csce642-finalproj)

[测试 RL 在量子控制中的应用](https://github.com/AnikenC/QuantumControlWithRL) - 特别关注电路级和脉冲级门校准任务

[用于机器人插入任务的 MuJoCo 模拟](https://github.com/gintautas12358/Mujoco-Eleanor)

[使用基于贝叶斯优化的课程学习提高自主赛车深度强化学习方法的环境鲁棒性](https://github.com/PRISHIta123/Curriculum_RL_for_Driving)

[迷宫](https://github.com/EndikaEiros/dumb_maze_runner)

[倒立摆](https://github.com/AniruddhS24/inverted-pendulum)

[多任务机器人学习](https://github.com/Eyshika/Multi_Task_Robot_Learning)

[与 ROS NIAS-API 类似的 CoppeliaSim 机器人模拟器的绑定](https://github.com/knowledgetechnologyuhh/nicol_coppeliasim)

[中国跳棋环境中，经过完整参数共享训练的 PPO 代理进行自我对弈](https://github.com/noahadhikari/pettingzoo-chinese-checkers)

[实现 DDPG 进行简单的倒水](https://github.com/yashas-salankimatt/csce642-finalproj)

[竞技体育的两步法：以击剑为例](https://github.com/YCK1130/IMRL-HF)

[曲棍球环境中的强化学习](https://github.com/JSteegmueller/The-Q-Learners)

[一个用于自动生成伸手动作以抓取扁平电缆连接器插入姿势的环境](https://github.com/maki8maki/Gym_Cable_RL)

[研究如何训练自适应人机界面，以在获得良好控制的同时最大限度地减少用户交互](https://github.com/KilianFt/Adaptive-HCI)

[赛车v2](https://github.com/Merealtea/CarRacingv2)

[深度Q学习解决俄罗斯方块模拟器](https://github.com/ItaiBear/TetrisGameMaster)

[空气曲棍球锦标赛](https://github.com/thomasbonenfant/air_hockey_challenge)

[汽车人 VIP 的基于视觉的操控探索](https://github.com/acmiyaguchi/autobots_visman)

[使用 UR5e 机械臂和 Robotiq 2F-85 夹持器来操纵柔性物体](https://github.com/ian-chuang/homestri-ur5e-rl)

[倒立摆强化学习](https://github.com/shuoyang97/inverted_pendulum_reinforcement_learning)

[包含三足步行机器人的硬件、电气和软件组件](https://github.com/Lexseal/Triped)

[通过双手灵活性掌握钢琴演奏技巧](https://github.com/halo2718/Commented-RoboPianist)

[Kikato 的灵巧钢琴演奏与深度强化学习](https://github.com/kikato2022/kikarobopianist)

[使用 GraphDB 作为内存的聊天机器人示例](https://github.com/misanthropic-ai/graphdb-example)

[曲棍球环境](https://github.com/emilbreustedt/RL-Hockey)

[防止赛车冲出赛道。在最少的步数内完成比赛](https://github.com/akshaykadam100/Car-Racing)

[自动驾驶汽车SoC](https://github.com/shambhavii13/Autonomous_Moving_Vehicle_SoC)

[使用 Panda 的非常简单的 MuJoCo 拾取和放置任务](https://github.com/volunt4s/Simple-MuJoCo-PickNPlace)

[三足蚂蚁](https://github.com/ugo-nama-kun/three_legged_ant)

[使用 NEAT RL 算法解决 ATARI Retro Pong](https://github.com/MatSaf123/neat-retro-pong)

[蚂蚁六腿环境](https://github.com/savanagrawal/Gymnasium-MuJoCo-Ant-Six-Legs)

[在 iCub 人形机器人上重现与 RL 项目相关的灵巧操作实验的代码](https://github.com/hsp-iit/rl-icub-dexterous-manipulation)

[空气曲棍球挑战赛的源代码](https://github.com/sombitd/AirRL)

[山地车强化学习](https://github.com/ryota0051/rl-mountaincar)

[DRL_Taxi_Custom](https://github.com/Douglch/DRL_Taxi_Custom)

[工业机器人机械手（KUKA KR16-2）接住发出的网球](https://github.com/LuanGBR/Kuka_RL_Control)

[使用凸模型预测控制（MPC）的四足动物运动的 Python 实现](https://github.com/yinghansun/pympc-quadruped)

[激光曲棍球环境中的 SAC 代理](https://github.com/nilskiKonjIzDunava/rl-hockey-sac-agent)

[基于深度学习的代理使用 GUI 玩贪吃蛇游戏](https://github.com/wanghan8866/MyThirdYearProject1)

[使用 MyCobot 的机械臂任务强化学习框架](https://github.com/matinmoezzi/MyCobotGym)

[一个用于构建自主系统的沙盒。从自动驾驶汽车开始。由MockaSort Studio精心打造](https://github.com/MockaSort-Studio/ADP8)

[通过深度强化学习灵巧地弹奏钢琴](https://github.com/google-research/robopianist)




### 无人机 <span id="UAV"></span>

[基于四旋翼飞行器的 RL 环境代码](https://github.com/arachakonda/gym-quad)

[使用 RL 和低级控制器控制四轴飞行器](https://github.com/Prakyathkantharaju/quadcopter)

[添加新环境：四旋翼飞行器](https://github.com/bzx20/Brax_mydrone)

[四旋翼飞行器利用钩式机械手抓取和运输有效载荷](https://github.com/AIMotionLab-SZTAKI/quadrotor-hook-1DoF)

[飞行和漂浮模型，例如四旋翼飞行器、悬挂有效载荷的四旋翼飞行器等](https://github.com/vkotaru/udaan)

[强化学习方法实现四轴飞行器的安全三维导航](https://github.com/shaikh58/quad-nav-rl)

[探索如何利用受椋鸟启发的无人机群来可视化看不见的火灾动态，从而增强消防员的态势感知和安全](https://github.com/Jybbs/thermur)

[无人机RL](https://github.com/jasonjabbour/DroneRL)

[RoVerFly：四旋翼飞行器-有效载荷系统的稳健且多功能隐式混合控制](https://github.com/mintaeshkim/roverfly)

[使用 MuJoCo 为 Bitcraze Crazyflie 2 无人机定制的 OpenAI Gym 环境](https://github.com/viktorlorentz/quad-rl)

[仿生飞鼠机器人的计算机模拟和飞行优化](https://github.com/jbvilla/MSc-thesis-code)

[通过遗传算法改进滑翔机的设计](https://github.com/featherware/glider)

[DroneSim2Sim：无人机的 Sim2Sim 传输基准](https://github.com/Wangshengyang2004/DroneSim2Sim)

[MuJoCo gym 的无人机执行各种活动。传感器包括：2 个摄像头（立体摄像头）、加速度计、陀螺仪](https://github.com/Engineering-Geek/gym-drone)

[在 PyBullet 环境中模拟六轴飞行器（无人机），使用 YOLOv8 动态检测和统计人员数量](https://github.com/aarohiin/Hexacopter-virtual-simulation-for-people-detection)

[RL-UAV 是一个专注于无人机模拟的强化学习项目](https://github.com/Engineering-Geek/RL-UAV)

[MuJoCo 中的无人机模拟](https://github.com/arachakonda/MTP-MuJoCo)

[在模拟环境中训练无人机，使其自主导航到目标拾取位置，从该位置拾取并运送到目标位置](https://github.com/NorwegianIcecube/AutoDrone)

[Isaac Gym 无人机环境](https://github.com/esquivelrs/DTU-RL-Isaac-Gym-Drone-Env)

[无人机仿真](https://github.com/C-monC/Drone-simluation)

[四轴飞行器有效载荷抓取与运输轨迹规划与控制设计](https://github.com/antalpeter1/tdk-2022)

[四轴飞行器](https://github.com/mnasser02/gymnasium_quadcopter)


## 平台 <span id="platform"></span>

[Brax 是一种快速且完全可微分的物理引擎](https://github.com/CLeARoboticsLab/friction-estimator) - [其他1](https://github.com/suddenabnormalsecrets/brax)


[用于机器人强化学习端到端开发的工具集](https://github.com/Zolkin1/robot_rl)

[MuJoCo 物理模拟器的 GPU 优化版本](https://github.com/google-deepmind/mujoco_warp)

[使用 LLM 实现全自动具身模拟](https://github.com/MetaX-MACA/Embodied_AI_Simulation)

[LeRobot致力于提供基于 PyTorch 的机器人模型、数据集和工具](https://github.com/huggingface/lerobot)

[一个模块化、原始优先、Python优先的PyTorch强化学习库](https://github.com/pytorch/rl)

[Safari SDK：适用于 Google DeepMind Gemini 机器人模型的 SDK](https://github.com/google-deepmind/gemini-robotics-sdk)

[人机交互强化学习套件](https://github.com/huggingface/gym-hil)

[DORA（面向数据流的机器人架构）是一款中间件，旨在简化基于 AI 的机器人应用程序的创建。它提供低延迟、可组合和分布式数据流功能](https://github.com/dora-rs/dora)

[一个基于 Flask 的综合 REST API 服务器，用于通过 MuJoCo 模拟或真实硬件连接控制软机器人](https://github.com/yhbcode000/robot-control-server)

[天寿：一个优雅的 PyTorch 深度强化学习库](https://github.com/thu-ml/tianshou)

[EnvPool是一个基于 C++ 的批处理环境池，DGX-A100 上的 Mujoco 模拟器原始帧率约为 300 万帧](https://github.com/Vettinari/envpool313)

[使用MuJoCo进行实时预测控制的交互式应用程序和软件框架](https://github.com/anupamkaul/mujoco-mpc-24) - 人形动作捕捉追踪，[其他1](https://github.com/anupamkaul/mujoco-24)、[其他2](https://github.com/alexper490/mujoco-mpc-cassie)

[LeRobot 旨在用 PyTorch 为现实世界的机器人技术提供模型、数据集和工具](https://github.com/LiuQiang-AI/liu_lerobot) - [其他](https://github.com/huggingface/lerobot)

[Gym](https://github.com/openai/gym) - 用于开发和比较强化学习算法，它提供了一个用于在学习算法和环境之间进行通信的标准 API，以及一组兼容该 API 的标准环境。已迁移至 [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) 

[Agility Robotics 的 Cassie 机器人的 mujoco 模拟因尽可能快地向前行走/奔跑而获得奖励](https://github.com/perrin-isir/gym-cassie-run) - [其他](https://github.com/AlexandreChenu/gym_cassie_dcil)

[在本地、Slurm 和 GCP 上运行 RL 代码](https://github.com/bstadie/rl_starter_kit)

[机器人套件](https://github.com/Aleenatron/Robot-Manipulation-)

[允许用户通过网络浏览器与机器人互动](https://github.com/openroboticmetaverse/mvp_mujoco_simulation)

[一个优雅的 PyTorch 深度强化学习库](https://github.com/thu-ml/tianshou)

[开发用于机器人任务的 RL 代理的环境](https://github.com/alefram/TEG)

[robosuite是一个基于MuJoCo物理引擎的机器人学习模拟框架](https://github.com/HumanoidAI/robosuite-dev) - [其他2](https://github.com/JesseDill/robosuite_articulated) 、 [其他3](https://github.com/jacklishufan/cs269-proj) 、[其他4](https://github.com/SruthiSudhakar/robosuite) 、[其他5](https://github.com/huihanl/robosuite-sirius-fleet)

[Google Cloud Platform 上的数据和 AI 平台](https://github.com/Simbamon/GCP_ML)

[基于MuJoCo的多平台、模块化机器人仿真框架](https://github.com/NoneJou072/robopal) - 主要用于机械臂的强化学习和控制算法实现

[人机交互学习（HILL）和多智能体强化学习（MARL）研究平台](https://github.com/cogment/cogment-verse)

[包含 REINFORCE、AC2、SAC 和 PPO 等热门算法的实现，并集成到 Gymnasium 环境](https://github.com/zachoines/RL-Grimoire)

[七种机器人模型、八种夹爪模型、六种控制器模式和九种标准化任务](https://github.com/lemonlemonde/robosuite1.4-modded)

[ReDMan 是一个开源模拟平台，为可靠的灵巧操作提供了安全 RL 算法的标准化实现](https://github.com/PKU-Alignment/ReDMan)

[Ray 由一个核心分布式运行时和一组用于加速 ML 工作负载的 AI 库组成](https://github.com/ray-project/ray)

[Jax 中实现的强化学习算法集合](https://github.com/nutorbit/rl-zoo)

[机器人学习的统一框架](https://github.com/vikashplus/robohive)

[一种多功能模块化框架，使用框图方法运行/模拟动态系统](https://github.com/implementedrobotics/BlockFlow)

[在加速器硬件上进行大规模并行刚体物理模拟](https://github.com/google/brax)

[通才generalist](https://github.com/grahamannett/generalist)


## 工具 <span id="tool"></span>

[MuJoCo 模拟、可视化和数据处理的综合工具包](https://github.com/ShanningZhuang/mujoco_tools)

[将 robot urdf 文件转换为 mjcf 的工具](https://github.com/FFTAI/Wiki-GRx-MJCF) - [将 URDF 模型转换为 MJCF 模型的实用工具](https://github.com/ipa320/urdf2mjcf) - [其他](https://github.com/kscalelabs/urdf2mjcf)

[用于将MJCF（MuJoCo 建模格式）机器人模型文件中的有限元素转换为 URDF 的脚本](https://github.com/Yasu31/mjcf_urdf_simple_converter)

[基于 Web 的模拟环境可视化工具](https://github.com/NVlabs/sim-web-visualizer)

[一种强化学习框架，用于在持续学习场景中探索网络拓扑结构](https://github.com/kat-ko/topology-playground)

[Genesis强化学习（RL）框架](https://github.com/Jcouronne/Genesis-RL)

[用于生成 Mujoco 模型的动画，进而可用于训练机器人执行定制行为](https://github.com/kscalelabs/mujoco-animator)

[本项目提供了一个框架，用于通过XR（VR/AR）输入设备在机器人硬件和MuJoCo仿真中控制机器人。它允许用户使用通过XR控制器捕捉到的自然手部动作来操控机器人手臂](https://github.com/XR-Robotics/XRoboToolkit-Teleop-Sample-Python)

[旨在对多任务和元强化学习进行基准测试的机器人环境集合](https://github.com/Farama-Foundation/Metaworld)

[用于处理 MuJoCo MJCF 模型的常用工具](https://github.com/janelia-anibody/mujoco_utils)

[评估各种 DRL 算法在功耗和性能之间的权衡](https://github.com/lucastrefezza/reinforcement-learning-sustainability-benchmark)

[Jax-Baseline 是一种使用 JAX 和 Flax/Haiku 库的强化学习实现，反映了 Stable-Baselines 的功能](https://github.com/tinker495/jax-baseline)

[强化学习工具包（RLTK）](https://github.com/1Kaustubh122/reinforcement-learning-toolkit)

[将现实世界的坐标空间映射到模拟坐标空间](https://github.com/WT-MM/retos)

[MLPro：集成多关节动力学与接触（MuJoCo）](https://github.com/fhswf/MLPro-Int-MuJoCo)

[Google DeepMind MuJoCo 的现代模拟包装器](https://github.com/MGross21/mujoco-toolbox)

[Fast-UMI：一种可扩展且独立于硬件的通用操作接口](https://github.com/zxzm-zak/FastUMI_Data)

[mink 是一个基于MuJoCo物理引擎的 Python 微分逆运动学库](https://github.com/kevinzakka/mink) - [其他](https://github.com/jonathanembleyriches/mink)

[用于边缘 AI 和机器人的 CUDA 容器](https://github.com/dusty-nv/jetson-containers)

[将其组织在单个文件中来增强可读性](https://github.com/Taka-Hashimoto/Simple_TDMPC)

[一个基于 C++ 的批处理环境池 EnvPool](https://github.com/sail-sg/envpool) - 基于 C++ 的高性能并行环境执行引擎（矢量化环境），适用于通用 RL 环境

[用于强化学习的机器人模拟环境集合](https://github.com/Farama-Foundation/Gymnasium-Robotics)

[基于Onshape API，从组件中检索信息并构建适合物理模拟的机器人描述（URDF、SDF、MuJoCo）](https://github.com/Rhoban/onshape-to-robot)

[Onshape 到机器人（URDF、SDF、MuJoCo）](https://github.com/nikolasdoan/onshape-urdf)

[机器人领域的扩散模型](https://github.com/SquareRootTwo/Diffusion-Policy-Collision-Avoidance)

[用于处理MuJoCo Python 绑定和dm_control 的实用程序](https://github.com/kevinzakka/mujoco_utils)

[通过潜在想象力进行学习的行为](https://github.com/falheisen/BE_dreamer)

[可作为各种强化学习 (RL) 算法的实验场地](https://github.com/seisenmann/RL-Playground)

[使用 MuJoCo 物理引擎执行系统辨识](https://github.com/based-robotics/mujoco-sysid)

[BuildingGym 项目提供了一个 API，用于轻松训练适用于所有 EnergyPlus 环境的强化学习控制算法，并包含常见强化学习算法的实现：策略梯度、DQN、A2C、A3C 等](https://github.com/BuildingGym/BuildingGym)

[Dreamer 的干净 Python 重新实现](https://github.com/minhphd/PyDreamerV1)

[用于自动将动作捕捉添加到 mujoco xml 文件的工具](https://github.com/mochan-b/mujoco_mocapper)

[强化学习算法的实现](https://github.com/sgoodfriend/rl-algo-impls)

[Mechcat Mujoco 查看器](https://github.com/ialab-yale/meshcat-mujoco)

[加速多智能体强化学习的程序环境生成](https://github.com/tomalner18/MAax)

[流行的 DRL 算法的简单实现](https://github.com/HengLuRepos/lighter-RL)

[SERL：用于样本高效机器人强化学习的软件套件](https://github.com/rail-berkeley/serl) - [其他](https://github.com/serl-robot/serl)

[为许多有用的机器人库提供通用 API](https://github.com/Tass0sm/corallab-lib)

[MCPHC_old](https://github.com/NamiNaziri/MCPHC_old)

[使用 OpenAI gym 的强化学习示例集合](https://github.com/Makoto1021/reinforcement-learning-examples)

[基于 GPU 加速模拟的内部工具](https://github.com/Caltech-AMBER/ambersim)

[一个用于优化的 Python 库，面向模块化机器人和进化计算](https://github.com/ci-group/revolve2)

[深度强化学习算法和环境的 PyTorch 实现](https://github.com/liu-cui/Deep-Reinforcement-Learning-in-Action-with-PyTorch)

[reboot-toolkit](https://github.com/RebootMotion/reboot-toolkit)

[unfaithful-cot-replication](https://github.com/bpwu1/unfaithful-cot-replication)

[结构化的模块化设置，用于使用 Ray RLlib 库训练强化学习 (RL) 模型](https://github.com/artificial-experience/ray-rllib-proto)

[用于机器人操作的模块化接口](https://github.com/raunaqbhirangi/manimo)

[统一原生 MuJoCo (MJC) 和 MuJoCo-XLA (MJX) 中实现的环境的开发和接口](https://github.com/Co-Evolve/mujoco-utils)

[专注于快速构建 DQN 模型原型](https://github.com/odiaz1066/lagomorph)

[包含几个具有正定成本函数的 gym 环境，旨在与稳定的 RL 代理兼容](https://github.com/rickstaa/stable-gym)

[Transformer (TIT) 中 Transformer 作为深度强化学习骨干的官方实现](https://github.com/anonymoussubmission321/TIT_anonymous)

[cleanrl 具有研究友好特性的深度强化学习算法的高质量单文件实现（PPO、DQN、C51、DDPG、TD3、SAC、PPG）](https://github.com/IanWangg/CleanRL-Projects) - [其他](https://github.com/eleninisioti/dirtyrl) 、 [其他2](CleanRL：深度强化学习算法的高质量单文件实现) 、 [其他3](https://github.com/jyoung2247/dl_project) 、[其他4](分布式、循环、深度强化学习算法的最小实现) 、[其他5](https://github.com/vwxyzjn/cleanrl) 、[其他6](https://github.com/superboySB/mindspore-cleanrl) 、  [其他7](https://github.com/gosu0rZzz/thesis_exp) 、 [其他8](https://github.com/moraguma/PyET)

[基于 OpenAI 的 RL 库](https://github.com/MnSBlog/Pinokio.RL)

[提供了一个用于在学习算法和环境之间进行通信的标准 API](https://github.com/fliegla/diffDrive)

[包含 Google Research发布的代码](https://github.com/Rulial/GoogleRe-Pi)

[为硕士论文项目的开发和一些研究活动提供环境](https://github.com/unisa-acg/oracle-force-optimizer)

[RL-Bandits](https://github.com/MuhangTian/RL-Bandits)

[适用于 ML 和 AI 项目/实验的实用小模板](https://github.com/WillieCubed/ai-project-template)

[用于开发和比较强化学习算法的工具包](https://github.com/drakyanerlanggarizkiwardhana/gym)

[使用 Unity ML-Agents (AI) 进行深度强化学习的 3D 包装](https://github.com/bryanat/Reinforcement-Learning-Unity-3D-Packing)

[一些基于 MuJoCo 物理引擎构建的 (C/C++) 示例和扩展](https://github.com/wpumacay/mujoco-ext)

[Mujoco Deepmind 的 Python 绑定中存储库mujoco_panda的实现](https://github.com/varadVaidya/mujoco_arm)



[另一个 Python RL 库](https://github.com/tfurmston/tfrlrl)

[深度强化学习算法的简单单文件实现](https://github.com/vcharraut/rl-basics)

[PyTorch 中基于模型的强化学习的最小库](https://github.com/aidanscannell/mbrl-under-uncertainty)

[标准化机器学习的集成中间件框架](https://github.com/fhswf/MLPro)

[OpenAI Gym 环境使用 pybullet 来制作Tyrannosaur](https://github.com/bingjeff/trex-gym)

[通用人工智能实验室开发的容器](https://github.com/HorizonRoboticsInternal/gail-container)

[强化学习库之间的互操作](https://github.com/epignatelli/helx)

[Mujoco并行模拟](https://github.com/Daniellayeghi/MujocoParallel)

[现代机器学习论文的实现，包括 PPO、PPG 和 POP3D](https://github.com/rusenburn/Axel)

[机器学习和数据科学的附加软件包](https://github.com/nixvital/ml-pkgs)

[Emei 是一个用于开发因果强化学习算法的工具包](https://github.com/polixir/emei)

[YAROK - 另一个机器人框架](https://github.com/danfergo/yarok)

[JAX（Flax）实现具有连续动作空间的深度强化学习算法](https://github.com/ikostrikov/jaxrl) 

[用于处理 MuJoCo 中使用的复合 Wavefront OBJ 文件的 CLI](https://github.com/kevinzakka/obj2mjcf)

[用于执行无梯度优化的 Python 工具箱](https://github.com/facebookresearch/nevergrad)



## 杂项 <span id="misc"></span>

[仿生机器人](https://github.com/hty0111/Biorobotics)

[rl_project](https://github.com/NehalNetha/rl_project)

[weekend](https://github.com/mohammad200h/weekend)



[InterGP](https://github.com/tdardinier/InterGP) - 收集数据、训练代理的流程

[深度强化学习课程完成的近端策略优化作业](https://github.com/caiopetruccirosa/half-cheetah-ppo)

[Go2-Unity](https://github.com/rohit-kumar-j/Go2-Unity)

[ACM AI 所有研讨会内容代码等的存储库](https://github.com/acmucsd/acm-ai-workshops) - 内容按季度组织

[Docker Wiki 和示例](https://github.com/dotd/docker_wiki)

[sim2real-trunk](https://github.com/vandaele/sim2real-trunk)

[ClearML_SCHOOL](https://github.com/MichaelNed/ClearML_SCHOOL)

[一个最小（但独立）的 MuJoCo 模拟器来运行模拟](https://github.com/mosesnah-shared/mujoco-py-v2)

[微电网的 IRIS 代码](https://github.com/shukla-yash/IRIS-Minigrid)

[使用 mujoco 进行 DOQ 模拟](https://github.com/griffinaddison/doq_viz)

[franka_simulation](https://github.com/Yujin1007/franka_simulation)

[网络可塑性](https://github.com/arjunpat/network-plasticity)

[PPO 和 Friends 是近端策略优化的 PyTorch 实现，同时还具有各种额外的优化和附加组件](https://github.com/lior10r/ppo_and_friends)

[pixel_gcrl](https://github.com/nicolascastanet/pixel_gcrl)

[具有策略预算的个性化强化学习](https://github.com/dimonenka/RL_policy_budget)

[sb3-mujoco-1](https://github.com/hansen1416/sb3-mujoco-1)

[使用 GP 作为探索指标](https://github.com/contagon/gp4expl)

[高级软件实践](https://github.com/YongBonJeon/Advanced-Software-Practices)

[实施监督 Actor-Critic 策略提炼作为其他迁移学习 RL 方法的基础](https://github.com/HAI-lab-UVA/policy-distillation-andrew)

[DRL-AirHockey](https://github.com/zhalehmehrabi/DRL-AirHockey) - [其他1](https://github.com/ShuoZheLi/air_hockey_challenge_robosuite)

[mt-world-model-pretraining](https://github.com/jaredmejia/mt-world-model-pretraining)

[了解 Transformer 的研讨会](https://github.com/klao/t9r-class)

[RoboDog项目](https://github.com/Stblacq/robodog)

[amr_fleet_offboard_infra_frontend](https://github.com/DockDockGo/amr_fleet_offboard_infra_frontend)

[network-plasticity](https://github.com/arjunpat/network-plasticity)

[自己实现的深度强化学习算法](https://github.com/minghongx/deeprl)

[用于控制推测解码中需要预测的标记数量](https://github.com/skrider/speculative-forecasting)

[LLM_CD](https://github.com/ElmoPA/LLM_CD)

[无监督强化学习](https://github.com/siddharthbharthulwar/unsupervised-rl)

[通过 10 个视觉变化因素扩展 Metaworld 环境](https://github.com/dtch1997/factor-world)

[rl_learning](https://github.com/yuxuehui/rl_learning)

[many_gamma](https://github.com/samlobel/many_gamma)

[231A_project](https://github.com/johnviljoen/231A_project)

[cs340lab4](https://github.com/Dylan920424/cs340lab4)

[强化学习研究](https://github.com/fredsonaguiar/bang_bang_mountain_car)

[DPC_for_robotics](https://github.com/pnnl/DPC_for_robotics)

[talar-openreview-fork](https://github.com/ezhang7423/talar-openreview-fork)

[pytorch-TD3fG-fast](https://github.com/www8098/pytorch-TD3fG-fast)

[symmetry-cs285-2](https://github.com/YasinSonmez/symmetry-cs285-2)

[training-gym](https://github.com/joshbrowning2358/training-gym)

[尝试实施强化学习](https://github.com/WhoKnowsWhoCares/RL)

[S7-RL](https://github.com/JJulessNL/S7-RL)

[clean-jax-rl](https://github.com/chkda/clean-jax-rl)

[SIMCSUM](https://github.com/MehwishFatimah/SimCSum)

[mb-强化](https://github.com/nhaij/mb-reinforcement)

[CQLEnsemble](https://github.com/XGsombra/CQLEnsemble)

[factored-rl-ppo-handson](https://github.com/davera-017/factored-rl-ppo-handson)

[oc-jax](https://github.com/Shunichi09/oc-jax)

[漩涡示例](https://github.com/DeaconSeals/maelstrom-examples)

[rl-cbf-2](https://github.com/dtch1997/rl-cbf-2)

[GCPrior](https://github.com/magenta1223/GCPrior)

[sb3-mujoco-2](https://github.com/hansen1416/sb3-mujoco-2)

[Reinforcement-Learning-2023](https://github.com/bencer3283/Reinforcement-Learning-2023)

[Prism](https://github.com/motschel123/Prism)

[rep_complexity_rl](https://github.com/realgourmet/rep_complexity_rl)

[CustomGymEnvs](https://github.com/DeaconKaiJ/Custom_Gym)

[游戏AI](https://github.com/craigdods/Game-Playing-AIs)

[更新 D4Rl 以获取最新的 Gymnasium API](https://github.com/Altriaex/d4rl)

[planseqlearn](https://github.com/planseqlearn/planseqlearn)

[人工生命环境](https://github.com/IBN5101/APx-IP)

[简单的独立平面推动焦点示例](https://github.com/UM-ARM-Lab/pushing_FOCUS)

[rl_learning](https://github.com/loxs123/rl_learning)

[强化学习实验](https://github.com/rddy/ggrl)

[kics_rl_lab](https://github.com/dtch1997/svf-gymnasium)

[Gym 环境解决方案](https://github.com/jinymusim/gym-solutions)

[gym 的安全价值函数](https://github.com/dtch1997/svf-gymnasium)

[CQL_sepsis](https://github.com/NanFang2023/CQL_sepsis)

[长期记忆系统](https://github.com/grahamseamans/ltm)

[OCMR](https://github.com/rpapallas/OCMR)

[HybridSim](https://github.com/dmiller12/HybridSim)

[关键用户旅程（CUJ）](https://github.com/woshiyyya/CUJ)

[orax](https://github.com/ethanluoyc/orax)

[MAZE](https://github.com/DuangZhu/MAZE)

[safetyBraxFramework](https://github.com/YusenWu2022/safetyBraxFramework)

[旅游预测项目](https://github.com/VorkovN/TourismPredictionProject)

[InfusedHKS](https://github.com/SSHAY007/InfusedHKS)

[mario-icm](https://github.com/denmanorwatCDS/mario-icm)

[inctxdt](https://github.com/grahamannett/inctxdt)

[web3env](https://github.com/Crinstaniev/web3env)

[T-AIA-902](https://github.com/SimonMonnier/T-AIA-902)

[rl_air-hockey_telluride](https://github.com/lunagava/rl_air-hockey_telluride)

[panda_robot](https://github.com/Yuchengxiao997/panda_robot)

[Praktikum](https://github.com/dima2139/Praktikum)

[VKR](https://github.com/Crechted/VKR)

[crow](https://github.com/ghl3/crow)

[CRA_push](https://github.com/UT-Austin-RobIn/CRA_push)

[包含数据集处理、遗传算法、神经网络等](https://github.com/BartoszBrodowski/computational-intelligence)

[RLproject](https://github.com/ttopeor/RLproject)

[展示了平面二维机器人，但可以立即将其推广到空间三维机器人](https://github.com/jongwoolee127/redundancy_resolution)

[p8_sewbot](https://github.com/kasperfg16/p8_sewbot)

[smarts_git](https://github.com/rongxiaoqu/smarts_git)

[一个沙盒仓库](https://github.com/jeh15/sandbox)

[eth-rl](https://github.com/Crinstaniev/eth-rl)

[用于 SRL 实验室实践的 Jupyter 笔记本](https://github.com/srl-ethz/lab-practice-nbs)

[Demo 282 Guarrera](https://github.com/matteoguarrera/demo_282)

[crazyflie_backflipping](https://github.com/AIMotionLab-SZTAKI/crazyflie_backflipping)

[强化学习实验](https://github.com/parthh01/rl_stuff)

[gail_demo](https://github.com/archana53/gail_demo)

[npds-workspace](https://github.com/ashiskb/npds-workspace)

[Advanced_Software](https://github.com/jiseok99/Advanced_Software)

[Reinforcement-Learning](https://github.com/leopoldlacroix/Reinforcement-Learning)

[fyp_v1](https://github.com/derekcth-wm21/fyp_v1)

[模块化部署](https://github.com/olivier-serris/ModularRollouts)

[玩具 ML 项目](https://github.com/pauldb89/ml)

[skill-basedGCRL](https://github.com/magenta1223/skill-basedGCRL)

[ML/DL/CS 领域的一些工作清单](https://github.com/vshmyhlo/research) - 包括基于 GAN 的图像生成、物体检测、神经机器翻译、相似性和度量学习、语音转文本、文本转语音

[CHTC 上的 Mujoco](https://github.com/NicholasCorrado/CHTC)

[从各种来源尝试的实践课程](https://github.com/BhaskarJoshi-01/Competitive-Programming)

[这是Spinning Up的一个克隆版本，目标是使用最新的 PyTorch 版本](https://github.com/haha1227/spinningup-pytorch)

[TradeMasterReBuild](https://github.com/DVampire/TradeMasterReBuild)

[Fast Campus 强化学习](https://github.com/Junyoungpark/ReinforcementLearningAtoZ)

[Reddit 评论机器人是一个基于 Python 的自动回复器](https://github.com/benparrysapps/comment-meme-generator)

[一些强化学习的算法](https://github.com/etu7912a48/RL_algorithm) - 使用的环境是Windows10上的Python 3.10

[Gym的欠驱动机器人](https://github.com/RonAvr/Underactuated_with_gym)