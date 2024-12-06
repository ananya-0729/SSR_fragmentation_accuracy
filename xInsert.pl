#!/usr/bin/perl
use strict;
use warnings;
use List::Util 'shuffle';

sub insert_random_x {
    my ($input_file, $output_file, $num_insertions) = @_;

    open my $in_fh, '<', $input_file or die "Cannot open input file: $!";
    open my $out_fh, '>', $output_file or die "Cannot open output file: $!";

    my $inside_sequence = 0;
    my $current_sequence = '';

    while (my $line = <$in_fh>) {
        chomp $line;
        if ($line =~ /^>/) {
            # Header line
            if ($inside_sequence) {
                process_sequence($out_fh, $current_sequence, $num_insertions);
                $current_sequence = ''; # Reset current sequence
            }
            print $out_fh $line . "\n";
            $inside_sequence = 1;
        } elsif ($inside_sequence) {
            # Sequence line
            $current_sequence .= $line;
        }
    }

    # Process the last sequence
    if ($inside_sequence && $current_sequence) {
        process_sequence($out_fh, $current_sequence, $num_insertions);
    }

    close $in_fh;
    close $out_fh;
}

sub process_sequence {
    my ($out_fh, $sequence, $num_insertions) = @_;
    my @sequence_chars = split //, $sequence;
    for (1..$num_insertions) {
        my $random_position = int(rand(@sequence_chars));
        splice(@sequence_chars, $random_position, 0, 'X');
    }
    print $out_fh join("", @sequence_chars) . "\n";
}

if (@ARGV != 3) {
    die "Usage: $0 input_file output_file num_insertions\n";
}

my ($input_file_path, $output_file_path, $num_insertions) = @ARGV;
insert_random_x($input_file_path, $output_file_path, $num_insertions);
