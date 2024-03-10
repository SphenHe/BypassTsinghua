#include <iostream>
#include <climits>
#include <vector>
#include <algorithm>

using namespace std;
// 用于表示无穷大的值
const int INF = INT_MAX / 2; // 防止整数溢出
// Floyd算法实现函数
void floyd(vector<vector<int>>& dist, int n) {
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                // 如果i到k和k到j都是可达的
                if (dist[i][k] < INF && dist[k][j] < INF) {
                    // 更新i到j的最短路径
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
}

int main() {
    // 输入顶点数量和边的数量
    int n, e;
    cout << "Enter the number of vertices: ";
    cin >> n;
    cout << "Enter the number of edges: ";
    cin >> e;
    // 初始化距离矩阵，开始时设为无穷大
    vector<vector<int>> dist(n, vector<int>(n, INF));
    // 读取边的信息并设置距离
    cout << "Enter the edges (u, v, weight) : " << endl;
    for (int i = 0; i < e; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        dist[u][v] = w;
    }
    // 设置自身到自身的距离为0
    for (int i = 0; i < n; ++i) {
        dist[i][i] = 0;
    }
    // 调用Floyd算法
    floyd(dist, n);
    // 输出结果
    cout << "Shortest distances between every pair of vertices:" << endl;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (dist[i][j] == INF)
                cout << "INF" << " ";
            else
                cout << dist[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
