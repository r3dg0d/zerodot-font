## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[9] DotZero-Italic[wght].ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>💥 <b>ERROR</b> Check tabular widths don't have kerning. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#tabular-kerning">tabular_kerning</a></summary>
    <div>


> 
> Tabular glyphs should not have kerning, as they are meant to be used in tables.
> 
> This check looks for kerning in:
> - all glyphs in a font in combination with tabular numerals;
> - tabular symbols in combination with tabular numerals.
> 
> "Tabular symbols" is defined as:
> - for fonts with a "tnum" feature, all "tnum" substitution target glyphs;
> - for fonts without a "tnum" feature, all glyphs that have the same width
> as the tabular numerals, but limited to numbers, math and currency symbols.
> 
> This check may produce false positives for fonts with no "tnum" feature
> and with equal-width numerals (and other same-width symbols) that are
> not intended to be used as tabular numerals.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4440





* 💥 **ERROR** <p>Failed with HarfBuzzError: Failed to open: fonts/variable/DotZero-Italic[wght].ttf</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/tabular_kerning.py&quot;, line 62, in check_tabular_kerning
    vhb.hbfont.funcs = funcs
    ^^^^^^^^^^
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/vharfbuzz/__init__.py&quot;, line 39, in hbfont
    blob = hb.Blob.from_file_path(self.filename)
  File &quot;src/uharfbuzz/_blob.pxi&quot;, line 54, in uharfbuzz._harfbuzz.Blob.from_file_path

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>


