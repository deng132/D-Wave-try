from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler_auto=EmbeddingComposite(DWaveSampler(solver={'topology__type':'pegasus'}))


linear={('q1','q1'):1590.97,('q2','q2'):1590.63,('q3','q3'):1600.23,('q4','q4'):1582.91,('q5','q5'):1606.78,('q6','q6'):1572.6,('q7','q7'):1612.13,('q8','q8'):1561.21,('q9','q9'):1550.09,('q10','q10'):1617.63,('q11','q11'):1934.37,('q12','q12'):1934.37,('q13','q13'):1931.6,('q14','q14'):1931.49,('q15','q15'):1939.53,('q16','q16'):1939.53,('w1','w1'):-0.173183,('w2','w2'):-0.0577275,('w3','w3'):-0.0577275,('w4','w4'):-0.0577275,('w5','w5'):-0.0577275,('w6','w6'):-0.0577275,('w7','w7'):-0.0577275,('w8','w8'):-0.342568,('w9','w9'):-0.114189,('w10','w10'):-0.114189,('w11','w11'):-0.114189,('w12','w12'):-0.114189,('w13','w13'):-0.114189,('w14','w14'):-0.114189,('w15','w15'):-0.171284,('w16','w16'):-0.0570945,('w17','w17'):-0.0570945,('w18','w18'):-0.0570945,('w19','w19'):-0.0570945,('w20','w20'):-0.0570945,('w21','w21'):-0.0570945,('w22','w22'):-0.343324,('w23','w23'):-0.114441,('w24','w24'):-0.114441,('w25','w25'):-0.114441,('w26','w26'):-0.114441,('w27','w27'):-0.114441,('w28','w28'):-0.114441,('w29','w29'):-0.171662,('w30','w30'):-0.0572206,('w31','w31'):-0.0572206,('w32','w32'):-0.0572206,('w33','w33'):-0.0572206,('w34','w34'):-0.0572206,('w35','w35'):-0.0572206,('w36','w36'):-25.4673,('w37','w37'):-8.48911,('w38','w38'):-8.48911,('w39','w39'):-8.48911,('w40','w40'):-8.48911,('w41','w41'):-8.48911,('w42','w42'):-8.48911,('w43','w43'):-0.344082,('w44','w44'):-0.114694,('w45','w45'):-0.114694,('w46','w46'):-0.114694,('w47','w47'):-0.114694,('w48','w48'):-0.114694,('w49','w49'):-0.114694,('w50','w50'):-0.172041,('w51','w51'):-0.0573469,('w52','w52'):-0.0573469,('w53','w53'):-0.0573469,('w54','w54'):-0.0573469,('w55','w55'):-0.0573469,('w56','w56'):-0.0573469,('w57','w57'):-25.35,('w58','w58'):-8.44999,('w59','w59'):-8.44999,('w60','w60'):-8.44999,('w61','w61'):-8.44999,('w62','w62'):-8.44999,('w63','w63'):-8.44999,('w64','w64'):-25.4059,('w65','w65'):-8.46865,('w66','w66'):-8.46865,('w67','w67'):-8.46865,('w68','w68'):-8.46865,('w69','w69'):-8.46865,('w70','w70'):-8.46865,('w71','w71'):-0.344842,('w72','w72'):-0.114947,('w73','w73'):-0.114947,('w74','w74'):-0.114947,('w75','w75'):-0.114947,('w76','w76'):-0.114947,('w77','w77'):-0.114947,('w78','w78'):-0.17242,('w79','w79'):-0.0574735,('w80','w80'):-0.0574735,('w81','w81'):-0.0574735,('w82','w82'):-0.0574735,('w83','w83'):-0.0574735,('w84','w84'):-0.0574735,('w85','w85'):-25.2328,('w86','w86'):-8.41092,('w87','w87'):-8.41092,('w88','w88'):-8.41092,('w89','w89'):-8.41092,('w90','w90'):-8.41092,('w91','w91'):-8.41092,('w92','w92'):-25.2885,('w93','w93'):-8.42949,('w94','w94'):-8.42949,('w95','w95'):-8.42949,('w96','w96'):-8.42949,('w97','w97'):-8.42949,('w98','w98'):-8.42949,('w99','w99'):-25.3443,('w100','w100'):-8.4481,('w101','w101'):-8.4481,('w102','w102'):-8.4481,('w103','w103'):-8.4481,('w104','w104'):-8.4481,('w105','w105'):-8.4481,('w106','w106'):-0.345603,('w107','w107'):-0.115201,('w108','w108'):-0.115201,('w109','w109'):-0.115201,('w110','w110'):-0.115201,('w111','w111'):-0.115201,('w112','w112'):-0.115201,('w113','w113'):-0.172801,('w114','w114'):-0.0576004,('w115','w115'):-0.0576004,('w116','w116'):-0.0576004,('w117','w117'):-0.0576004,('w118','w118'):-0.0576004,('w119','w119'):-0.0576004,('w120','w120'):-25.1157,('w121','w121'):-8.37189,('w122','w122'):-8.37189,('w123','w123'):-8.37189,('w124','w124'):-8.37189,('w125','w125'):-8.37189,('w126','w126'):-8.37189,('w127','w127'):-25.1711,('w128','w128'):-8.39037,('w129','w129'):-8.39037,('w130','w130'):-8.39037,('w131','w131'):-8.39037,('w132','w132'):-8.39037,('w133','w133'):-8.39037,('w134','w134'):-25.2267,('w135','w135'):-8.40889,('w136','w136'):-8.40889,('w137','w137'):-8.40889,('w138','w138'):-8.40889,('w139','w139'):-8.40889,('w140','w140'):-8.40889,('w141','w141'):-25.2824,('w142','w142'):-8.42746,('w143','w143'):-8.42746,('w144','w144'):-8.42746,('w145','w145'):-8.42746,('w146','w146'):-8.42746,('w147','w147'):-8.42746,('w148','w148'):0.342568,('w149','w149'):0.345603,('w150','w150'):0.173183,('w151','w151'):0.173183,('w152','w152'):0.171284,('w153','w153'):0.172801,('w154','w154'):0.173183,('w155','w155'):0.173183,('w156','w156'):25.1157,('w157','w157'):0.342568,('w158','w158'):0.342568,('w159','w159'):0.342568,('w160','w160'):0.171284,('w161','w161'):0.171284,('w162','w162'):0.171284,('w163','w163'):0.343324,('w164','w164'):0.171662,('w165','w165'):25.4673,('w166','w166'):0.343324,('w167','w167'):0.171662,('w168','w168'):25.4673,('w169','w169'):25.4673,('w170','w170'):25.1711,('w171','w171'):0.343324,('w172','w172'):0.343324,('w173','w173'):0.171662,('w174','w174'):0.171662,('w175','w175'):25.4673,('w176','w176'):0.344082,('w177','w177'):0.172041,('w178','w178'):25.35,('w179','w179'):25.4059,('w180','w180'):0.344082,('w181','w181'):0.172041,('w182','w182'):25.35,('w183','w183'):25.4059,('w184','w184'):25.35,('w185','w185'):25.2267,('w186','w186'):0.344082,('w187','w187'):0.344082,('w188','w188'):0.172041,('w189','w189'):0.172041,('w190','w190'):25.35,('w191','w191'):25.4059,('w192','w192'):25.4059,('w193','w193'):0.344842,('w194','w194'):0.17242,('w195','w195'):25.2328,('w196','w196'):25.2885,('w197','w197'):25.3443,('w198','w198'):0.344842,('w199','w199'):0.17242,('w200','w200'):25.2328,('w201','w201'):25.2885,('w202','w202'):25.3443,('w203','w203'):25.2328,('w204','w204'):25.2824,('w205','w205'):0.344842,('w206','w206'):0.344842,('w207','w207'):0.17242,('w208','w208'):0.17242,('w209','w209'):25.2328,('w210','w210'):25.2885,('w211','w211'):25.2885,('w212','w212'):25.3443,('w213','w213'):25.3443,('w214','w214'):25.1157,('w215','w215'):0.345603,('w216','w216'):0.345603,('w217','w217'):0.345603,('w218','w218'):0.172801,('w219','w219'):0.172801,('w220','w220'):0.172801,('w221','w221'):25.1157,('w222','w222'):25.1157,('w223','w223'):25.1711,('w224','w224'):25.1711,('w225','w225'):25.1711,('w226','w226'):25.2267,('w227','w227'):25.2267,('w228','w228'):25.2267,('w229','w229'):25.2824,('w230','w230'):25.2824,('w231','w231'):25.2824}

