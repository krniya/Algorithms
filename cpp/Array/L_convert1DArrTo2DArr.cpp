

vector<vector<int>> construct2DArray(vector<int> &original, int m, int n)
{
    if (m * n != original.size())
    {
        return {};
    }

    std::vector<std::vector<int>> result(m, std::vector<int>(n));

    for (int i = 0; i < m; ++i)
    {
        result[i] = std::vector<int>(original.begin() + i * n, original.begin() + i * n + n);
    }

    return result;
}