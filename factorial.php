<!--
    - Purpose: This program takes an input and outputs its factorial.
    - Author: Brett MacIsaac.
-->

<!DOCTYPE html >
<html lang = "en">
    <head>
        <meta charset = "utf-8" /> <!-- So the browser understands what encoding method is used -->
        <meta name = "description" content = "A basic php-embedded web page that calculates a number's factorial." />
        <meta name = "keywords"    content = "factorial, n, factorial, nth" />
        <meta name = "author"       content = "Brett MacIsaac" />
        <title>Factorial Calculator - Result</title>
    </head>
    
    <body>
        <!-- Access necessary php functions -->
        <?php include ("mathfunctions.php"); ?>
        
        <h1>Factorial Calculator</h1>
        
        <?php
            // Declare and assign a variable an appropriate value from the form (if it exists).
            $n = 0;
            if (isset($_GET["number"])) // If data from form exists.
            { $n = $_GET["number"]; }

            // Validation and output of the factorial (or error message).
            if (isPositiveInteger($n)) // User has entered a valid input.
            {
                // Output as list.
                echo "<p>", $n, "! is ", factorial($n), ".</p>"; // Output factorial of user's input.
            }
            else // Non-valid input.
            {
                echo "<p>Please enter a positive integer.</p>"; // Error message.
            }
            echo "<p><a href = 'index.php'>Back</a></p>";
        ?>
    </body>
    
</html>