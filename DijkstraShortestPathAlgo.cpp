/* SHORTEST PATH IN UNDIRECTED WEIGHTED GRAPH / DIRECTED WEIGHTED GRAPH   ( DIJKSTRA'S ALGO ) 
TC : O((|V|+|E|)*log|V|)     
SC : O(2*|V|)
KEY POINTS :    Bfs with priority queue or use set data structure as it also avoids multiple similar distances to same node 
	• Dijkstra's Algorithm cannot be applied on graphs having negative weight cycle because calculation of cost to reach a destination node from the source node becomes complex as more you take turns in neg wt cycle the dist dec more thus it causes infinite loop. 
	• You can use Dijkstra's algorithm in both directed and undirected graphs, because you simply add nodes into the Priority Queue when you have an edge to travel to from your adjacency list.
	• you can apply Dijkstra on DAG
	• Dijkstra's algorithm does work on graphs with cycles (either undirected or directed), as long as it is a positive weight cycle
The Priority Queue (MIN HEAP) will have pair {distance,node}
(distance => distance from src to this node )
So as we have the short dist to node we can take it out and update the dist of its ajn nodes , and as the dist of any node is updated its put to priority Queue so it can update its ajn to more short dist from src .
  */
 #include <bits/stdc++.h>
 using namespace std;
Void Dijkstra(int src,vector<vector<int>>&adj,int n){
Vector<int>par(n); // for finding shortest path from src to other nodes
For(int i=0;i<n;i++) par[i]=i;
Par[src]=-1;
vector<int>dist(n+1,INT_MAX);
priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pq;
pq.push({0,src});
dist[src]=0;
while(!pq.empty()){
    auto pr=pq.top();
    pq.pop();
    int distSrctoNode=pr.first;
    int node=pr.second;
    for(auto ajnpr:adj[node]){
        if(dist[node]+ajnpr.second<dist[ajnpr.first]){
         // or use distSrctoNode instead of dist[node]
            dist[ajnpr.first]=dist[node]+ajnpr.second;
            pq.push({dist[ajnpr.first],ajnpr.first});
            par[ajn]=node; // who updated distance (min)
        }
    }
}
for(int i=1;i<=n;i++){
   cout<<dist[i]<<" ";
}
// path from src to X
  vector<int>path;
  int nodes=X;
  while(nodes!=-1){
    path.pb(nodes)
    nodes=par[nodes];
  }
 reverse(path.begin(),path.end());
// can print all paths 
// all distances finded
}
int main(){
    int n,e;
    cin>>n>>e;
    vector<vector<int>>adj(n+1);
    for(int i=0;i<e;i++){
        int u,v;
        cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    int src;
    cin>>src;
    Dijkstra(src,adj,n);
}
