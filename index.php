<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>Test av bildvisning</h1>
	<br>
	<br>

<?php
// Här är en testdel för php-skript.
//$test = "Yalla";
//$best = $test + "hej";
//echo $best;
//echo "<h1>Hello</h1>"; //den här blir heading 1

?>



<?php
    /*Den här delen är till för att identifiera den 
    senaste uppladdade bilden i img-mappen*/

    $dir = "img"; //$dir är en variabel, den kan lika gärna heta $bajs.

    $files = glob($dir . "/*.*");
    usort($files, function($a, $b){
        return (filemtime($a) < filemtime($b));
    });

    $files = array_slice($files, 0, 1);

    foreach($files as $file)
        //echo "<img src='" . $file. "' alt='code'>"; // här använder vi html syntax:en [img src] för att visa en bild och filsökvägen = $files.

    //echo "senaste bilden har filnamn $file";
    $lastImage = "<img src = '$file' height='80%'>";
    echo $lastImage;
    print $file;


?>

</body>
</html>
