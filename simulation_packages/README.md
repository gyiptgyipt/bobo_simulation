### Driver
#### friction
solidwork က ဆွဲတဲ့ urdf မှာ caster ၄ လုံးပါပြီး simulation လုပ်ဖို့ ခက်တာကြောင့် caster ၂ လုံးဖြုတ် ကျန်တဲ့ နှစ်လုံးကို ရှေ့နောက် ညီအောင် y-axis 0 နေရာမှာထားပါတယ်။ ဒါနဲ့တင် မလုံလောက်လို့ friction ထည့်ပါတယ်။
```diff
  <gazebo reference="front_right_caster_wheel_link">
    <material>Gazebo/Black</material>
    <!--tags are from: http://gazebosim.org/tutorials/?tut=ros_urdf-->
    <!--These values fixed the robot from bouncing side to side:
          Problem: http://answers.gazebosim.org/question/24459/model-contact-with-ground-issue/
          solution: see: http://answers.gazebosim.org/question/3334/slip1-slip2-in-urdf/-->
    <kp>1000000.0</kp>
    <kd>10.0</kd>
    <mu1>0.0</mu1>
    <mu2>0.0</mu2>
    <fdir1>1 0 0</fdir1>
    <maxVel>1.0</maxVel>
    <minDepth>0.00</minDepth>
  </gazebo>
  <gazebo reference="back_right_caster_wheel_link">
    <material>Gazebo/Black</material>
    <!--tags are from: http://gazebosim.org/tutorials/?tut=ros_urdf-->
    <!--These values fixed the robot from bouncing side to side:
          Problem: http://answers.gazebosim.org/question/24459/model-contact-with-ground-issue/
          solution: see: http://answers.gazebosim.org/question/3334/slip1-slip2-in-urdf/-->
    <kp>1000000.0</kp>
    <kd>10.0</kd>
    <mu1>0.0</mu1>
    <mu2>0.0</mu2>
    <fdir1>1 0 0</fdir1>
    <maxVel>1.0</maxVel>
    <minDepth>0.00</minDepth>
  </gazebo>

  <gazebo reference="left_wheel_link">
    <material>Gazebo/Black</material>
    <kp>1000000.0</kp>
    <kd>10.0</kd>
    <mu1>1.1</mu1>
    <mu2>1.1</mu2>
    <fdir1>1 0 0</fdir1>
    <maxVel>1.0</maxVel>
    <minDepth>0.00</minDepth>
  </gazebo>
  <!--  -->
<gazebo reference="right_wheel_link">
    <material>Gazebo/Black</material>
    <kp>1000000.0</kp>
    <kd>10.0</kd>
    <mu1>1.1</mu1>
    <mu2>1.1</mu2>
    <fdir1>1 0 0</fdir1>
    <maxVel>1.0</maxVel>
    <minDepth>0.00</minDepth>
</gazebo>
```
ပိုမို အဆင်ပြေအောင်လို့ caster နှစ်ခုကို z-axis 2cm စီ နှိမ့်လိုက်ပါတယ်။
```diff
<joint name="back_right_caster_joint" type="revolute">
    <!-- <origin rpy="0 0 0" xyz="-0.16676 -0 0.1"/> -->
    <origin rpy="0 0 -0.02" xyz="-0.16676 -0 0.1"/>
```

