# WebCrawlerPractice
Simple and buggy ut course info crawler

功能：
---

* 获取UT所有Program的课程列表，根据需要对单一Program所有的课程进行访问，获取有关于这门课的信息，并保存至本地
* 功能本身与UT自己的Arts & Sciences Calendar类似，仅作练手用

代码结构：
-----

* Program，Course两个储存类

  * 两项储存类均有一个visible标签方便用于文本存储以及分辨是否有效
  * 数据结构为字典

* Finder作为基础的爬虫模版

  * 包含一个待访问的域名domain，一个访问domain返回其html文本的method
  * 子类均使用字典保存信息
  * 两个子类需要实现的方法：

    * data\_extraction：提取网页中的次级连接并获取html，存储于字典中
    * data\_construction：对字典中的所有html进行分析，提取信息

* ProgramFinder为Finder子类

  * 从Program Info Page提取所有Program名称及链接，建立Program类存储于字典中
  * 对于非标准链接，设置visible为false

* CourseFinder为Finder子类

  * 从指定Program Page中提取所有course code，建立Course类，生成对应的Course Finder链接，保存html
  * 对字典中所有已有课程，分析html文件，分辨链接是否有效，对有效链接保存信息

* FileSystem负责保存爬下来的字典，字典均为key：object的格式，并且要求object有一个visible的标签及getter
* Main实现了一个简单的命令行交互：提供Program列表，用户需选取Program及学期

不足：
---

* 作为爬虫，代码本身无法直接分辨第一次提取的课程代码所属的学期，这样就会产生很多的无效的Course类
* 一次使用仅能对一个学期的课程进行提取

未来可能的改进：
--------

* 单Program可能包含有上百个课程，可能改用多线程提高效率
* 对课程的space／enrol进行一个统计
* Prerequisite的描述并不是标准化的，若需要对其进行判断则必须进行文本分析
