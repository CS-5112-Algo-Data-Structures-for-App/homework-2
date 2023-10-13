# Problem 1b


def maxsum_tree(vertices, adjacency) -> int:
    def max_sum_func(node, parent_selected, dp):
    	if dp[(node, parent_selected)] != None:
    		return dp[(node, parent_selected)]
    
    	node_max = 0
    
    	if not parent_selected:
            with_node = vertices[node] + sum(max_sum_func(child, True, dp) for child in adjacency[node])
            with_out_node = sum(max_sum_func(child, False, dp) for child in adjacency[node])
            node_max = max(with_node,with_out_node)
    	else:
            node_max = sum(max_sum_func(child, 0, dp) for child in adjacency[node])
    
    	dp[(node, parent_selected)] = node_max
    	return node_max

    def get_root(adjacency):
        children_lst = []
        for values_lst in adjacency.values():
            children_lst += values_lst

        for node in adjacency.keys():
            if node not in children_lst:
                root = node
        return root
    

    
    # Initialization of the dp
    dp = {}
    for node in vertices:
        for parent_bool in [True, False]:
            dp[(node, parent_bool)] = None

    # calling the solve function for root with parent not selected
    max_sum = max_sum_func(get_root(adjacency), False, dp)
    
    return max_sum
        
