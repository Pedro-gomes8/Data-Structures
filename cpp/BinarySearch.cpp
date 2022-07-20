#include <iostream>
#include <vector>
using namespace std;

int search(vector<int> array, int item, int low = 0, int high = 0)
{
    if (!high)
        high = array.size();
    if (array.size() == 1)
        return low;
    int mid = (low + high) / 2;
    int guess = array[mid];

    if (guess < item)
    {
        low = mid;
        return search(array, item, low, high);
    }
    if (guess > item)
    {
        high = mid;
        return search(array, item, low, high);
    }
    else
        return mid;
}
int main()
{
    vector<int> array = {2, 5, 6, 8, 10, 12, 13, 14, 16, 53};
    cout << search(array, 53) << endl;
    return 0;
}
