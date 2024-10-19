---
title: 成员
nav:
  order: 3
  tooltip: 关于我们
---

# {% include icon.html icon="fa-solid fa-users" %}24 赛季团队成员

历史成员请参考[历届成员](/team/history)。

{% include section.html %}

## {% include icon.html icon="fa-solid fa-users" %}指导老师

{% include list_portrait.html data="members" component="portrait" filters="role: 指导老师" %}

## {% include icon.html icon="fa-solid fa-users" %}团队负责人
{% include list_portrait.html data="members" component="portrait" filters="type: 24赛季团队负责人, time: 24" %}

## {% include icon.html icon="fa-solid fa-users" %}机械组
  
{% include list_portrait.html data="members" component="portrait" filters="role: 机械组" style="small" %}

## {% include icon.html icon="fa-solid fa-users" %}电路组

{% include list_portrait.html data="members" component="portrait" filters="role: 电路组" style="small" %}
## {% include icon.html icon="fa-solid fa-users" %}嵌软组

{% include list_portrait.html data="members" component="portrait" filters="role: 嵌软组" style="small" %}
## {% include icon.html icon="fa-solid fa-users" %}算法组

{% include list_portrait.html data="members" component="portrait" filters="role: 算法组" style="small" %}
## {% include icon.html icon="fa-solid fa-users" %}运营组

{% include list_portrait.html data="members" component="portrait" filters="role: 运营组" style="small" %}

## {% include icon.html icon="fa-solid fa-users" %}梯队



{% include section.html background="images/background.jpg" dark=true %}

这里可以加一段衔接语

{% include section.html %}

{% capture content %}

{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}

# 杰出人物

{% include list_portrait.html data="members" component="portrait" filters="type: 杰出人物" %}