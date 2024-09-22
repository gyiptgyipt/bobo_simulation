### README
###### Dropped empty horizontal range data Warning and map not received #1812

အရ map မပေါ်ရတဲ့ အကြောင်းသည် lidar ရဲ့ z position က Zero ဖြစ်နေလို့ဆိုပါတယ်။ ဘာလို့လဲဆိုတော့ tracking_frame=robot_frame ဖြစ်နေတာမို့လို့ base_footprint ရဲ့ z position ဖြစ်နေတာလို့ ဆိုပါတယ်။ documentation အရတော့ tracking_frame ကို အောက်ပါအတိုင်း ဖေါ်ပြပါတယ်။
```
tracking_frame
   The ROS frame ID of the frame that is tracked by the SLAM algorithm. If an IMU is used, it
   should be at its position, although it might be rotated. A common choice is “imu_link”.
```
- အဲ့တော့ tracking_frame=lidar_link ထည့်ပေးပြီး ဖြေရှင်းနိင်တယ်လို့ဆိုပါတယ်။
- နောက် ဖြေရှင်းနည်းကတော့ tracking_frame=robot_frame ပဲထားမယ်ဆိုရင် 2D Trajectory Builder ရဲ့ z range ကို အောက်ပါအတိုင်း သတ်မှတ်ပေးလို့ရတယ်ဆိုပါတယ်။
```
TRAJECTORY_BUILDER_2D.min_z =3.
TRAJECTORY_BUILDER_2D.max_z =4.
```
အဲ့ကောင်သည် pose of lidar_frame w.r.t robot_frame ဖြစ်သင့်ပါတယ်။





### TODO