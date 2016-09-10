#!/usr/bin/perl

$title = "COMP 490 CGI-BIN"; # Title of HTML page
$values = $ENV{'QUERY_STRING'}; # Get the argument (will only accept one var and value)

($varname, $url) = split(/=/,$values); # Get the var name and value

$command=`/usr/bin/curl -s $url`; # Get the url webpage ( -s argument for curl makes it silent) 

print "Content-type: text/html\n\n";

print "$varname = $url"; # Debug purposes to check var name and url

#Display a simple html page
print <<"EOF";
<HTML>

<HEAD>
<TITLE>$title</TITLE>
</HEAD>

<BODY>
<H1>$title by Karan Bhamra.</H1>
<p>Filler paragraph material.</p>

</BODY>

</HTML>
EOF

print $command;  #Display the user inputted webpage
