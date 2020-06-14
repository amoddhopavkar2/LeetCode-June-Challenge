# PROBLEM STATEMENT - Cheapest Flights Within K Stops
# There are n cities connected by m flights. 
# Each flight starts from city u and arrives at v with a price w.
# Given all the cities and flights, together with starting city src and the destination dst, 
# find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

# Belman - Ford Algorithm

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dist = [[float('inf')] * n for _ in range(2)] # [pre, cur] or [cur, pre]
        dist[0][src] = dist[1][src] = 0
        
        for i in range(K+1):
            for u, v, w in flights:
                dist[i&1][v] = min(dist[i&1][v], dist[~i&1][u] + w)
        
        return dist[K&1][dst] if dist[K&1][dst] < float('inf') else -1