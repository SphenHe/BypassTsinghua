# 决策方法论-HW1

### T1.

<!-- 1. 随机漫步（Random Walk）：在一维或多维空间中，一个粒子从某个点出发，每个时间单位向任意方向移动固定距离。粒子的下一步位置仅依赖于当前位置，而与之前的轨迹无关。

2. 马尔可夫链（Markov Chain）：包含有限个状态的离散时间马尔可夫过程。在每个时间步，系统从一个状态转移到另一个状态，转移概率仅依赖于当前状态。如股票市场、天气预报、基因序列等

3. 泊松过程（Poisson Process）：这是一个连续时间马尔可夫过程，描述了在固定时间间隔内，事件发生的次数。如电话呼叫到达呼叫中心的次数、车辆到达收费站的数量

4. 随机矩阵乘法：假设有一系列随机矩阵与一个向量相乘。每次乘法都是基于当前向量和随机选择的矩阵。向量的下一个状态仅依赖于当前状态和所选矩阵，与之前选择的矩阵无关。 -->

1. 传染病感染人数
2. 布朗运动
3. 车站排队人数
4. 天气预报

### T2.

马尔可夫决策过程的前五要素：

1. 阶段：每个周期（如一天）作为一个阶段，阶段集合 T = {1, 2, 3, ...}。

2. 状态：机器可以处于两个状态，正常运行（i=1）或发生故障（i=2），状态集合 S = {1, 2}。

3. 决策（方案）：当机器处于正常运行状态时，正常生产（$a_1$）；当机器发生故障时，可以选择全面修理（$a_2$）或简单修理（$a_3$）。决策集合 A = {$a_1$, $a_2$, $a_3$}。

4. 状态转移概率：
   - 对于状态 i=1（正常运行）：
       - 选择行为 $a_1$（正常生产）：$P_a$(1, 1) = 0.7（下一个周期仍然正常运行的概率）；$P_a$(1, 2) = 0.3（下一个周期发生故障的概率）。
   - 对于状态 i=2（发生故障）：
       - 选择行为 $a_2$（全面修理）：$P_a$(2, 1) = 0.6（当前周期内修好，即下一个周期正常运行的概率）；$P_a$(2, 2) = 0.4（当前周期内未修好，即下一个周期仍然发生故障的概率）。
       - 选择行为 $a_3$（简单修理）：$P_a$(2, 1) = 0.4（当前周期内修好，即下一个周期正常运行的概率）；$P_a$(2, 2) = 0.6（当前周期内未修好，即下一个周期仍然发生故障的概率）。

5. 成本：
   - 对于状态 i=1（正常运行）：
       - 选择行为 $a_1$（正常生产）：$g_{a_1}$(1) = -10（期望收益为10元，成本为负值）。
   - 对于状态 i=2（发生故障）：
       - 选择行为 $a_2$（全面修理）：$g_{a_2}$(2) = 5（全面修理需要支付5元成本）。
       - 选择行为 $a_3$（简单修理）：$g_{a_3}$(2) = 2（简单修理需要支付2元成本）。
