#!/usr/bin/perl

use strict;
use warnings;

#Usage perl splitbyXs.pl < test.fa

$/ = "\n>";

while (<>) {
    s/>//g;
    my ($id, @seq) = split (/\n+/, $_);
    my @slices = split (/X+/, join("", @seq));
    my $num = 0;
    foreach my $seq (@slices) {
        $num++;
        print ">$id\_$num\n";
        while ($seq) {
            print substr($seq, 0, 80), "\n";
            substr($seq, 0, 80) = '';
        }
    }
}
