var heightChecker = function(heights) {
    
    var expected = heights.slice().sort((a,b) => a-b)
    var unmatch = 0
   
    for (i in expected){
        if (heights[i] != expected[i]) {
            unmatch += 1
        }        
    }
    return unmatch    
};