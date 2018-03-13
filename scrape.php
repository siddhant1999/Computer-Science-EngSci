<?php

$input = array();
$input = explode(PHP_EOL,$_POST['input']);


$page = file_get_contents('https://google.ca/');//gets full source of page
$headLocation = strpos($page,"</head>") + 7;//get location of the end of the </head>
//$page = substr($page,$headLocation);//substring to keep only body
//$page = strip_tags($page);//strip html tags
//$page htmlspecialchars($page);//eliminate special characters*/

echo $page;//page is now a variable
?>
