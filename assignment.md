class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        int[] minDist = new int[n];
        boolean[] visited = new boolean[n];

        for (int i = 0; i < n; i++)
            minDist[i] = Integer.MAX_VALUE;

        minDist[0] = 0;
        int totalCost = 0;

        for (int count = 0; count < n; count++) {
            int u = -1;

            // Find unvisited point with minimum cost
            for (int i = 0; i < n; i++) {
                if (!visited[i] && (u == -1 || minDist[i] < minDist[u]))
                    u = i;
            }

            visited[u] = true;
            totalCost += minDist[u];

            // Update distances
            for (int v = 0; v < n; v++) {
                if (!visited[v]) {
                    int cost = Math.abs(points[u][0] - points[v][0])
                             + Math.abs(points[u][1] - points[v][1]);

                    minDist[v] = Math.min(minDist[v], cost);
                }
            }
        }

        return totalCost;
    }
}
