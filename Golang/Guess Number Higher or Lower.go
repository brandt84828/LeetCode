/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
    low := 0
    high := n
    for low <= high {
        mid := low + (high - low) / 2
        g := guess(mid)
        if g < 0 {
            high = mid - 1
        } else if g > 0 {
            low = mid + 1
        } else {
            return mid
        }
    }
    return -1
}