class UserMainCode {
    public int findMinHop(int input1, int[] input2) {
        // Check if array is null or empty
        if (input2 == null || input2.length == 0 || input1 <= 0) {
            return -1;
        }
        
        // Check if first element is even (as mentioned in the note)
        if (input2[0] % 2 != 0) {
            return -1;
        }
        
        for (int h = 1; h <= input1; h++) {
            boolean allEven = true;
            
            int index = 0;
            while (index < input1) {
                if (input2[index] % 2 != 0) {
                    allEven = false;
                    break;
                }
                
                index += h;
            }
            
            if (allEven) {
                return h;
            }
        }
        return -1;
    }
}