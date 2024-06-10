#include <bits/stdc++.h>
using namespace std;

void combinationFinder(vector<vector<int>> &combinations, int arr[], vector<int> data, int start, int end, int r);

void printComb(int arr[], int n, int r)
{
    vector<vector<int>> combination;
    vector<int> data;
    combinationFinder(combination, arr, data, 0, n - 1, r);
    cout << endl;
    cout << combination.size() << "  hello" << endl;
    for (auto x : combination)
    {
        for (auto y : x)
        {
            cout << y;
        }
        cout << endl;
    }
}

void combinationFinder(vector<vector<int>> &combination, int arr[], vector<int> data, int start, int end, int r)
{
    if (data.size() == r)
    {
        combination.push_back(data);
        return;
    }

    for (int i = start; i <= end; i++)
    {
        // cout << arr[i] << "     ";
        data.push_back(arr[i]);
        for (auto x : data)
        {
            cout << x << "    ";
        }
        cout << endl;
        combinationFinder(combination, arr, data, i + 1, end, r);
        cout << "After Return:  ";
        for (auto x : data)
        {
            cout << x << "    ";
        }
        cout << endl;
    }
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    int r = 3;
    int n = sizeof(arr) / sizeof(arr[0]);
    printComb(arr, n, r);
}