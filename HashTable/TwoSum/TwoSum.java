import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
      Map<Integer, Integer> map = new HashMap<>();
      for (int i = 0; i < nums.length; i++) {
          map.put(nums[i], i);
      }
      for (int i = 0; i < nums.length; i++) {
          int complement = target - nums[i];
          if (map.containsKey(complement) && map.get(complement) != i) {
              return new int[] { i, map.get(complement) };
          }
      }
      throw new IllegalArgumentException("No two sum solution");
}
  	public static void main(String[] args) {
  		int[] list = {1,3,5,7,8};
  		Solution a= new Solution();
  		list = a.twoSum(list,4);
  		System.out.printf("The result is [%d,%d]!%n",list[0],list[1]);
  	}
}
