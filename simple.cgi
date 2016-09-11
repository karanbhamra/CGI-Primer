#!/usr/bin/perl
use URI::Escape;

$title = "COMP 490 CGI-BIN"; # Title of HTML page
$values = $ENV{'QUERY_STRING'}; # Get the argument (will only accept one var and value)

($varname, $url) = split(/=/,$values); # Get the var name and value, seperated by '='

print "Content-type: text/html\n\n";  # Specify content type

$newurl = uri_unescape($url);	# Remove url encoding to use raw url

$command=`/usr/bin/curl -L $newurl`; # Get the url webpage ( -L argument for curl makes it follow redirect) 

#Display a simple html page
print <<"EOF";
<!doctype html>
<HTML lang="en">
<HEAD>
<TITLE>$title</TITLE>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="css/styles.css">
</HEAD>
<BODY>
<H1 id="mytitle">$title by Karan Bhamra</H1>
<form action="simple.cgi" id="myform">
URL:<br>
<input type="text" name="url" value="" id="myurl"><br>
<input type="submit" formenctype="multipart/form-data" value="Submit" id="mybutton">
</form>
</BODY>
</HTML>
EOF

print $command;  #Display the user inputted webpage
