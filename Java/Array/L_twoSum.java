class TwoSum {
    public int[] twoSum_bf(int[] nums, int target) {
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }
}



class L_twoSum {
    public static void main(String[] args) {
        TwoSum ts = new TwoSum();
        System.out.println(ts.twoSum_bf(new int[]{2, 7, 11, 15}, 9));
    }
}