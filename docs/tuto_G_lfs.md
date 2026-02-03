
# 大文件支持

```shell
git init .
# 让仓库支持LFS
git lfs install
git lfs track "*"
git add .gitattributes
```

.gitattributes文件内容为（除了该文件其他都用大文件跟踪）：
```text
*               filter=lfs diff=lfs merge=lfs -text
.gitattributes  filter= diff= merge= text
```

```shell
git commit -m "init LFS config"

# 添加大文件
git add dyrone.bigfile
git commit -m "Add a really big file"
# 查看跟踪的大文件
git lfs track
# 推送
git remote add origin https://git.code.tencent.com/OpenHUTB/dependencies.git
git push --set-upstream origin master
```



常用命令
```shell
git lfs status  // 查看当前git lfs对象的状态

git lfs ls-files  // 查看当前哪些文件是使用lfs管理的

# 放弃工作区的更改
git checkout -- .
# 放弃暂存区的更改
git reset HEAD
```


## 资产仓库
目前使用的是腾讯工蜂社区版 git lfs 进行资产管理

###### 查看仓库的容量

进入 [项目首页](https://git.code.tencent.com/OpenHUTB/Content) （如果没有权限访问，则注册后发送用户名到 [whd@hutb.edu.cn](whd@hutb.edu.cn) ），打开左侧的`设置->高级设置`，在页面中选择`版本库设置`。

该产品单仓库容量配额为 5GB，单文件限制 128M；LFS储存为 512 GB、单 LFS 文件限制为 5 G。


###### 注册网络回调钩子

按照上一步中的操作，进入`设置->高级设置->网络回调钩子`，设置 Url 和秘密令牌，当有推送事件时候触发 hutb 仓库的编译。

## 常见问题

###### 拉取时候出现错误：smudge filter lfs failed
设置以下命令后再拉取
```shell
# 跳过污点：稍后会以更快的速度批量下载二进制文件。
set GIT_LFS_SKIP_SMUDGE=1
git pull
# 获取二进制文件
git lfs pull
```

###### 拉取大文件报错： remote error: tls: handshake failure
显示更多调试信息（无效尝试）：
```shell
set GIT_TRACE=true
set GIT_CURL_VERBOSE=true
# 显示git配置
git config -l --show-origin

git lfs pull
```
解决：安装最新的git版本`Git-2.52.0-64-bit.exe`报错，回退到版本`Git-2.40.0-64-bit.exe`后拉取大文件成功。


## 依赖的大文件仓库

* MinGit-2.40.0-busybox-64-bit.zip
 [下载地址](https://github.com/git-for-windows/git/releases/tag/v2.40.0.windows.1) 


## 参考

* [如何存储 Git 大文件？](https://www.cnblogs.com/88223100/p/How-do-I-store-large-Git-files.html) 

* [如何使用 Git LFS](https://help.aliyun.com/zh/yunxiao/user-guide/how-to-use-git-lfs)




