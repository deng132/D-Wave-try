from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler_auto=EmbeddingComposite(DWaveSampler(solver={'topology__type':'pegasus'}))


linear={('q1','q1'):1175.95,('q2','q2'):1126.62,('q3','q3'):1228.36,('q4','q4'):1080.26,('q5','q5'):1304.78,('q6','q6'):1090.62,('q7','q7'):1404.79,('q8','q8'):1157.38,('q9','q9'):1283.9,('q10','q10'):1531.64,('q11','q11'):1685.56,('q12','q12'):1685.56,('q13','q13'):1858.1,('q14','q14'):1841.47,('q15','q15'):2053.9,('q16','q16'):2053.9,('w1','w1'):-24.9383,('w2','w2'):-8.31276,('w3','w3'):-8.31276,('w4','w4'):-8.31276,('w5','w5'):-8.31276,('w6','w6'):-8.31276,('w7','w7'):-8.31276,('w8','w8'):-49.3298,('w9','w9'):-16.4433,('w10','w10'):-16.4433,('w11','w11'):-16.4433,('w12','w12'):-16.4433,('w13','w13'):-16.4433,('w14','w14'):-16.4433,('w15','w15'):-24.6648,('w16','w16'):-8.22161,('w17','w17'):-8.22161,('w18','w18'):-8.22161,('w19','w19'):-8.22161,('w20','w20'):-8.22161,('w21','w21'):-8.22161,('w22','w22'):-49.4387,('w23','w23'):-16.4796,('w24','w24'):-16.4796,('w25','w25'):-16.4796,('w26','w26'):-16.4796,('w27','w27'):-16.4796,('w28','w28'):-16.4796,('w29','w29'):-24.7193,('w30','w30'):-8.23976,('w31','w31'):-8.23976,('w32','w32'):-8.23976,('w33','w33'):-8.23976,('w34','w34'):-8.23976,('w35','w35'):-8.23976,('w36','w36'):-147.993,('w37','w37'):-49.3311,('w38','w38'):-49.3311,('w39','w39'):-49.3311,('w40','w40'):-49.3311,('w41','w41'):-49.3311,('w42','w42'):-49.3311,('w43','w43'):-49.5478,('w44','w44'):-16.5159,('w45','w45'):-16.5159,('w46','w46'):-16.5159,('w47','w47'):-16.5159,('w48','w48'):-16.5159,('w49','w49'):-16.5159,('w50','w50'):-24.7738,('w51','w51'):-8.25795,('w52','w52'):-8.25795,('w53','w53'):-8.25795,('w54','w54'):-8.25795,('w55','w55'):-8.25795,('w56','w56'):-8.25795,('w57','w57'):-123.327,('w58','w58'):-41.1088,('w59','w59'):-41.1088,('w60','w60'):-41.1088,('w61','w61'):-41.1088,('w62','w62'):-41.1088,('w63','w63'):-41.1088,('w64','w64'):-123.599,('w65','w65'):-41.1996,('w66','w66'):-41.1996,('w67','w67'):-41.1996,('w68','w68'):-41.1996,('w69','w69'):-41.1996,('w70','w70'):-41.1996,('w71','w71'):-49.6572,('w72','w72'):-16.5524,('w73','w73'):-16.5524,('w74','w74'):-16.5524,('w75','w75'):-16.5524,('w76','w76'):-16.5524,('w77','w77'):-16.5524,('w78','w78'):-24.8285,('w79','w79'):-8.27618,('w80','w80'):-8.27618,('w81','w81'):-8.27618,('w82','w82'):-8.27618,('w83','w83'):-8.27618,('w84','w84'):-8.27618,('w85','w85'):-98.6605,('w86','w86'):-32.8868,('w87','w87'):-32.8868,('w88','w88'):-32.8868,('w89','w89'):-32.8868,('w90','w90'):-32.8868,('w91','w91'):-32.8868,('w92','w92'):-98.8783,('w93','w93'):-32.9594,('w94','w94'):-32.9594,('w95','w95'):-32.9594,('w96','w96'):-32.9594,('w97','w97'):-32.9594,('w98','w98'):-32.9594,('w99','w99'):-99.0966,('w100','w100'):-33.0322,('w101','w101'):-33.0322,('w102','w102'):-33.0322,('w103','w103'):-33.0322,('w104','w104'):-33.0322,('w105','w105'):-33.0322,('w106','w106'):-49.7668,('w107','w107'):-16.5889,('w108','w108'):-16.5889,('w109','w109'):-16.5889,('w110','w110'):-16.5889,('w111','w111'):-16.5889,('w112','w112'):-16.5889,('w113','w113'):-24.8834,('w114','w114'):-8.29445,('w115','w115'):-8.29445,('w116','w116'):-8.29445,('w117','w117'):-8.29445,('w118','w118'):-8.29445,('w119','w119'):-8.29445,('w120','w120'):-73.995,('w121','w121'):-24.665,('w122','w122'):-24.665,('w123','w123'):-24.665,('w124','w124'):-24.665,('w125','w125'):-24.665,('w126','w126'):-24.665,('w127','w127'):-74.1583,('w128','w128'):-24.7194,('w129','w129'):-24.7194,('w130','w130'):-24.7194,('w131','w131'):-24.7194,('w132','w132'):-24.7194,('w133','w133'):-24.7194,('w134','w134'):-74.322,('w135','w135'):-24.774,('w136','w136'):-24.774,('w137','w137'):-24.774,('w138','w138'):-24.774,('w139','w139'):-24.774,('w140','w140'):-24.774,('w141','w141'):-74.4861,('w142','w142'):-24.8287,('w143','w143'):-24.8287,('w144','w144'):-24.8287,('w145','w145'):-24.8287,('w146','w146'):-24.8287,('w147','w147'):-24.8287,('w148','w148'):49.3298,('w149','w149'):49.7668,('w150','w150'):24.9383,('w151','w151'):24.9383,('w152','w152'):24.6648,('w153','w153'):24.8834,('w154','w154'):24.9383,('w155','w155'):24.9383,('w156','w156'):73.995,('w157','w157'):49.3298,('w158','w158'):49.3298,('w159','w159'):49.3298,('w160','w160'):24.6648,('w161','w161'):24.6648,('w162','w162'):24.6648,('w163','w163'):49.4387,('w164','w164'):24.7193,('w165','w165'):147.993,('w166','w166'):49.4387,('w167','w167'):24.7193,('w168','w168'):147.993,('w169','w169'):147.993,('w170','w170'):74.1583,('w171','w171'):49.4387,('w172','w172'):49.4387,('w173','w173'):24.7193,('w174','w174'):24.7193,('w175','w175'):147.993,('w176','w176'):49.5478,('w177','w177'):24.7738,('w178','w178'):123.327,('w179','w179'):123.599,('w180','w180'):49.5478,('w181','w181'):24.7738,('w182','w182'):123.327,('w183','w183'):123.599,('w184','w184'):123.327,('w185','w185'):74.322,('w186','w186'):49.5478,('w187','w187'):49.5478,('w188','w188'):24.7738,('w189','w189'):24.7738,('w190','w190'):123.327,('w191','w191'):123.599,('w192','w192'):123.599,('w193','w193'):49.6572,('w194','w194'):24.8285,('w195','w195'):98.6605,('w196','w196'):98.8783,('w197','w197'):99.0966,('w198','w198'):49.6572,('w199','w199'):24.8285,('w200','w200'):98.6605,('w201','w201'):98.8783,('w202','w202'):99.0966,('w203','w203'):98.6605,('w204','w204'):74.4861,('w205','w205'):49.6572,('w206','w206'):49.6572,('w207','w207'):24.8285,('w208','w208'):24.8285,('w209','w209'):98.6605,('w210','w210'):98.8783,('w211','w211'):98.8783,('w212','w212'):99.0966,('w213','w213'):99.0966,('w214','w214'):73.995,('w215','w215'):49.7668,('w216','w216'):49.7668,('w217','w217'):49.7668,('w218','w218'):24.8834,('w219','w219'):24.8834,('w220','w220'):24.8834,('w221','w221'):73.995,('w222','w222'):73.995,('w223','w223'):74.1583,('w224','w224'):74.1583,('w225','w225'):74.1583,('w226','w226'):74.322,('w227','w227'):74.322,('w228','w228'):74.322,('w229','w229'):74.4861,('w230','w230'):74.4861,('w231','w231'):74.4861}

