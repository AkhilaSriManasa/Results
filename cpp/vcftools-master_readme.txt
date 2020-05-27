                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.


  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  0. Additional Definitions.

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License.

  "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version.

  The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  1. Exception to Section 3 of the GNU GPL.

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL.

  2. Conveying Modified Versions.

  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy.

  3. Object Code Incorporating Material from Library Header Files.

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document.

  4. Combined Works.

  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:

   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.

   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document.

   d) Do one of the following:

       0) Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

       1) Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version.

   e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)

  5. Combined Libraries.

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

   a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work.

  6. Revised Versions of the GNU Lesser General Public License.

  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation.

  If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library.

# VCFtools

A set of tools written in Perl and C++ for working with [VCF files](https://samtools.github.io/hts-specs/VCFv4.2.pdf), such as those generated by the
[1000 Genomes Project](http://www.1000genomes.org/).

Project website: https://vcftools.github.io/

License
-------

The program package is released under the GNU Lesser General Public License version 3.0
(LGPLv3). See the `LICENSE` file for the complete LGPL license text.

Credits
-------

- Adam Auton (Binary Executable)
- Petr Danecek (Perl Module)
- Anthony Marcketta (Binary Executable)

Building VCFtools
-----------------

General help about the building process's configuration step can be acquired via:

```
./configure --help
```

### Build from Release Tarball

```
./configure
make
make install
```
You may need `sudo` permissions to run `make install`.

### Build from GitHub

```
git clone https://github.com/vcftools/vcftools.git
cd vcftools
./autogen.sh
./configure
make
make install
```
You many need `sudo` permissions to run `make install`.

Documentation
-------------

Documentation and usage examples can be found here:

https://vcftools.github.io/examples.html

A manual page is also available. If prefix is set to `/usr` or if `MANPATH` points to
`$prefix/share/man`, you can access the manual page via:

```
man vcftools
```

Getting Help
------------

The best way to get help regarding VCFtools is to email the mailing list:

vcftools-help@lists.sourceforge.net

Citation
--------

If you make use of VCFtools in your research, we would appreciate a citation of the following paper:

> **The Variant Call Format and VCFtools**, Petr Danecek, Adam Auton, Goncalo Abecasis, Cornelis
> A. Albers, Eric Banks, Mark A. DePristo, Robert Handsaker, Gerton Lunter, Gabor Marth, Stephen
> T. Sherry, Gilean McVean, Richard Durbin and 1000 Genomes Project Analysis Group,
> **Bioinformatics**, 2011 http://dx.doi.org/10.1093/bioinformatics/btr330
100	100	1	id1_100	.	.	HM2	gene1	5
110	110	1	id1_110	CAAA	C,CA	0	.	6
110	110	1	id2_110	C	T	0	.	6
130	130	1	id1_130	G	T	HM2	.	7
130	130	1	id2_130	GAA	GG	HM2	.	7
140	140	1	id1_140	GT	G	0	.	8
150	150	1	id1_150	TAAAA	T	0	.	9
110	150	2	id2_110_150	CAAA	C	HM2	gene2	.
160	160	2	id2_160	TAAAA	TC	0	gene3	11
# Examples of user-defined filters. Edit and run with -f filters.txt.
# The examples below are self-explanatory. Notice the use of the predefined
#  variables ($PASS, $FAIL, $MATCH, $RECORD) and methods (error).


# In this example, a minimum value of AF1=0.1 is required
{
    tag  => 'INFO/AF1',                       # The VCF tag to apply this filter on
        name => 'MinAF',                          # The filter ID
        desc => 'Minimum AF1 [0.01]',             # Description for the VCF header
        test => sub { return $MATCH < 0.01 ? $FAIL : $PASS },
},


# Filter all indels (presence of INDEL tag is tested)
{
    tag      => 'INFO/INDEL',
    apply_to => 'indels',         # Can be one of SNPs, indels, all. Default: [All]
    name     => 'Indel',
    desc     => 'INDEL tag present',
    test     => sub { return $FAIL },
},


# Only loci with enough reads supporting the variant will pass the filter
{
    tag      => 'INFO/DP4',
    name     => 'FewAlts',
    desc     => 'Too few reads supporting the variant',
    apply_to => 'SNPs',
    test     => sub {
        if ( !($MATCH =~ /^([^,]+),([^,]+),([^,]+),(.+)$/) )
        {
            error("Could not parse INFO/DP4: $CHROM:$POS [$MATCH]");
        }
        if ( 0.1*($1+$2) > $3+$4  ) { return $PASS; }
        return $FAIL;
    },
},

# Example of filtering based on genotype columns and the QUAL column
{
    tag      => 'FORMAT/PL',
    name     => 'NoHets',
    desc     => 'Inbred homozygous mouse, no hets expected',
    apply_to => 'SNPs',
    test     => sub {
            for my $pl (@$MATCH)
            {
                my @pls = split(/,/,$pl);
                if ( $pls[1]<$pls[0] && $pls[1]<$pls[2] ) { return $FAIL; }
            }
        return $PASS;
    },
},


# This example splits the four PV4 values into four tags names PV0, PV1, PV2 and PV3. 
#   Note the use of the 'header' key, and the $RECORD and $VCF variables.
{
    header   => [ 
                    qq[key=INFO,ID=PV0,Number=1,Type=Float,Description="P-value for strand bias"],
                    qq[key=INFO,ID=PV1,Number=1,Type=Float,Description="P-value for baseQ bias"],
                    qq[key=INFO,ID=PV2,Number=1,Type=Float,Description="P-value for mapQ bias"],
                    qq[key=INFO,ID=PV3,Number=1,Type=Float,Description="P-value for tail distance bias"] 
                ], 
    tag      => 'INFO/PV4',
    name     => 'SplitPV4',
    desc     => 'Split PV4',
    apply_to => 'all',
    test     => sub {
        my @vals = split(/,/,$MATCH);
        $$RECORD[7] = $VCF->add_info_field($$RECORD[7],'PV0'=>$vals[0],'PV1'=>$vals[1],'PV2'=>$vals[2],'PV3'=>$vals[3]);
        return $PASS;
    },
},

# Do whatever you want with every record and edit it according to your needs. This silly
#   example removes the tag SILLY in records where ID is set and depth is bigger than 5.
{
    tag      => 'Dummy',
    test     => sub {
        if ( $$RECORD[2] eq '.' ) { return $PASS; } # Modify only lines with ID
        my $dp = $vcf->get_info_field($$RECORD[7],'DP');
        if ( $dp>5 ) { $$RECORD[7] = $VCF->add_info_field($$RECORD[7],'SILLY'=>undef); }
        return $PASS;
    },
}


# Filter records with the value XY absent or not equal to 42
{
    tag      => 'Dummy',
    header   => [
        qq[key=FILTER,ID=XY,Description="XY not OK"],
    ],
    test     => sub {
        my $xy      = $VCF->get_info_field($$RECORD[7],'XY');
        my $is_bad  = ( !defined $xy or $xy!=42 ) ? 1 : 0;
        $$RECORD[6] = $VCF->add_filter($$RECORD[6],'XY'=>$is_bad);
        return $PASS;
    },
},


# Annotate INFO field with SINGLETON flag when one and only one sample is different from the reference
{
    header   => [ 
        qq[key=INFO,ID=SINGLETON,Number=0,Type=Flag,Description="Only one non-ref sample"],
    ],
    tag      => 'FORMAT/GT',
    name     => 'Dummy',
    desc     => 'Dummy',
    test     => sub {
        my $nalt = 0;
        for my $gt (@$MATCH)
        {
            my @gt = $VCF->split_gt($gt);
            for my $allele (@gt)
            {
                if ( $allele ne 0 && $allele ne '.' ) { $nalt++; last; }
            }
            if ( $nalt>1 ) { last; }
        }
        if ( $nalt==1 ) { $$RECORD[7] = $VCF->add_info_field($$RECORD[7],'SINGLETON'=>''); }
        return $PASS;
    },
},


# Set genotypes to unknown ("." or "./." depending on ploidy) when coverage is low (by Shane McCarthy).
{
    tag      => 'FORMAT/DP',
    name     => 'MinSampleDP',
    desc     => 'Genotypes set to . for samples with DP < 2',
    apply_to => 'all',
    test     => sub {
        my $i = 8;
        for my $dp (@$MATCH)
        {
            $i++;
            next unless ($dp<2);
            my @format = split(/:/,$$RECORD[$i]);
            $format[0] = $format[0] =~ /\// ? "./." : ".";
            $$RECORD[$i] = join(":",@format);
        }
        return $PASS;
    },
},

ploidy =>
{
    20 =>
    [
        { from=>1,     to=>61275, M=>1, F=>2 },
        { from=>61282, to=>63231, F=>1 },
        { from=>63244, to=>63967, M=>1, F=>0 },
        { from=>65288, to=>68303, M=>0, F=>1 },
    ],
}
