# -*- coding: utf-8 -*-
"""This module consists of data for CrossStraitXML.py.

This module includes data needed for CrossStraitXML.py, namely abbreviations,
characters that were separated by radicals, and tables.
"""

abbreviations = [(u"【臺】", u"臺灣", ""), (u"〈口〉", u"口語", ""),
                 (u"【陸】", u"大陸", ""), (u"〈書〉", u"書面語", ""),
                 (u"〈諺〉", u"諺語", "")]
# One simplified character couldn't be found: （艹+带）.
simplified_separated = [(u"（口+恶）", u"𫫇"), (u"（齿+楚）", u"𬺓"),
                        (u"（王+粲）", u"璨"), (u"（山+历）", u"𫵷"),
                        (u"（亻+单）", u"𫢸"), (u"（兆+页）", u"𫖯"),
                        (u"（匽+鸟）", u"𬸘"), (u"（危+页）", u"𬱟"),
                        (u"（君+页）", u"𫖳"), (u"（土+仑）", u"𫭢"),
                        (u"（土+区）", u"𫭟"), (u"（土+单）", u"𫮃"),
                        (u"（土+娄）", u"𪣻"), (u"（齿+奇）", u"𬺈"),
                        (u"（女+𢀖）", u"𫰛"), (u"（学-子+石）", u"𬒈"),
                        (u"（寻+阝）", u"𬩽"), (u"（山+大+车）", u"𪨶"),
                        (u"（山+带）", u"𫶇"), (u"（齿+兒）", u"𫠜"),
                        (u"（山+献）", u"𪩘"), (u"（岂+页）", u"𫖮"),
                        (u"（广+钦）", u"𫷷"), (u"（弓+区）", u"𫸩"),
                        (u"（支+页）", u"𫠆"), (u"（族+鸟）", u"𬸦"),
                        (u"（既+鱼）", u"𬶨"), (u"（日+见）", u"𬀪"),
                        (u"（日+韦）", u"𬀩"), (u"（木+夹）", u"𬂩"),
                        (u"（木+质）", u"𬃊"), (u"（此+鱼）", u"𫚖"),
                        (u"（氵+万）", u"𬇕"), (u"（氵+国）", u"𬇹"),
                        (u"（氵+贝）", u"𬇙"), (u"（汤+玉）", u"𬍡"),
                        (u"（火+区）", u"𬉼"), (u"（火+单）", u"𬊤"),
                        (u"（火+寻）", u"𬊈"), (u"（狂+鸟）", u"𫛭"),
                        (u"（狱+鸟）", u"𬸚"), (u"（王+乐）", u"𬍛"),
                        (u"（王+寻）", u"𬍤"), (u"（甫+鸟）", u"𬷕"),
                        (u"（由+页）", u"𬱖"), (u"（番+鸟）", u"𬸪"),
                        (u"（目+见）", u"𪾢"), (u"（石+览）", u"𬒗"),
                        (u"（𥫗+贡）", u"𬕂"), (u"（纟+享）", u"𬘯"),
                        (u"（纟+京）", u"𫟅"), (u"（纟+冘）", u"𬘘"),
                        (u"（纟+因）", u"𬘡"), (u"（纟+完）", u"𬘫"),
                        (u"（纟+寅）", u"𬙂"), (u"（纟+川）", u"𬘓"),
                        (u"（纟+希）", u"𫄨"), (u"（纟+延）", u"𫄧"),
                        (u"（纟+廷）", u"𬘩"), (u"（纟+意）", u"𫄷"),
                        (u"（纟+林）", u"𬘭"), (u"（纟+熏）", u"𫄸"),
                        (u"（纟+襄）", u"𬙋"), (u"（纟+青）", u"𬘬"),
                        (u"（纟+墨）", u"𬙊"), (u"（艹+为）", u"𫇭"),
                        (u"（艹+问）", u"𬜬"), (u"（艹+频）", u"𬞟"),
                        (u"（艹+鹝）", u"𬟁"), (u"（虫+东）", u"𬟽"),
                        (u"（螨-虫+王）", u"𫞩"), (u"（衤+责）", u"𫌀"),
                        (u"（讠+于）", u"𬣙"), (u"（讠+叟）", u"𫍲"),
                        (u"（讠+同）", u"𫍣"), (u"（讠+咸）", u"𫍯"),
                        (u"（讠+垔）", u"𬤇"), (u"（讠+㝉）", u"𬣞"),
                        (u"（讠+惠）", u"𬤝"), (u"（讠+戋）", u"𬣡"),
                        (u"（讠+是）", u"𬤊"), (u"（讠+睘）", u"𫍽"),
                        (u"（讠+艮）", u"𬣳"), (u"（责+力）", u"𪟝"),
                        (u"（赛-贝+鸟）", u"𬸣"), (u"（车+兀）", u"𫐄"),
                        (u"（车+兒）", u"𫐐"), (u"（车+柔）", u"𫐓"),
                        (u"（车+氏）", u"𬨂"), (u"（车+贲）", u"𮝷"),
                        (u"（车+酋）", u"𬨎"), (u"（酉+农）", u"𬪩"),
                        (u"（钅+享）", u"𬭚"), (u"（钅+仑）", u"𬬭"),
                        (u"（钅+侯）", u"𬭤"), (u"（钅+共）", u"𫟹"),
                        (u"（钅+其）", u"𫓹"), (u"（钅+卢）", u"𬬻"),
                        (u"（钅+召）", u"𬬿"), (u"（钅+喜）", u"𬭳"),
                        (u"（钅+圭）", u"𫓯"), (u"（钅+夫）", u"𫓧"),
                        (u"（钅+宏）", u"𬭎"), (u"（钅+弋）", u"𬬩"),
                        (u"（钅+彗）", u"𬭬"), (u"（钅+敝）", u"𬭯"),
                        (u"（钅+斤）", u"𬬱"), (u"（钅+术）", u"𬬸"),
                        (u"（钅+杜）", u"𬭊"), (u"（钅+母）", u"𬭁"),
                        (u"（钅+波）", u"𬭛"), (u"（钅+申）", u"𬬹"),
                        (u"（钅+番）", u"𫔍"), (u"（钅+矞）", u"𫔎"),
                        (u"（钅+粦）", u"𬭸"), (u"（钅+翁）", u"𬭩"),
                        (u"（钅+肙）", u"𫓶"), (u"（钅+达）", u"𫟼"),
                        (u"（钅+遂）", u"𬭼"), (u"（钅+长）", u"𬬮"),
                        (u"（钅+麦）", u"鿏"), (u"（钅+黑）", u"𬭶"),
                        (u"（门+垔）", u"𬮱"), (u"（门+臬）", u"𫔶"),
                        (u"（阝+岂）", u"𬮿"), (u"（阝+贵）", u"𬯎"),
                        (u"（饣+亶）", u"𫗴"), (u"（饣+束）", u"𫗧"),
                        (u"（马+丕）", u"𬳵"), (u"（马+余）", u"𬳿"),
                        (u"（马+先）", u"𬳽"), (u"（马+冋）", u"𬳶"),
                        (u"（马+匋）", u"𫘦"), (u"（马+原）", u"𫘪"),
                        (u"（马+夬）", u"𫘝"), (u"（马+奚）", u"𫘬"),
                        (u"（马+录）", u"𫘧"), (u"（马+文）", u"𫘜"),
                        (u"（马+是）", u"𫘨"), (u"（马+玄）", u"𫠊"),
                        (u"（阝+齐）", u"𬯀"), (u"（马+砉）", u"𬴃"),
                        (u"（马+粦）", u"𬴊"), (u"（鱼+兆）", u"𬶐"),
                        (u"（鱼+剌）", u"𬶟"), (u"（鱼+危）", u"𬶏"),
                        (u"（鱼+句）", u"𬶋"), (u"（鱼+喜）", u"𬶮"),
                        (u"（鱼+它）", u"𬶍"), (u"（鱼+巤）", u"𫚭"),
                        (u"（鱼+师）", u"𫚕"), (u"（鱼+柬）", u"𬶠"),
                        (u"（鱼+祭）", u"𬶭"), (u"（黾+阝）", u"𫑡"),
                        (u"（齿+介）", u"𬹼"), (u"（木+规）", u"𬃀")]