> 
> A font's winAscent and winDescent values should be greater than or equal to
> the head table's yMax, abs(yMin) values. If they are less than these values,
> clipping can occur on Windows platforms
> (https://github.com/RedHatBrand/Overpass/issues/33).
> 
> If the font includes tall/deep writing systems such as Arabic or Devanagari,
> the winAscent and winDescent can be greater than the yMax and absolute yMin
> values to accommodate vowel marks.
> 
> When the 'win' Metrics are significantly greater than the UPM, the linespacing
> can appear too loose. To counteract this, enabling the OS/2 fsSelection
> bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values
> instead. This means the font developer can control the linespacing with
> the 'typo' values, whilst avoiding clipping by setting the 'win' values to
> values greater than the yMax and absolute yMin.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 327, but got 300 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking with ots-sanitize. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ots">ots</a></summary>
    <div>


> 
> The OpenType Sanitizer (OTS) is a tool that checks that the font is
> structually well-formed and passes various sanity checks. It is used by
> many web browsers to check web fonts before using them; fonts which fail
> such checks are blocked by browsers.
> 
> This check runs OTS on the font and reports any errors or warnings that
> it finds.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>ots-sanitize returned an error code (1). Output follows:</p>
<p>Failed to open: fonts/variable/DotZero-Italic[wght].ttf</p>
 [code: ots-sanitize-error]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking with fontTools.ttx <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ttx-roundtrip">ttx_roundtrip</a></summary>
    <div>


> 
> One way of testing whether or not fonts are well-formed at the
> binary level is to convert them to TTX and then back to binary. Structural
> problems within the binary font will show up as errors during conversion.
> This is not necessarily something that a designer will be able to address
> but is evidence of a potential bug in the font compiler used to generate
> the binary.




> Original proposal: https://github.com/fonttools/fontbakery/issues/1763





* 🔥 **FAIL** <p>usage: ttx [options] inputfile1 [... inputfileN]</p>
 



* 🔥 **FAIL**  



* 🔥 **FAIL** <p>TTX -- From OpenType To XML And Back</p>
 



* 🔥 **FAIL** <p>If an input file is a TrueType or OpenType font file, it will be</p>
 



* 🔥 **FAIL** <p>decompiled to a TTX file (an XML-based text format).</p>
 



* 🔥 **FAIL** <p>If an input file is a TTX file, it will be compiled to whatever</p>
 



* 🔥 **FAIL** <p>format the data is in, a TrueType or OpenType/CFF font file.</p>
 



* 🔥 **FAIL** <p>A special input value of - means read from the standard input.</p>
 



* 🔥 **FAIL** <p>Output files are created so they are unique: an existing file is</p>
 



* 🔥 **FAIL** <p>never overwritten.</p>
 



* 🔥 **FAIL** <p>General options</p>
 



* 🔥 **FAIL** <p>===============</p>
 



* 🔥 **FAIL** <p>-h Help            print this message.</p>
 



* 🔥 **FAIL** <p>--version          show version and exit.</p>
 



* 🔥 **FAIL** <p>-d <outputfolder>  Specify a directory where the output files are</p>
 



* 🔥 **FAIL** <p>to be created.</p>
 



* 🔥 **FAIL** <p>-o <outputfile>    Specify a file to write the output to. A special</p>
 



* 🔥 **FAIL** <p>value of - would use the standard output.</p>
 



* 🔥 **FAIL** <p>-f                 Overwrite existing output file(s), ie. don't append</p>
 



* 🔥 **FAIL** <p>numbers.</p>
 



* 🔥 **FAIL** <p>-v                 Verbose: more messages will be written to stdout</p>
 



* 🔥 **FAIL** <p>about what is being done.</p>
 



* 🔥 **FAIL** <p>-q                 Quiet: No messages will be written to stdout about</p>
 



* 🔥 **FAIL** <p>what is being done.</p>
 



* 🔥 **FAIL** <p>-a                 allow virtual glyphs ID's on compile or decompile.</p>
 



* 🔥 **FAIL** <p>Dump options</p>
 



* 🔥 **FAIL** <p>============</p>
 



* 🔥 **FAIL** <p>-l           List table info: instead of dumping to a TTX file, list</p>
 



* 🔥 **FAIL** <p>some minimal info about each table.</p>
 



* 🔥 **FAIL** <p>-t <table>   Specify a table to dump. Multiple -t options</p>
 



* 🔥 **FAIL** <p>are allowed. When no -t option is specified, all tables</p>
 



* 🔥 **FAIL** <p>will be dumped.</p>
 



* 🔥 **FAIL** <p>-x <table>   Specify a table to exclude from the dump. Multiple</p>
 



* 🔥 **FAIL** <p>-x options are allowed. -t and -x are mutually exclusive.</p>
 



* 🔥 **FAIL** <p>-s           Split tables: save the TTX data into separate TTX files per</p>
 



* 🔥 **FAIL** <p>table and write one small TTX file that contains references</p>
 



* 🔥 **FAIL** <p>to the individual table dumps. This file can be used as</p>
 



* 🔥 **FAIL** <p>input to ttx, as long as the table files are in the</p>
 



* 🔥 **FAIL** <p>same directory.</p>
 



* 🔥 **FAIL** <p>-g           Split glyf table: Save the glyf data into separate TTX files</p>
 



* 🔥 **FAIL** <p>per glyph and write a small TTX for the glyf table which</p>
 



* 🔥 **FAIL** <p>contains references to the individual TTGlyph elements.</p>
 



* 🔥 **FAIL** <p>NOTE: specifying -g implies -s (no need for -s together</p>
 



* 🔥 **FAIL** <p>with -g)</p>
 



* 🔥 **FAIL** <p>-i           Do NOT disassemble TT instructions: when this option is</p>
 



* 🔥 **FAIL** <p>given, all TrueType programs (glyph programs, the font</p>
 



* 🔥 **FAIL** <p>program and the pre-program) will be written to the TTX</p>
 



* 🔥 **FAIL** <p>file as hex data instead of assembly. This saves some time</p>
 



* 🔥 **FAIL** <p>and makes the TTX file smaller.</p>
 



* 🔥 **FAIL** <p>-z <format>  Specify a bitmap data export option for EBDT:</p>
 



* 🔥 **FAIL** <p>{'raw', 'row', 'bitwise', 'extfile'} or for the CBDT:</p>
 



* 🔥 **FAIL** <p>{'raw', 'extfile'} Each option does one of the following:</p>
 



* 🔥 **FAIL** <p>-z raw</p>
 



* 🔥 **FAIL** <p>export the bitmap data as a hex dump</p>
 



* 🔥 **FAIL** <p>-z row</p>
 



* 🔥 **FAIL** <p>export each row as hex data</p>
 



* 🔥 **FAIL** <p>-z bitwise</p>
 



* 🔥 **FAIL** <p>export each row as binary in an ASCII art style</p>
 



* 🔥 **FAIL** <p>-z extfile</p>
 



* 🔥 **FAIL** <p>export the data as external files with XML references</p>
 



* 🔥 **FAIL** <p>If no export format is specified 'raw' format is used.</p>
 



* 🔥 **FAIL** <p>-e           Don't ignore decompilation errors, but show a full traceback</p>
 



* 🔥 **FAIL** <p>and abort.</p>
 



* 🔥 **FAIL** <p>-y <number>  Select font number for TrueType Collection (.ttc/.otc),</p>
 



* 🔥 **FAIL** <p>starting from 0.</p>
 



* 🔥 **FAIL** <p>--unicodedata &lt;UnicodeData.txt&gt;</p>
 



* 🔥 **FAIL** <p>Use custom database file to write character names in the</p>
 



* 🔥 **FAIL** <p>comments of the cmap TTX output.</p>
 



* 🔥 **FAIL** <p>--newline <value></p>
 



* 🔥 **FAIL** <p>Control how line endings are written in the XML file. It</p>
 



* 🔥 **FAIL** <p>can be 'LF', 'CR', or 'CRLF'. If not specified, the</p>
 



* 🔥 **FAIL** <p>default platform-specific line endings are used.</p>
 



* 🔥 **FAIL** <p>Compile options</p>
 



* 🔥 **FAIL** <p>-m           Merge with TrueType-input-file: specify a TrueType or</p>
 



* 🔥 **FAIL** <p>OpenType font file to be merged with the TTX file. This</p>
 



* 🔥 **FAIL** <p>option is only valid when at most one TTX file is specified.</p>
 



* 🔥 **FAIL** <p>-b           Don't recalc glyph bounding boxes: use the values in the</p>
 



* 🔥 **FAIL** <p>TTX file as-is.</p>
 



* 🔥 **FAIL** <p>--recalc-timestamp</p>
 



* 🔥 **FAIL** <p>Set font 'modified' timestamp to current time.</p>
 



* 🔥 **FAIL** <p>By default, the modification time of the TTX file will be</p>
 



* 🔥 **FAIL** <p>used.</p>
 



* 🔥 **FAIL** <p>--no-recalc-timestamp</p>
 



* 🔥 **FAIL** <p>Keep the original font 'modified' timestamp.</p>
 



* 🔥 **FAIL** <p>--flavor <type></p>
 



* 🔥 **FAIL** <p>Specify flavor of output font file. May be 'woff' or 'woff2'.</p>
 



* 🔥 **FAIL** <p>Note that WOFF2 requires the Brotli Python extension,</p>
 



* 🔥 **FAIL** <p>available at <a href="https://github.com/google/brotli">https://github.com/google/brotli</a></p>
 



* 🔥 **FAIL** <p>--with-zopfli</p>
 



* 🔥 **FAIL** <p>Use Zopfli instead of Zlib to compress WOFF. The Python</p>
 



* 🔥 **FAIL** <p>extension is available at <a href="https://pypi.python.org/pypi/zopfli">https://pypi.python.org/pypi/zopfli</a></p>
 



* 🔥 **FAIL** <p>--optimize-font-speed</p>
 



* 🔥 **FAIL** <p>Enable optimizations that prioritize speed over file size.</p>
 



* 🔥 **FAIL** <p>This mainly affects how glyf t able and gvar / VARC tables are</p>
 



* 🔥 **FAIL** <p>compiled. The produced fonts will be larger, but rendering</p>
 



* 🔥 **FAIL** <p>performance will be improved with HarfBuzz and other text</p>
 



* 🔥 **FAIL** <p>layout engines.</p>
 



* 🔥 **FAIL** <p>ERROR: File not found: &quot;fonts/variable/DotZero-Italic[wght].ttf&quot;</p>
 



* 🔥 **FAIL** <h1>TTX had some problem parsing the generated XML file. This most likely mean there's some problem in the font. Please inspect the output of ttx in order to find more on what went wrong. A common problem is the presence of control characteres outside the accepted character range as defined in the XML spec. FontTools has got a bug which causes TTX to generate corrupt XML files in those cases. So, check the entries of the name table and remove any control chars that you find there. The full ttx error message was:</h1>
<p>usage: ttx [options] inputfile1 [... inputfileN]</p>
<p>TTX -- From OpenType To XML And Back</p>
<p>If an input file is a TrueType or OpenType font file, it will be
decompiled to a TTX file (an XML-based text format).
If an input file is a TTX file, it will be compiled to whatever
format the data is in, a TrueType or OpenType/CFF font file.
A special input value of - means read from the standard input.</p>
<p>Output files are created so they are unique: an existing file is
never overwritten.</p>
<h1>General options</h1>
<p>-h Help            print this message.
--version          show version and exit.
-d <outputfolder>  Specify a directory where the output files are
to be created.
-o <outputfile>    Specify a file to write the output to. A special
value of - would use the standard output.
-f                 Overwrite existing output file(s), ie. don't append
numbers.
-v                 Verbose: more messages will be written to stdout
about what is being done.
-q                 Quiet: No messages will be written to stdout about
what is being done.
-a                 allow virtual glyphs ID's on compile or decompile.</p>
<h1>Dump options</h1>
<p>-l           List table info: instead of dumping to a TTX file, list
some minimal info about each table.
-t <table>   Specify a table to dump. Multiple -t options
are allowed. When no -t option is specified, all tables
will be dumped.
-x <table>   Specify a table to exclude from the dump. Multiple
-x options are allowed. -t and -x are mutually exclusive.
-s           Split tables: save the TTX data into separate TTX files per
table and write one small TTX file that contains references
to the individual table dumps. This file can be used as
input to ttx, as long as the table files are in the
same directory.
-g           Split glyf table: Save the glyf data into separate TTX files
per glyph and write a small TTX for the glyf table which
contains references to the individual TTGlyph elements.
NOTE: specifying -g implies -s (no need for -s together
with -g)
-i           Do NOT disassemble TT instructions: when this option is
given, all TrueType programs (glyph programs, the font
program and the pre-program) will be written to the TTX
file as hex data instead of assembly. This saves some time
and makes the TTX file smaller.
-z <format>  Specify a bitmap data export option for EBDT:
{'raw', 'row', 'bitwise', 'extfile'} or for the CBDT:
{'raw', 'extfile'} Each option does one of the following:</p>
<pre><code>         -z raw
           export the bitmap data as a hex dump
         -z row
           export each row as hex data
         -z bitwise
           export each row as binary in an ASCII art style
         -z extfile
           export the data as external files with XML references

         If no export format is specified 'raw' format is used.
</code></pre>
<p>-e           Don't ignore decompilation errors, but show a full traceback
and abort.
-y <number>  Select font number for TrueType Collection (.ttc/.otc),
starting from 0.
--unicodedata &lt;UnicodeData.txt&gt;
Use custom database file to write character names in the
comments of the cmap TTX output.
--newline <value>
Control how line endings are written in the XML file. It
can be 'LF', 'CR', or 'CRLF'. If not specified, the
default platform-specific line endings are used.</p>
<h1>Compile options</h1>
<p>-m           Merge with TrueType-input-file: specify a TrueType or
OpenType font file to be merged with the TTX file. This
option is only valid when at most one TTX file is specified.
-b           Don't recalc glyph bounding boxes: use the values in the
TTX file as-is.
--recalc-timestamp
Set font 'modified' timestamp to current time.
By default, the modification time of the TTX file will be
used.
--no-recalc-timestamp
Keep the original font 'modified' timestamp.
--flavor <type>
Specify flavor of output font file. May be 'woff' or 'woff2'.
Note that WOFF2 requires the Brotli Python extension,
available at <a href="https://github.com/google/brotli">https://github.com/google/brotli</a>
--with-zopfli
Use Zopfli instead of Zlib to compress WOFF. The Python
extension is available at <a href="https://pypi.python.org/pypi/zopfli">https://pypi.python.org/pypi/zopfli</a>
--optimize-font-speed
Enable optimizations that prioritize speed over file size.
This mainly affects how glyf t able and gvar / VARC tables are
compiled. The produced fonts will be larger, but rendering
performance will be improved with HarfBuzz and other text
layout engines.</p>
<p>ERROR: Unknown file type: &quot;/tmp/tmpxej93x4u&quot;</p>
<p>======</p>
 



* 🔥 **FAIL** <p>usage: ttx [options] inputfile1 [... inputfileN]</p>
 



* 🔥 **FAIL**  



* 🔥 **FAIL** <p>TTX -- From OpenType To XML And Back</p>
 



* 🔥 **FAIL** <p>If an input file is a TrueType or OpenType font file, it will be</p>
 



* 🔥 **FAIL** <p>decompiled to a TTX file (an XML-based text format).</p>
 



* 🔥 **FAIL** <p>If an input file is a TTX file, it will be compiled to whatever</p>
 



* 🔥 **FAIL** <p>format the data is in, a TrueType or OpenType/CFF font file.</p>
 



* 🔥 **FAIL** <p>A special input value of - means read from the standard input.</p>
 



* 🔥 **FAIL** <p>Output files are created so they are unique: an existing file is</p>
 



* 🔥 **FAIL** <p>never overwritten.</p>
 



* 🔥 **FAIL** <p>General options</p>
 



* 🔥 **FAIL** <p>===============</p>
 



* 🔥 **FAIL** <p>-h Help            print this message.</p>
 



* 🔥 **FAIL** <p>--version          show version and exit.</p>
 



* 🔥 **FAIL** <p>-d <outputfolder>  Specify a directory where the output files are</p>
 



* 🔥 **FAIL** <p>to be created.</p>
 



* 🔥 **FAIL** <p>-o <outputfile>    Specify a file to write the output to. A special</p>
 



* 🔥 **FAIL** <p>value of - would use the standard output.</p>
 



* 🔥 **FAIL** <p>-f                 Overwrite existing output file(s), ie. don't append</p>
 



* 🔥 **FAIL** <p>numbers.</p>
 



* 🔥 **FAIL** <p>-v                 Verbose: more messages will be written to stdout</p>
 



* 🔥 **FAIL** <p>about what is being done.</p>
 



* 🔥 **FAIL** <p>-q                 Quiet: No messages will be written to stdout about</p>
 



* 🔥 **FAIL** <p>what is being done.</p>
 



* 🔥 **FAIL** <p>-a                 allow virtual glyphs ID's on compile or decompile.</p>
 



* 🔥 **FAIL** <p>Dump options</p>
 



* 🔥 **FAIL** <p>============</p>
 



* 🔥 **FAIL** <p>-l           List table info: instead of dumping to a TTX file, list</p>
 



* 🔥 **FAIL** <p>some minimal info about each table.</p>
 



* 🔥 **FAIL** <p>-t <table>   Specify a table to dump. Multiple -t options</p>
 



* 🔥 **FAIL** <p>are allowed. When no -t option is specified, all tables</p>
 



* 🔥 **FAIL** <p>will be dumped.</p>
 



* 🔥 **FAIL** <p>-x <table>   Specify a table to exclude from the dump. Multiple</p>
 



* 🔥 **FAIL** <p>-x options are allowed. -t and -x are mutually exclusive.</p>
 



* 🔥 **FAIL** <p>-s           Split tables: save the TTX data into separate TTX files per</p>
 



* 🔥 **FAIL** <p>table and write one small TTX file that contains references</p>
 



* 🔥 **FAIL** <p>to the individual table dumps. This file can be used as</p>
 



* 🔥 **FAIL** <p>input to ttx, as long as the table files are in the</p>
 



* 🔥 **FAIL** <p>same directory.</p>
 



* 🔥 **FAIL** <p>-g           Split glyf table: Save the glyf data into separate TTX files</p>
 



* 🔥 **FAIL** <p>per glyph and write a small TTX for the glyf table which</p>
 



* 🔥 **FAIL** <p>contains references to the individual TTGlyph elements.</p>
 



* 🔥 **FAIL** <p>NOTE: specifying -g implies -s (no need for -s together</p>
 



* 🔥 **FAIL** <p>with -g)</p>
 



* 🔥 **FAIL** <p>-i           Do NOT disassemble TT instructions: when this option is</p>
 



* 🔥 **FAIL** <p>given, all TrueType programs (glyph programs, the font</p>
 



* 🔥 **FAIL** <p>program and the pre-program) will be written to the TTX</p>
 



* 🔥 **FAIL** <p>file as hex data instead of assembly. This saves some time</p>
 



* 🔥 **FAIL** <p>and makes the TTX file smaller.</p>
 



* 🔥 **FAIL** <p>-z <format>  Specify a bitmap data export option for EBDT:</p>
 



* 🔥 **FAIL** <p>{'raw', 'row', 'bitwise', 'extfile'} or for the CBDT:</p>
 



* 🔥 **FAIL** <p>{'raw', 'extfile'} Each option does one of the following:</p>
 



* 🔥 **FAIL** <p>-z raw</p>
 



* 🔥 **FAIL** <p>export the bitmap data as a hex dump</p>
 



* 🔥 **FAIL** <p>-z row</p>
 



* 🔥 **FAIL** <p>export each row as hex data</p>
 



* 🔥 **FAIL** <p>-z bitwise</p>
 



* 🔥 **FAIL** <p>export each row as binary in an ASCII art style</p>
 



* 🔥 **FAIL** <p>-z extfile</p>
 



* 🔥 **FAIL** <p>export the data as external files with XML references</p>
 



* 🔥 **FAIL** <p>If no export format is specified 'raw' format is used.</p>
 



* 🔥 **FAIL** <p>-e           Don't ignore decompilation errors, but show a full traceback</p>
 



* 🔥 **FAIL** <p>and abort.</p>
 



* 🔥 **FAIL** <p>-y <number>  Select font number for TrueType Collection (.ttc/.otc),</p>
 



* 🔥 **FAIL** <p>starting from 0.</p>
 



* 🔥 **FAIL** <p>--unicodedata &lt;UnicodeData.txt&gt;</p>
 



* 🔥 **FAIL** <p>Use custom database file to write character names in the</p>
 



* 🔥 **FAIL** <p>comments of the cmap TTX output.</p>
 



* 🔥 **FAIL** <p>--newline <value></p>
 



* 🔥 **FAIL** <p>Control how line endings are written in the XML file. It</p>
 



* 🔥 **FAIL** <p>can be 'LF', 'CR', or 'CRLF'. If not specified, the</p>
 



* 🔥 **FAIL** <p>default platform-specific line endings are used.</p>
 



* 🔥 **FAIL** <p>Compile options</p>
 



* 🔥 **FAIL** <p>-m           Merge with TrueType-input-file: specify a TrueType or</p>
 



* 🔥 **FAIL** <p>OpenType font file to be merged with the TTX file. This</p>
 



* 🔥 **FAIL** <p>option is only valid when at most one TTX file is specified.</p>
 



* 🔥 **FAIL** <p>-b           Don't recalc glyph bounding boxes: use the values in the</p>
 



* 🔥 **FAIL** <p>TTX file as-is.</p>
 



* 🔥 **FAIL** <p>--recalc-timestamp</p>
 



* 🔥 **FAIL** <p>Set font 'modified' timestamp to current time.</p>
 



* 🔥 **FAIL** <p>By default, the modification time of the TTX file will be</p>
 



* 🔥 **FAIL** <p>used.</p>
 



* 🔥 **FAIL** <p>--no-recalc-timestamp</p>
 



* 🔥 **FAIL** <p>Keep the original font 'modified' timestamp.</p>
 



* 🔥 **FAIL** <p>--flavor <type></p>
 



* 🔥 **FAIL** <p>Specify flavor of output font file. May be 'woff' or 'woff2'.</p>
 



* 🔥 **FAIL** <p>Note that WOFF2 requires the Brotli Python extension,</p>
 



* 🔥 **FAIL** <p>available at <a href="https://github.com/google/brotli">https://github.com/google/brotli</a></p>
 



* 🔥 **FAIL** <p>--with-zopfli</p>
 



* 🔥 **FAIL** <p>Use Zopfli instead of Zlib to compress WOFF. The Python</p>
 



* 🔥 **FAIL** <p>extension is available at <a href="https://pypi.python.org/pypi/zopfli">https://pypi.python.org/pypi/zopfli</a></p>
 



* 🔥 **FAIL** <p>--optimize-font-speed</p>
 



* 🔥 **FAIL** <p>Enable optimizations that prioritize speed over file size.</p>
 



* 🔥 **FAIL** <p>This mainly affects how glyf t able and gvar / VARC tables are</p>
 



* 🔥 **FAIL** <p>compiled. The produced fonts will be larger, but rendering</p>
 



* 🔥 **FAIL** <p>performance will be improved with HarfBuzz and other text</p>
 



* 🔥 **FAIL** <p>layout engines.</p>
 



* 🔥 **FAIL** <p>ERROR: Unknown file type: &quot;/tmp/tmpxej93x4u&quot;</p>
 







</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-avar-table">mandatory_avar_table</a></summary>
    <div>


> 
> Most variable fonts should include an avar table to correctly define
> axes progression rates.
> 
> For example, a weight axis from 0% to 100% doesn't map directly to 100 to 1000,
> because a 10% progression from 0% may be too much to define the 200,
> while 90% may be too little to define the 900.
> 
> If the progression rates of axes is linear, this check can be ignored.
> Fontmake will also skip adding an avar table if the progression rates
> are linear. However, it is still recommended that designers visually proof
> each instance is at the expected weight, width etc.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3100





* ⚠️ **WARN** <p>This variable font does not have an avar table. Most variable fonts should include an avar table to correctly define axes progression rates.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* uni2599 (U+2599): L&lt;&lt;0.0,385.0&gt;--&lt;330.0,385.0&gt;&gt; has the same coordinates as a previous segment.

* uni2599 (U+2599): L&lt;&lt;330.0,-275.0&gt;--&lt;330.0,385.0&gt;&gt; has the same coordinates as a previous segment.

* uni259B (U+259B): L&lt;&lt;330.0,385.0&gt;--&lt;330.0,1045.0&gt;&gt; has the same coordinates as a previous segment.

* uni259B (U+259B): L&lt;&lt;0.0,385.0&gt;--&lt;330.0,385.0&gt;&gt; has the same coordinates as a previous segment.

* uni259C (U+259C): L&lt;&lt;330.0,385.0&gt;--&lt;330.0,1045.0&gt;&gt; has the same coordinates as a previous segment.

* uni259C (U+259C): L&lt;&lt;330.0,385.0&gt;--&lt;660.0,385.0&gt;&gt; has the same coordinates as a previous segment.

* uni259F (U+259F): L&lt;&lt;330.0,-275.0&gt;--&lt;330.0,385.0&gt;&gt; has the same coordinates as a previous segment.

* uni259F (U+259F): L&lt;&lt;330.0,385.0&gt;--&lt;660.0,385.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[9] DotZero[wght].ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>💥 <b>ERROR</b> Check tabular widths don't have kerning. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#tabular-kerning">tabular_kerning</a></summary>
    <div>


> 
> Tabular glyphs should not have kerning, as they are meant to be used in tables.
> 
> This check looks for kerning in:
> - all glyphs in a font in combination with tabular numerals;
> - tabular symbols in combination with tabular numerals.
> 
> "Tabular symbols" is defined as:
> - for fonts with a "tnum" feature, all "tnum" substitution target glyphs;
> - for fonts without a "tnum" feature, all glyphs that have the same width
> as the tabular numerals, but limited to numbers, math and currency symbols.
> 
> This check may produce false positives for fonts with no "tnum" feature
> and with equal-width numerals (and other same-width symbols) that are
> not intended to be used as tabular numerals.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4440





* 💥 **ERROR** <p>Failed with HarfBuzzError: Failed to open: fonts/variable/DotZero[wght].ttf</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/tabular_kerning.py&quot;, line 62, in check_tabular_kerning
    vhb.hbfont.funcs = funcs
    ^^^^^^^^^^
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/vharfbuzz/__init__.py&quot;, line 39, in hbfont
    blob = hb.Blob.from_file_path(self.filename)
  File &quot;src/uharfbuzz/_blob.pxi&quot;, line 54, in uharfbuzz._harfbuzz.Blob.from_file_path

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>


> 
> A font's winAscent and winDescent values should be greater than or equal to
> the head table's yMax, abs(yMin) values. If they are less than these values,
> clipping can occur on Windows platforms
> (https://github.com/RedHatBrand/Overpass/issues/33).
> 
> If the font includes tall/deep writing systems such as Arabic or Devanagari,
> the winAscent and winDescent can be greater than the yMax and absolute yMin
> values to accommodate vowel marks.
> 
> When the 'win' Metrics are significantly greater than the UPM, the linespacing
> can appear too loose. To counteract this, enabling the OS/2 fsSelection
> bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values
> instead. This means the font developer can control the linespacing with
> the 'typo' values, whilst avoiding clipping by setting the 'win' values to
> values greater than the yMax and absolute yMin.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 327, but got 300 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking with ots-sanitize. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ots">ots</a></summary>
    <div>


> 
> The OpenType Sanitizer (OTS) is a tool that checks that the font is
> structually well-formed and passes various sanity checks. It is used by
> many web browsers to check web fonts before using them; fonts which fail
> such checks are blocked by browsers.
> 
> This check runs OTS on the font and reports any errors or warnings that
> it finds.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>ots-sanitize returned an error code (1). Output follows:</p>
<p>Failed to open: fonts/variable/DotZero[wght].ttf</p>
 [code: ots-sanitize-error]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking with fontTools.ttx <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ttx-roundtrip">ttx_roundtrip</a></summary>
    <div>


> 
> One way of testing whether or not fonts are well-formed at the
> binary level is to convert them to TTX and then back to binary. Structural
> problems within the binary font will show up as errors during conversion.
> This is not necessarily something that a designer will be able to address
> but is evidence of a potential bug in the font compiler used to generate
> the binary.




> Original proposal: https://github.com/fonttools/fontbakery/issues/1763





* 🔥 **FAIL** <p>usage: ttx [options] inputfile1 [... inputfileN]</p>
 



* 🔥 **FAIL**  



* 🔥 **FAIL** <p>TTX -- From OpenType To XML And Back</p>
 



* 🔥 **FAIL** <p>If an input file is a TrueType or OpenType font file, it will be</p>
 



* 🔥 **FAIL** <p>decompiled to a TTX file (an XML-based text format).</p>
 



* 🔥 **FAIL** <p>If an input file is a TTX file, it will be compiled to whatever</p>
 



* 🔥 **FAIL** <p>format the data is in, a TrueType or OpenType/CFF font file.</p>
 



* 🔥 **FAIL** <p>A special input value of - means read from the standard input.</p>
 



* 🔥 **FAIL** <p>Output files are created so they are unique: an existing file is</p>
 



* 🔥 **FAIL** <p>never overwritten.</p>
 



* 🔥 **FAIL** <p>General options</p>
 



* 🔥 **FAIL** <p>===============</p>
 



* 🔥 **FAIL** <p>-h Help            print this message.</p>
 



* 🔥 **FAIL** <p>--version          show version and exit.</p>
 



* 🔥 **FAIL** <p>-d <outputfolder>  Specify a directory where the output files are</p>
 



* 🔥 **FAIL** <p>to be created.</p>
 



* 🔥 **FAIL** <p>-o <outputfile>    Specify a file to write the output to. A special</p>
 



* 🔥 **FAIL** <p>value of - would use the standard output.</p>
 



* 🔥 **FAIL** <p>-f                 Overwrite existing output file(s), ie. don't append</p>
 



* 🔥 **FAIL** <p>numbers.</p>
 



* 🔥 **FAIL** <p>-v                 Verbose: more messages will be written to stdout</p>
 



* 🔥 **FAIL** <p>about what is being done.</p>
 



* 🔥 **FAIL** <p>-q                 Quiet: No messages will be written to stdout about</p>
 



* 🔥 **FAIL** <p>what is being done.</p>
 



* 🔥 **FAIL** <p>-a                 allow virtual glyphs ID's on compile or decompile.</p>
 



* 🔥 **FAIL** <p>Dump options</p>
 



* 🔥 **FAIL** <p>============</p>
 



* 🔥 **FAIL** <p>-l           List table info: instead of dumping to a TTX file, list</p>
 



* 🔥 **FAIL** <p>some minimal info about each table.</p>
 



* 🔥 **FAIL** <p>-t <table>   Specify a table to dump. Multiple -t options</p>
 



* 🔥 **FAIL** <p>are allowed. When no -t option is specified, all tables</p>
 



* 🔥 **FAIL** <p>will be dumped.</p>
 



* 🔥 **FAIL** <p>-x <table>   Specify a table to exclude from the dump. Multiple</p>
 



* 🔥 **FAIL** <p>-x options are allowed. -t and -x are mutually exclusive.</p>
 



* 🔥 **FAIL** <p>-s           Split tables: save the TTX data into separate TTX files per</p>
 



* 🔥 **FAIL** <p>table and write one small TTX file that contains references</p>
 



* 🔥 **FAIL** <p>to the individual table dumps. This file can be used as</p>
 



* 🔥 **FAIL** <p>input to ttx, as long as the table files are in the</p>
 



* 🔥 **FAIL** <p>same directory.</p>
 



* 🔥 **FAIL** <p>-g           Split glyf table: Save the glyf data into separate TTX files</p>
 



* 🔥 **FAIL** <p>per glyph and write a small TTX for the glyf table which</p>
 



* 🔥 **FAIL** <p>contains references to the individual TTGlyph elements.</p>
 



* 🔥 **FAIL** <p>NOTE: specifying -g implies -s (no need for -s together</p>
 



* 🔥 **FAIL** <p>with -g)</p>
 



* 🔥 **FAIL** <p>-i           Do NOT disassemble TT instructions: when this option is</p>
 



* 🔥 **FAIL** <p>given, all TrueType programs (glyph programs, the font</p>
 



* 🔥 **FAIL** <p>program and the pre-program) will be written to the TTX</p>
 



* 🔥 **FAIL** <p>file as hex data instead of assembly. This saves some time</p>
 



* 🔥 **FAIL** <p>and makes the TTX file smaller.</p>
 



* 🔥 **FAIL** <p>-z <format>  Specify a bitmap data export option for EBDT:</p>
 



* 🔥 **FAIL** <p>{'raw', 'row', 'bitwise', 'extfile'} or for the CBDT:</p>
 



* 🔥 **FAIL** <p>{'raw', 'extfile'} Each option does one of the following:</p>
 



* 🔥 **FAIL** <p>-z raw</p>
 



* 🔥 **FAIL** <p>export the bitmap data as a hex dump</p>
 



* 🔥 **FAIL** <p>-z row</p>
 



* 🔥 **FAIL** <p>export each row as hex data</p>
 



* 🔥 **FAIL** <p>-z bitwise</p>
 



* 🔥 **FAIL** <p>export each row as binary in an ASCII art style</p>
 



* 🔥 **FAIL** <p>-z extfile</p>
 



* 🔥 **FAIL** <p>export the data as external files with XML references</p>
 



* 🔥 **FAIL** <p>If no export format is specified 'raw' format is used.</p>
 



* 🔥 **FAIL** <p>-e           Don't ignore decompilation errors, but show a full traceback</p>
 



* 🔥 **FAIL** <p>and abort.</p>
 



* 🔥 **FAIL** <p>-y <number>  Select font number for TrueType Collection (.ttc/.otc),</p>
 



* 🔥 **FAIL** <p>starting from 0.</p>
 



* 🔥 **FAIL** <p>--unicodedata &lt;UnicodeData.txt&gt;</p>
 



* 🔥 **FAIL** <p>Use custom database file to write character names in the</p>
 



* 🔥 **FAIL** <p>comments of the cmap TTX output.</p>
 



* 🔥 **FAIL** <p>--newline <value></p>
 



* 🔥 **FAIL** <p>Control how line endings are written in the XML file. It</p>
 



* 🔥 **FAIL** <p>can be 'LF', 'CR', or 'CRLF'. If not specified, the</p>
 



* 🔥 **FAIL** <p>default platform-specific line endings are used.</p>
 



* 🔥 **FAIL** <p>Compile options</p>
 



* 🔥 **FAIL** <p>-m           Merge with TrueType-input-file: specify a TrueType or</p>
 



* 🔥 **FAIL** <p>OpenType font file to be merged with the TTX file. This</p>
 



* 🔥 **FAIL** <p>option is only valid when at most one TTX file is specified.</p>
 



* 🔥 **FAIL** <p>-b           Don't recalc glyph bounding boxes: use the values in the</p>
 



* 🔥 **FAIL** <p>TTX file as-is.</p>
 



* 🔥 **FAIL** <p>--recalc-timestamp</p>
 



* 🔥 **FAIL** <p>Set font 'modified' timestamp to current time.</p>
 



* 🔥 **FAIL** <p>By default, the modification time of the TTX file will be</p>
 



* 🔥 **FAIL** <p>used.</p>
 



* 🔥 **FAIL** <p>--no-recalc-timestamp</p>
 



* 🔥 **FAIL** <p>Keep the original font 'modified' timestamp.</p>
 



* 🔥 **FAIL** <p>--flavor <type></p>
 



* 🔥 **FAIL** <p>Specify flavor of output font file. May be 'woff' or 'woff2'.</p>
 



* 🔥 **FAIL** <p>Note that WOFF2 requires the Brotli Python extension,</p>
 



* 🔥 **FAIL** <p>available at <a href="https://github.com/google/brotli">https://github.com/google/brotli</a></p>
 



* 🔥 **FAIL** <p>--with-zopfli</p>
 



* 🔥 **FAIL** <p>Use Zopfli instead of Zlib to compress WOFF. The Python</p>
 



* 🔥 **FAIL** <p>extension is available at <a href="https://pypi.python.org/pypi/zopfli">https://pypi.python.org/pypi/zopfli</a></p>
 



* 🔥 **FAIL** <p>--optimize-font-speed</p>
 



* 🔥 **FAIL** <p>Enable optimizations that prioritize speed over file size.</p>
 



* 🔥 **FAIL** <p>This mainly affects how glyf t able and gvar / VARC tables are</p>
 



* 🔥 **FAIL** <p>compiled. The produced fonts will be larger, but rendering</p>
 



* 🔥 **FAIL** <p>performance will be improved with HarfBuzz and other text</p>
 



* 🔥 **FAIL** <p>layout engines.</p>
 



* 🔥 **FAIL** <p>ERROR: File not found: &quot;fonts/variable/DotZero[wght].ttf&quot;</p>
 



* 🔥 **FAIL** <h1>TTX had some problem parsing the generated XML file. This most likely mean there's some problem in the font. Please inspect the output of ttx in order to find more on what went wrong. A common problem is the presence of control characteres outside the accepted character range as defined in the XML spec. FontTools has got a bug which causes TTX to generate corrupt XML files in those cases. So, check the entries of the name table and remove any control chars that you find there. The full ttx error message was:</h1>
<p>usage: ttx [options] inputfile1 [... inputfileN]</p>
<p>TTX -- From OpenType To XML And Back</p>
<p>If an input file is a TrueType or OpenType font file, it will be
decompiled to a TTX file (an XML-based text format).
If an input file is a TTX file, it will be compiled to whatever
format the data is in, a TrueType or OpenType/CFF font file.
A special input value of - means read from the standard input.</p>
<p>Output files are created so they are unique: an existing file is
never overwritten.</p>
<h1>General options</h1>
<p>-h Help            print this message.
--version          show version and exit.
-d <outputfolder>  Specify a directory where the output files are
to be created.
-o <outputfile>    Specify a file to write the output to. A special
value of - would use the standard output.
-f                 Overwrite existing output file(s), ie. don't append
numbers.
-v                 Verbose: more messages will be written to stdout
about what is being done.
-q                 Quiet: No messages will be written to stdout about
what is being done.
-a                 allow virtual glyphs ID's on compile or decompile.</p>
<h1>Dump options</h1>
<p>-l           List table info: instead of dumping to a TTX file, list
some minimal info about each table.
-t <table>   Specify a table to dump. Multiple -t options
are allowed. When no -t option is specified, all tables
will be dumped.
-x <table>   Specify a table to exclude from the dump. Multiple
-x options are allowed. -t and -x are mutually exclusive.
-s           Split tables: save the TTX data into separate TTX files per
table and write one small TTX file that contains references
to the individual table dumps. This file can be used as
input to ttx, as long as the table files are in the
same directory.
-g           Split glyf table: Save the glyf data into separate TTX files
per glyph and write a small TTX for the glyf table which
contains references to the individual TTGlyph elements.
NOTE: specifying -g implies -s (no need for -s together
with -g)
-i           Do NOT disassemble TT instructions: when this option is
given, all TrueType programs (glyph programs, the font
program and the pre-program) will be written to the TTX
file as hex data instead of assembly. This saves some time
and makes the TTX file smaller.
-z <format>  Specify a bitmap data export option for EBDT:
{'raw', 'row', 'bitwise', 'extfile'} or for the CBDT:
{'raw', 'extfile'} Each option does one of the following:</p>
<pre><code>         -z raw
           export the bitmap data as a hex dump
         -z row
           export each row as hex data
         -z bitwise
           export each row as binary in an ASCII art style
         -z extfile
           export the data as external files with XML references

         If no export format is specified 'raw' format is used.
</code></pre>
<p>-e           Don't ignore decompilation errors, but show a full traceback
and abort.
-y <number>  Select font number for TrueType Collection (.ttc/.otc),
starting from 0.
--unicodedata &lt;UnicodeData.txt&gt;
Use custom database file to write character names in the
comments of the cmap TTX output.
--newline <value>
Control how line endings are written in the XML file. It
can be 'LF', 'CR', or 'CRLF'. If not specified, the
default platform-specific line endings are used.</p>
<h1>Compile options</h1>
<p>-m           Merge with TrueType-input-file: specify a TrueType or
OpenType font file to be merged with the TTX file. This
option is only valid when at most one TTX file is specified.
-b           Don't recalc glyph bounding boxes: use the values in the
TTX file as-is.
--recalc-timestamp
Set font 'modified' timestamp to current time.
By default, the modification time of the TTX file will be
used.
--no-recalc-timestamp
Keep the original font 'modified' timestamp.
--flavor <type>
Specify flavor of output font file. May be 'woff' or 'woff2'.
Note that WOFF2 requires the Brotli Python extension,
available at <a href="https://github.com/google/brotli">https://github.com/google/brotli</a>
--with-zopfli
Use Zopfli instead of Zlib to compress WOFF. The Python
extension is available at <a href="https://pypi.python.org/pypi/zopfli">https://pypi.python.org/pypi/zopfli</a>
--optimize-font-speed
Enable optimizations that prioritize speed over file size.
This mainly affects how glyf t able and gvar / VARC tables are
compiled. The produced fonts will be larger, but rendering
performance will be improved with HarfBuzz and other text
layout engines.</p>
<p>ERROR: Unknown file type: &quot;/tmp/tmp611jooc_&quot;</p>
<p>======</p>
 



* 🔥 **FAIL** <p>usage: ttx [options] inputfile1 [... inputfileN]</p>
 



* 🔥 **FAIL**  



* 🔥 **FAIL** <p>TTX -- From OpenType To XML And Back</p>
 



* 🔥 **FAIL** <p>If an input file is a TrueType or OpenType font file, it will be</p>
 



* 🔥 **FAIL** <p>decompiled to a TTX file (an XML-based text format).</p>
 



* 🔥 **FAIL** <p>If an input file is a TTX file, it will be compiled to whatever</p>
 



* 🔥 **FAIL** <p>format the data is in, a TrueType or OpenType/CFF font file.</p>
 



* 🔥 **FAIL** <p>A special input value of - means read from the standard input.</p>
 



* 🔥 **FAIL** <p>Output files are created so they are unique: an existing file is</p>
 



* 🔥 **FAIL** <p>never overwritten.</p>
 



* 🔥 **FAIL** <p>General options</p>
 



* 🔥 **FAIL** <p>===============</p>
 



* 🔥 **FAIL** <p>-h Help            print this message.</p>
 



* 🔥 **FAIL** <p>--version          show version and exit.</p>
 



* 🔥 **FAIL** <p>-d <outputfolder>  Specify a directory where the output files are</p>
 



* 🔥 **FAIL** <p>to be created.</p>
 



* 🔥 **FAIL** <p>-o <outputfile>    Specify a file to write the output to. A special</p>
 



* 🔥 **FAIL** <p>value of - would use the standard output.</p>
 



* 🔥 **FAIL** <p>-f                 Overwrite existing output file(s), ie. don't append</p>
 



* 🔥 **FAIL** <p>numbers.</p>
 



* 🔥 **FAIL** <p>-v                 Verbose: more messages will be written to stdout</p>
 



* 🔥 **FAIL** <p>about what is being done.</p>
 



* 🔥 **FAIL** <p>-q                 Quiet: No messages will be written to stdout about</p>
 



* 🔥 **FAIL** <p>what is being done.</p>
 



* 🔥 **FAIL** <p>-a                 allow virtual glyphs ID's on compile or decompile.</p>
 



* 🔥 **FAIL** <p>Dump options</p>
 



* 🔥 **FAIL** <p>============</p>
 



* 🔥 **FAIL** <p>-l           List table info: instead of dumping to a TTX file, list</p>
 



* 🔥 **FAIL** <p>some minimal info about each table.</p>
 



* 🔥 **FAIL** <p>-t <table>   Specify a table to dump. Multiple -t options</p>
 



* 🔥 **FAIL** <p>are allowed. When no -t option is specified, all tables</p>
 



* 🔥 **FAIL** <p>will be dumped.</p>
 



* 🔥 **FAIL** <p>-x <table>   Specify a table to exclude from the dump. Multiple</p>
 



* 🔥 **FAIL** <p>-x options are allowed. -t and -x are mutually exclusive.</p>
 



* 🔥 **FAIL** <p>-s           Split tables: save the TTX data into separate TTX files per</p>
 



* 🔥 **FAIL** <p>table and write one small TTX file that contains references</p>
 



* 🔥 **FAIL** <p>to the individual table dumps. This file can be used as</p>
 



* 🔥 **FAIL** <p>input to ttx, as long as the table files are in the</p>
 



* 🔥 **FAIL** <p>same directory.</p>
 



* 🔥 **FAIL** <p>-g           Split glyf table: Save the glyf data into separate TTX files</p>
 



* 🔥 **FAIL** <p>per glyph and write a small TTX for the glyf table which</p>
 



* 🔥 **FAIL** <p>contains references to the individual TTGlyph elements.</p>
 



* 🔥 **FAIL** <p>NOTE: specifying -g implies -s (no need for -s together</p>
 



* 🔥 **FAIL** <p>with -g)</p>
 



* 🔥 **FAIL** <p>-i           Do NOT disassemble TT instructions: when this option is</p>
 



* 🔥 **FAIL** <p>given, all TrueType programs (glyph programs, the font</p>
 



* 🔥 **FAIL** <p>program and the pre-program) will be written to the TTX</p>
 



* 🔥 **FAIL** <p>file as hex data instead of assembly. This saves some time</p>
 



* 🔥 **FAIL** <p>and makes the TTX file smaller.</p>
 



* 🔥 **FAIL** <p>-z <format>  Specify a bitmap data export option for EBDT:</p>
 



* 🔥 **FAIL** <p>{'raw', 'row', 'bitwise', 'extfile'} or for the CBDT:</p>
 



* 🔥 **FAIL** <p>{'raw', 'extfile'} Each option does one of the following:</p>
 



* 🔥 **FAIL** <p>-z raw</p>
 



* 🔥 **FAIL** <p>export the bitmap data as a hex dump</p>
 



* 🔥 **FAIL** <p>-z row</p>
 



* 🔥 **FAIL** <p>export each row as hex data</p>
 



* 🔥 **FAIL** <p>-z bitwise</p>
 



* 🔥 **FAIL** <p>export each row as binary in an ASCII art style</p>
 



* 🔥 **FAIL** <p>-z extfile</p>
 



* 🔥 **FAIL** <p>export the data as external files with XML references</p>
 



* 🔥 **FAIL** <p>If no export format is specified 'raw' format is used.</p>
 



* 🔥 **FAIL** <p>-e           Don't ignore decompilation errors, but show a full traceback</p>
 



* 🔥 **FAIL** <p>and abort.</p>
 



* 🔥 **FAIL** <p>-y <number>  Select font number for TrueType Collection (.ttc/.otc),</p>
 



* 🔥 **FAIL** <p>starting from 0.</p>
 



* 🔥 **FAIL** <p>--unicodedata &lt;UnicodeData.txt&gt;</p>
 



* 🔥 **FAIL** <p>Use custom database file to write character names in the</p>
 



* 🔥 **FAIL** <p>comments of the cmap TTX output.</p>
 



* 🔥 **FAIL** <p>--newline <value></p>
 



* 🔥 **FAIL** <p>Control how line endings are written in the XML file. It</p>
 



* 🔥 **FAIL** <p>can be 'LF', 'CR', or 'CRLF'. If not specified, the</p>
 



* 🔥 **FAIL** <p>default platform-specific line endings are used.</p>
 



* 🔥 **FAIL** <p>Compile options</p>
 



* 🔥 **FAIL** <p>-m           Merge with TrueType-input-file: specify a TrueType or</p>
 



* 🔥 **FAIL** <p>OpenType font file to be merged with the TTX file. This</p>
 



* 🔥 **FAIL** <p>option is only valid when at most one TTX file is specified.</p>
 



* 🔥 **FAIL** <p>-b           Don't recalc glyph bounding boxes: use the values in the</p>
 



* 🔥 **FAIL** <p>TTX file as-is.</p>
 



* 🔥 **FAIL** <p>--recalc-timestamp</p>
 



* 🔥 **FAIL** <p>Set font 'modified' timestamp to current time.</p>
 



* 🔥 **FAIL** <p>By default, the modification time of the TTX file will be</p>
 



* 🔥 **FAIL** <p>used.</p>
 



* 🔥 **FAIL** <p>--no-recalc-timestamp</p>
 



* 🔥 **FAIL** <p>Keep the original font 'modified' timestamp.</p>
 



* 🔥 **FAIL** <p>--flavor <type></p>
 



* 🔥 **FAIL** <p>Specify flavor of output font file. May be 'woff' or 'woff2'.</p>
 



* 🔥 **FAIL** <p>Note that WOFF2 requires the Brotli Python extension,</p>
 



* 🔥 **FAIL** <p>available at <a href="https://github.com/google/brotli">https://github.com/google/brotli</a></p>
 



* 🔥 **FAIL** <p>--with-zopfli</p>
 



* 🔥 **FAIL** <p>Use Zopfli instead of Zlib to compress WOFF. The Python</p>
 



* 🔥 **FAIL** <p>extension is available at <a href="https://pypi.python.org/pypi/zopfli">https://pypi.python.org/pypi/zopfli</a></p>
 



* 🔥 **FAIL** <p>--optimize-font-speed</p>
 



* 🔥 **FAIL** <p>Enable optimizations that prioritize speed over file size.</p>
 



* 🔥 **FAIL** <p>This mainly affects how glyf t able and gvar / VARC tables are</p>
 



* 🔥 **FAIL** <p>compiled. The produced fonts will be larger, but rendering</p>
 



* 🔥 **FAIL** <p>performance will be improved with HarfBuzz and other text</p>
 



* 🔥 **FAIL** <p>layout engines.</p>
 



* 🔥 **FAIL** <p>ERROR: Unknown file type: &quot;/tmp/tmp611jooc_&quot;</p>
 







</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-avar-table">mandatory_avar_table</a></summary>
    <div>


> 
> Most variable fonts should include an avar table to correctly define
> axes progression rates.
> 
> For example, a weight axis from 0% to 100% doesn't map directly to 100 to 1000,
> because a 10% progression from 0% may be too much to define the 200,
> while 90% may be too little to define the 900.
> 
> If the progression rates of axes is linear, this check can be ignored.
> Fontmake will also skip adding an avar table if the progression rates
> are linear. However, it is still recommended that designers visually proof
> each instance is at the expected weight, width etc.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3100





* ⚠️ **WARN** <p>This variable font does not have an avar table. Most variable fonts should include an avar table to correctly define axes progression rates.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* uni2599 (U+2599): L&lt;&lt;0.0,385.0&gt;--&lt;330.0,385.0&gt;&gt; has the same coordinates as a previous segment.

* uni2599 (U+2599): L&lt;&lt;330.0,-275.0&gt;--&lt;330.0,385.0&gt;&gt; has the same coordinates as a previous segment.

* uni259B (U+259B): L&lt;&lt;330.0,385.0&gt;--&lt;330.0,1045.0&gt;&gt; has the same coordinates as a previous segment.

* uni259B (U+259B): L&lt;&lt;0.0,385.0&gt;--&lt;330.0,385.0&gt;&gt; has the same coordinates as a previous segment.

* uni259C (U+259C): L&lt;&lt;330.0,385.0&gt;--&lt;330.0,1045.0&gt;&gt; has the same coordinates as a previous segment.

* uni259C (U+259C): L&lt;&lt;330.0,385.0&gt;--&lt;660.0,385.0&gt;&gt; has the same coordinates as a previous segment.

* uni259F (U+259F): L&lt;&lt;330.0,-275.0&gt;--&lt;330.0,385.0&gt;&gt; has the same coordinates as a previous segment.

* uni259F (U+259F): L&lt;&lt;330.0,385.0&gt;--&lt;660.0,385.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 4 | 0 | 6 | 8 | 43 | 6 | 175 | 0 | 
| 2% | 0% | 2% | 3% | 18% | 2% | 72% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
