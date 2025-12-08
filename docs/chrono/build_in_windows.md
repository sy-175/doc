# Windows 下 Chrono 的源代码编译

1. 克隆仓库
    ```shell
    git clone https://github.com/OpenHUTB/chrono.git
    ```
2. 使用CMake配置chrono

    设置好`Where is the source code`为`C:/workspace/chrono`；`Where to build the binarys:`为`C:/Packages/chrono_build`

    依此点击`Configure`按钮，选择合适的平台，比如x64。

    点击`Generate`。

!!! 注意
   如果点击`Configure`报没有Eigen的错误，则运行`chrono\contrib\build-scripts\windows\buildEigen.bat`进行Eigen安装。

3. 使用VS2019双击打开`C:\Packages\chrono_build\Chrono.sln`。选择`Release`进行构建。




## 参考

* [安装Chrono教程](https://api.projectchrono.org/tutorial_install_chrono.html#scripts)
