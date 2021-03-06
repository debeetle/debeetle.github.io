# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Galileo.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "debeetle/debeetle.github.io@master"
}

# 站点设置
site_name = "实验报告"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-2-20T16:51+08:00"
author = "chaos"
email = "zhangchaoyi13@foxmail.com"
author_homepage = "https://github.com/debeetle"
description = "好耍不过人耍人"
key_words = ['Maverick', 'chaos', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way"
    },
    {
        "name": "像素答疑",
        "url": "https://hijiangtao.github.io/2017/07/09/Device-Viewport-and-Pixel-Introduction/",
        "brief": "前端各类像素概念以及viewport汇总"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [

    {
        "name": "GitHub",
        "url": "https://github.com/debeetle",
        "icon": "gi gi-github"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "W0o0FvoPdBOLyOli4SKHa1Tq-gzGzoHsz",
    "appKey": "gmv0hxHEqhQ7sc3ge2slbDkM",
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