quadratic={('q1','q2'):-901.707,('q1','q3'):160.326,('q1','q4'):209.657,('q1','q5'):133.604,('q1','q6'):174.713,('q1','q7'):106.882,('q1','q8'):139.769,('q1','q9'):104.826,('q1','q10'):80.1612,('q1','q11'):53.4406,('q1','q12'):53.4406,('q1','q13'):26.7202,('q1','q14'):26.7202,('q1','w8'):16.4433,('q1','w9'):16.4433,('q1','w12'):16.4433,('q1','w13'):16.4433,('q1','w15'):8.22161,('q1','w16'):8.22161,('q1','w19'):8.22161,('q1','w20'):8.22161,('q1','w36'):49.3311,('q1','w37'):49.3311,('q1','w40'):49.3311,('q1','w41'):49.3311,('q1','w57'):41.1088,('q1','w58'):41.1088,('q1','w61'):41.1088,('q1','w62'):41.1088,('q1','w85'):32.8868,('q1','w86'):32.8868,('q1','w89'):32.8868,('q1','w90'):32.8868,('q1','w120'):24.665,('q1','w121'):24.665,('q1','w124'):24.665,('q1','w125'):24.665,('q1','w148'):-49.3298,('q1','w152'):-24.6648,('q1','w156'):-73.995,('q1','w157'):-49.3298,('q1','w158'):-49.3298,('q1','w160'):-24.6648,('q1','w161'):-24.6648,('q1','w165'):-147.993,('q1','w168'):-147.993,('q1','w169'):-147.993,('q1','w178'):-123.327,('q1','w182'):-123.327,('q1','w184'):-123.327,('q1','w195'):-98.6605,('q1','w200'):-98.6605,('q1','w203'):-98.6605,('q1','w214'):-73.995,('q1','w221'):-73.995,('q2','q3'):160.326,('q2','q4'):209.657,('q2','q5'):133.604,('q2','q6'):174.713,('q2','q7'):106.882,('q2','q8'):139.769,('q2','q9'):104.826,('q2','q10'):80.1612,('q2','q11'):69.8838,('q2','q12'):69.8838,('q2','q13'):34.9418,('q2','q14'):34.9418,('q2','w8'):32.8865,('q2','w9'):16.4433,('q2','w10'):16.4433,('q2','w11'):16.4433,('q2','w12'):16.4433,('q2','w13'):16.4433,('q2','w14'):16.4433,('q2','w15'):16.4432,('q2','w16'):8.22161,('q2','w17'):8.22161,('q2','w18'):8.22161,('q2','w19'):8.22161,('q2','w20'):8.22161,('q2','w21'):8.22161,('q2','w36'):49.3311,('q2','w38'):49.3311,('q2','w40'):49.3311,('q2','w42'):49.3311,('q2','w57'):41.1088,('q2','w59'):41.1088,('q2','w61'):41.1088,('q2','w63'):41.1088,('q2','w85'):32.8868,('q2','w87'):32.8868,('q2','w89'):32.8868,('q2','w91'):32.8868,('q2','w120'):24.665,('q2','w123'):24.665,('q2','w125'):24.665,('q2','w126'):24.665,('q2','w156'):-73.995,('q2','w157'):-49.3298,('q2','w158'):-49.3298,('q2','w159'):-49.3298,('q2','w160'):-24.6648,('q2','w161'):-24.6648,('q2','w162'):-24.6648,('q2','w165'):-147.993,('q2','w168'):-147.993,('q2','w175'):-147.993,('q2','w178'):-123.327,('q2','w182'):-123.327,('q2','w190'):-123.327,('q2','w195'):-98.6605,('q2','w200'):-98.6605,('q2','w209'):-98.6605,('q2','w221'):-73.995,('q2','w222'):-73.995,('q3','q4'):-891.65,('q3','q5'):133.899,('q3','q6'):175.098,('q3','q7'):107.118,('q3','q8'):140.078,('q3','q9'):105.058,('q3','q10'):80.3382,('q3','q11'):53.5586,('q3','q12'):53.5586,('q3','q13'):26.7792,('q3','q14'):26.7792,('q3','w22'):16.4796,('q3','w25'):16.4796,('q3','w27'):16.4796,('q3','w28'):16.4796,('q3','w29'):8.23976,('q3','w32'):8.23976,('q3','w34'):8.23976,('q3','w35'):8.23976,('q3','w36'):49.3311,('q3','w39'):49.3311,('q3','w41'):49.3311,('q3','w42'):49.3311,('q3','w64'):41.1996,('q3','w65'):41.1996,('q3','w68'):41.1996,('q3','w69'):41.1996,('q3','w92'):32.9594,('q3','w93'):32.9594,('q3','w96'):32.9594,('q3','w97'):32.9594,('q3','w127'):24.7194,('q3','w129'):24.7194,('q3','w131'):24.7194,('q3','w133'):24.7194,('q3','w163'):-49.4387,('q3','w164'):-24.7193,('q3','w165'):-147.993,('q3','w169'):-147.993,('q3','w170'):-74.1583,('q3','w171'):-49.4387,('q3','w172'):-49.4387,('q3','w173'):-24.7193,('q3','w174'):-24.7193,('q3','w175'):-147.993,('q3','w179'):-123.599,('q3','w183'):-123.599,('q3','w191'):-123.599,('q3','w196'):-98.8783,('q3','w201'):-98.8783,('q3','w210'):-98.8783,('q3','w223'):-74.1583,('q3','w225'):-74.1583,('q4','q5'):133.899,('q4','q6'):175.098,('q4','q7'):107.118,('q4','q8'):140.078,('q4','q9'):105.058,('q4','q10'):80.3382,('q4','q11'):70.0381,('q4','q12'):70.0381,('q4','q13'):35.019,('q4','q14'):35.019,('q4','w22'):32.9591,('q4','w23'):16.4796,('q4','w24'):16.4796,('q4','w25'):16.4796,('q4','w26'):16.4796,('q4','w27'):16.4796,('q4','w28'):16.4796,('q4','w29'):16.4795,('q4','w30'):8.23976,('q4','w31'):8.23976,('q4','w32'):8.23976,('q4','w33'):8.23976,('q4','w34'):8.23976,('q4','w35'):8.23976,('q4','w36'):98.6621,('q4','w37'):49.3311,('q4','w38'):49.3311,('q4','w39'):49.3311,('q4','w40'):49.3311,('q4','w41'):49.3311,('q4','w42'):49.3311,('q4','w64'):41.1996,('q4','w66'):41.1996,('q4','w68'):41.1996,('q4','w70'):41.1996,('q4','w92'):32.9594,('q4','w94'):32.9594,('q4','w96'):32.9594,('q4','w98'):32.9594,('q4','w127'):24.7194,('q4','w130'):24.7194,('q4','w132'):24.7194,('q4','w133'):24.7194,('q4','w166'):-49.4387,('q4','w167'):-24.7193,('q4','w168'):-147.993,('q4','w169'):-147.993,('q4','w170'):-74.1583,('q4','w171'):-49.4387,('q4','w172'):-49.4387,('q4','w173'):-24.7193,('q4','w174'):-24.7193,('q4','w175'):-147.993,('q4','w179'):-123.599,('q4','w183'):-123.599,('q4','w192'):-123.599,('q4','w196'):-98.8783,('q4','w201'):-98.8783,('q4','w211'):-98.8783,('q4','w224'):-74.1583,('q4','w225'):-74.1583,('q5','q6'):-905.655,('q5','q7'):107.355,('q5','q8'):140.387,('q5','q9'):105.29,('q5','q10'):80.5155,('q5','q11'):53.6768,('q5','q12'):53.6768,('q5','q13'):26.8383,('q5','q14'):26.8383,('q5','w43'):16.5159,('q5','w46'):16.5159,('q5','w48'):16.5159,('q5','w49'):16.5159,('q5','w50'):8.25795,('q5','w53'):8.25795,('q5','w55'):8.25795,('q5','w56'):8.25795,('q5','w57'):41.1088,('q5','w60'):41.1088,('q5','w62'):41.1088,('q5','w63'):41.1088,('q5','w64'):41.1996,('q5','w67'):41.1996,('q5','w69'):41.1996,('q5','w70'):41.1996,('q5','w99'):33.0322,('q5','w100'):33.0322,('q5','w103'):33.0322,('q5','w104'):33.0322,('q5','w134'):24.774,('q5','w136'):24.774,('q5','w138'):24.774,('q5','w140'):24.774,('q5','w176'):-49.5478,('q5','w177'):-24.7738,('q5','w178'):-123.327,('q5','w179'):-123.599,('q5','w184'):-123.327,('q5','w185'):-74.322,('q5','w186'):-49.5478,('q5','w187'):-49.5478,('q5','w188'):-24.7738,('q5','w189'):-24.7738,('q5','w190'):-123.327,('q5','w191'):-123.599,('q5','w192'):-123.599,('q5','w197'):-99.0966,('q5','w202'):-99.0966,('q5','w212'):-99.0966,('q5','w226'):-74.322,('q5','w228'):-74.322,('q6','q7'):107.355,('q6','q8'):140.387,('q6','q9'):105.29,('q6','q10'):80.5155,('q6','q11'):70.1927,('q6','q12'):70.1927,('q6','q13'):35.0963,('q6','q14'):35.0963,('q6','w43'):33.0319,('q6','w44'):16.5159,('q6','w45'):16.5159,('q6','w46'):16.5159,('q6','w47'):16.5159,('q6','w48'):16.5159,('q6','w49'):16.5159,('q6','w50'):16.5159,('q6','w51'):8.25795,('q6','w52'):8.25795,('q6','w53'):8.25795,('q6','w54'):8.25795,('q6','w55'):8.25795,('q6','w56'):8.25795,('q6','w57'):82.2177,('q6','w58'):41.1088,('q6','w59'):41.1088,('q6','w60'):41.1088,('q6','w61'):41.1088,('q6','w62'):41.1088,('q6','w63'):41.1088,('q6','w64'):82.3992,('q6','w65'):41.1996,('q6','w66'):41.1996,('q6','w67'):41.1996,('q6','w68'):41.1996,('q6','w69'):41.1996,('q6','w70'):41.1996,('q6','w99'):33.0322,('q6','w101'):33.0322,('q6','w103'):33.0322,('q6','w105'):33.0322,('q6','w134'):24.774,('q6','w137'):24.774,('q6','w139'):24.774,('q6','w140'):24.774,('q6','w180'):-49.5478,('q6','w181'):-24.7738,('q6','w182'):-123.327,('q6','w183'):-123.599,('q6','w184'):-123.327,('q6','w185'):-74.322,('q6','w186'):-49.5478,('q6','w187'):-49.5478,('q6','w188'):-24.7738,('q6','w189'):-24.7738,('q6','w190'):-123.327,('q6','w191'):-123.599,('q6','w192'):-123.599,('q6','w197'):-99.0966,('q6','w202'):-99.0966,('q6','w213'):-99.0966,('q6','w227'):-74.322,('q6','w228'):-74.322,('q7','q8'):-943.501,('q7','q9'):105.522,('q7','q10'):80.6933,('q7','q11'):53.7953,('q7','q12'):53.7953,('q7','q13'):26.8976,('q7','q14'):26.8976,('q7','w71'):16.5524,('q7','w74'):16.5524,('q7','w76'):16.5524,('q7','w77'):16.5524,('q7','w78'):8.27618,('q7','w81'):8.27618,('q7','w83'):8.27618,('q7','w84'):8.27618,('q7','w85'):32.8868,('q7','w88'):32.8868,('q7','w90'):32.8868,('q7','w91'):32.8868,('q7','w92'):32.9594,('q7','w95'):32.9594,('q7','w97'):32.9594,('q7','w98'):32.9594,('q7','w99'):33.0322,('q7','w102'):33.0322,('q7','w104'):33.0322,('q7','w105'):33.0322,('q7','w141'):24.8287,('q7','w143'):24.8287,('q7','w145'):24.8287,('q7','w147'):24.8287,('q7','w193'):-49.6572,('q7','w194'):-24.8285,('q7','w195'):-98.6605,('q7','w196'):-98.8783,('q7','w197'):-99.0966,('q7','w203'):-98.6605,('q7','w204'):-74.4861,('q7','w205'):-49.6572,('q7','w206'):-49.6572,('q7','w207'):-24.8285,('q7','w208'):-24.8285,('q7','w209'):-98.6605,('q7','w210'):-98.8783,('q7','w211'):-98.8783,('q7','w212'):-99.0966,('q7','w213'):-99.0966,('q7','w229'):-74.4861,('q7','w231'):-74.4861,('q8','q9'):105.522,('q8','q10'):80.6933,('q8','q11'):70.3477,('q8','q12'):70.3477,('q8','q13'):35.1738,('q8','q14'):35.1738,('q8','w71'):33.1048,('q8','w72'):16.5524,('q8','w73'):16.5524,('q8','w74'):16.5524,('q8','w75'):16.5524,('q8','w76'):16.5524,('q8','w77'):16.5524,('q8','w78'):16.5524,('q8','w79'):8.27618,('q8','w80'):8.27618,('q8','w81'):8.27618,('q8','w82'):8.27618,('q8','w83'):8.27618,('q8','w84'):8.27618,('q8','w85'):65.7737,('q8','w86'):32.8868,('q8','w87'):32.8868,('q8','w88'):32.8868,('q8','w89'):32.8868,('q8','w90'):32.8868,('q8','w91'):32.8868,('q8','w92'):65.9189,('q8','w93'):32.9594,('q8','w94'):32.9594,('q8','w95'):32.9594,('q8','w96'):32.9594,('q8','w97'):32.9594,('q8','w98'):32.9594,('q8','w99'):66.0644,('q8','w100'):33.0322,('q8','w101'):33.0322,('q8','w102'):33.0322,('q8','w103'):33.0322,('q8','w104'):33.0322,('q8','w105'):33.0322,('q8','w141'):24.8287,('q8','w144'):24.8287,('q8','w146'):24.8287,('q8','w147'):24.8287,('q8','w198'):-49.6572,('q8','w199'):-24.8285,('q8','w200'):-98.6605,('q8','w201'):-98.8783,('q8','w202'):-99.0966,('q8','w203'):-98.6605,('q8','w204'):-74.4861,('q8','w205'):-49.6572,('q8','w206'):-49.6572,('q8','w207'):-24.8285,('q8','w208'):-24.8285,('q8','w209'):-98.6605,('q8','w210'):-98.8783,('q8','w211'):-98.8783,('q8','w212'):-99.0966,('q8','w213'):-99.0966,('q8','w230'):-74.4861,('q8','w231'):-74.4861,('q9','q10'):-1007.11,('q9','q11'):70.503,('q9','q12'):70.503,('q9','q13'):35.2514,('q9','q14'):35.2514,('q9','w106'):33.1779,('q9','w107'):16.5889,('q9','w108'):16.5889,('q9','w109'):16.5889,('q9','w110'):16.5889,('q9','w111'):16.5889,('q9','w112'):16.5889,('q9','w113'):16.5889,('q9','w114'):8.29445,('q9','w115'):8.29445,('q9','w116'):8.29445,('q9','w117'):8.29445,('q9','w118'):8.29445,('q9','w119'):8.29445,('q9','w120'):49.33,('q9','w121'):24.665,('q9','w122'):24.665,('q9','w123'):24.665,('q9','w124'):24.665,('q9','w125'):24.665,('q9','w126'):24.665,('q9','w127'):49.4389,('q9','w128'):24.7194,('q9','w129'):24.7194,('q9','w130'):24.7194,('q9','w131'):24.7194,('q9','w132'):24.7194,('q9','w133'):24.7194,('q9','w134'):49.548,('q9','w135'):24.774,('q9','w136'):24.774,('q9','w137'):24.774,('q9','w138'):24.774,('q9','w139'):24.774,('q9','w140'):24.774,('q9','w141'):49.6574,('q9','w142'):24.8287,('q9','w143'):24.8287,('q9','w144'):24.8287,('q9','w145'):24.8287,('q9','w146'):24.8287,('q9','w147'):24.8287,('q9','w214'):-73.995,('q9','w215'):-49.7668,('q9','w216'):-49.7668,('q9','w217'):-49.7668,('q9','w218'):-24.8834,('q9','w219'):-24.8834,('q9','w220'):-24.8834,('q9','w221'):-73.995,('q9','w222'):-73.995,('q9','w223'):-74.1583,('q9','w224'):-74.1583,('q9','w225'):-74.1583,('q9','w226'):-74.322,('q9','w227'):-74.322,('q9','w228'):-74.322,('q9','w229'):-74.4861,('q9','w230'):-74.4861,('q9','w231'):-74.4861,('q10','q11'):53.9141,('q10','q12'):53.9141,('q10','q13'):26.957,('q10','q14'):26.957,('q10','w106'):16.5889,('q10','w107'):16.5889,('q10','w110'):16.5889,('q10','w111'):16.5889,('q10','w113'):8.29445,('q10','w114'):8.29445,('q10','w117'):8.29445,('q10','w118'):8.29445,('q10','w120'):24.665,('q10','w122'):24.665,('q10','w124'):24.665,('q10','w126'):24.665,('q10','w127'):24.7194,('q10','w128'):24.7194,('q10','w131'):24.7194,('q10','w132'):24.7194,('q10','w134'):24.774,('q10','w135'):24.774,('q10','w138'):24.774,('q10','w139'):24.774,('q10','w141'):24.8287,('q10','w142'):24.8287,('q10','w145'):24.8287,('q10','w146'):24.8287,('q10','w149'):-49.7668,('q10','w153'):-24.8834,('q10','w156'):-73.995,('q10','w170'):-74.1583,('q10','w185'):-74.322,('q10','w204'):-74.4861,('q10','w214'):-73.995,('q10','w215'):-49.7668,('q10','w216'):-49.7668,('q10','w218'):-24.8834,('q10','w219'):-24.8834,('q10','w222'):-73.995,('q10','w223'):-74.1583,('q10','w224'):-74.1583,('q10','w226'):-74.322,('q10','w227'):-74.322,('q10','w229'):-74.4861,('q10','w230'):-74.4861,('q11','q12'):-1204.44,('q11','q13'):27.0165,('q11','q14'):35.3292,('q11','w1'):8.31276,('q11','w2'):8.31276,('q11','w5'):8.31276,('q11','w6'):8.31276,('q11','w8'):16.4433,('q11','w10'):16.4433,('q11','w12'):16.4433,('q11','w14'):16.4433,('q11','w22'):16.4796,('q11','w23'):16.4796,('q11','w26'):16.4796,('q11','w27'):16.4796,('q11','w43'):16.5159,('q11','w44'):16.5159,('q11','w47'):16.5159,('q11','w48'):16.5159,('q11','w71'):16.5524,('q11','w72'):16.5524,('q11','w75'):16.5524,('q11','w76'):16.5524,('q11','w106'):16.5889,('q11','w108'):16.5889,('q11','w110'):16.5889,('q11','w112'):16.5889,('q11','w148'):-49.3298,('q11','w149'):-49.7668,('q11','w150'):-24.9383,('q11','w151'):-24.9383,('q11','w154'):-24.9383,('q11','w157'):-49.3298,('q11','w159'):-49.3298,('q11','w163'):-49.4387,('q11','w166'):-49.4387,('q11','w171'):-49.4387,('q11','w176'):-49.5478,('q11','w180'):-49.5478,('q11','w186'):-49.5478,('q11','w193'):-49.6572,('q11','w198'):-49.6572,('q11','w205'):-49.6572,('q11','w215'):-49.7668,('q11','w217'):-49.7668,('q12','q13'):27.0165,('q12','q14'):35.3292,('q12','w1'):8.31276,('q12','w3'):8.31276,('q12','w5'):8.31276,('q12','w7'):8.31276,('q12','w8'):16.4433,('q12','w11'):16.4433,('q12','w13'):16.4433,('q12','w14'):16.4433,('q12','w22'):16.4796,('q12','w24'):16.4796,('q12','w26'):16.4796,('q12','w28'):16.4796,('q12','w43'):16.5159,('q12','w45'):16.5159,('q12','w47'):16.5159,('q12','w49'):16.5159,('q12','w71'):16.5524,('q12','w73'):16.5524,('q12','w75'):16.5524,('q12','w77'):16.5524,('q12','w106'):16.5889,('q12','w109'):16.5889,('q12','w111'):16.5889,('q12','w112'):16.5889,('q12','w148'):-49.3298,('q12','w149'):-49.7668,('q12','w150'):-24.9383,('q12','w151'):-24.9383,('q12','w155'):-24.9383,('q12','w158'):-49.3298,('q12','w159'):-49.3298,('q12','w163'):-49.4387,('q12','w166'):-49.4387,('q12','w172'):-49.4387,('q12','w176'):-49.5478,('q12','w180'):-49.5478,('q12','w187'):-49.5478,('q12','w193'):-49.6572,('q12','w198'):-49.6572,('q12','w206'):-49.6572,('q12','w216'):-49.7668,('q12','w217'):-49.7668,('q13','q14'):-1274.16,('q13','w1'):8.31276,('q13','w4'):8.31276,('q13','w6'):8.31276,('q13','w7'):8.31276,('q13','w15'):8.22161,('q13','w17'):8.22161,('q13','w19'):8.22161,('q13','w21'):8.22161,('q13','w29'):8.23976,('q13','w30'):8.23976,('q13','w33'):8.23976,('q13','w34'):8.23976,('q13','w50'):8.25795,('q13','w51'):8.25795,('q13','w54'):8.25795,('q13','w55'):8.25795,('q13','w78'):8.27618,('q13','w79'):8.27618,('q13','w82'):8.27618,('q13','w83'):8.27618,('q13','w113'):8.29445,('q13','w115'):8.29445,('q13','w117'):8.29445,('q13','w119'):8.29445,('q13','w150'):-24.9383,('q13','w152'):-24.6648,('q13','w153'):-24.8834,('q13','w154'):-24.9383,('q13','w155'):-24.9383,('q13','w160'):-24.6648,('q13','w162'):-24.6648,('q13','w164'):-24.7193,('q13','w167'):-24.7193,('q13','w173'):-24.7193,('q13','w177'):-24.7738,('q13','w181'):-24.7738,('q13','w188'):-24.7738,('q13','w194'):-24.8285,('q13','w199'):-24.8285,('q13','w207'):-24.8285,('q13','w218'):-24.8834,('q13','w220'):-24.8834,('q14','w1'):16.6255,('q14','w2'):8.31276,('q14','w3'):8.31276,('q14','w4'):8.31276,('q14','w5'):8.31276,('q14','w6'):8.31276,('q14','w7'):8.31276,('q14','w15'):8.22161,('q14','w18'):8.22161,('q14','w20'):8.22161,('q14','w21'):8.22161,('q14','w29'):8.23976,('q14','w31'):8.23976,('q14','w33'):8.23976,('q14','w35'):8.23976,('q14','w50'):8.25795,('q14','w52'):8.25795,('q14','w54'):8.25795,('q14','w56'):8.25795,('q14','w78'):8.27618,('q14','w80'):8.27618,('q14','w82'):8.27618,('q14','w84'):8.27618,('q14','w113'):8.29445,('q14','w116'):8.29445,('q14','w118'):8.29445,('q14','w119'):8.29445,('q14','w151'):-24.9383,('q14','w152'):-24.6648,('q14','w153'):-24.8834,('q14','w154'):-24.9383,('q14','w155'):-24.9383,('q14','w161'):-24.6648,('q14','w162'):-24.6648,('q14','w164'):-24.7193,('q14','w167'):-24.7193,('q14','w174'):-24.7193,('q14','w177'):-24.7738,('q14','w181'):-24.7738,('q14','w189'):-24.7738,('q14','w194'):-24.8285,('q14','w199'):-24.8285,('q14','w208'):-24.8285,('q14','w219'):-24.8834,('q14','w220'):-24.8834,('q15','q16'):-1367.27,('w1','w2'):8.31276,('w1','w3'):8.31276,('w1','w4'):8.31276,('w8','w9'):16.4433,('w8','w10'):16.4433,('w8','w11'):16.4433,('w15','w16'):8.22161,('w15','w17'):8.22161,('w15','w18'):8.22161,('w22','w23'):16.4796,('w22','w24'):16.4796,('w22','w25'):16.4796,('w29','w30'):8.23976,('w29','w31'):8.23976,('w29','w32'):8.23976,('w36','w37'):49.3311,('w36','w38'):49.3311,('w36','w39'):49.3311,('w43','w44'):16.5159,('w43','w45'):16.5159,('w43','w46'):16.5159,('w50','w51'):8.25795,('w50','w52'):8.25795,('w50','w53'):8.25795,('w57','w58'):41.1088,('w57','w59'):41.1088,('w57','w60'):41.1088,('w64','w65'):41.1996,('w64','w66'):41.1996,('w64','w67'):41.1996,('w71','w72'):16.5524,('w71','w73'):16.5524,('w71','w74'):16.5524,('w78','w79'):8.27618,('w78','w80'):8.27618,('w78','w81'):8.27618,('w85','w86'):32.8868,('w85','w87'):32.8868,('w85','w88'):32.8868,('w92','w93'):32.9594,('w92','w94'):32.9594,('w92','w95'):32.9594,('w99','w100'):33.0322,('w99','w101'):33.0322,('w99','w102'):33.0322,('w106','w107'):16.5889,('w106','w108'):16.5889,('w106','w109'):16.5889,('w113','w114'):8.29445,('w113','w115'):8.29445,('w113','w116'):8.29445,('w120','w121'):24.665,('w120','w122'):24.665,('w120','w123'):24.665,('w127','w128'):24.7194,('w127','w129'):24.7194,('w127','w130'):24.7194,('w134','w135'):24.774,('w134','w136'):24.774,('w134','w137'):24.774,('w141','w142'):24.8287,('w141','w143'):24.8287,('w141','w144'):24.8287}

Q={**linear, **quadratic}
sampleset=sampler_auto.sample_qubo(Q,num_reads=1000,label='RTU optimization 8steps')
print(sampleset)