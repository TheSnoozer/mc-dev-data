from .types import Vsn

__all__ = ('version_urls',)


"""A dict mapping each Minecraft version to the URL of the corresponding
   pre-release or release wiki page. Pre-release pages are preferred, when
   available, as they contain more information about protocol changes."""
version_urls = {
    Vsn('1.13.2',      404): 'https://wiki.vg/index.php?title=Protocol&oldid=14388',
    Vsn('1.13.2-pre2', 403): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14359',
    Vsn('1.13.2-pre1', 402): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14357',
    Vsn('1.13.1',      401): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14264',
    Vsn('1.13.1-pre2', 400): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14261',
    Vsn('1.13.1-pre1', 399): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14255',
    Vsn('18w33a',      398): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14252',
    Vsn('18w32a',      397): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14247',
    Vsn('18w31a',      396): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14196',
    Vsn('18w30b',      395): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14189',
    Vsn('18w30a',      394): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14158',
    Vsn('1.13',        393): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14132',
    Vsn('1.13-pre10',  392): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14126',
    Vsn('1.13-pre9',   391): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14124',
    Vsn('1.13-pre8',   390): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14117',
    Vsn('1.13-pre7',   389): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14107',
    Vsn('1.13-pre6',   388): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14095',
    Vsn('1.13-pre5',   387): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14088',
    Vsn('1.13-pre4',   386): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14072',
    Vsn('1.13-pre3',   385): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14045',
    Vsn('1.13-pre2',   384): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=14030',
    Vsn('1.13-pre1',   383): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13971',
    Vsn('18w22c',      382): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13965',
    Vsn('18w22b',      381): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13951',
    Vsn('18w22a',      380): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13947',
    Vsn('18w21b',      379): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13930',
    Vsn('18w21a',      378): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13926',
    Vsn('18w20c',      377): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13917',
    Vsn('18w20b',      376): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13913',
    Vsn('18w20a',      375): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13910',
    Vsn('18w19b',      374): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13905',
    Vsn('18w19a',      373): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13896',
    Vsn('18w16a',      372): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13891',
    Vsn('18w15a',      371): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13824',
    Vsn('18w14b',      370): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13744',
    Vsn('18w14a',      369): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13741',
    Vsn('18w11a',      368): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13724',
    Vsn('18w10d',      367): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13702',
    Vsn('18w10c',      366): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13699',
    Vsn('18w10b',      365): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13693',
    Vsn('18w10a',      364): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13692',
    Vsn('18w09a',      363): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13671',
    Vsn('18w08b',      362): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13666',
    Vsn('18w08a',      361): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13662',
    Vsn('18w07c',      360): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13658',
    Vsn('18w07b',      359): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13653',
    Vsn('18w07a',      358): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13648',
    Vsn('18w06a',      357): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13636',
    Vsn('18w05a',      356): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13628',
    Vsn('18w03b',      355): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13623',
    Vsn('18w02a',      353): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13582',
    Vsn('18w01a',      352): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13576',
    Vsn('17w50a',      351): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13556',
    Vsn('17w49b',      350): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13524',
    Vsn('17w49a',      349): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13516',
    Vsn('17w48a',      348): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13512',
    Vsn('17w47b',      347): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13487',
    Vsn('17w47a',      346): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13476',
    Vsn('17w46a',      345): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13472',
    Vsn('17w45b',      344): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13414',
    Vsn('17w45a',      343): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13413',
    Vsn('17w43b',      342): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13398',
    Vsn('17w43a',      341): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13396',
    Vsn('1.12.2',      340): 'http://wiki.vg/index.php?title=Protocol&oldid=13488',
    Vsn('1.12.2-pre2', 339): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13355',
    Vsn('1.12.1',      338): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13287',
    Vsn('1.12.1-pre1', 337): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13267',
    Vsn('17w31a',      336): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=13265',
    Vsn('1.12',        335): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=12929',
    Vsn('1.12-pre7',   334): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=12918',
    Vsn('1.12-pre6',   333): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=12909',
    Vsn('1.12-pre5',   332): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=10809',
    Vsn('1.12-pre4',   331): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=10804',
    Vsn('1.12-pre3',   330): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=10803',
    Vsn('1.12-pre2',   329): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=10418',
    Vsn('1.12-pre1',   328): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=9819',
    Vsn('17w18b',      327): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8548',
    Vsn('17w18a',      326): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8546',
    Vsn('17w17b',      325): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8536',
    Vsn('17w17a',      324): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8528',
    Vsn('17w16b',      323): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8519',
    Vsn('17w16a',      322): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8515',
    Vsn('17w15a',      321): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8499',
    Vsn('17w14a',      320): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8490',
    Vsn('17w13b',      319): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8475',
    Vsn('17w13a',      318): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8454',
    Vsn('17w06a',      317): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8414',
    Vsn('1.11.2',      316): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8356',
    Vsn('1.11',        315): 'http://wiki.vg/index.php?title=Protocol&oldid=8405',
    Vsn('1.11-pre1',   314): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8249',
    Vsn('16w44a',      313): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8246',
    Vsn('16w42a',      312): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8225',
    Vsn('16w41a',      311): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8218',
    Vsn('16w40a',      310): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8204',
    Vsn('16w39c',      309): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8177',
    Vsn('16w39b',      308): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8149',
    Vsn('16w39a',      307): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8141',
    Vsn('16w38a',      306): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8118',
    Vsn('16w36a',      305): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8099',
    Vsn('16w35a',      304): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8094',
    Vsn('16w33a',      303): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8084',
    Vsn('16w32b',      302): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8063',
    Vsn('16w32a',      301): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=8062',
    Vsn('1.10.2',      210): 'http://wiki.vg/index.php?title=Protocol&oldid=8235',
    Vsn('1.10-pre2',   205): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7961',
    Vsn('1.10-pre1',   204): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7950',
    Vsn('16w21b',      203): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7935',
    Vsn('16w21a',      202): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7877',
    Vsn('16w20a',      201): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7859',
    Vsn('1.9.4',       110): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7804',
    Vsn('1.9.2',       109): 'http://wiki.vg/index.php?title=Protocol&oldid=7817',
    Vsn('1.9.1',       108): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7552',
    Vsn('1.9',         107): 'http://wiki.vg/index.php?title=Protocol&oldid=7617',
    Vsn('1.9-pre4',    106): 'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7412',
    Vsn('16w04a',      97):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7374',
    Vsn('16w02a',      95):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7313',
    Vsn('15w51b',      94):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7261',
    Vsn('15w40b',      76):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=7122',
    Vsn('15w38b',      73):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6965',
    Vsn('15w38a',      72):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6932',
    Vsn('15w36d',      70):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6925',
    Vsn('15w36c',      69):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6883',
# These commented-out pages use a format that isn't supported by the current parser:
#    Vsn('15w35e',      66):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6851',
#    Vsn('15w35b',      63):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6829',
#    Vsn('15w34a',      58):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6809',
#    Vsn('15w33c',      57):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6806',
#    Vsn('15w33b',      56):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6796',
#    Vsn('15w33a',      55):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6790',
#    Vsn('15w32c',      54):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6788',
#    Vsn('15w32a',      52):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6785',
#    Vsn('15w31c',      51):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6780',
#    Vsn('15w31b',      50):  'http://wiki.vg/index.php?title=Pre-release_protocol&oldid=6746',
    Vsn('1.8.9',       47):  'http://wiki.vg/index.php?title=Protocol&oldid=7368',
}
