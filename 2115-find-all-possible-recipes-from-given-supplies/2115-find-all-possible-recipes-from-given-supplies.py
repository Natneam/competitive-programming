class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        construct the graph { ingredient : [recipe, recipe, ...]  }
        indegree of all the recipes
        start from the all the supplies
        
        do typical topological sort by recording the nodes peoped from the queue
        
        return the recorded values which are also in the recipies list not in supplies 
        
        """
        
        graph = defaultdict(list)
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
        
        #log the indegree
        indegree = defaultdict(int)
        
        for node in graph:
            for neighbour in graph[node]:
                indegree[neighbour] += 1
        
           
        #start the topological sort from the supplies
        queue = deque()
        for supply in supplies:
            queue.append(supply)
                
        all_recipes = []
        
        while queue:
            node = queue.popleft()
            all_recipes.append(node)
            
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    del indegree[neighbour]
                    queue.append(neighbour)
        
        return list(set(all_recipes).intersection(set(recipes)))
                