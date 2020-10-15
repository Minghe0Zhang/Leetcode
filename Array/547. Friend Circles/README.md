# 547. Friend Circles
sol1: dfs
sol2: union-find
> 初始时每个个体的根朋友为自己本身
若 M[i][j] == 1，说明 i 和 j是朋友
找到 i 的根朋友 i_parent 和 j 的根朋友 j_parent
若两者根朋友一样说明是一个朋友圈，不做操作
若两者根朋友不一样，说明是不同的朋友圈，则执行合并朋友圈的操作：将j的根朋友 j_parent 的根朋友设置为 i 的根朋友 i_parent，总数减一