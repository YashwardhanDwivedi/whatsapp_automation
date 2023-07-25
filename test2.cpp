
priority_queue<int, vector<int>, greater<int>> q;
vector<int> v;

for (int i = 0; i < n; i++)
{
    q.push(arr[i]);
    if (q.size() > k)
    {
        v.push_back(q.top());
        q.pop();
    }
}
while (!q.empty())
{
    v.push_back(q.top());
    q.pop();
}
return v;
}