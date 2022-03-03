public class Solution11 {
    public int MaxArea(int[] height) {
        int S = 0, i = 0, j = height.Length -1;
        while (i < j) {
            S = Math.Max(S, (j - i) * Math.Min(height[i], height[j]));
            if (height[i] < height[j])
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        return S;
    }
}