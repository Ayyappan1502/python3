<?php
print_r($argv);
print($argc."\n");
if(count($argv) != 2){
    die("usage : md5 \"<string>\"\n");
}

print(md5($argv[1]));