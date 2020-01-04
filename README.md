# 时间戳转化工具

时间戳和日期相互转化的Alfred小工具。如下图：

![image-20200104154757755](https://github.com/BaskerShu/datetime_converter_workflow/blob/master/release/image-20200104154757755.png)

项目的思路来自 https://github.com/mwaterfall/alfred-datetime-format-converter ，但是该项目不支持自定义时区，所以自己重写了这个小项目。

### 安装下载

点击链接进行下载安装
![下载](https://raw.github.com/BaskerShu/datetime_converter_workflow/master/release/datetime_converter_workflow.alfredworkflow)

### 使用

#### 1. 如何使用?

唤醒Alfred工作栏后，输入`dt`激活该工具，之后按照需要输入 时间戳、日期、now 就可以了

#### 2. 工具默认的时区是什么？

默认时区的是你当地的时区

#### 3. 如何修改时区

![image-20200104155526853](https://github.com/BaskerShu/datetime_converter_workflow/blob/master/release/image-20200104155526853.png)

在该界面中，将`Script`的命令修改为 `ALFRED_TZ={tz} python process.py "{query}"`，其中`tz`的值是你需要的时区（tz的具体值，可以在https://en.wikipedia.org/wiki/List_of_tz_database_time_zones查找）。

例如：

```bash
ALFRED_TZ=Africa/Addis_Ababa python process.py "{query}"
```

