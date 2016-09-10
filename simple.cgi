#!/usr/bin/perl
use URI::Escape;

$title = "COMP 490 CGI-BIN"; # Title of HTML page
$values = $ENV{'QUERY_STRING'}; # Get the argument (will only accept one var and value)

($varname, $url) = split(/=/,$values); # Get the var name and value, seperated by '='

print "Content-type: text/html\n\n";  # Specify content type

$newurl = uri_unescape($url);	# Remove url encoding to use raw url
# print "$varname = $url"; # Debug purposes to check var name and url

#$fullurl = "http://www.$url/"; # create full url by adding protocol to the given url
# print $fullurl; # Debug purpose to get full webpage url

$command=`/usr/bin/curl -L $newurl`; # Get the url webpage ( -L argument for curl makes it follow redirect) 

#Display a simple html page
print <<"EOF";
<HTML>
<HEAD>
<TITLE>$title</TITLE>
</HEAD>
<BODY>
<H1>$title by Karan Bhamra.</H1>
<form action="simple.cgi">
URL:<br>
<input type="text" name="url" value=""><br>
<input type="submit" formenctype="multipart/form-data" value="Submit">
</form>
</BODY>
</HTML>
EOF

print $command;  #Display the user inputted webpage
