<?php
    /*
    * A collection of user-defined maths functions.
    */

    /*
    * Returns true if the argument is a positive (>= 0) integer; otherwise, false.
    */
    function isPositiveInteger($n)
    {
        if (is_numeric($n)) // If $n is a number.
        {
            if ($n == floor($n)) // If an integer (floor function removes decimals).
            {
                if ($n >= 0) // If $n is positive.
                {
                    return true;
                }
            }
        }
        
        // Return false if $n isn't a number, isn't an integer, or isn't positive.
        return false;
    }

    /*
    * Returns the factorial of the given input.
    */
    function factorial ($n) 
    {
        $result = 1; // Variable to store the nth factorial.
        
        // Variable used to multiply the result on each iteration of the below loop.
        $factor = $n;
        
        // Loop to multiply $result by n ... 2.
        // Factor 1 and 0 aren't multipled as they don't change the result.
        while ($factor > 1) 
        {
          $result = $result * $factor;
          $factor--; // Next factor
        }
        
        return $result;
    }
?>
