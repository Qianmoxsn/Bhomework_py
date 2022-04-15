# 课题:自动驾驶公交车调度系统
项目看板：[跳转->项目看板](https://github.com/Qianmoxsn/Bhomework_py/projects/1)  
项目设计图：[跳转->项目设计图](img/flow%20chart4.15.svg)

## 目录
- [课题:自动驾驶公交车调度系统](#课题自动驾驶公交车调度系统)
  - [目录](#目录)
  - [概述](#概述)
  - [基本规则](#基本规则)
- [版本描述及需求](#版本描述及需求)
  - [1.核心版本（OJ版本）](#1核心版本oj版本)
    - [基本说明](#基本说明)
    - [输入说明](#输入说明)
    - [输出说明](#输出说明)
    - [策略说明](#策略说明)
      - [先来先服务策略（FCFS）](#先来先服务策略fcfs)
      - [最短寻找时间优先（SSTF）](#最短寻找时间优先sstf)
      - [顺便服务策略（SCAN）](#顺便服务策略scan)
      - [策略补充说明：](#策略补充说明)
    - [测试样例](#测试样例)
      - [输入样例](#输入样例)
      - [输出样例](#输出样例)
  - [2.动画并发版本](#2动画并发版本)
  - [3.文件输入版本](#3文件输入版本)

---

## 概述

用程序模拟一个城市自动驾驶公交车调度系统。自动驾驶公交车调度系统，系统中的要素如下示意图：  
<img src="img/syt.png">

---

## 基本规则

- 规则1：有一个闭环的公交轨道，公交车只能在轨道上运行。轨道的位置由像素坐标表示，长度以像素个数为单位计算。
- 规则2：公交车运行方向分顺时针、逆时针两种方向，根据调度策略可切换方向。
- 规则3：轨道内预先设置乘车站N个，车站的位置由像素坐标表示，车站距离不相等。
- 规则4：由程序接收动态发出（读文件或键盘、鼠标操作）的乘车请求，动态刷新显示“等待请求数”指标；然后根据请求车站情况，更新车站的状态：没有乘车请求的车站显示为蓝色，有乘车请求的车站显示为红色（要能表示两个方向的请求）。
- 规则5：一辆车的载客数不限，可以接收所经过的所有乘车站请求。车辆的车速保持匀速不变，都设置为1 S，车速以每秒多少像素表示。
- 规则6：程序初始，默认一辆公交车从轨道的左上角发车，根据调度策略确定行驶方向，按设定车速S行驶（定时刷新显示公交车的当前位置和“时间”显示，时间以秒为单位），途经有乘车请求的车站时停车P秒，完成本站的所有请求，刷新显示“已完成请求数”和“最大等待时间”指标。
- 规则7：由程序接收动态发出（读文件或键盘、鼠标操作）的“停运”指令，收到停运指令后，程序不再接收新的乘车请求（准备收车状态），但需要将已有乘车请求处理完，然后更新“已完成请求数”和“最大等待时间”指标，程序退出。
- 规则8：最大等待时间的计算方法，每个乘车请求发出后，直到公交车经过请求车站完成服务的时间间隔，以秒为单位，取所有乘车请求完成时间的最大值。


---

# 版本描述及需求

## 1.核心版本（OJ版本）

### 基本说明

- 环形轨道，一辆车，车辆可以双向任意行驶。我们规定车辆的原始位置为0（该位置也是车站1的位置），按顺时针方向每个单位位置坐标加1。

> 如果轨道总长为10，则按顺时针方向走，位置9的下一个为位置0。车站编号同理，也是按顺时针方向依次递增。

- 车速固定，每秒一个单位。**停车接人**或**乘客下车**时需要停车一秒钟。**无论一次停站完成几个服务停留时间统一为1秒钟**。
- 各站之间距离相等，车辆经过站点时，根据调度策略，车辆可以停也可以不停。其他位置不允许停车。车辆只能在站点停站时才能改变行驶方向。
- 各站之间距离可配置，站点个数可配置，调度策略可配置。这三个参数保存在配置文件中，程序要通过读配置文件获取。

> 配置文件的名字为dict.dic。 配置文件为文本文件，以#号开头的行是注释。 每行一个参数，  
> 格式为：`参数 = 值`的形式。

其中参数有三个:  
`TOTAL_STATION`，代表站点总数，为大于1且小于等于10的整数；  
`DISTANCE`，代表每站之间的距离，为大于0且小于6的整数；  
`STRATEGY`，代表调度策略，只能是`FCFS`（先来先服务），`SSTF`（最短寻找时间优先）和 `SCAN`（顺便服务）之一。

> 另外:  
> 1. 如果某个参数没有出现在配置文件中，则该参数取缺省值。
>
> 三个参数的缺省值如下：
>
>     TOTAL_STATION = 5    
>     STRATEGY = FCFS    
>     DISTANCE = 2   
>
> 2. 三个参数在文件中的顺序没有规定。  
> 3. 显然，`TOTAL_STATION`与`DISTANCE`乘积就是**轨道总长度**，所以配置文件中没有这个参数。

### 输入说明

若干行，每行一个指令。  
指令共5种。分别为end、clock、counterclockwise、clockwise 和target。
***
||||   
|---|:--:|:---:|
|`end`| 结束指令|只在最后一行出现一次； | 
|`clock`| 时钟指令|每出现一次代表过了一秒钟； | 
|`counterclockwise`、`clockwise`、`target`|为请求指令|同一行内后边有一个整数。|   
|||| 
|`counterclockwise`|表示逆时针方向|整数代表请求发生的站点号 | 
|`clockwise`|代表顺时针方向|整数代表请求发生的站点号  |
|`target`|车厢内请求|整数代表要去的站点号。|

***

### 输出说明

程序开始，先输出一次初始状态，然后每个clock输出一次当前状态。每次输出的格式如下：

    BUS:  
    position:0  
    target: 0000000000  
    STATION:  
    clockwise: 0000000000  
    counterclockwise: 0000000000 


> **其中前三行代表车辆:**  
> ||||   
> |---|:--:|:---:|  
> |`BUS`|固定不变|-|  
> |`position`|固定不变|后边的数字代表当前车辆位置|   
> |`target`|固定不变|后边一排数字依次代表车内站点请求情况，0表示没有请求，1表示有请求。|  
>   
> **后三行代表各站点的状态:**  
> ||||  
> |---|:---:|:---:|
> |`STATION`| 固定不变|-|
> |`clockwise`| 固定不变|后边的数字依次代表各站点顺时针方向的请求情况，0表示没有请求，1表示有请求。|
> |`counterclockwise`| 固定不变|后边的数字依次代表各站点逆时针方向的请求情况，0表示没有请求，1表示有请求。|

---
### 策略说明  
#### 先来先服务策略（FCFS）
**将所有乘车请求按发出时间排队，然后按队列顺序逐一完成**  
> - 先来先服务是一种随即服务算法，是一种最简单的电梯调度算法。它根据乘客请求乘坐电梯的先后次序进行调度。此算法的优点是公平、简单，且每个乘客的请求都能依次地得到处理，不会出现某一乘客的请求长期得不到满足的情况。  
> - 这种方法在载荷较轻松的时，性能尚可接受，在载荷较大的情况下，这种算法的性能就会严重下降，甚至恶化  
> - 人们之所以研究这种在载荷较大的情况下几乎不可用的算法，有两个原因：
>> - 任何调度算法在请求队列长度为1时，请求速率极低或相邻请求的间隔为无穷大时使用先来先服务算法既对调度效率不会产生影响，而且实现这种算法极其简单。  
>> - 先来先服务算法可以作为衡量其他算法的标准。  

---

#### 最短寻找时间优先（SSTF）  
**寻找可最快到达车站**  
> - 最短寻找时间优先策略选择下一个服务对象的原则是最短寻找时间。这样乘车请求队列中距当前公交车位置能够最先到达的车站请求信号就是下一个服务对象。注意计算最短寻找时间时，要在当前方向和反方向两个方向去计算，然后找出最短的行驶方向和到达时间。 
> - 在重载荷的情况下，最短寻找时间优先算法的平均响应时间较短，但响应时间的方差较大，原因是队列中的某些请求可能长时间得不到响应，出现所谓的“饿死”现象。

---

#### 顺便服务策略（SCAN）
**（1）按小车当前位置和当前行驶方向，计算所有等待乘车请求的预计完成时间，找出最短完成时间的车站，作为当前目标进行调度。**  
**（2）若按规则（1）找出的最短完成时间超过跑完轨道一半距离时间时，应该切换行驶方向。然后重新按规则1找出最短完成时间的车站，作为当前目标进行调度。**  
> - 顺便服务策略是一种按照车站顺序依次服务请求策略，它让公交车方向较稳定地往返运行，在运行过程中优先响应在当前运行方向的最快到达车站请求。避免了公交车频繁的切换行驶方向。  
> - 顺便服务策略的平均响应时间比最短寻找时间优先算法长，但是响应时间方差比最短寻找时间优先算法小，从统计学角度来讲，顺便服务策略要比最短寻找时间优先算法稳定。



#### 策略补充说明：

1. 每一个请求均为单独的服务，就是说**车内请求与站台请求没有必然联系**；
2. 当车**完成服务时要选择路程短的方向行驶**，如果两个方向路程相同则选择**顺时针方向**；
3. 如果在某个请求**没有完成时**再有**相同的请求发生**，则该请求被**抛弃**。如果**已完成的请求再次发生**时应按**新请求**处理。
4. 对于*先来先服务策略*，车一次停站只完成一个请求，即使在这个站点上即有乘车请求，车内也有到该站的请求也只能按算法完成其中的一个。但是如果下一个请求恰好在同一站点，则可以一次停站完成2个或2个以上的请求。也就是说只停1秒完成多个请求。
5. 对于*最短寻找时间优先策略*，一次服务的请求（目标）一旦确定，即使中途产生更优的请求也不可以更改。但如果新的请求恰好可以顺便服务（同方向的站台请求或车内请求），可以为新的请求停站。
6. 程序计算离当前车的位置最近的`target`、`counterclockwise`、`clockwise`请求，如果**都没有请求则原地不动**，否则**按最近的路线（顺、逆时针）去接（送）**，如果车途中遇到与车目前**同方向的上车请求或下车请求**可以停下一秒解决【**请求至少在车到请求地前一个clock提出**，到达该请求地时再提出请求的忽略】，**反方向的上车请求忽略**，车接到人（送完人）后，反复此过程，直到end
7. 对于*顺便服务策略*，**行驶方向由第一个请求决定**。在行使过程中，如果所有的请求按照**当前的行驶方向找出的最短完成时间**超过**跑完轨道一半距离时间**时，应该**切换行驶方向**。
8. 车辆行驶过程中如果**经过的站点有服务请求**，则不管这个请求的类型**一律停站**，并认为此请求完成。
9. 对于*后两种策略*，如果车辆在某站点本没有停车计划，新的请求要至少要提前1秒钟产生才能享受顺便服务。也就是说不为太近的请求停车。

### 测试样例  
#### 输入样例  
```
clock
counterclockwise 3
clock
clock
clock
clock
clock
clock
target 10
clock
clock
clock
clock
clock
clock
clock
clock
clock
clock
clock
end
```
#### 输出样例 
```
BUS:
position:0
target: 0000000000
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:0
target: 0000000000
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:1
target: 0000000000
STATION:
clockwise: 0000000000
counterclockwise: 0010000000
BUS:
position:2
target: 0000000000
STATION:
clockwise: 0000000000
counterclockwise: 0010000000
BUS:
position:3
target: 0000000000
STATION:
clockwise: 0000000000
counterclockwise: 0010000000
BUS:
position:4
target: 0000000000
STATION:
clockwise: 0000000000
counterclockwise: 0010000000
BUS:
position:5
target: 0000000000
STATION:
clockwise: 0000000000
counterclockwise: 0010000000
BUS:
position:6
target: 0000000000
STATION:
clockwise: 0000000000
counterclockwise: 0010000000
BUS:
position:6
target: 0000000001
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:5
target: 0000000001
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:4
target: 0000000001
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:3
target: 0000000001
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:2
target: 0000000001
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:1
target: 0000000001
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:0
target: 0000000001
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:29
target: 0000000001
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:28
target: 0000000001
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:27
target: 0000000001
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
BUS:
position:27
target: 0000000000
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
end
STATION:
clockwise: 0000000000
counterclockwise: 0000000000
```
## 2.动画并发版本
暂无
## 3.文件输入版本
暂无
