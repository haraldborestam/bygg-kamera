<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>Test av bildimport</h1>
	<br>
	<br>

<?php

    $dir = "img";

    $files = glob($dir . "/*.*");
    usort($files, function($a, $b){
        return (filemtime($a) < filemtime($b));
    });

    $files = array_slice($files, 0, 1);

    foreach($files as $file)
        echo "<img src='" . $file. "' alt='code'>";

?>

</body>
</html>
