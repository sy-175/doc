# Windows 下 Chrono 的源代码编译

1. 克隆仓库
    ```shell
    git clone https://github.com/OpenHUTB/chrono.git
    ```
2. 使用CMake配置chrono

    设置好`Where is the source code`为`C:/workspace/chrono`；`Where to build the binarys:`为`C:/Packages/chrono_build`

    依此点击`Configure`按钮，选择合适的平台，比如`x64`。

    点击`Generate`。

!!! 注意
   如果点击`Configure`报没有Eigen的错误，则运行`chrono\contrib\build-scripts\windows\buildEigen.bat`进行Eigen安装。然后再点击`Configure`。

3. 使用VS2019双击打开`C:\Packages\chrono_build\Chrono.sln`。选择`Release`或`Debug`进行构建。

## 运行 buildChrono.bat

安装相关依赖：

[OptiX SDK 7.5.0](https://developer.nvidia.com/designworks/optix/downloads/legacy)

[swigwin](https://sourceforge.net/projects/swig/files/swigwin/)

[occt-vc14-64](https://dev.opencascade.org/release/previous#node-88166)

[fastrtps 2.14.5](https://github.com/eProsima/Fast-DDS/releases?page=8)

[MKL](https://api.projectchrono.org/module_mkl_installation.html)

```shell
git clone https://github.com/eProsima/Fast-DDS.git Fast-DDS-2.14.5
cd Fast-DDS-2.14.5
# 注意：编译v2.4.0代码到编译Fast-DDS时会报错：error c3861:“ Mtx init”: 找不到标识符
git checkout -b v2.14.5 v2.14.5
# 拉取子模块android-ifaddrs,asio,fascdr,tinyxml2
git submodule update --init
#需要添加一个子模块
git submodule add https://github.com/foonathan/memory.git thirdparty/foonathan-memory


# 编译 fastcdr
cd thirdparty/fastcdr
mkdir build & cd build
cmake ../ -DCMAKE_INSTALL_PREFIX=C:\Packages\eProsima\Fast-DDS-2.14.5\thirdparty\install
#如果在ubuntu下因为cmake的版本低导致camke失败，可以直接在源码中修改cmake最低要求版本号
# 使用vs打开build目录下生成的sln工程文件，编译，安装（右键INSTALL工程，在弹出的菜单中选择“仅用于项目->仅生成INSTALL”，会安装编译产物）；
# 如果是linux，则使用命令 make && make install
call "%ProgramFiles%\Microsoft Visual Studio\2022\Community\MSBuild\Current\bin\MSBuild.exe" fastcdr.sln


# 编译tinyxml2
cd thirdparty/tinyxml2
mkdir build & cd build
cmake ../ -DCMAKE_INSTALL_PREFIX=C:\Packages\eProsima\Fast-DDS-2.14.5\thirdparty\install
# 使用vs打开sln工程，编译，安装；
# 如果是linux，则使用命令 make && make install



# 编译 foonathan-memory
cd thirdparty/foonathan-memory
mkdir build & cd build
cmake ../ -DFOONATHAN_MEMORY_BUILD_EXAMPLES=OFF -DFOONATHAN_MEMORY_BUILD_TESTS=OFF -DCMAKE_INSTALL_PREFIX=C:\Packages\eProsima\Fast-DDS-2.14.5\thirdparty\install
# 使用vs打开sln工程，编译，安装；如果是linux，则使用命令 make && make install


# 编译Fast-DDS和调试
cd Fast-DDS-2.14.5
mkdir build & cd build
cmake ../ -DCMAKE_PREFIX_PATH="C:\Packages\eProsima\Fast-DDS-2.14.5\thirdparty\asio\asio;C:\Packages\eProsima\Fast-DDS-2.14.5\thirdparty\install" -DCMAKE_INSTALL_PREFIX=C:\Packages\eProsima\Fast-DDS-2.14.5_install -DNO_TLS=ON -DCOMPILE_EXAMPLES=ON
# 在目录 C:\Packages\eProsima\Fast-DDS-2.14.5\build\examples\cpp\dds\DiscoveryServerExample 打开 DiscoveryServerExample.sln，编译 fastrtps 和 DiscoveryServerExample
# 然后再使用vs打开build/fastrtps.sln工程，编译，安装

```


## 问题

* 编译完成后，运行`demo_PARSER_OpenSim`报错
```text
由于找不到 `Irrlicht.dll`，无法继续执行代码
```
解决：将`C:\Packages\irrlicht-1.8.5\bin\Win64-VisualStudio\Irrlicht.dll`拷贝到`D:\Build\chrono\bin\Release`目录下，再重新运行。

* 编译 Debug 版本报错：
```text
无法打开文件“python311_d.lib”
无法打开文件“..\..\..\lib\Debug\Chrono_parsers_d.lib”
```

原因：缺少`python311_d.lib`是因为使用的是python发布版，而不是debug版本。

缺少`Chrono_parsers_d.lib`是因为需要编译 Chrono_parsers。

C++中Debug模式下 #include <Python.h> 会提示链接错误信息 无法打开文件“python311_d.lib”

解决：参考[链接](https://www.cnblogs.com/Jeffxu/p/17965842) ，在 [chrono/src/chrono_parsers
/ChParserPython.cpp包含头文件时](https://github.com/OpenHUTB/chrono/blob/hutb/src/chrono_parsers/ChParserPython.cpp) ，临时去掉 Debug 模式，待后面再恢复之前的模式，操作方式如下：

```cpp
#ifdef _DEBUG
#undef _DEBUG
#include <Python.h>
#define _DEBUG
#else
#include <Python.h>
#endif
```



* 编译错误：

```text
无法打开包括文件: “cuda_runtime.h”: No such file or directory
无法打开输入文件“Chrono_modal.lib”
无法打开输入文件“..\..\..\lib\Release\Chrono_parsers.lib”
```

解决：移除需要CUDA的sensor模块的编译。

* 运行`chrono\contrib\build-scripts\windows\buildVSG.bat`出现Vulkan找不到的错误：

```text
Could NOT find Vulkan: (Required is at least version "1.1.70.0")
```

解决：[下载 vulkan](https://vulkan.lunarg.com/sdk/home#windows) ；解决不了可以暂时关闭报错的模块

* eigen3找不到，报错：`ERROR: cannot find Eigen3 version information`

解决（需要包含后面的`include/eigen3`）：
```shell
set EIGEN3_INSTALL_DIR="C:/Packages/eigen/include/eigen3"
```

* 编译2.4.0时，fastrtps 中的 “ _Mtx_init”:identifier not found

* 构建blaze时候报错
```text
Could NOT find BLAS (missing: BLAS_LIBRARIES)
```

```shell
configure_file(<input> <output>
               [COPYONLY] [ESCAPE_QUOTES] [@ONLY]
               [NEWLINE_STYLE [UNIX|DOS|WIN32|LF|CRLF] ])
```
将文件复制到另一个位置并修改其内容。

当然，这里的修改其内容也不是任意地修改，也是遵循一定的规则：将input文件复制到output文件，并在输入文件内容中的变量，替换引用为@VAR@或${VAR}的变量值。每个变量引用将替换为该变量的当前值，如果未定义该变量，则为空字符串。





## 参考

* [安装Chrono教程](https://api.projectchrono.org/tutorial_install_chrono.html#scripts)
* [cmake生成Visual Studio工程后的INSTALL项目使用](https://blog.csdn.net/loveoobaby/article/details/133954891)
* [windows编译调试FastDDS](https://www.cnblogs.com/shawn-meng/p/18856436)