quadratic={('q1','q2'):-1093.93,('q1','q3'):27.5896,('q1','q4'):36.0787,('q1','q5'):27.4625,('q1','q6'):35.9125,('q1','q7'):27.3355,('q1','q8'):35.7464,('q1','q9'):35.5805,('q1','q10'):27.2086,('q1','q11'):0.371115,('q1','q12'):0.371115,('q1','q13'):0.185557,('q1','q14'):0.185557,('q1','w8'):0.114189,('q1','w9'):0.114189,('q1','w12'):0.114189,('q1','w13'):0.114189,('q1','w15'):0.0570945,('q1','w16'):0.0570945,('q1','w19'):0.0570945,('q1','w20'):0.0570945,('q1','w36'):8.48911,('q1','w37'):8.48911,('q1','w40'):8.48911,('q1','w41'):8.48911,('q1','w57'):8.44999,('q1','w58'):8.44999,('q1','w61'):8.44999,('q1','w62'):8.44999,('q1','w85'):8.41092,('q1','w86'):8.41092,('q1','w89'):8.41092,('q1','w90'):8.41092,('q1','w120'):8.37189,('q1','w121'):8.37189,('q1','w124'):8.37189,('q1','w125'):8.37189,('q1','w148'):-0.342568,('q1','w152'):-0.171284,('q1','w156'):-25.1157,('q1','w157'):-0.342568,('q1','w158'):-0.342568,('q1','w160'):-0.171284,('q1','w161'):-0.171284,('q1','w165'):-25.4673,('q1','w168'):-25.4673,('q1','w169'):-25.4673,('q1','w178'):-25.35,('q1','w182'):-25.35,('q1','w184'):-25.35,('q1','w195'):-25.2328,('q1','w200'):-25.2328,('q1','w203'):-25.2328,('q1','w214'):-25.1157,('q1','w221'):-25.1157,('q2','q3'):27.5896,('q2','q4'):36.0787,('q2','q5'):27.4625,('q2','q6'):35.9125,('q2','q7'):27.3355,('q2','q8'):35.7464,('q2','q9'):35.5805,('q2','q10'):27.2086,('q2','q11'):0.485305,('q2','q12'):0.485305,('q2','q13'):0.242652,('q2','q14'):0.242652,('q2','w8'):0.228379,('q2','w9'):0.114189,('q2','w10'):0.114189,('q2','w11'):0.114189,('q2','w12'):0.114189,('q2','w13'):0.114189,('q2','w14'):0.114189,('q2','w15'):0.114189,('q2','w16'):0.0570945,('q2','w17'):0.0570945,('q2','w18'):0.0570945,('q2','w19'):0.0570945,('q2','w20'):0.0570945,('q2','w21'):0.0570945,('q2','w36'):8.48911,('q2','w38'):8.48911,('q2','w40'):8.48911,('q2','w42'):8.48911,('q2','w57'):8.44999,('q2','w59'):8.44999,('q2','w61'):8.44999,('q2','w63'):8.44999,('q2','w85'):8.41092,('q2','w87'):8.41092,('q2','w89'):8.41092,('q2','w91'):8.41092,('q2','w120'):8.37189,('q2','w123'):8.37189,('q2','w125'):8.37189,('q2','w126'):8.37189,('q2','w156'):-25.1157,('q2','w157'):-0.342568,('q2','w158'):-0.342568,('q2','w159'):-0.342568,('q2','w160'):-0.171284,('q2','w161'):-0.171284,('q2','w162'):-0.171284,('q2','w165'):-25.4673,('q2','w168'):-25.4673,('q2','w175'):-25.4673,('q2','w178'):-25.35,('q2','w182'):-25.35,('q2','w190'):-25.35,('q2','w195'):-25.2328,('q2','w200'):-25.2328,('q2','w209'):-25.2328,('q2','w221'):-25.1157,('q2','w222'):-25.1157,('q3','q4'):-1091.01,('q3','q5'):27.5231,('q3','q6'):35.9918,('q3','q7'):27.3958,('q3','q8'):35.8253,('q3','q9'):35.6591,('q3','q10'):27.2687,('q3','q11'):0.371934,('q3','q12'):0.371934,('q3','q13'):0.185967,('q3','q14'):0.185967,('q3','w22'):0.114441,('q3','w25'):0.114441,('q3','w27'):0.114441,('q3','w28'):0.114441,('q3','w29'):0.0572206,('q3','w32'):0.0572206,('q3','w34'):0.0572206,('q3','w35'):0.0572206,('q3','w36'):8.48911,('q3','w39'):8.48911,('q3','w41'):8.48911,('q3','w42'):8.48911,('q3','w64'):8.46865,('q3','w65'):8.46865,('q3','w68'):8.46865,('q3','w69'):8.46865,('q3','w92'):8.42949,('q3','w93'):8.42949,('q3','w96'):8.42949,('q3','w97'):8.42949,('q3','w127'):8.39037,('q3','w129'):8.39037,('q3','w131'):8.39037,('q3','w133'):8.39037,('q3','w163'):-0.343324,('q3','w164'):-0.171662,('q3','w165'):-25.4673,('q3','w169'):-25.4673,('q3','w170'):-25.1711,('q3','w171'):-0.343324,('q3','w172'):-0.343324,('q3','w173'):-0.171662,('q3','w174'):-0.171662,('q3','w175'):-25.4673,('q3','w179'):-25.4059,('q3','w183'):-25.4059,('q3','w191'):-25.4059,('q3','w196'):-25.2885,('q3','w201'):-25.2885,('q3','w210'):-25.2885,('q3','w223'):-25.1711,('q3','w225'):-25.1711,('q4','q5'):27.5231,('q4','q6'):35.9918,('q4','q7'):27.3958,('q4','q8'):35.8253,('q4','q9'):35.6591,('q4','q10'):27.2687,('q4','q11'):0.486376,('q4','q12'):0.486376,('q4','q13'):0.243187,('q4','q14'):0.243187,('q4','w22'):0.228883,('q4','w23'):0.114441,('q4','w24'):0.114441,('q4','w25'):0.114441,('q4','w26'):0.114441,('q4','w27'):0.114441,('q4','w28'):0.114441,('q4','w29'):0.114441,('q4','w30'):0.0572206,('q4','w31'):0.0572206,('q4','w32'):0.0572206,('q4','w33'):0.0572206,('q4','w34'):0.0572206,('q4','w35'):0.0572206,('q4','w36'):16.9782,('q4','w37'):8.48911,('q4','w38'):8.48911,('q4','w39'):8.48911,('q4','w40'):8.48911,('q4','w41'):8.48911,('q4','w42'):8.48911,('q4','w64'):8.46865,('q4','w66'):8.46865,('q4','w68'):8.46865,('q4','w70'):8.46865,('q4','w92'):8.42949,('q4','w94'):8.42949,('q4','w96'):8.42949,('q4','w98'):8.42949,('q4','w127'):8.39037,('q4','w130'):8.39037,('q4','w132'):8.39037,('q4','w133'):8.39037,('q4','w166'):-0.343324,('q4','w167'):-0.171662,('q4','w168'):-25.4673,('q4','w169'):-25.4673,('q4','w170'):-25.1711,('q4','w171'):-0.343324,('q4','w172'):-0.343324,('q4','w173'):-0.171662,('q4','w174'):-0.171662,('q4','w175'):-25.4673,('q4','w179'):-25.4059,('q4','w183'):-25.4059,('q4','w192'):-25.4059,('q4','w196'):-25.2885,('q4','w201'):-25.2885,('q4','w211'):-25.2885,('q4','w224'):-25.1711,('q4','w225'):-25.1711,('q5','q6'):-1086.88,('q5','q7'):27.4563,('q5','q8'):35.9044,('q5','q9'):35.7378,('q5','q10'):27.3289,('q5','q11'):0.372756,('q5','q12'):0.372756,('q5','q13'):0.186377,('q5','q14'):0.186377,('q5','w43'):0.114694,('q5','w46'):0.114694,('q5','w48'):0.114694,('q5','w49'):0.114694,('q5','w50'):0.0573469,('q5','w53'):0.0573469,('q5','w55'):0.0573469,('q5','w56'):0.0573469,('q5','w57'):8.44999,('q5','w60'):8.44999,('q5','w62'):8.44999,('q5','w63'):8.44999,('q5','w64'):8.46865,('q5','w67'):8.46865,('q5','w69'):8.46865,('q5','w70'):8.46865,('q5','w99'):8.4481,('q5','w100'):8.4481,('q5','w103'):8.4481,('q5','w104'):8.4481,('q5','w134'):8.40889,('q5','w136'):8.40889,('q5','w138'):8.40889,('q5','w140'):8.40889,('q5','w176'):-0.344082,('q5','w177'):-0.172041,('q5','w178'):-25.35,('q5','w179'):-25.4059,('q5','w184'):-25.35,('q5','w185'):-25.2267,('q5','w186'):-0.344082,('q5','w187'):-0.344082,('q5','w188'):-0.172041,('q5','w189'):-0.172041,('q5','w190'):-25.35,('q5','w191'):-25.4059,('q5','w192'):-25.4059,('q5','w197'):-25.3443,('q5','w202'):-25.3443,('q5','w212'):-25.3443,('q5','w226'):-25.2267,('q5','w228'):-25.2267,('q6','q7'):27.4563,('q6','q8'):35.9044,('q6','q9'):35.7378,('q6','q10'):27.3289,('q6','q11'):0.48745,('q6','q12'):0.48745,('q6','q13'):0.243724,('q6','q14'):0.243724,('q6','w43'):0.229388,('q6','w44'):0.114694,('q6','w45'):0.114694,('q6','w46'):0.114694,('q6','w47'):0.114694,('q6','w48'):0.114694,('q6','w49'):0.114694,('q6','w50'):0.114694,('q6','w51'):0.0573469,('q6','w52'):0.0573469,('q6','w53'):0.0573469,('q6','w54'):0.0573469,('q6','w55'):0.0573469,('q6','w56'):0.0573469,('q6','w57'):16.9,('q6','w58'):8.44999,('q6','w59'):8.44999,('q6','w60'):8.44999,('q6','w61'):8.44999,('q6','w62'):8.44999,('q6','w63'):8.44999,('q6','w64'):16.9373,('q6','w65'):8.46865,('q6','w66'):8.46865,('q6','w67'):8.46865,('q6','w68'):8.46865,('q6','w69'):8.46865,('q6','w70'):8.46865,('q6','w99'):8.4481,('q6','w101'):8.4481,('q6','w103'):8.4481,('q6','w105'):8.4481,('q6','w134'):8.40889,('q6','w137'):8.40889,('q6','w139'):8.40889,('q6','w140'):8.40889,('q6','w180'):-0.344082,('q6','w181'):-0.172041,('q6','w182'):-25.35,('q6','w183'):-25.4059,('q6','w184'):-25.35,('q6','w185'):-25.2267,('q6','w186'):-0.344082,('q6','w187'):-0.344082,('q6','w188'):-0.172041,('q6','w189'):-0.172041,('q6','w190'):-25.35,('q6','w191'):-25.4059,('q6','w192'):-25.4059,('q6','w197'):-25.3443,('q6','w202'):-25.3443,('q6','w213'):-25.3443,('q6','w227'):-25.2267,('q6','w228'):-25.2267,('q7','q8'):-1082.03,('q7','q9'):35.8167,('q7','q10'):27.3892,('q7','q11'):0.373578,('q7','q12'):0.373578,('q7','q13'):0.186789,('q7','q14'):0.186789,('q7','w71'):0.114947,('q7','w74'):0.114947,('q7','w76'):0.114947,('q7','w77'):0.114947,('q7','w78'):0.0574735,('q7','w81'):0.0574735,('q7','w83'):0.0574735,('q7','w84'):0.0574735,('q7','w85'):8.41092,('q7','w88'):8.41092,('q7','w90'):8.41092,('q7','w91'):8.41092,('q7','w92'):8.42949,('q7','w95'):8.42949,('q7','w97'):8.42949,('q7','w98'):8.42949,('q7','w99'):8.4481,('q7','w102'):8.4481,('q7','w104'):8.4481,('q7','w105'):8.4481,('q7','w141'):8.42746,('q7','w143'):8.42746,('q7','w145'):8.42746,('q7','w147'):8.42746,('q7','w193'):-0.344842,('q7','w194'):-0.17242,('q7','w195'):-25.2328,('q7','w196'):-25.2885,('q7','w197'):-25.3443,('q7','w203'):-25.2328,('q7','w204'):-25.2824,('q7','w205'):-0.344842,('q7','w206'):-0.344842,('q7','w207'):-0.17242,('q7','w208'):-0.17242,('q7','w209'):-25.2328,('q7','w210'):-25.2885,('q7','w211'):-25.2885,('q7','w212'):-25.3443,('q7','w213'):-25.3443,('q7','w229'):-25.2824,('q7','w231'):-25.2824,('q8','q9'):35.8167,('q8','q10'):27.3892,('q8','q11'):0.488526,('q8','q12'):0.488526,('q8','q13'):0.244262,('q8','q14'):0.244262,('q8','w71'):0.229894,('q8','w72'):0.114947,('q8','w73'):0.114947,('q8','w74'):0.114947,('q8','w75'):0.114947,('q8','w76'):0.114947,('q8','w77'):0.114947,('q8','w78'):0.114947,('q8','w79'):0.0574735,('q8','w80'):0.0574735,('q8','w81'):0.0574735,('q8','w82'):0.0574735,('q8','w83'):0.0574735,('q8','w84'):0.0574735,('q8','w85'):16.8218,('q8','w86'):8.41092,('q8','w87'):8.41092,('q8','w88'):8.41092,('q8','w89'):8.41092,('q8','w90'):8.41092,('q8','w91'):8.41092,('q8','w92'):16.859,('q8','w93'):8.42949,('q8','w94'):8.42949,('q8','w95'):8.42949,('q8','w96'):8.42949,('q8','w97'):8.42949,('q8','w98'):8.42949,('q8','w99'):16.8962,('q8','w100'):8.4481,('q8','w101'):8.4481,('q8','w102'):8.4481,('q8','w103'):8.4481,('q8','w104'):8.4481,('q8','w105'):8.4481,('q8','w141'):8.42746,('q8','w144'):8.42746,('q8','w146'):8.42746,('q8','w147'):8.42746,('q8','w198'):-0.344842,('q8','w199'):-0.17242,('q8','w200'):-25.2328,('q8','w201'):-25.2885,('q8','w202'):-25.3443,('q8','w203'):-25.2328,('q8','w204'):-25.2824,('q8','w205'):-0.344842,('q8','w206'):-0.344842,('q8','w207'):-0.17242,('q8','w208'):-0.17242,('q8','w209'):-25.2328,('q8','w210'):-25.2885,('q8','w211'):-25.2885,('q8','w212'):-25.3443,('q8','w213'):-25.3443,('q8','w230'):-25.2824,('q8','w231'):-25.2824,('q9','q10'):-1077.28,('q9','q11'):0.489604,('q9','q12'):0.489604,('q9','q13'):0.244802,('q9','q14'):0.244802,('q9','w106'):0.230402,('q9','w107'):0.115201,('q9','w108'):0.115201,('q9','w109'):0.115201,('q9','w110'):0.115201,('q9','w111'):0.115201,('q9','w112'):0.115201,('q9','w113'):0.115201,('q9','w114'):0.0576004,('q9','w115'):0.0576004,('q9','w116'):0.0576004,('q9','w117'):0.0576004,('q9','w118'):0.0576004,('q9','w119'):0.0576004,('q9','w120'):16.7438,('q9','w121'):8.37189,('q9','w122'):8.37189,('q9','w123'):8.37189,('q9','w124'):8.37189,('q9','w125'):8.37189,('q9','w126'):8.37189,('q9','w127'):16.7807,('q9','w128'):8.39037,('q9','w129'):8.39037,('q9','w130'):8.39037,('q9','w131'):8.39037,('q9','w132'):8.39037,('q9','w133'):8.39037,('q9','w134'):16.8178,('q9','w135'):8.40889,('q9','w136'):8.40889,('q9','w137'):8.40889,('q9','w138'):8.40889,('q9','w139'):8.40889,('q9','w140'):8.40889,('q9','w141'):16.8549,('q9','w142'):8.42746,('q9','w143'):8.42746,('q9','w144'):8.42746,('q9','w145'):8.42746,('q9','w146'):8.42746,('q9','w147'):8.42746,('q9','w214'):-25.1157,('q9','w215'):-0.345603,('q9','w216'):-0.345603,('q9','w217'):-0.345603,('q9','w218'):-0.172801,('q9','w219'):-0.172801,('q9','w220'):-0.172801,('q9','w221'):-25.1157,('q9','w222'):-25.1157,('q9','w223'):-25.1711,('q9','w224'):-25.1711,('q9','w225'):-25.1711,('q9','w226'):-25.2267,('q9','w227'):-25.2267,('q9','w228'):-25.2267,('q9','w229'):-25.2824,('q9','w230'):-25.2824,('q9','w231'):-25.2824,('q10','q11'):0.374403,('q10','q12'):0.374403,('q10','q13'):0.187201,('q10','q14'):0.187201,('q10','w106'):0.115201,('q10','w107'):0.115201,('q10','w110'):0.115201,('q10','w111'):0.115201,('q10','w113'):0.0576004,('q10','w114'):0.0576004,('q10','w117'):0.0576004,('q10','w118'):0.0576004,('q10','w120'):8.37189,('q10','w122'):8.37189,('q10','w124'):8.37189,('q10','w126'):8.37189,('q10','w127'):8.39037,('q10','w128'):8.39037,('q10','w131'):8.39037,('q10','w132'):8.39037,('q10','w134'):8.40889,('q10','w135'):8.40889,('q10','w138'):8.40889,('q10','w139'):8.40889,('q10','w141'):8.42746,('q10','w142'):8.42746,('q10','w145'):8.42746,('q10','w146'):8.42746,('q10','w149'):-0.345603,('q10','w153'):-0.172801,('q10','w156'):-25.1157,('q10','w170'):-25.1711,('q10','w185'):-25.2267,('q10','w204'):-25.2824,('q10','w214'):-25.1157,('q10','w215'):-0.345603,('q10','w216'):-0.345603,('q10','w218'):-0.172801,('q10','w219'):-0.172801,('q10','w222'):-25.1157,('q10','w223'):-25.1711,('q10','w224'):-25.1711,('q10','w226'):-25.2267,('q10','w227'):-25.2267,('q10','w229'):-25.2824,('q10','w230'):-25.2824,('q11','q12'):-1293.76,('q11','q13'):0.187614,('q11','q14'):0.245342,('q11','w1'):0.0577275,('q11','w2'):0.0577275,('q11','w5'):0.0577275,('q11','w6'):0.0577275,('q11','w8'):0.114189,('q11','w10'):0.114189,('q11','w12'):0.114189,('q11','w14'):0.114189,('q11','w22'):0.114441,('q11','w23'):0.114441,('q11','w26'):0.114441,('q11','w27'):0.114441,('q11','w43'):0.114694,('q11','w44'):0.114694,('q11','w47'):0.114694,('q11','w48'):0.114694,('q11','w71'):0.114947,('q11','w72'):0.114947,('q11','w75'):0.114947,('q11','w76'):0.114947,('q11','w106'):0.115201,('q11','w108'):0.115201,('q11','w110'):0.115201,('q11','w112'):0.115201,('q11','w148'):-0.342568,('q11','w149'):-0.345603,('q11','w150'):-0.173183,('q11','w151'):-0.173183,('q11','w154'):-0.173183,('q11','w157'):-0.342568,('q11','w159'):-0.342568,('q11','w163'):-0.343324,('q11','w166'):-0.343324,('q11','w171'):-0.343324,('q11','w176'):-0.344082,('q11','w180'):-0.344082,('q11','w186'):-0.344082,('q11','w193'):-0.344842,('q11','w198'):-0.344842,('q11','w205'):-0.344842,('q11','w215'):-0.345603,('q11','w217'):-0.345603,('q12','q13'):0.187614,('q12','q14'):0.245342,('q12','w1'):0.0577275,('q12','w3'):0.0577275,('q12','w5'):0.0577275,('q12','w7'):0.0577275,('q12','w8'):0.114189,('q12','w11'):0.114189,('q12','w13'):0.114189,('q12','w14'):0.114189,('q12','w22'):0.114441,('q12','w24'):0.114441,('q12','w26'):0.114441,('q12','w28'):0.114441,('q12','w43'):0.114694,('q12','w45'):0.114694,('q12','w47'):0.114694,('q12','w49'):0.114694,('q12','w71'):0.114947,('q12','w73'):0.114947,('q12','w75'):0.114947,('q12','w77'):0.114947,('q12','w106'):0.115201,('q12','w109'):0.115201,('q12','w111'):0.115201,('q12','w112'):0.115201,('q12','w148'):-0.342568,('q12','w149'):-0.345603,('q12','w150'):-0.173183,('q12','w151'):-0.173183,('q12','w155'):-0.173183,('q12','w158'):-0.342568,('q12','w159'):-0.342568,('q12','w163'):-0.343324,('q12','w166'):-0.343324,('q12','w172'):-0.343324,('q12','w176'):-0.344082,('q12','w180'):-0.344082,('q12','w187'):-0.344082,('q12','w193'):-0.344842,('q12','w198'):-0.344842,('q12','w206'):-0.344842,('q12','w216'):-0.345603,('q12','w217'):-0.345603,('q13','q14'):-1291.6,('q13','w1'):0.0577275,('q13','w4'):0.0577275,('q13','w6'):0.0577275,('q13','w7'):0.0577275,('q13','w15'):0.0570945,('q13','w17'):0.0570945,('q13','w19'):0.0570945,('q13','w21'):0.0570945,('q13','w29'):0.0572206,('q13','w30'):0.0572206,('q13','w33'):0.0572206,('q13','w34'):0.0572206,('q13','w50'):0.0573469,('q13','w51'):0.0573469,('q13','w54'):0.0573469,('q13','w55'):0.0573469,('q13','w78'):0.0574735,('q13','w79'):0.0574735,('q13','w82'):0.0574735,('q13','w83'):0.0574735,('q13','w113'):0.0576004,('q13','w115'):0.0576004,('q13','w117'):0.0576004,('q13','w119'):0.0576004,('q13','w150'):-0.173183,('q13','w152'):-0.171284,('q13','w153'):-0.172801,('q13','w154'):-0.173183,('q13','w155'):-0.173183,('q13','w160'):-0.171284,('q13','w162'):-0.171284,('q13','w164'):-0.171662,('q13','w167'):-0.171662,('q13','w173'):-0.171662,('q13','w177'):-0.172041,('q13','w181'):-0.172041,('q13','w188'):-0.172041,('q13','w194'):-0.17242,('q13','w199'):-0.17242,('q13','w207'):-0.17242,('q13','w218'):-0.172801,('q13','w220'):-0.172801,('q14','w1'):0.115455,('q14','w2'):0.0577275,('q14','w3'):0.0577275,('q14','w4'):0.0577275,('q14','w5'):0.0577275,('q14','w6'):0.0577275,('q14','w7'):0.0577275,('q14','w15'):0.0570945,('q14','w18'):0.0570945,('q14','w20'):0.0570945,('q14','w21'):0.0570945,('q14','w29'):0.0572206,('q14','w31'):0.0572206,('q14','w33'):0.0572206,('q14','w35'):0.0572206,('q14','w50'):0.0573469,('q14','w52'):0.0573469,('q14','w54'):0.0573469,('q14','w56'):0.0573469,('q14','w78'):0.0574735,('q14','w80'):0.0574735,('q14','w82'):0.0574735,('q14','w84'):0.0574735,('q14','w113'):0.0576004,('q14','w116'):0.0576004,('q14','w118'):0.0576004,('q14','w119'):0.0576004,('q14','w151'):-0.173183,('q14','w152'):-0.171284,('q14','w153'):-0.172801,('q14','w154'):-0.173183,('q14','w155'):-0.173183,('q14','w161'):-0.171284,('q14','w162'):-0.171284,('q14','w164'):-0.171662,('q14','w167'):-0.171662,('q14','w174'):-0.171662,('q14','w177'):-0.172041,('q14','w181'):-0.172041,('q14','w189'):-0.172041,('q14','w194'):-0.17242,('q14','w199'):-0.17242,('q14','w208'):-0.17242,('q14','w219'):-0.172801,('q14','w220'):-0.172801,('q15','q16'):-1296.56,('w1','w2'):0.0577275,('w1','w3'):0.0577275,('w1','w4'):0.0577275,('w8','w9'):0.114189,('w8','w10'):0.114189,('w8','w11'):0.114189,('w15','w16'):0.0570945,('w15','w17'):0.0570945,('w15','w18'):0.0570945,('w22','w23'):0.114441,('w22','w24'):0.114441,('w22','w25'):0.114441,('w29','w30'):0.0572206,('w29','w31'):0.0572206,('w29','w32'):0.0572206,('w36','w37'):8.48911,('w36','w38'):8.48911,('w36','w39'):8.48911,('w43','w44'):0.114694,('w43','w45'):0.114694,('w43','w46'):0.114694,('w50','w51'):0.0573469,('w50','w52'):0.0573469,('w50','w53'):0.0573469,('w57','w58'):8.44999,('w57','w59'):8.44999,('w57','w60'):8.44999,('w64','w65'):8.46865,('w64','w66'):8.46865,('w64','w67'):8.46865,('w71','w72'):0.114947,('w71','w73'):0.114947,('w71','w74'):0.114947,('w78','w79'):0.0574735,('w78','w80'):0.0574735,('w78','w81'):0.0574735,('w85','w86'):8.41092,('w85','w87'):8.41092,('w85','w88'):8.41092,('w92','w93'):8.42949,('w92','w94'):8.42949,('w92','w95'):8.42949,('w99','w100'):8.4481,('w99','w101'):8.4481,('w99','w102'):8.4481,('w106','w107'):0.115201,('w106','w108'):0.115201,('w106','w109'):0.115201,('w113','w114'):0.0576004,('w113','w115'):0.0576004,('w113','w116'):0.0576004,('w120','w121'):8.37189,('w120','w122'):8.37189,('w120','w123'):8.37189,('w127','w128'):8.39037,('w127','w129'):8.39037,('w127','w130'):8.39037,('w134','w135'):8.40889,('w134','w136'):8.40889,('w134','w137'):8.40889,('w141','w142'):8.42746,('w141','w143'):8.42746,('w141','w144'):8.42746}

Q={**linear, **quadratic}
sampleset=sampler_auto.sample_qubo(Q,num_reads=1000,label='RTU optimization 8steps')
print(sampleset)