#!/usr/bin/perl

$url = "www.example.com";
$command=`/usr/bin/curl -s $url`;
$title = "COMP 490 CGI-BIN";
 
print "Content-type: text/html\n\n";
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

#print "COMP 490 CGI-BIN Program by Karan Bhamra\n";

#print $command;
