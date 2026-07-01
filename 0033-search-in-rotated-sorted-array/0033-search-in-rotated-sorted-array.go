func search(nums []int, target int) int {
   left,right := 0,len(nums)-1

   for left<=right{
        if nums[left] == target{
            return left
        }
        if nums[right] == target{
            return right
        }
        left++
        right--
   } 
   return -1
}