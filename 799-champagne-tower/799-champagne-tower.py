class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        layer = [poured]
        
        for _ in range(query_row):
            new_layer = [0]* (len(layer) + 1)
            for i in range(len(layer)):
                pour = (layer[i] - 1) / 2
                if pour > 0:
                    new_layer[i] += pour
                    new_layer[i + 1] += pour
            layer = new_layer
        
        return min(1, layer[query_glass])
                    