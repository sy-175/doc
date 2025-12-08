# Git 所管理的依赖

## 分析

```shell
# 查看支持的命令
Engine\Binaries\DotNET\GitDependencies.exe -h
```
得知默认的下载缓存位于`engine\.git\ue4-gitdeps`目录下，并且可以通过 `--cache=<PATH>` 指定自定义的缓冲目录，来 [跳过](https://github.com/OpenHUTB/engine/issues/13) 编译时的下载依赖过程。

