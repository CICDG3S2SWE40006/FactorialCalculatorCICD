<!--
- Purpose: This program takes an input and outputs its factorial.
-->

<!DOCTYPE html >
<html lang = "en">
    <head>
    
        <meta charset = "utf-8" /> <!-- So the browser understands what encoding method is used -->
        <meta name = "description" content = "A basic php-embedded web page that calculates a number's factorial." />
        <meta name = "keywords"    content = "factorial, n, factorial, nth" />
        <meta name = "author"      content = "Brett MacIsaac" />
        <title>Factorial Calculator</title>
        
    </head>
    
    <body>
        
        <h1>Factorial Calculator</h1>
        
        <form id = "frmFactorial" method = "get" action = "factorial.php">
            <!-- Textbox for entering a number. -->
            <p>
                <label for = "txtNumber">Enter a positive integer: </label>
                <input type = "text" id = "txtNumber" name = "number" />
            </p>
            
            <!-- Button which results in the factorial being calculated and returned -->
            <input type = "submit" value = "Calculate Factorial" />
        </form>
        
    </body>
    
</html>