# cnblogs2hexo2jekyll
一键博客搬家（自动把博客园的所有文章转为多文件的markdown（md） 方便放在hexo上。把博客园转换成jekyll格式；把博客园转换成hexo格式。

**原理：** 解析cnblogs博客备份的xml文件，生成md文件

**本项目：**

 - 增加从hexo 到jekyll 的格式切换。
 - 修正文件路径非法的问题(测试)。

# 依赖
无外置依赖 本来想解析xml的 奈何不标准 遂手写正则

# 使用说明
在博客园管理后台 点击博客备份 下载自己的博客xml描述文件  
之后clone本项目 点开`cnblogs2hexo.py` 更改里面xml_file的名称为自己导出文件的名称  
执行 于是在本地自动生成了所有md文件  

# TODO
自动下载所有图片  

