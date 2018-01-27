# CrossStraitXML

## Description
CrossStraitXML is a tool written in python to convert an original Cross-strait Dictionary ([兩岸詞典](https://github.com/g0v/moedict-data-csld)) XLSX file to an XML dictionary file in the logical [XDXF format](https://github.com/soshial/xdxf_makedict/blob/master/format_standard/xdxf_description.md), which can be used with dictionary software that support this format.

## Screenshots
![Screenshot of XDXF Cross-strait Dictionary open on GoldenDict 1.5](https://github.com/k-sl/CrossStraitXML/blob/master/images/screenshot-b.png)
Screenshot of XDXF Cross-strait Dictionary with bopomofo transcriptions open on [GoldenDict](https://github.com/goldendict/goldendict) 1.5

![Screenshot of XDXF Cross-strait Dictionary open on GoldenDict 1.5](https://github.com/k-sl/CrossStraitXML/blob/master/images/screenshot-s.png)
Screenshot of XDXF Cross-strait Dictionary with text converted to simplified Chinese open on [GoldenDict](https://github.com/goldendict/goldendict) 1.5

## Dependencies
* [OpenCC](https://github.com/BYVoid/OpenCC) (for converting to simplified Chinese)
* Python packages:
    * [lxml](http://lxml.de/)
    * [tdqm](https://github.com/noamraph/tqdm)
    * [openpyxl](https://pypi.python.org/pypi/openpyxl)
    * [opencc](https://pypi.python.org/pypi/OpenCC)

## Usage
(Assuming Python 2.7 and all dependencies are installed and crossstraitxml.py and data.py are in the same folder:) Run the script on a folder with a Cross-strait Dictionary file (named “兩岸詞典.xlsx”) to convert it into an XDXF file with the default filename on the same folder, without bopomofo transcriptions. Optionally use one or several of the arguments below.

### Arguments
* `-i` or `--input-file`
The name (and location if not on the current folder) of the original Cross-strait XLSX file to be converted. The default is a file named “兩岸詞典.xlsx” on the current folder. E.g.:
```
python crossstraitxml.py -i ~/Downloads/NameOfLACFile.xlsx
```

* `-o` or `--output-file`
The name (and location if not on the current folder) of the resulting XDXF file. By default this will be “兩岸詞典_ + dictionary version + - + converter version + .xdxf”. E.g.:
```
python crossstraitxml.py -o ~/Dictionaries/XDXFFileName.xdxf
```

* `-b` or `--bopomofo`
Include bopomofo transcriptions. Pinyin transcriptions are always included.

* `-s` or `--simplified`
Convert the text of the definitions to simplified Chinese automatically. While most of the text should be correctly converted, automatic conversion is not perfect and mistakes will remain in the resulting file. The headwords are always included in both variants as they are included in the original file.

## Dictionary Files
Cross-strait Dictionary files in XDXF format converted with the most recent version of CrossStraitXML can be found [here](https://github.com/k-sl/CrossStraitXML/tree/master/XDXF%20LAC).

## Limitations
The XDXF format doesn't recognize transcriptions (such as pinyin). The pinyin transcription will be displayed on every entry, as pronunciation, but the entries are not searchable by pinyin. Hopefully this will be implemented in a future version of XDXF.

The XDXF format doesn't recognize different writing systems (such as traditional and simplified Chinese), as such both versions are always displayed, with no indication of which is which or option to display only one. Both versions are searchable, however. Hopefully this will be implemented in a future version of XDXF.

## Credits and Licenses
Cross-strait Dictionary (兩岸詞典) is licensed under a under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.

CrossStraitXML is not licensed or copyrighted, it is released into the public domain.