#### Plus or Minus One meter test
ဘယ်လိုပဲ friction ထည့်သော်လည်းပဲ hardware robot သို့မဟုတ် simulation robot ရဲ့ 1 meter distance သည်  differential drive kinematic ရဲ့ tf 1 meter နဲ့ အကွာအဝေး အတိအကျ မတူပါဘူး။
- 20 Hz သုံးထားတာလည်း သတိပြုသင့်တယ်။
နမူနာ ယူဖို့အတွက် တရုတ်ရဲ့ reeman robot ကို စစ်ဆေးတဲ့အခါ အောက်ပါအတိုင်းတွေ့ရတယ်။
```md
./install/include/teb_local_planner/teb_config.h:    double weight_max_vel_theta; //!< Optimization weight for satisfying the maximum allowed angular velocity
./install/include/teb_local_planner/teb_config.h:    robot.max_vel_x = 0.4;
./install/include/teb_local_planner/teb_config.h:    robot.max_vel_x_backwards = 0.2;
./install/include/teb_local_planner/teb_config.h:    robot.max_vel_y = 0.0;
./install/include/teb_local_planner/teb_config.h:    robot.max_vel_trans = 0.0;
./install/include/teb_local_planner/teb_config.h:    robot.max_vel_theta = 0.3;
./install/include/teb_local_planner/teb_config.h:    obstacles.obstacle_proximity_ratio_max_vel = 1;


./install/share/yoyo_bringup/param/local_planner_params_robot4.yaml:max_vel_x: 0.5
./install/share/yoyo_bringup/param/local_planner_params_robot4.yaml:max_vel_x_backwards: 0.0
./install/share/yoyo_bringup/param/local_planner_params_robot4.yaml:max_vel_y: 0.0
./install/share/yoyo_bringup/param/local_planner_params_robot4.yaml:max_vel_theta: 0.5
./install/share/yoyo_bringup/param/local_planner_params_robot2.yaml:max_vel_x: 0.15
./install/share/yoyo_bringup/param/local_planner_params_robot2.yaml:max_vel_x_backwards: 0.0
./install/share/yoyo_bringup/param/local_planner_params_robot2.yaml:max_vel_y: 0.0
./install/share/yoyo_bringup/param/local_planner_params_robot2.yaml:max_vel_theta: 0.15
./install/share/yoyo_bringup/param/local_planner_params_robot3.yaml:max_vel_x: 0.5
./install/share/yoyo_bringup/param/local_planner_params_robot3.yaml:max_vel_x_backwards: 0.0
./install/share/yoyo_bringup/param/local_planner_params_robot3.yaml:max_vel_y: 0.0
./install/share/yoyo_bringup/param/local_planner_params_robot3.yaml:max_vel_theta: 0.5
./install/share/yoyo_bringup/param/local_planner_params_robot1.yaml:max_vel_x: 0.5
./install/share/yoyo_bringup/param/local_planner_params_robot1.yaml:max_vel_x_backwards: 0.0
./install/share/yoyo_bringup/param/local_planner_params_robot1.yaml:max_vel_y: 0.0
./install/share/yoyo_bringup/param/local_planner_params_robot1.yaml:max_vel_theta: 0.5
./install/share/yoyo_bringup/param/local_planner_params_robot5.yaml:max_vel_x: 0.5
./install/share/yoyo_bringup/param/local_planner_params_robot5.yaml:max_vel_x_backwards: 0.0
./install/share/yoyo_bringup/param/local_planner_params_robot5.yaml:max_vel_y: 0.0
./install/share/yoyo_bringup/param/local_planner_params_robot5.yaml:max_vel_theta: 0.5
./install/share/yoyo_bringup/param/teb_local_planner_params_common.yaml:  # max_vel_x: 0.5 🌟
./install/share/yoyo_bringup/param/teb_local_planner_params_common.yaml:  # max_vel_x_backwards: 0.0 🌟
./install/share/yoyo_bringup/param/teb_local_planner_params_common.yaml:  # max_vel_y: 0.0
./install/share/yoyo_bringup/param/teb_local_planner_params_common.yaml:  # max_vel_theta: 0.5 🌟
./install/share/yoyo_bringup/param/teb_local_planner_params_common.yaml:  weight_max_vel_x: 2
./install/share/yoyo_bringup/param/teb_local_planner_params_common.yaml:  weight_max_vel_y: 1
./install/share/yoyo_bringup/param/teb_local_planner_params_common.yaml:  weight_max_vel_theta: 1
```
ဆိုတော့ ကာ သူတို့သည် max velocity 0.5 meter persecond နဲ့ backward အတွက် 0.0 ထားထားတယ်။ နောက်ပြန်မသွားခိုင်းတဲ့သဘောပေါ့။
-  ဆိုတော့ ကျတော်တို့လည်းပဲ min velocity = 0.0 နဲ့ 🌟 max velocity 0.5 သုံးမယ်။ 
-  1 meter test လုပ်တဲ့အခါ 0.5 သုံးမလား 0.25 သုံးမလား 0.3 လား 0.4 လားဆိုတော့ 🔥 0.25 ms နဲ့ test မယ်ဗျာ။
- 0.25 ms ကို 20 Hz နဲ့ မြှောက်တဲ့အခါ 1 second မှာ 5 meter သွားရမှာပါ။ ဒါပေမဲ့ ကျတော်တို့ အချိန်နဲ့ မစစ်ဆေးဘဲ simulation သို့ မဟုတ် real environment မှာ 1 meter သွားခိုင်းပြီး rviz မှာ tf 1 meter ပြည့်မပြည့် စစ်ဆေးပါမယ်။
- plus ပြီးရင် minus စမ်းချင်စမ်းလို့ရပါတယ်။

#### Plus or Minus 2pi radian test
- max_vel_theta က 0.5 radian per second ထားတော့ ကျတော်တို့လည်း 🌟 max_angular_velocity = 0.5 ထားပြီး 2Pi test ကတော့ 🔥 0.25 rds နဲ့ စမ်းမယ်ဗျာ။
- robot ကို angular 0.25 rds * 20 Hz ဆိုရင် 5 radian ရောက်ရပါမယ်။ ဒါပေမဲ့ ကျတော်တို့ အချိန်နဲ့ မခိုင်းဘဲ 2PI radian ပြည့်အောင် publish လုပ်ပေးပါမယ်။
- plus ပြီးရင် minus စမ်းကို စမ်းရပါမယ်။

ros-humble-diff-drive-controller/jammy 2.37.3-1jammy.20240911.164844 amd64 [upgradable from: 2.37.2-1jammy.20240823.151618]
