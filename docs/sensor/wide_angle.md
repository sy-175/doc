# 广角相机传感器

广角相机传感器模拟了广角、鱼眼和大扭曲相机镜头的系统。为解决此问题，该模型实现采用了**立方体贴图**方法，具体解释如下：

* 传感器生成6个标准透视相机，指向所有方向（前、后、左、右、上、下），以捕获整个环境。

* 它使用一个 [计算着色器](https://mp.weixin.qq.com/s/yB5oKXeL7bYjZ3NioE3NvQ) (Compute Shader)，基于数学镜头模型（例如，Kannala-Brandt模型）对这 6 幅图像进行采样，并将它们拼接成一幅 2D 输出图像。



## 参考

* [原生鱼眼相机仿真效果及代码分析](https://mp.weixin.qq.com/s/GsEzR-R0xvIyUzSor6j6XQ)