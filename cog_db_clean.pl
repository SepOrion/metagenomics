#=============================================================================
#     FileName: clean_cog_db.pl
#         Desc: Filter genes in cog database which can't correspond to any COG ID.
#       Author: tanhao
#        Email: tanhao2013@gmail.com
#     HomePage: http://buttonwood.github.io
#      Version: 0.0.1
#   LastChange: 2014-05-09 11:19:35
#      History:
#   example: clean_cog_db.pl -myva myva whog >cog_clean.fa
#=============================================================================

use strict;
use warnings;
use Getopt::Long;
use Data::Dumper;

my($k_c,$myva,$blast,$verbose,$help);

my %cog;

GetOptions(
	"keycol:i"		=> \$k_c,
	"myva:s"			=> \$myva,
	"blast:s"			=> \$blast,
	"verbose"		=> \$verbose,
	"help:s"			=>	\$help,
);

if (@ARGV != 1 || $help) {
	die("Examples:\n\tperl $0 -keycol 5 -blast *.blast.tab whog >*.blast.tab.info\n
\tperl $0 -myva myva whog > clean.cog.fa\n");
}

my $whog = shift;

&read_whog($whog,\%cog) if ($whog);
#print Dumper(\%cog);

&filter($myva,\%cog) if ($myva);

&parse_tab($blast, $k_c, \%cog) if ($blast and $k_c);

sub read_whog{
	my($whog_file,$cog_ref)=@_;
	open IN,$whog_file or die $!;
#=pod
	my $title = '';
	while (<IN>) {
		chomp;
		if(/^\[/){
			my @t = split("\] ", $_, 2);
			#print $t[1],"\n";
			$title = $t[1];
		}elsif(/^  \w+:/){
			s/^\s+//;
			my @b = split /\s+/;
			shift @b;
			foreach my $y (@b) {
				$cog_ref->{$y} = $title if ($title);
			}
		}else{
			next;
		}
	}
=pod
	$/="^\["; <>;	$/="\n";
	while (<>) {
		print $_;
		my $title = $_;
		print $_;
		my $seq_name = $1 if($title =~ /^(\S+)/);
		print $seq_name, "***\n";
		$/="^\[";
        my $seq=<>;
        chomp $seq;
        my @t = split("\n",$seq);
        foreach my $x (@t) {
        	if ($x =~ /^  \w+:/) {
        		s/^\s+//;	chomp;
        		my @b = split /\s+/;
        		shift @b;
        		foreach my $y (@b) {
        			$cog_ref->{$y} = $seq_name;
        		}
        	}
        }
        $/="\n";
	}
=cut
	close IN;
}

sub filter {
	my ($myva,$cog_ref)=@_;
    open IN,$myva or die $!;
    while(<IN>){
    	chomp;
    	(my $title=$_) =~ s/^>//;
    	$/=">";
    	chomp(my $seq=<IN>);
    	$/="\n";
    	if(exists $cog_ref->{$title}){
    		my $info = $cog_ref->{$title};
    		print ">$title\t$info\n$seq";
    	}
    }
    close IN;
}

sub parse_tab {
	my ($tab, $col,$cog_ref)=@_;
	open IN,$tab or die $!;
	while (<IN>) {
		chomp;
		my @t = split;
		print join("\t",@t[0..13]);
		print "\t",$cog_ref->{$t[($col - 1)]} if (exists $cog_ref->{$t[($col - 1)]});
		print "\n";
	}
	close IN;
}
