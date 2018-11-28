graph = {}
graph["乐谱"] = {}
graph["乐谱"]["唱片"] = 5
graph["乐谱"]["海报"] = 0
graph["唱片"] = {}
graph["唱片"]["吉他"] = 15
graph["唱片"]["架子鼓"] = 20
graph["海报"] = {}
graph["海报"]["吉他"] = 30
graph["海报"]["架子鼓"] = 35
graph["吉他"] = {}
graph["吉他"]["钢琴"] = 20
graph["架子鼓"] = {}
graph["架子鼓"]["钢琴"] = 10
graph["钢琴"] = {}

infinity = float("inf")
costs = {}
costs["唱片"] = 5
costs["海报"] = 0
costs["吉他"] = infinity
costs["架子鼓"] = infinity 
costs["钢琴"] = infinity  

parents = {}
parents["唱片"] = "乐谱"
parents["海报"] = "乐谱"
parents["吉他"] = None
parents["架子鼓"] = None
parents["钢琴"] = None

processed = [] 
# 找到开销最小的节点
def find_lowest_cost_node(costs):	
    # 初始化数据	
    lowest_cost = infinity	
    lowest_cost_node = None	
    # 遍历所有节点	
    for node in costs:		
        # 该节点没有被处理		
        if not node in processed:			
            # 如果当前节点的开销比已经存在的开销小，则更新该节点为开销最小的节点			
            if costs[node] < lowest_cost:				
                lowest_cost = costs[node]				
                lowest_cost_node = node	
    return lowest_cost_node 
# 找到最短路径
def find_shortest_path():	
    node = "钢琴"	
    shortest_path = ["钢琴"]	
    while parents[node] != "乐谱":		
        shortest_path.append(parents[node])		
        node = parents[node]	
    shortest_path.append("乐谱")	
    return shortest_path
#寻找加权的最短路径
def dijkstra():	
    # 查询到目前开销最小的节点	
    node = find_lowest_cost_node(costs)	
    # 只要有开销最小的节点就循环	
    while node is not None:		
        # 获取该节点当前开销		
        cost = costs[node]		
        # 获取该节点相邻的节点		
        neighbors = graph[node]		
        # 遍历这些相邻节点		
        for n in neighbors :			
            # 计算经过当前节点到达相邻结点的开销,即当前节点的开销加上当前节点到相邻节点的开销			
            new_cost = cost + neighbors[n]			
            # 如果计算获得的开销比原本该节点的开销小，更新该节点的开销和父节点			
            if new_cost < costs[n]:				
                costs[n] = new_cost				
                parents[n] = node		
        # 遍历完毕该节点的所有相邻节点，说明该节点已经处理完毕		
        print(node)
        processed.append(node)		
        # 去查找下一个开销最小的节点，若存在则继续执行循环，若不存在结束循环		
        node = find_lowest_cost_node(costs)	
    # 循环完毕说明所有节点都已经处理完毕	
    shortest_path = find_shortest_path()	
    shortest_path.reverse()	
    print(shortest_path)		

# 测试
dijkstra()
