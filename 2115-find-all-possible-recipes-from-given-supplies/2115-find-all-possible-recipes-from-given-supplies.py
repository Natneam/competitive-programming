class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        construct the graph { ingredient : [recipe, recipe, ...]  }
        indegree of all the recipes
        start from the all the nodes(recipe or ingredient) which have an indegree 0
        
        do typical topological sort by recording the nodes peoped from the element
        
        return the recorder recipes in the which are also in the resipies list not in ingredients 
        
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
                