# One character couldn't be found: （土+夅）.
both_separated = [(u"（土+翏）", u"𪤗"), (u"（山+曲）", u"𪨰"),
                  (u"（牙+合）", u"𬌗"), (u"（石+肯）", u"𬒔")]
# There are only two HTML tables in the dictionary. XDXF doesn't support
# tables, a table with <br/> newlines in a <pre> tag works with Goldendict,
# for some unknown reason, it might (and should) not work everywhere.

tables = [(u"""<table style="border: 1px solid #000000; border-collapse: collapse; padding: 2px;">    <tr>        <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; word-spacing: normal; font-weight: bold;">方位</td>        <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; word-spacing: normal; font-weight: bold;">星宿名</td>        <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; word-spacing: normal; font-weight: bold;">說明</td>    </tr>    <tr>        <td rowspan="7" style="border: 1px solid #000000; text-align: center; white-space: nowrap; vertical-align: top; font-weight: bold;">東方青龍七宿</td>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">角宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">東方青龍的第一宿，有二顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">亢宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">東方青龍的第二宿，有四顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">氐宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">東方青龍的第三宿，有四顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">房宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">東方青龍的第四宿，有四顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">心宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">東方青龍的第五宿，有三顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">尾宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">東方青龍的第六宿，有九顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">箕宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">東方青龍的第七宿，有四顆星。</td>    </tr>    <tr>        <td rowspan="7" style="border: 1px solid #000000; text-align: center; white-space: nowrap; vertical-align: top; font-weight: bold;">西方白虎七宿</td>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">奎宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">西方白虎的第一宿，有十六顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">婁宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">西方白虎的第二宿，有三顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">胃宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">西方白虎的第三宿，有三顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">昴宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">西方白虎的第四宿，有七顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">畢宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">西方白虎的第五宿，有八顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">觜宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">西方白虎的第六宿，有三顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">參宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">西方白虎的第七宿，有七顆星。</td>    </tr>    <tr>        <td rowspan="7" style="border: 1px solid #000000; text-align: center; white-space: nowrap; vertical-align: top; font-weight: bold;">南方朱雀七宿</td>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">井宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">南方朱雀七宿的第一宿，有八顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">鬼宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">南方朱雀七宿的第二宿，有四顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">柳宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">南方朱雀七宿的第三宿，有八顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">星宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">南方朱雀七宿的第四宿，有七顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">張宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">南方朱雀七宿的第五宿，有六顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">翼宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">南方朱雀七宿的第六宿，有二十二顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">軫宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">南方朱雀七宿的第七宿，有四顆星。</td>    </tr>    <tr>        <td rowspan="7" style="border: 1px solid #000000; text-align: center; white-space: nowrap; vertical-align: top; font-weight: bold;">北方玄武七宿</td>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">斗宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">北方玄武的第一宿，有六顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">牛宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">北方玄武的第二宿，有六顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">女宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">北方玄武的第三宿，有四顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">虛宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">北方玄武的第四宿，有二顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">危宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">北方玄武的第五宿，有三顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">室宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">北方玄武的第六宿，有二顆星。</td>    </tr>    <tr>        <td style="font-size: 12pt; border: 1px solid #000000; text-align: center;">壁宿</td>        <td style="font-size: 12pt; border: 1px solid #000000;">北方玄武的第七宿，原有二顆星，後增為二十三顆。</td>    </tr></table>""",
           u"""_lt_pre_mt_+--------------+--------+------------------------------------------------+_lt_br/_mt_
           | 方位          | 星宿名  | 說明                                           |_lt_br/_mt_
           +--------------+--------+------------------------------------------------+_lt_br/_mt_
           | 東方青龍七宿   | 角宿    | 東方青龍的第一宿，有二顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 亢宿    | 東方青龍的第二宿，有四顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 氐宿    | 東方青龍的第三宿，有四顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 房宿    | 東方青龍的第四宿，有四顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 心宿    | 東方青龍的第五宿，有三顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 尾宿    | 東方青龍的第六宿，有九顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 箕宿    | 東方青龍的第七宿，有四顆星。                       |_lt_br/_mt_
           +--------------+--------+------------------------------------------------+_lt_br/_mt_
           | 西方白虎七宿   | 奎宿    | 西方白虎的第一宿，有十六顆星。                      |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 婁宿    | 西方白虎的第二宿，有三顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 胃宿    | 西方白虎的第三宿，有三顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 昴宿    | 西方白虎的第四宿，有七顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 畢宿    | 西方白虎的第五宿，有八顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 觜宿    | 西方白虎的第六宿，有三顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 參宿    | 西方白虎的第七宿，有七顆星。                       |_lt_br/_mt_
           +--------------+--------+------------------------------------------------+_lt_br/_mt_
           | 南方朱雀七宿   | 井宿    | 南方朱雀七宿的第一宿，有八顆星。                    |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 鬼宿    | 南方朱雀七宿的第二宿，有四顆星。                    |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 柳宿    | 南方朱雀七宿的第三宿，有八顆星。                    |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 星宿    | 南方朱雀七宿的第四宿，有七顆星。                    |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 張宿    | 南方朱雀七宿的第五宿，有六顆星。                    |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 翼宿    | 南方朱雀七宿的第六宿，有二十二顆星。                 |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 軫宿    | 南方朱雀七宿的第七宿，有四顆星。                    |_lt_br/_mt_
           +--------------+--------+------------------------------------------------+_lt_br/_mt_
           | 北方玄武七宿   | 斗宿    | 北方玄武的第一宿，有六顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 牛宿    | 北方玄武的第二宿，有六顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 女宿    | 北方玄武的第三宿，有四顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 虛宿    | 北方玄武的第四宿，有二顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 危宿    | 北方玄武的第五宿，有三顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 室宿    | 北方玄武的第六宿，有二顆星。                       |_lt_br/_mt_
           +              +--------+------------------------------------------------+_lt_br/_mt_
           |              | 壁宿    | 北方玄武的第七宿，原有二顆星，後增為二十三顆。        |_lt_br/_mt_
           +--------------+--------+------------------------------------------------+_lt_/pre_mt_"""),
          (u"""<table style="border: 1px solid #000000; border-collapse: collapse; padding: 2px">      <tr>          <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; font-weight:bold">季別</td>          <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; font-weight:bold">節氣名</td>          <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; font-weight:bold">陽曆日期</td>          <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; font-weight:bold">農曆節氣</td>          <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; font-weight:bold">相關事項</td>      </tr>      <tr>          <td rowspan="6" style="border: 1px solid #000000; text-align: center;">春</td>          <td style="border: 1px solid #000000; text-align: center;">立春</td>          <td style="border: 1px solid #000000; white-space: nowrap">2月3日至5日</td>          <td style="border: 1px solid #000000;">正月節氣</td>          <td style="border: 1px solid #000000;">一般習俗以立春日為春季之始。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">雨水</td>          <td style="border: 1px solid #000000; white-space: nowrap">2月18日至20日</td>          <td style="border: 1px solid #000000;">正月中氣</td>          <td style="border: 1px solid #000000;">雨量漸豐，氣溫回暖，適合春耕。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">驚蟄</td>          <td style="border: 1px solid #000000; white-space: nowrap">3月5日至7日</td>          <td style="border: 1px solid #000000;">2月節氣</td>          <td style="border: 1px solid #000000;">冬眠動物開始活動。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">春分</td>          <td style="border: 1px solid #000000; white-space: nowrap">3月20日至22日</td>          <td style="border: 1px solid #000000;">2月中氣</td>          <td style="border: 1px solid #000000;">太陽直射赤道，晝夜平均，之後，北半球晝漸長。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">清明</td>          <td style="border: 1px solid #000000; white-space: nowrap">4月4日至6日</td>          <td style="border: 1px solid #000000;">3月節氣</td>          <td style="border: 1px solid #000000;">民間有掃墓祭祖習俗。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">穀雨</td>          <td style="border: 1px solid #000000; white-space: nowrap">4月19日至21日</td>          <td style="border: 1px solid #000000;">3月中氣</td>          <td style="border: 1px solid #000000;">大部分地區降雨量增加，有利於種植。</td>      </tr>      <tr>          <td rowspan="6" style="border: 1px solid #000000; text-align: center;">夏</td>          <td style="border: 1px solid #000000; text-align: center;">立夏</td>          <td style="border: 1px solid #000000; white-space: nowrap">5月5日至7日</td>          <td style="border: 1px solid #000000;">4月節氣</td>          <td style="border: 1px solid #000000;">一般習俗以立夏日為夏季之始。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">小滿</td>          <td style="border: 1px solid #000000; white-space: nowrap">5月20日至22日</td>          <td style="border: 1px solid #000000;">4月中氣</td>          <td style="border: 1px solid #000000;">穀物生長已近盈滿。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">芒種</td>          <td style="border: 1px solid #000000; white-space: nowrap">6月5日至7日</td>          <td style="border: 1px solid #000000;">5月節氣</td>          <td style="border: 1px solid #000000;">穀物芒花盛開；大部分地區忙於夏收夏種。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">夏至</td>          <td style="border: 1px solid #000000; white-space: nowrap">6月21日至22日</td>          <td style="border: 1px solid #000000;">5月中氣</td>          <td style="border: 1px solid #000000;">北半球白晝最長，夜晚最短。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">小暑</td>          <td style="border: 1px solid #000000; white-space: nowrap">7月6日至8日</td>          <td style="border: 1px solid #000000;">6月節氣</td>          <td style="border: 1px solid #000000;">漸近最熱時節。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">大暑</td>          <td style="border: 1px solid #000000;">7月22日至24日</td>          <td style="border: 1px solid #000000;">6月中氣</td>          <td style="border: 1px solid #000000;">一年中大部分地區天氣最熱。</td>      </tr>      <tr>          <td rowspan="6" style="border: 1px solid #000000; text-align: center;">秋</td>          <td style="border: 1px solid #000000; text-align: center;">立秋</td>          <td style="border: 1px solid #000000; white-space: nowrap">8月7日至9日</td>          <td style="border: 1px solid #000000;">7月節氣</td>          <td style="border: 1px solid #000000;">一般習俗以立秋日為秋季之始。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">處暑</td>          <td style="border: 1px solid #000000; white-space: nowrap">8月22日至24日</td>          <td style="border: 1px solid #000000;">7月中氣</td>          <td style="border: 1px solid #000000;">此日後暑氣漸消。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">白露</td>          <td style="border: 1px solid #000000; white-space: nowrap">9月7日至9日</td>          <td style="border: 1px solid #000000;">8月節氣</td>          <td style="border: 1px solid #000000;">大部分地區天氣漸涼，大陸北部早晚凝結白露。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">秋分</td>          <td style="border: 1px solid #000000; white-space: nowrap">9月22日至24日</td>          <td style="border: 1px solid #000000;">8月中氣</td>          <td style="border: 1px solid #000000;">晝夜等長，之後，北半球夜漸長。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">寒露</td>          <td style="border: 1px solid #000000; white-space: nowrap">10月8日至9日</td>          <td style="border: 1px solid #000000;">9月節氣</td>          <td style="border: 1px solid #000000;">大陸秋寒多露，漸近霜降。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">霜降</td>          <td style="border: 1px solid #000000; white-space: nowrap">10月23日至24日</td>          <td style="border: 1px solid #000000;">9月中氣</td>          <td style="border: 1px solid #000000;">黃河流域出現初霜。</td>      </tr>      <tr>          <td rowspan="6" style="border: 1px solid #000000; text-align: center;">冬</td>          <td style="border: 1px solid #000000; text-align: center;">立冬</td>          <td style="border: 1px solid #000000; white-space: nowrap">11月7日至8日</td>          <td style="border: 1px solid #000000;">10月節氣</td>          <td style="border: 1px solid #000000;">一般習俗以立冬日為冬季之始。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">小雪</td>          <td style="border: 1px solid #000000; white-space: nowrap">11月22日至23日</td>          <td style="border: 1px solid #000000;">10月中氣</td>          <td style="border: 1px solid #000000;">黃河流域開始降少量雪。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">大雪</td>          <td style="border: 1px solid #000000; white-space: nowrap">12月6日至8日</td>          <td style="border: 1px solid #000000;">11月節氣</td>          <td style="border: 1px solid #000000;">黃河中下游地區常出現降雪。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">冬至</td>          <td style="border: 1px solid #000000; white-space: nowrap">12月21日至23日</td>          <td style="border: 1px solid #000000;">11月中氣</td>          <td style="border: 1px solid #000000;">北半球黑夜最長，白晝最短。應節食品為南湯圓、北餛飩。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">小寒</td>          <td style="border: 1px solid #000000; white-space: nowrap">1月5日至7日</td>          <td style="border: 1px solid #000000;">12月節氣</td>          <td style="border: 1px solid #000000;">漸近最冷時節。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">大寒</td>          <td style="border: 1px solid #000000; white-space: nowrap">1月20日至21日</td>          <td style="border: 1px solid #000000;">12月中氣</td>          <td style="border: 1px solid #000000;">一年中大部分地區天氣最冷。</td>      </tr>  </table></span>""",
           u"""_lt_pre_mt_+------+--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
| 季別  | 節氣名 | 陽曆日期       | 農曆節氣 | 相關事項                                               |_lt_br/_mt_
+------+--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  立春  | 2月3日至5日    | 正月節氣 | 一般習俗以立春日為春季之始。                              |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  雨水  | 2月18日至20日  | 正月中氣 | 雨量漸豐，氣溫回暖，適合春耕。                            |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|  春  |  驚蟄  | 3月5日至7日    | 2月節氣  | 冬眠動物開始活動。                                      |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  春分  | 3月20日至22日  | 2月中氣  | 太陽直射赤道，晝夜平均，之後，北半球晝漸長。                |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  清明  | 4月4日至6日    | 3月節氣  | 民間有掃墓祭祖習俗。                                    |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  穀雨  | 4月19日至21日  | 3月中氣  | 大部分地區降雨量增加，有利於種植。                         |_lt_br/_mt_
+------+--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  立夏  | 5月5日至7日    | 4月節氣  | 一般習俗以立夏日為夏季之始。                              |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  小滿  | 5月20日至22日  | 4月中氣  | 穀物生長已近盈滿。                                      |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|  夏  |  芒種  | 6月5日至7日    | 5月節氣  | 穀物芒花盛開；大部分地區忙於夏收夏種。                      |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  夏至  | 6月21日至22日  | 5月中氣  | 北半球白晝最長，夜晚最短。                               |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  小暑  | 7月6日至8日    | 6月節氣  | 漸近最熱時節。                                         |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  大暑  | 7月22日至24日  | 6月中氣  | 一年中大部分地區天氣最熱。                               |_lt_br/_mt_
+------+--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  立秋  | 8月7日至9日    | 7月節氣  | 一般習俗以立秋日為秋季之始。                              |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  處暑  | 8月22日至24日  | 7月中氣  | 此日後暑氣漸消。                                        |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|  秋  |  白露  | 9月7日至9日    | 8月節氣  | 大部分地區天氣漸涼，大陸北部早晚凝結白露。                  |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  秋分  | 9月22日至24日  | 8月中氣  | 晝夜等長，之後，北半球夜漸長。                            |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  寒露  | 10月8日至9日   | 9月節氣  | 大陸秋寒多露，漸近霜降。                                 |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  霜降  | 10月23日至24日 | 9月中氣  | 黃河流域出現初霜。                                      |_lt_br/_mt_
+------+--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  立冬  | 11月7日至8日   | 10月節氣 | 一般習俗以立冬日為冬季之始。                              |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  小雪  | 11月22日至23日 | 10月中氣 | 黃河流域開始降少量雪。                                   |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|  冬  |  大雪  | 12月6日至8日   | 11月節氣 | 黃河中下游地區常出現降雪。                                |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  冬至  | 12月21日至23日 | 11月中氣 | 北半球黑夜最長，白晝最短。應節食品為南湯圓、北餛飩。          |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  小寒  | 1月5日至7日    | 12月節氣 | 漸近最冷時節。                                         |_lt_br/_mt_
+      +--------+--------------+---------+------------------------------------------------------+_lt_br/_mt_
|      |  大寒  | 1月20日至21日  | 12月中氣 | 一年中大部分地區天氣最冷。                               |_lt_br/_mt_
+------+--------+--------------+---------+------------------------------------------------------+_lt_/pre_mt_"""),
          (u"""<table style="border: 1px solid #000000; border-collapse: collapse; padding: 2px">      <tr>          <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; font-weight:bold">季別</td>          <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; font-weight:bold">節氣名</td>          <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; font-weight:bold">陽曆日期</td>          <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; font-weight:bold">農曆節氣</td>          <td style="border: 1px solid #000000; text-align: center; white-space: nowrap; font-weight:bold">相關事項</td>      </tr>      <tr>          <td rowspan="6" style="border: 1px solid #000000; text-align: center;">春</td>          <td style="border: 1px solid #000000; text-align: center;">立春</td>          <td style="border: 1px solid #000000; white-space: nowrap">2月3日至5日</td>          <td style="border: 1px solid #000000;">正月節氣</td>          <td style="border: 1px solid #000000;">一般習俗以立春日為春季之始。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">雨水</td>          <td style="border: 1px solid #000000; white-space: nowrap">2月18日至20日</td>          <td style="border: 1px solid #000000;">正月中氣</td>          <td style="border: 1px solid #000000;">雨量漸豐，氣溫回暖，適合春耕。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">驚蟄</td>          <td style="border: 1px solid #000000; white-space: nowrap">3月5日至7日</td>          <td style="border: 1px solid #000000;">2月節氣</td>          <td style="border: 1px solid #000000;">冬眠動物開始活動。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">春分</td>          <td style="border: 1px solid #000000; white-space: nowrap">3月20日至22日</td>          <td style="border: 1px solid #000000;">2月中氣</td>          <td style="border: 1px solid #000000;">太陽直射赤道，晝夜平均，之後，北半球晝漸長。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">清明</td>          <td style="border: 1px solid #000000; white-space: nowrap">4月4日至6日</td>          <td style="border: 1px solid #000000;">3月節氣</td>          <td style="border: 1px solid #000000;">民間有掃墓祭祖習俗。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">穀雨</td>          <td style="border: 1px solid #000000; white-space: nowrap">4月19日至21日</td>          <td style="border: 1px solid #000000;">3月中氣</td>          <td style="border: 1px solid #000000;">大部分地區降雨量增加，有利於種植。</td>      </tr>      <tr>          <td rowspan="6" style="border: 1px solid #000000; text-align: center;">夏</td>          <td style="border: 1px solid #000000; text-align: center;">立夏</td>          <td style="border: 1px solid #000000; white-space: nowrap">5月5日至7日</td>          <td style="border: 1px solid #000000;">4月節氣</td>          <td style="border: 1px solid #000000;">一般習俗以立夏日為夏季之始。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">小滿</td>          <td style="border: 1px solid #000000; white-space: nowrap">5月20日至22日</td>          <td style="border: 1px solid #000000;">4月中氣</td>          <td style="border: 1px solid #000000;">穀物生長已近盈滿。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">芒種</td>          <td style="border: 1px solid #000000; white-space: nowrap">6月5日至7日</td>          <td style="border: 1px solid #000000;">5月節氣</td>          <td style="border: 1px solid #000000;">穀物芒花盛開；大部分地區忙於夏收夏種。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">夏至</td>          <td style="border: 1px solid #000000; white-space: nowrap">6月21日至22日</td>          <td style="border: 1px solid #000000;">5月中氣</td>          <td style="border: 1px solid #000000;">北半球白晝最長，夜晚最短。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">小暑</td>          <td style="border: 1px solid #000000; white-space: nowrap">7月6日至8日</td>          <td style="border: 1px solid #000000;">6月節氣</td>          <td style="border: 1px solid #000000;">漸近最熱時節。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">大暑</td>          <td style="border: 1px solid #000000;">7月22日至24日</td>          <td style="border: 1px solid #000000;">6月中氣</td>          <td style="border: 1px solid #000000;">一年中大部分地區天氣最熱。</td>      </tr>      <tr>          <td rowspan="6" style="border: 1px solid #000000; text-align: center;">秋</td>          <td style="border: 1px solid #000000; text-align: center;">立秋</td>          <td style="border: 1px solid #000000; white-space: nowrap">8月7日至9日</td>          <td style="border: 1px solid #000000;">7月節氣</td>          <td style="border: 1px solid #000000;">一般習俗以立秋日為秋季之始。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">處暑</td>          <td style="border: 1px solid #000000; white-space: nowrap">8月22日至24日</td>          <td style="border: 1px solid #000000;">7月中氣</td>          <td style="border: 1px solid #000000;">此日後暑氣漸消。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">白露</td>          <td style="border: 1px solid #000000; white-space: nowrap">9月7日至9日</td>          <td style="border: 1px solid #000000;">8月節氣</td>          <td style="border: 1px solid #000000;">大部分地區天氣漸涼，大陸北部早晚凝結白露。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">秋分</td>          <td style="border: 1px solid #000000; white-space: nowrap">9月22日至24日</td>          <td style="border: 1px solid #000000;">8月中氣</td>          <td style="border: 1px solid #000000;">晝夜等長，之後，北半球夜漸長。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">寒露</td>          <td style="border: 1px solid #000000; white-space: nowrap">10月8日至9日</td>          <td style="border: 1px solid #000000;">9月節氣</td>          <td style="border: 1px solid #000000;">大陸秋寒多露，漸近霜降。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">霜降</td>          <td style="border: 1px solid #000000; white-space: nowrap">10月23日至24日</td>          <td style="border: 1px solid #000000;">9月中氣</td>          <td style="border: 1px solid #000000;">黃河流域出現初霜。</td>      </tr>      <tr>          <td rowspan="6" style="border: 1px solid #000000; text-align: center;">冬</td>          <td style="border: 1px solid #000000; text-align: center;">立冬</td>          <td style="border: 1px solid #000000; white-space: nowrap">11月7日至8日</td>          <td style="border: 1px solid #000000;">10月節氣</td>          <td style="border: 1px solid #000000;">一般習俗以立冬日為冬季之始。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">小雪</td>          <td style="border: 1px solid #000000; white-space: nowrap">11月22日至23日</td>          <td style="border: 1px solid #000000;">10月中氣</td>          <td style="border: 1px solid #000000;">黃河流域開始降少量雪。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">大雪</td>          <td style="border: 1px solid #000000; white-space: nowrap">12月6日至8日</td>          <td style="border: 1px solid #000000;">11月節氣</td>          <td style="border: 1px solid #000000;">黃河中下游地區常出現降雪。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">冬至</td>          <td style="border: 1px solid #000000; white-space: nowrap">12月21日至23日</td>          <td style="border: 1px solid #000000;">11月中氣</td>          <td style="border: 1px solid #000000;">北半球黑夜最長，白晝最短。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">小寒</td>          <td style="border: 1px solid #000000; white-space: nowrap">1月5日至7日</td>          <td style="border: 1px solid #000000;">12月節氣</td>          <td style="border: 1px solid #000000;">漸近最冷時節。</td>      </tr>      <tr>          <td style="border: 1px solid #000000; text-align: center;">大寒</td>          <td style="border: 1px solid #000000; white-space: nowrap">1月20日至21日</td>          <td style="border: 1px solid #000000;">12月中氣</td>          <td style="border: 1px solid #000000;">一年中大部分地區天氣最冷。</td>      </tr>  </table>""",
           u"""_lt_pre_mt_+------+-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
| 季別  | 節氣名 | 陽曆日期       | 農曆節氣 | 相關事項                                       |_lt_br/_mt_
+------+-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  立春  | 2月3日至5日    | 正月節氣 | 一般習俗以立春日為春季之始。                      |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  雨水  | 2月18日至20日  | 正月中氣 | 雨量漸豐，氣溫回暖，適合春耕。                    |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|  春  |  驚蟄  | 3月5日至7日    | 2月節氣  | 冬眠動物開始活動。                              |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  春分  | 3月20日至22日  | 2月中氣  | 太陽直射赤道，晝夜平均，之後，北半球晝漸長。        |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  清明  | 4月4日至6日    | 3月節氣  | 民間有掃墓祭祖習俗。                            |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  穀雨  | 4月19日至21日  | 3月中氣  | 大部分地區降雨量增加，有利於種植。                 |_lt_br/_mt_
+------+-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  立夏  | 5月5日至7日    | 4月節氣  | 一般習俗以立夏日為夏季之始。                      |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  小滿  | 5月20日至22日  | 4月中氣  | 穀物生長已近盈滿。                              |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|  夏  |  芒種  | 6月5日至7日    | 5月節氣  | 穀物芒花盛開；大部分地區忙於夏收夏種。              |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  夏至  | 6月21日至22日  | 5月中氣  | 北半球白晝最長，夜晚最短。                       |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  小暑  | 7月6日至8日    | 6月節氣  | 漸近最熱時節。                                 |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  大暑  | 7月22日至24日  | 6月中氣  | 一年中大部分地區天氣最熱。                       |_lt_br/_mt_
+------+-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  立秋  | 8月7日至9日    | 7月節氣  | 一般習俗以立秋日為秋季之始。                      |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  處暑  | 8月22日至24日  | 7月中氣  | 此日後暑氣漸消。                                |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|  秋  |  白露  | 9月7日至9日    | 8月節氣  | 大部分地區天氣漸涼，大陸北部早晚凝結白露。          |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  秋分  | 9月22日至24日  | 8月中氣  | 晝夜等長，之後，北半球夜漸長。                    |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  寒露  | 10月8日至9日   | 9月節氣  | 大陸秋寒多露，漸近霜降。                         |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  霜降  | 10月23日至24日 | 9月中氣  | 黃河流域出現初霜。                              |_lt_br/_mt_
+------+-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  立冬  | 11月7日至8日   | 10月節氣 | 一般習俗以立冬日為冬季之始。                      |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  小雪  | 11月22日至23日 | 10月中氣 | 黃河流域開始降少量雪。                           |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|  冬  |  大雪  | 12月6日至8日   | 11月節氣 | 黃河中下游地區常出現降雪。                        |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  冬至  | 12月21日至23日 | 11月中氣 | 北半球黑夜最長，白晝最短。                       |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  小寒  | 1月5日至7日    | 12月節氣 | 漸近最冷時節。                                 |_lt_br/_mt_
+      +-------+---------------+---------+----------------------------------------------+_lt_br/_mt_
|      |  大寒  | 1月20日至21日  | 12月中氣 | 一年中大部分地區天氣最冷。                       |_lt_br/_mt_
+------+-------+---------------+---------+----------------------------------------------+_lt_/pre_mt_"""),
          (u"""<table border="1"><tr><td align="center" nowrap="nowrap">易經卦序</td><td align="center" nowrap="nowrap">卦名</td><td align="center" nowrap="nowrap">卦形</td><td align="center" nowrap="nowrap">組合</td><td align="center">卦義</td></tr><tr><td align="center">1</td><td align="center" nowrap="nowrap">乾</td><td align="center">☰<br />☰</td><td align="center" nowrap="nowrap">乾下乾上</td><td>象徵君子應自強不息，努力永不懈怠。</td></tr><tr><td align="center">2</td><td align="center" nowrap="nowrap">坤</td><td align="center">☷<br />☷</td><td align="center" nowrap="nowrap">坤下坤上</td><td>象徵女德。</td></tr><tr><td align="center">3</td><td align="center" nowrap="nowrap">屯</td><td align="center">☵<br />☳</td><td align="center" nowrap="nowrap">震下坎上</td><td>象徵剛柔始交而難生。</td></tr><tr><td align="center">4</td><td align="center" nowrap="nowrap">蒙</td><td align="center">☶<br />☵</td><td align="center" nowrap="nowrap">坎下艮上</td><td>象徵進退兩難，不知所適。</td></tr><tr><td align="center">5</td><td align="center" nowrap="nowrap">需</td><td align="center">☵<br />☰</td><td align="center" nowrap="nowrap">乾下坎上</td><td>象徵有險在前，需待乃進。</td></tr><tr><td align="center">6</td><td align="center" nowrap="nowrap">訟</td><td align="center">☰<br />☵</td><td align="center" nowrap="nowrap">坎下乾上</td><td>象徵人事有紛爭，形成訴訟。</td></tr><tr><td align="center">7</td><td align="center" nowrap="nowrap">師</td><td align="center">☷<br />☵</td><td align="center" nowrap="nowrap">坎下坤上</td><td>象徵君子以容民畜眾。</td></tr><tr><td align="center">8</td><td align="center" nowrap="nowrap">比</td><td align="center">☵<br />☷</td><td align="center" nowrap="nowrap">坤下坎上</td><td>象徵親近比附，相互合作。</td></tr><tr><td align="center">9</td><td align="center" nowrap="nowrap">小畜</td><td align="center">☴<br />☰</td><td align="center" nowrap="nowrap">乾下巽上</td><td>象徵小有所畜。</td></tr><tr><td align="center">10</td><td align="center" nowrap="nowrap">履</td><td align="center">☰<br />☱</td><td align="center" nowrap="nowrap">兌下乾上</td><td>象徵行履要有禮儀。</td></tr><tr><td align="center">11</td><td align="center" nowrap="nowrap">泰</td><td align="center">☷<br />☰</td><td align="center" nowrap="nowrap">乾下坤上</td><td>象徵天地交而二氣通。</td></tr><tr><td align="center">12</td><td align="center" nowrap="nowrap">否</td><td align="center">☰<br />☷</td><td align="center" nowrap="nowrap">坤下乾上</td><td>象徵陰陽不交，萬物不通。</td></tr><tr><td align="center">13</td><td align="center" nowrap="nowrap">同人</td><td align="center">☰<br />☲</td><td align="center" nowrap="nowrap">離下乾上</td><td>象徵與人和協。</td></tr><tr><td align="center">14</td><td align="center" nowrap="nowrap">大有</td><td align="center">☲<br />☰</td><td align="center" nowrap="nowrap">乾下離上</td><td>象徵盛大豐有。</td></tr><tr><td align="center">15</td><td align="center" nowrap="nowrap">謙</td><td align="center">☷<br />☶</td><td align="center" nowrap="nowrap">艮下坤上</td><td>象徵內止外順而終有成。</td></tr><tr><td align="center">16</td><td align="center" nowrap="nowrap">豫</td><td align="center">☳<br />☷</td><td align="center" nowrap="nowrap">坤下震上</td><td>象徵萬物欣暢，生生不息。</td></tr><tr><td align="center">17</td><td align="center" nowrap="nowrap">隨</td><td align="center">☱<br />☳</td><td align="center" nowrap="nowrap">震下兌上</td><td>象徵隨和。</td></tr><tr><td align="center">18</td><td align="center" nowrap="nowrap">蠱</td><td align="center">☶<br />☴</td><td align="center" nowrap="nowrap">巽下艮上</td><td>象徵上下不交。</td></tr><tr><td align="center">19</td><td align="center" nowrap="nowrap">臨</td><td align="center">☷<br />☱</td><td align="center" nowrap="nowrap">兌下坤上</td><td>象徵在上臨下。</td></tr><tr><td align="center">20</td><td align="center" nowrap="nowrap">觀</td><td align="center">☴<br />☷</td><td align="center" nowrap="nowrap">坤下巽上</td><td>象徵先王教化風行於世。</td></tr><tr><td align="center">21</td><td align="center" nowrap="nowrap">噬嗑</td><td align="center">☲<br />☳</td><td align="center" nowrap="nowrap">震下離上</td><td>象徵以刑罰治國，亦象徵市集聚合天下貨物以交易。</td></tr><tr><td align="center">22</td><td align="center" nowrap="nowrap">賁</td><td align="center">☶<br />☲</td><td align="center" nowrap="nowrap">離下艮上</td><td>象徵可以有小利，且有所往。</td></tr><tr><td align="center">23</td><td align="center" nowrap="nowrap">剝</td><td align="center">☶<br />☷</td><td align="center" nowrap="nowrap">坤下艮上</td><td>象徵剝落。</td></tr><tr><td align="center">24</td><td align="center" nowrap="nowrap">復</td><td align="center">☷<br />☳</td><td align="center" nowrap="nowrap">震下坤上</td><td>象徵機運循環。</td></tr><tr><td align="center">25</td><td align="center" nowrap="nowrap">无妄</td><td align="center">☰<br />☳</td><td align="center" nowrap="nowrap">震下乾上</td><td>象徵至誠無虛妄。</td></tr><tr><td align="center">26</td><td align="center" nowrap="nowrap">大畜</td><td align="center">☶<br />☰</td><td align="center" nowrap="nowrap">乾下艮上</td><td>象徵君子能剛健篤實，蓄積富有。</td></tr><tr><td align="center">27</td><td align="center" nowrap="nowrap">頤</td><td align="center">☶<br />☳</td><td align="center" nowrap="nowrap">震下艮上</td><td>象徵養正就吉利。</td></tr><tr><td align="center">28</td><td align="center" nowrap="nowrap">大過</td><td align="center">☱<br />☴</td><td align="center" nowrap="nowrap">巽下兌上</td><td>象徵陽剛過盛，調濟剛柔，走向亨通。</td></tr><tr><td align="center">29</td><td align="center" nowrap="nowrap">坎</td><td align="center">☵<br />☵</td><td align="center" nowrap="nowrap">坎下坎上</td><td>象徵險難重重。</td></tr><tr><td align="center">30</td><td align="center" nowrap="nowrap">離</td>
<td align="center">☲<br />☲</td><td align="center" nowrap="nowrap">離下離上</td><td>象以陰柔之質而得中正。</td></tr><tr><td align="center">31</td><td align="center" nowrap="nowrap">咸</td><td align="center">☱<br />☶</td><td align="center" nowrap="nowrap">艮下兌上</td><td>象徵感應。意謂堅守正道，則諸事亨通順利。</td></tr><tr><td align="center">32</td><td align="center" nowrap="nowrap">恆</td><td align="center">☳<br />☴</td><td align="center" nowrap="nowrap">巽下震上</td><td>象徵長久不變的道理。</td></tr><tr><td align="center">33</td><td align="center" nowrap="nowrap">遯</td><td align="center">☰<br />☶</td><td align="center" nowrap="nowrap">艮下乾上</td><td>象徵逃離隱退。</td></tr><tr><td align="center">34</td><td align="center" nowrap="nowrap">大壯</td><td align="center">☳<br />☰</td><td align="center" nowrap="nowrap">乾下震上</td><td>象徵陽剛盛長。</td></tr><tr><td align="center">35</td><td align="center" nowrap="nowrap">晉</td><td align="center">☲<br />☷</td><td align="center" nowrap="nowrap">坤下離上</td><td>象徵日出地上。</td></tr><tr><td align="center">36</td><td align="center" nowrap="nowrap">明夷</td><td align="center">☷<br />☲</td><td align="center" nowrap="nowrap">離下坤上</td><td>象徵賢者不得志，憂讒畏譏。</td></tr><tr><td align="center">37</td><td align="center" nowrap="nowrap">家人</td><td align="center">☴<br />☲</td><td align="center" nowrap="nowrap">離下巽上</td><td>象徵修養家內之道。</td></tr><tr><td align="center">38</td><td align="center" nowrap="nowrap">睽</td><td align="center">☲<br />☱</td><td align="center" nowrap="nowrap">兌下離上</td><td>象徵違背、背離。</td></tr><tr><td align="center">39</td><td align="center" nowrap="nowrap">蹇</td><td align="center">☵<br />☶</td><td align="center" nowrap="nowrap">艮下坎上</td><td>象徵身陷困境時，應修養德行，以渡難關。</td></tr><tr><td align="center">40</td><td align="center" nowrap="nowrap">解</td><td align="center">☳<br />☵</td><td align="center" nowrap="nowrap">坎下震上</td><td>象徵險難緩解。</td></tr><tr><td align="center">41</td><td align="center" nowrap="nowrap">損</td><td align="center">☶<br />☱</td><td align="center" nowrap="nowrap">兌下艮上</td><td>象徵減損。</td></tr><tr><td align="center">42</td><td align="center" nowrap="nowrap">益</td><td align="center">☴<br />☳</td><td align="center" nowrap="nowrap">震下巽上</td><td>象徵君子為人民服務，減損自己的享受，而增益人民的幸福。</td></tr><tr><td align="center">43</td><td align="center" nowrap="nowrap">夬</td><td align="center">☱<br />☰</td><td align="center" nowrap="nowrap">乾下兌上</td><td>象徵決斷。</td></tr><tr><td align="center">44</td><td align="center" nowrap="nowrap">姤</td><td align="center">☰<br />☴</td><td align="center" nowrap="nowrap">巽下乾上</td><td>象徵柔、剛相遇。</td></tr><tr><td align="center">45</td><td align="center" nowrap="nowrap">萃</td><td align="center">☱<br />☷</td><td align="center" nowrap="nowrap">坤下兌上</td><td>象徵聚合、亨通。</td></tr><tr><td align="center">46</td><td align="center" nowrap="nowrap">升</td><td align="center">☷<br />☴</td><td align="center" nowrap="nowrap">巽下坤上</td><td>象徵亨通。</td></tr><tr><td align="center">47</td><td align="center" nowrap="nowrap">困</td><td align="center">☱<br />☵</td><td align="center" nowrap="nowrap">坎下兌上</td><td>象徵君子雖然處在艱困的環境，也要犧牲奉獻，實現高尚的志向。</td></tr><tr><td align="center">48</td><td align="center" nowrap="nowrap">井</td><td align="center">☵<br />☴</td><td align="center" nowrap="nowrap">巽下坎上</td><td>象徵君子修德，終始無變。</td></tr><tr><td align="center">49</td><td align="center" nowrap="nowrap">革</td><td align="center">☱<br />☲</td><td align="center" nowrap="nowrap">離下兌上</td><td>象徵除舊更新。</td></tr><tr><td align="center">50</td><td align="center" nowrap="nowrap">鼎</td><td align="center">☲<br />☴</td><td align="center" nowrap="nowrap">巽下離上</td><td>象徵革故鼎新。</td></tr><tr><td align="center">51</td><td align="center" nowrap="nowrap">震</td><td align="center">☳<br />☳</td><td align="center" nowrap="nowrap">震下震上</td><td>象徵君子體察到雷電交相而來的現象，即以恐懼之心，修養其身。</td></tr><tr><td align="center">52</td><td align="center" nowrap="nowrap">艮</td><td align="center">☶<br />☶</td><td align="center" nowrap="nowrap">艮下艮上</td><td>象徵動靜不失其時，則其道光明。</td></tr><tr><td align="center">53</td><td align="center" nowrap="nowrap">漸</td><td align="center">☴<br />☶</td><td align="center" nowrap="nowrap">艮下巽上</td><td>象徵漸進。</td></tr><tr><td align="center">54</td><td align="center" nowrap="nowrap">歸妹</td><td align="center">☳<br />☱</td><td align="center" nowrap="nowrap">兌下震上</td><td>象徵夫唱婦隨。</td></tr><tr><td align="center">55</td><td align="center" nowrap="nowrap">豐</td><td align="center">☳<br />☲</td><td align="center" nowrap="nowrap">離下震上</td><td>象徵盛大。</td></tr><tr><td align="center">56</td><td align="center" nowrap="nowrap">旅</td><td align="center">☲<br />☶</td><td align="center" nowrap="nowrap">艮下離上</td><td>象徵羈旅在外。</td></tr><tr><td align="center">57</td><td align="center" nowrap="nowrap">巽</td><td align="center">☴<br />☴</td><td align="center" nowrap="nowrap">巽下巽上</td><td>象徵上下皆順，不相違逆，風行無所不入。</td></tr><tr><td align="center">58</td><td align="center" nowrap="nowrap">兌</td><td align="center">☱<br />☱</td><td align="center" nowrap="nowrap">兌下兌上</td><td>象徵亨通而利於守正。</td></tr><tr><td align="center">59</td><td align="center" nowrap="nowrap">渙</td><td align="center">☴<br />☵</td><td align="center" nowrap="nowrap">坎下巽上</td><td>象徵風行於水上，波濤激動，而披離解散。</td></tr><tr><td align="center">60</td><td align="center" nowrap="nowrap">節</td><td align="center">☵<br />☱</td><td align="center" nowrap="nowrap">兌下坎上</td><td>象徵水在澤中，乃得其節。</td></tr><tr><td align="center">61</td><td align="center" nowrap="nowrap">中孚</td><td align="center">☴<br />☱</td><td align="center" nowrap="nowrap">兌下巽上</td><td>象徵信發於中。</td></tr><tr><td align="center">62</td><td align="center" nowrap="nowrap">小過</td><td align="center">☳<br />☶</td><td align="center" nowrap="nowrap">艮下震上</td><td>徵利於守正，只可做小事，不宜做大事。</td></tr><tr><td align="center">63</td><td align="center" nowrap="nowrap">既濟</td><td align="center">☵<br />☲</td><td align="center" nowrap="nowrap">離下坎上</td><td>象徵目的已達到、任務已完成。</td></tr><tr><td align="center">64</td><td align="center" nowrap="nowrap">未濟</td><td align="center">☲<br />☵</td><td align="center" nowrap="nowrap">坎下離上</td><td>象徵水火性質不同，不相為用。</td></tr></table>""",
           u"""_lt_pre_mt_+----------+------+------+----------+------------------------------------------------------------+_lt_br/_mt_
| 易經卦序  | 卦名  | 卦形  |   組合    |                            卦義                             |_lt_br/_mt_
+----------+------+------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☰  | 乾下乾上  | 象徵君子應自強不息，努力永不懈怠。                               |_lt_br/_mt_
+     1    +  乾  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☰  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☷  | 坤下坤上  | 象徵女德。                                                   |_lt_br/_mt_
+     2    +  坤  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☷  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☵  | 震下坎上  | 象徵剛柔始交而難生。                                           |_lt_br/_mt_
+     3    +  屯  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☳  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☶  | 坎下艮上  | 象徵進退兩難，不知所適。                                        |_lt_br/_mt_
+     4    +  蒙  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☵  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☵  | 乾下坎上  | 象徵有險在前，需待乃進。                                       |_lt_br/_mt_
+     5    +  需  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☰  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☰  | 坎下乾上  | 象徵人事有紛爭，形成訴訟。                                      |_lt_br/_mt_
+     6    +  訟  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☵  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☷  | 坎下坤上  | 象徵君子以容民畜眾。                                           |_lt_br/_mt_
+     7    +  師  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☵  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☵  | 坤下坎上  | 象徵親近比附，相互合作。                                       |_lt_br/_mt_
+     8    +  比  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☷  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☴  | 乾下巽上  | 象徵小有所畜。                                                |_lt_br/_mt_
+     9    + 小畜 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☰  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☰  | 兌下乾上  | 象徵行履要有禮儀。                                            |_lt_br/_mt_
+    10    +  履  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☱  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☷  | 乾下坤上  | 象徵天地交而二氣通。                                           |_lt_br/_mt_
+    11    +  泰  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☰  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☰  | 坤下乾上  | 象徵陰陽不交，萬物不通。                                       |_lt_br/_mt_
+    12    +  否  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☷  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☰  | 離下乾上  | 象徵與人和協。                                               |_lt_br/_mt_
+    13    + 同人 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☲  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☲  | 乾下離上  | 象徵盛大豐有。                                               |_lt_br/_mt_
+    14    + 大有 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☰  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☷  | 艮下坤上  | 象徵內止外順而終有成。                                         |_lt_br/_mt_
+    15    +  謙  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☶  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☳  | 坤下震上  | 象徵萬物欣暢，生生不息。                                       |_lt_br/_mt_
+    16    +  豫  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☷  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☱  | 震下兌上  | 象徵隨和。                                                   |_lt_br/_mt_
+    17    +  隨  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☳  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☶  | 巽下艮上  | 象徵上下不交。                                               |_lt_br/_mt_
+    18    +  蠱  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☴  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☷  | 兌下坤上  | 象徵在上臨下。                                                |_lt_br/_mt_
+    19    +  臨  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☱  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☴  | 坤下巽上  | 象徵先王教化風行於世。                                         |_lt_br/_mt_
+    20    +  觀  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☷  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☲  | 震下離上  | 象徵以刑罰治國，亦象徵市集聚合天下貨物以交易。                     |_lt_br/_mt_
+    21    + 噬嗑 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☳  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☶  | 離下艮上  | 象徵可以有小利，且有所往。                                      |_lt_br/_mt_
+    22    +  賁  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☲  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☶  | 坤下艮上  | 象徵剝落。                                                   |_lt_br/_mt_
+    23    +  剝  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☷  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☷  | 震下坤上  | 象徵機運循環。                                                |_lt_br/_mt_
+    24    +  復  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☳  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☰  | 震下乾上  | 象徵至誠無虛妄。                                              |_lt_br/_mt_
+    25    + 无妄 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☳  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☶  | 乾下艮上  | 象徵君子能剛健篤實，蓄積富有。                                  |_lt_br/_mt_
+    26    + 大畜 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☰  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☶  | 震下艮上  | 象徵養正就吉利。                                              |_lt_br/_mt_
+    27    +  頤  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☳  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☱  | 巽下兌上  | 象徵陽剛過盛，調濟剛柔，走向亨通。                               |_lt_br/_mt_
+    28    + 大過 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☴  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☵  | 坎下坎上  | 象徵險難重重。                                                |_lt_br/_mt_
+    29    +  坎  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☵  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☲  | 離下離上  | 象以陰柔之質而得中正。                                         |_lt_br/_mt_
+    30    +  離  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☲  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☱  | 艮下兌上  | 象徵感應。意謂堅守正道，則諸事亨通順利。                          |_lt_br/_mt_
+    31    +  咸  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☶  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☳  | 巽下震上  | 象徵長久不變的道理。                                           |_lt_br/_mt_
+    32    +  恆  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☴  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☰  | 艮下乾上  | 象徵逃離隱退。                                                |_lt_br/_mt_
+    33    +  遯  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☶  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☳  | 乾下震上  | 象徵陽剛盛長。                                                |_lt_br/_mt_
+    34    + 大壯 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☰  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☲  | 坤下離上  | 象徵日出地上。                                                |_lt_br/_mt_
+    35    +  晉  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☷  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☷  | 離下坤上  | 象徵賢者不得志，憂讒畏譏。                                      |_lt_br/_mt_
+    36    + 明夷 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☲  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☴  | 離下巽上  | 象徵修養家內之道。                                             |_lt_br/_mt_
+    37    + 家人 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☲  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☲  | 兌下離上  | 象徵違背、背離。                                              |_lt_br/_mt_
+    38    +  睽  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☱  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☵  | 艮下坎上  | 象徵身陷困境時，應修養德行，以渡難關。                            |_lt_br/_mt_
+    39    +  蹇  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☶  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☳  | 坎下震上  | 象徵險難緩解。                                                |_lt_br/_mt_
+    40    +  解  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☵  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☶  | 兌下艮上  | 象徵減損。                                                   |_lt_br/_mt_
+    41    +  損  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☱  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☴  | 震下巽上  | 象徵君子為人民服務，減損自己的享受，而增益人民的幸福。               |_lt_br/_mt_
+    42    +  益  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☳  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☱  | 乾下兌上  | 象徵決斷。                                                   |_lt_br/_mt_
+    43    +  夬  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☰  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☰  | 巽下乾上  | 象徵柔、剛相遇。                                              |_lt_br/_mt_
+    44    +  姤  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☴  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☱  | 坤下兌上  | 象徵聚合、亨通。                                              |_lt_br/_mt_
+    45    +  萃  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☷  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☷  | 巽下坤上  | 象徵亨通。                                                   |_lt_br/_mt_
+    46    +  升  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☴  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☱  | 坎下兌上  | 象徵君子雖然處在艱困的環境，也要犧牲奉獻，實現高尚的志向。           |_lt_br/_mt_
+    47    +  困  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☵  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☵  | 巽下坎上  | 象徵君子修德，終始無變。                                       |_lt_br/_mt_
+    48    +  井  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☴  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☱  | 離下兌上  | 象徵除舊更新。                                                |_lt_br/_mt_
+    49    +  革  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☲  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☲  | 巽下離上  | 象徵革故鼎新。                                                |_lt_br/_mt_
+    50    +  鼎  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☴  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☳  | 震下震上  | 象徵君子體察到雷電交相而來的現象，即以恐懼之心，修養其身。           |_lt_br/_mt_
+    51    +  震  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☳  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☶  | 艮下艮上  | 象徵動靜不失其時，則其道光明。                                   |_lt_br/_mt_
+    52    +  艮  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☶  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☴  | 艮下巽上  | 象徵漸進。                                                   |_lt_br/_mt_
+    53    +  漸  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☶  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☳  | 兌下震上  | 象徵夫唱婦隨。                                                |_lt_br/_mt_
+    54    + 歸妹 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☱  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☳  | 離下震上  | 象徵盛大。                                                   |_lt_br/_mt_
+    55    +  豐  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☲  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☲  | 艮下離上  | 象徵羈旅在外。                                                |_lt_br/_mt_
+    56    +  旅  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☶  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☴  | 巽下巽上  | 象徵上下皆順，不相違逆，風行無所不入。                            |_lt_br/_mt_
+    57    +  巽  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☴  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☱  | 兌下兌上  | 象徵亨通而利於守正。                                           |_lt_br/_mt_
+    58    +  兌  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☱  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☴  | 坎下巽上  | 象徵風行於水上，波濤激動，而披離解散。                            |_lt_br/_mt_
+    59    +  渙  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☵  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☵  | 兌下坎上  | 象徵水在澤中，乃得其節。                                       |_lt_br/_mt_
+    60    +  節  +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☱  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☴  | 兌下巽上  | 象徵信發於中。                                                |_lt_br/_mt_
+    61    + 中孚 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☱  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☳  | 艮下震上  | 徵利於守正，只可做小事，不宜做大事。                             |_lt_br/_mt_
+    62    + 小過 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☶  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☵  | 離下坎上  | 象徵目的已達到、任務已完成。                                    |_lt_br/_mt_
+    63    + 既濟 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☲  |          |                                                            |_lt_br/_mt_
+----------+------+-------+----------+------------------------------------------------------------+_lt_br/_mt_
|          |      |   ☲  | 坎下離上   | 象徵水火性質不同，不相為用。                                   |_lt_br/_mt_
+    64    + 未濟 +-------+          +                                                            +_lt_br/_mt_
|          |      |   ☵  |          |                                                            |_lt_br/_mt_
+----------+------+------+----------+------------------------------------------------------------+_lt_/pre_mt_""")]
