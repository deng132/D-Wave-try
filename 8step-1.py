import numpy as np
np.set_printoptions(threshold=100000)
import pandas as pd
pd.set_option('display.max_columns', 100000)
pd.set_option('display.max_rows', 100000)
pd.set_option('display.width', 100000)
pd.set_option('display.max_colwidth', 100000)

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler_auto=EmbeddingComposite(DWaveSampler(solver={'topology__type':'pegasus'}))


linear={('q1','q1'):2122.51,('q2','q2'):2122.17,('q3','q3'):2074.99,('q4','q4'):2057.45,('q5','q5'):2053.18,('q6','q6'):2051.7,('q7','q7'):2055.3,('q8','q8'):2053.58,('q9','q9'):2052.53,('q10','q10'):2054.25,('q11','q11'):2058.54,('q12','q12'):2058.54,('q13','q13'):2062.97,('q14','q14'):2062.86,('q15','q15'):2067.55,('q16','q16'):2067.55,('w1','w1'):-0.173183,('w2','w2'):-0.0577275,('w3','w3'):-0.0577275,('w4','w4'):-0.0577275,('w5','w5'):-0.0577275,('w6','w6'):-0.0577275,('w7','w7'):-0.0577275,('w8','w8'):-0.342568,('w9','w9'):-0.114189,('w10','w10'):-0.114189,('w11','w11'):-0.114189,('w12','w12'):-0.114189,('w13','w13'):-0.114189,('w14','w14'):-0.114189,('w15','w15'):-0.171284,('w16','w16'):-0.0570945,('w17','w17'):-0.0570945,('w18','w18'):-0.0570945,('w19','w19'):-0.0570945,('w20','w20'):-0.0570945,('w21','w21'):-0.0570945,('w22','w22'):-0.343324,('w23','w23'):-0.114441,('w24','w24'):-0.114441,('w25','w25'):-0.114441,('w26','w26'):-0.114441,('w27','w27'):-0.114441,('w28','w28'):-0.114441,('w29','w29'):-0.171662,('w30','w30'):-0.0572206,('w31','w31'):-0.0572206,('w32','w32'):-0.0572206,('w33','w33'):-0.0572206,('w34','w34'):-0.0572206,('w35','w35'):-0.0572206,('w36','w36'):-25.7928,('w37','w37'):-8.59761,('w38','w38'):-8.59761,('w39','w39'):-8.59761,('w40','w40'):-8.59761,('w41','w41'):-8.59761,('w42','w42'):-8.59761,('w43','w43'):-0.344082,('w44','w44'):-0.114694,('w45','w45'):-0.114694,('w46','w46'):-0.114694,('w47','w47'):-0.114694,('w48','w48'):-0.114694,('w49','w49'):-0.114694,('w50','w50'):-0.172041,('w51','w51'):-0.0573469,('w52','w52'):-0.0573469,('w53','w53'):-0.0573469,('w54','w54'):-0.0573469,('w55','w55'):-0.0573469,('w56','w56'):-0.0573469,('w57','w57'):-0.856434,('w58','w58'):-0.285478,('w59','w59'):-0.285478,('w60','w60'):-0.285478,('w61','w61'):-0.285478,('w62','w62'):-0.285478,('w63','w63'):-0.285478,('w64','w64'):-0.858325,('w65','w65'):-0.286108,('w66','w66'):-0.286108,('w67','w67'):-0.286108,('w68','w68'):-0.286108,('w69','w69'):-0.286108,('w70','w70'):-0.286108,('w71','w71'):-0.344842,('w72','w72'):-0.114947,('w73','w73'):-0.114947,('w74','w74'):-0.114947,('w75','w75'):-0.114947,('w76','w76'):-0.114947,('w77','w77'):-0.114947,('w78','w78'):-0.17242,('w79','w79'):-0.0574735,('w80','w80'):-0.0574735,('w81','w81'):-0.0574735,('w82','w82'):-0.0574735,('w83','w83'):-0.0574735,('w84','w84'):-0.0574735,('w85','w85'):-0.685142,('w86','w86'):-0.228381,('w87','w87'):-0.228381,('w88','w88'):-0.228381,('w89','w89'):-0.228381,('w90','w90'):-0.228381,('w91','w91'):-0.228381,('w92','w92'):-0.686655,('w93','w93'):-0.228885,('w94','w94'):-0.228885,('w95','w95'):-0.228885,('w96','w96'):-0.228885,('w97','w97'):-0.228885,('w98','w98'):-0.228885,('w99','w99'):-0.688171,('w100','w100'):-0.22939,('w101','w101'):-0.22939,('w102','w102'):-0.22939,('w103','w103'):-0.22939,('w104','w104'):-0.22939,('w105','w105'):-0.22939,('w106','w106'):-0.345603,('w107','w107'):-0.115201,('w108','w108'):-0.115201,('w109','w109'):-0.115201,('w110','w110'):-0.115201,('w111','w111'):-0.115201,('w112','w112'):-0.115201,('w113','w113'):-0.172801,('w114','w114'):-0.0576004,('w115','w115'):-0.0576004,('w116','w116'):-0.0576004,('w117','w117'):-0.0576004,('w118','w118'):-0.0576004,('w119','w119'):-0.0576004,('w120','w120'):-0.513854,('w121','w121'):-0.171285,('w122','w122'):-0.171285,('w123','w123'):-0.171285,('w124','w124'):-0.171285,('w125','w125'):-0.171285,('w126','w126'):-0.171285,('w127','w127'):-0.514988,('w128','w128'):-0.171663,('w129','w129'):-0.171663,('w130','w130'):-0.171663,('w131','w131'):-0.171663,('w132','w132'):-0.171663,('w133','w133'):-0.171663,('w134','w134'):-0.516125,('w135','w135'):-0.172042,('w136','w136'):-0.172042,('w137','w137'):-0.172042,('w138','w138'):-0.172042,('w139','w139'):-0.172042,('w140','w140'):-0.172042,('w141','w141'):-0.517265,('w142','w142'):-0.172422,('w143','w143'):-0.172422,('w144','w144'):-0.172422,('w145','w145'):-0.172422,('w146','w146'):-0.172422,('w147','w147'):-0.172422,('w148','w148'):0.342568,('w149','w149'):0.345603,('w150','w150'):0.173183,('w151','w151'):0.173183,('w152','w152'):0.171284,('w153','w153'):0.172801,('w154','w154'):0.173183,('w155','w155'):0.173183,('w156','w156'):0.513854,('w157','w157'):0.342568,('w158','w158'):0.342568,('w159','w159'):0.342568,('w160','w160'):0.171284,('w161','w161'):0.171284,('w162','w162'):0.171284,('w163','w163'):0.343324,('w164','w164'):0.171662,('w165','w165'):25.7928,('w166','w166'):0.343324,('w167','w167'):0.171662,('w168','w168'):25.7928,('w169','w169'):25.7928,('w170','w170'):0.514988,('w171','w171'):0.343324,('w172','w172'):0.343324,('w173','w173'):0.171662,('w174','w174'):0.171662,('w175','w175'):25.7928,('w176','w176'):0.344082,('w177','w177'):0.172041,('w178','w178'):0.856434,('w179','w179'):0.858325,('w180','w180'):0.344082,('w181','w181'):0.172041,('w182','w182'):0.856434,('w183','w183'):0.858325,('w184','w184'):0.856434,('w185','w185'):0.516125,('w186','w186'):0.344082,('w187','w187'):0.344082,('w188','w188'):0.172041,('w189','w189'):0.172041,('w190','w190'):0.856434,('w191','w191'):0.858325,('w192','w192'):0.858325,('w193','w193'):0.344842,('w194','w194'):0.17242,('w195','w195'):0.685142,('w196','w196'):0.686655,('w197','w197'):0.688171,('w198','w198'):0.344842,('w199','w199'):0.17242,('w200','w200'):0.685142,('w201','w201'):0.686655,('w202','w202'):0.688171,('w203','w203'):0.685142,('w204','w204'):0.517265,('w205','w205'):0.344842,('w206','w206'):0.344842,('w207','w207'):0.17242,('w208','w208'):0.17242,('w209','w209'):0.685142,('w210','w210'):0.686655,('w211','w211'):0.686655,('w212','w212'):0.688171,('w213','w213'):0.688171,('w214','w214'):0.513854,('w215','w215'):0.345603,('w216','w216'):0.345603,('w217','w217'):0.345603,('w218','w218'):0.172801,('w219','w219'):0.172801,('w220','w220'):0.172801,('w221','w221'):0.513854,('w222','w222'):0.513854,('w223','w223'):0.514988,('w224','w224'):0.514988,('w225','w225'):0.514988,('w226','w226'):0.516125,('w227','w227'):0.516125,('w228','w228'):0.516125,('w229','w229'):0.517265,('w230','w230'):0.517265,('w231','w231'):0.517265}

quadratic={('q1','q2'):-1413.57,('q1','q3'):27.9422,('q1','q4'):36.5398,('q1','q5'):0.927804,('q1','q6'):1.21328,('q1','q7'):0.742238,('q1','q8'):0.970618,('q1','q9'):0.72796,('q1','q10'):0.556675,('q1','q11'):0.371115,('q1','q12'):0.371115,('q1','q13'):0.185557,('q1','q14'):0.185557,('q1','w8'):0.114189,('q1','w9'):0.114189,('q1','w12'):0.114189,('q1','w13'):0.114189,('q1','w15'):0.0570945,('q1','w16'):0.0570945,('q1','w19'):0.0570945,('q1','w20'):0.0570945,('q1','w36'):8.59761,('q1','w37'):8.59761,('q1','w40'):8.59761,('q1','w41'):8.59761,('q1','w57'):0.285478,('q1','w58'):0.285478,('q1','w61'):0.285478,('q1','w62'):0.285478,('q1','w85'):0.228381,('q1','w86'):0.228381,('q1','w89'):0.228381,('q1','w90'):0.228381,('q1','w120'):0.171285,('q1','w121'):0.171285,('q1','w124'):0.171285,('q1','w125'):0.171285,('q1','w148'):-0.171284,('q1','w152'):-0.0856418,('q1','w156'):-0.256927,('q1','w157'):-0.171284,('q1','w158'):-0.171284,('q1','w160'):-0.0856418,('q1','w161'):-0.0856418,('q1','w165'):-12.8964,('q1','w168'):-12.8964,('q1','w169'):-12.8964,('q1','w178'):-0.428217,('q1','w182'):-0.428217,('q1','w184'):-0.428217,('q1','w195'):-0.342571,('q1','w200'):-0.342571,('q1','w203'):-0.342571,('q1','w214'):-0.256927,('q1','w221'):-0.256927,('q2','q3'):27.9422,('q2','q4'):36.5398,('q2','q5'):0.927804,('q2','q6'):1.21328,('q2','q7'):0.742238,('q2','q8'):0.970618,('q2','q9'):0.72796,('q2','q10'):0.556675,('q2','q11'):0.485305,('q2','q12'):0.485305,('q2','q13'):0.242652,('q2','q14'):0.242652,('q2','w8'):0.228379,('q2','w9'):0.114189,('q2','w10'):0.114189,('q2','w11'):0.114189,('q2','w12'):0.114189,('q2','w13'):0.114189,('q2','w14'):0.114189,('q2','w15'):0.114189,('q2','w16'):0.0570945,('q2','w17'):0.0570945,('q2','w18'):0.0570945,('q2','w19'):0.0570945,('q2','w20'):0.0570945,('q2','w21'):0.0570945,('q2','w36'):8.59761,('q2','w38'):8.59761,('q2','w40'):8.59761,('q2','w42'):8.59761,('q2','w57'):0.285478,('q2','w59'):0.285478,('q2','w61'):0.285478,('q2','w63'):0.285478,('q2','w85'):0.228381,('q2','w87'):0.228381,('q2','w89'):0.228381,('q2','w91'):0.228381,('q2','w120'):0.171285,('q2','w123'):0.171285,('q2','w125'):0.171285,('q2','w126'):0.171285,('q2','w156'):-0.256927,('q2','w157'):-0.171284,('q2','w158'):-0.171284,('q2','w159'):-0.171284,('q2','w160'):-0.0856418,('q2','w161'):-0.0856418,('q2','w162'):-0.0856418,('q2','w165'):-12.8964,('q2','w168'):-12.8964,('q2','w175'):-12.8964,('q2','w178'):-0.428217,('q2','w182'):-0.428217,('q2','w190'):-0.428217,('q2','w195'):-0.342571,('q2','w200'):-0.342571,('q2','w209'):-0.342571,('q2','w221'):-0.256927,('q2','w222'):-0.256927,('q3','q4'):-1377.53,('q3','q5'):0.929852,('q3','q6'):1.21596,('q3','q7'):0.743876,('q3','q8'):0.972761,('q3','q9'):0.729567,('q3','q10'):0.557904,('q3','q11'):0.371934,('q3','q12'):0.371934,('q3','q13'):0.185967,('q3','q14'):0.185967,('q3','w22'):0.114441,('q3','w25'):0.114441,('q3','w27'):0.114441,('q3','w28'):0.114441,('q3','w29'):0.0572206,('q3','w32'):0.0572206,('q3','w34'):0.0572206,('q3','w35'):0.0572206,('q3','w36'):8.59761,('q3','w39'):8.59761,('q3','w41'):8.59761,('q3','w42'):8.59761,('q3','w64'):0.286108,('q3','w65'):0.286108,('q3','w68'):0.286108,('q3','w69'):0.286108,('q3','w92'):0.228885,('q3','w93'):0.228885,('q3','w96'):0.228885,('q3','w97'):0.228885,('q3','w127'):0.171663,('q3','w129'):0.171663,('q3','w131'):0.171663,('q3','w133'):0.171663,('q3','w163'):-0.171662,('q3','w164'):-0.0858308,('q3','w165'):-12.8964,('q3','w169'):-12.8964,('q3','w170'):-0.257494,('q3','w171'):-0.171662,('q3','w172'):-0.171662,('q3','w173'):-0.0858308,('q3','w174'):-0.0858308,('q3','w175'):-12.8964,('q3','w179'):-0.429162,('q3','w183'):-0.429162,('q3','w191'):-0.429162,('q3','w196'):-0.343327,('q3','w201'):-0.343327,('q3','w210'):-0.343327,('q3','w223'):-0.257494,('q3','w225'):-0.257494,('q4','q5'):0.929852,('q4','q6'):1.21596,('q4','q7'):0.743876,('q4','q8'):0.972761,('q4','q9'):0.729567,('q4','q10'):0.557904,('q4','q11'):0.486376,('q4','q12'):0.486376,('q4','q13'):0.243187,('q4','q14'):0.243187,('q4','w22'):0.228883,('q4','w23'):0.114441,('q4','w24'):0.114441,('q4','w25'):0.114441,('q4','w26'):0.114441,('q4','w27'):0.114441,('q4','w28'):0.114441,('q4','w29'):0.114441,('q4','w30'):0.0572206,('q4','w31'):0.0572206,('q4','w32'):0.0572206,('q4','w33'):0.0572206,('q4','w34'):0.0572206,('q4','w35'):0.0572206,('q4','w36'):17.1952,('q4','w37'):8.59761,('q4','w38'):8.59761,('q4','w39'):8.59761,('q4','w40'):8.59761,('q4','w41'):8.59761,('q4','w42'):8.59761,('q4','w64'):0.286108,('q4','w66'):0.286108,('q4','w68'):0.286108,('q4','w70'):0.286108,('q4','w92'):0.228885,('q4','w94'):0.228885,('q4','w96'):0.228885,('q4','w98'):0.228885,('q4','w127'):0.171663,('q4','w130'):0.171663,('q4','w132'):0.171663,('q4','w133'):0.171663,('q4','w166'):-0.171662,('q4','w167'):-0.0858308,('q4','w168'):-12.8964,('q4','w169'):-12.8964,('q4','w170'):-0.257494,('q4','w171'):-0.171662,('q4','w172'):-0.171662,('q4','w173'):-0.0858308,('q4','w174'):-0.0858308,('q4','w175'):-12.8964,('q4','w179'):-0.429162,('q4','w183'):-0.429162,('q4','w192'):-0.429162,('q4','w196'):-0.343327,('q4','w201'):-0.343327,('q4','w211'):-0.343327,('q4','w224'):-0.257494,('q4','w225'):-0.257494,('q5','q6'):-1366.78,('q5','q7'):0.745518,('q5','q8'):0.974909,('q5','q9'):0.731177,('q5','q10'):0.559136,('q5','q11'):0.372756,('q5','q12'):0.372756,('q5','q13'):0.186377,('q5','q14'):0.186377,('q5','w43'):0.114694,('q5','w46'):0.114694,('q5','w48'):0.114694,('q5','w49'):0.114694,('q5','w50'):0.0573469,('q5','w53'):0.0573469,('q5','w55'):0.0573469,('q5','w56'):0.0573469,('q5','w57'):0.285478,('q5','w60'):0.285478,('q5','w62'):0.285478,('q5','w63'):0.285478,('q5','w64'):0.286108,('q5','w67'):0.286108,('q5','w69'):0.286108,('q5','w70'):0.286108,('q5','w99'):0.22939,('q5','w100'):0.22939,('q5','w103'):0.22939,('q5','w104'):0.22939,('q5','w134'):0.172042,('q5','w136'):0.172042,('q5','w138'):0.172042,('q5','w140'):0.172042,('q5','w176'):-0.172041,('q5','w177'):-0.0860203,('q5','w178'):-0.428217,('q5','w179'):-0.429162,('q5','w184'):-0.428217,('q5','w185'):-0.258063,('q5','w186'):-0.172041,('q5','w187'):-0.172041,('q5','w188'):-0.0860203,('q5','w189'):-0.0860203,('q5','w190'):-0.428217,('q5','w191'):-0.429162,('q5','w192'):-0.429162,('q5','w197'):-0.344085,('q5','w202'):-0.344085,('q5','w212'):-0.344085,('q5','w226'):-0.258063,('q5','w228'):-0.258063,('q6','q7'):0.745518,('q6','q8'):0.974909,('q6','q9'):0.731177,('q6','q10'):0.559136,('q6','q11'):0.48745,('q6','q12'):0.48745,('q6','q13'):0.243724,('q6','q14'):0.243724,('q6','w43'):0.229388,('q6','w44'):0.114694,('q6','w45'):0.114694,('q6','w46'):0.114694,('q6','w47'):0.114694,('q6','w48'):0.114694,('q6','w49'):0.114694,('q6','w50'):0.114694,('q6','w51'):0.0573469,('q6','w52'):0.0573469,('q6','w53'):0.0573469,('q6','w54'):0.0573469,('q6','w55'):0.0573469,('q6','w56'):0.0573469,('q6','w57'):0.570956,('q6','w58'):0.285478,('q6','w59'):0.285478,('q6','w60'):0.285478,('q6','w61'):0.285478,('q6','w62'):0.285478,('q6','w63'):0.285478,('q6','w64'):0.572217,('q6','w65'):0.286108,('q6','w66'):0.286108,('q6','w67'):0.286108,('q6','w68'):0.286108,('q6','w69'):0.286108,('q6','w70'):0.286108,('q6','w99'):0.22939,('q6','w101'):0.22939,('q6','w103'):0.22939,('q6','w105'):0.22939,('q6','w134'):0.172042,('q6','w137'):0.172042,('q6','w139'):0.172042,('q6','w140'):0.172042,('q6','w180'):-0.172041,('q6','w181'):-0.0860203,('q6','w182'):-0.428217,('q6','w183'):-0.429162,('q6','w184'):-0.428217,('q6','w185'):-0.258063,('q6','w186'):-0.172041,('q6','w187'):-0.172041,('q6','w188'):-0.0860203,('q6','w189'):-0.0860203,('q6','w190'):-0.428217,('q6','w191'):-0.429162,('q6','w192'):-0.429162,('q6','w197'):-0.344085,('q6','w202'):-0.344085,('q6','w213'):-0.344085,('q6','w227'):-0.258063,('q6','w228'):-0.258063,('q7','q8'):-1368.29,('q7','q9'):0.732792,('q7','q10'):0.56037,('q7','q11'):0.373578,('q7','q12'):0.373578,('q7','q13'):0.186789,('q7','q14'):0.186789,('q7','w71'):0.114947,('q7','w74'):0.114947,('q7','w76'):0.114947,('q7','w77'):0.114947,('q7','w78'):0.0574735,('q7','w81'):0.0574735,('q7','w83'):0.0574735,('q7','w84'):0.0574735,('q7','w85'):0.228381,('q7','w88'):0.228381,('q7','w90'):0.228381,('q7','w91'):0.228381,('q7','w92'):0.228885,('q7','w95'):0.228885,('q7','w97'):0.228885,('q7','w98'):0.228885,('q7','w99'):0.22939,('q7','w102'):0.22939,('q7','w104'):0.22939,('q7','w105'):0.22939,('q7','w141'):0.172422,('q7','w143'):0.172422,('q7','w145'):0.172422,('q7','w147'):0.172422,('q7','w193'):-0.172421,('q7','w194'):-0.0862102,('q7','w195'):-0.342571,('q7','w196'):-0.343327,('q7','w197'):-0.344085,('q7','w203'):-0.342571,('q7','w204'):-0.258632,('q7','w205'):-0.172421,('q7','w206'):-0.172421,('q7','w207'):-0.0862102,('q7','w208'):-0.0862102,('q7','w209'):-0.342571,('q7','w210'):-0.343327,('q7','w211'):-0.343327,('q7','w212'):-0.344085,('q7','w213'):-0.344085,('q7','w229'):-0.258632,('q7','w231'):-0.258632,('q8','q9'):0.732792,('q8','q10'):0.56037,('q8','q11'):0.488526,('q8','q12'):0.488526,('q8','q13'):0.244262,('q8','q14'):0.244262,('q8','w71'):0.229894,('q8','w72'):0.114947,('q8','w73'):0.114947,('q8','w74'):0.114947,('q8','w75'):0.114947,('q8','w76'):0.114947,('q8','w77'):0.114947,('q8','w78'):0.114947,('q8','w79'):0.0574735,('q8','w80'):0.0574735,('q8','w81'):0.0574735,('q8','w82'):0.0574735,('q8','w83'):0.0574735,('q8','w84'):0.0574735,('q8','w85'):0.456762,('q8','w86'):0.228381,('q8','w87'):0.228381,('q8','w88'):0.228381,('q8','w89'):0.228381,('q8','w90'):0.228381,('q8','w91'):0.228381,('q8','w92'):0.45777,('q8','w93'):0.228885,('q8','w94'):0.228885,('q8','w95'):0.228885,('q8','w96'):0.228885,('q8','w97'):0.228885,('q8','w98'):0.228885,('q8','w99'):0.458781,('q8','w100'):0.22939,('q8','w101'):0.22939,('q8','w102'):0.22939,('q8','w103'):0.22939,('q8','w104'):0.22939,('q8','w105'):0.22939,('q8','w141'):0.172422,('q8','w144'):0.172422,('q8','w146'):0.172422,('q8','w147'):0.172422,('q8','w198'):-0.172421,('q8','w199'):-0.0862102,('q8','w200'):-0.342571,('q8','w201'):-0.343327,('q8','w202'):-0.344085,('q8','w203'):-0.342571,('q8','w204'):-0.258632,('q8','w205'):-0.172421,('q8','w206'):-0.172421,('q8','w207'):-0.0862102,('q8','w208'):-0.0862102,('q8','w209'):-0.342571,('q8','w210'):-0.343327,('q8','w211'):-0.343327,('q8','w212'):-0.344085,('q8','w213'):-0.344085,('q8','w230'):-0.258632,('q8','w231'):-0.258632,('q9','q10'):-1367.62,('q9','q11'):0.489604,('q9','q12'):0.489604,('q9','q13'):0.244802,('q9','q14'):0.244802,('q9','w106'):0.230402,('q9','w107'):0.115201,('q9','w108'):0.115201,('q9','w109'):0.115201,('q9','w110'):0.115201,('q9','w111'):0.115201,('q9','w112'):0.115201,('q9','w113'):0.115201,('q9','w114'):0.0576004,('q9','w115'):0.0576004,('q9','w116'):0.0576004,('q9','w117'):0.0576004,('q9','w118'):0.0576004,('q9','w119'):0.0576004,('q9','w120'):0.342569,('q9','w121'):0.171285,('q9','w122'):0.171285,('q9','w123'):0.171285,('q9','w124'):0.171285,('q9','w125'):0.171285,('q9','w126'):0.171285,('q9','w127'):0.343326,('q9','w128'):0.171663,('q9','w129'):0.171663,('q9','w130'):0.171663,('q9','w131'):0.171663,('q9','w132'):0.171663,('q9','w133'):0.171663,('q9','w134'):0.344083,('q9','w135'):0.172042,('q9','w136'):0.172042,('q9','w137'):0.172042,('q9','w138'):0.172042,('q9','w139'):0.172042,('q9','w140'):0.172042,('q9','w141'):0.344843,('q9','w142'):0.172422,('q9','w143'):0.172422,('q9','w144'):0.172422,('q9','w145'):0.172422,('q9','w146'):0.172422,('q9','w147'):0.172422,('q9','w214'):-0.256927,('q9','w215'):-0.172801,('q9','w216'):-0.172801,('q9','w217'):-0.172801,('q9','w218'):-0.0864005,('q9','w219'):-0.0864005,('q9','w220'):-0.0864005,('q9','w221'):-0.256927,('q9','w222'):-0.256927,('q9','w223'):-0.257494,('q9','w224'):-0.257494,('q9','w225'):-0.257494,('q9','w226'):-0.258063,('q9','w227'):-0.258063,('q9','w228'):-0.258063,('q9','w229'):-0.258632,('q9','w230'):-0.258632,('q9','w231'):-0.258632,('q10','q11'):0.374403,('q10','q12'):0.374403,('q10','q13'):0.187201,('q10','q14'):0.187201,('q10','w106'):0.115201,('q10','w107'):0.115201,('q10','w110'):0.115201,('q10','w111'):0.115201,('q10','w113'):0.0576004,('q10','w114'):0.0576004,('q10','w117'):0.0576004,('q10','w118'):0.0576004,('q10','w120'):0.171285,('q10','w122'):0.171285,('q10','w124'):0.171285,('q10','w126'):0.171285,('q10','w127'):0.171663,('q10','w128'):0.171663,('q10','w131'):0.171663,('q10','w132'):0.171663,('q10','w134'):0.172042,('q10','w135'):0.172042,('q10','w138'):0.172042,('q10','w139'):0.172042,('q10','w141'):0.172422,('q10','w142'):0.172422,('q10','w145'):0.172422,('q10','w146'):0.172422,('q10','w149'):-0.172801,('q10','w153'):-0.0864005,('q10','w156'):-0.256927,('q10','w170'):-0.257494,('q10','w185'):-0.258063,('q10','w204'):-0.258632,('q10','w214'):-0.256927,('q10','w215'):-0.172801,('q10','w216'):-0.172801,('q10','w218'):-0.0864005,('q10','w219'):-0.0864005,('q10','w222'):-0.256927,('q10','w223'):-0.257494,('q10','w224'):-0.257494,('q10','w226'):-0.258063,('q10','w227'):-0.258063,('q10','w229'):-0.258632,('q10','w230'):-0.258632,('q11','q12'):-1371.14,('q11','q13'):0.187614,('q11','q14'):0.245342,('q11','w1'):0.0577275,('q11','w2'):0.0577275,('q11','w5'):0.0577275,('q11','w6'):0.0577275,('q11','w8'):0.114189,('q11','w10'):0.114189,('q11','w12'):0.114189,('q11','w14'):0.114189,('q11','w22'):0.114441,('q11','w23'):0.114441,('q11','w26'):0.114441,('q11','w27'):0.114441,('q11','w43'):0.114694,('q11','w44'):0.114694,('q11','w47'):0.114694,('q11','w48'):0.114694,('q11','w71'):0.114947,('q11','w72'):0.114947,('q11','w75'):0.114947,('q11','w76'):0.114947,('q11','w106'):0.115201,('q11','w108'):0.115201,('q11','w110'):0.115201,('q11','w112'):0.115201,('q11','w148'):-0.171284,('q11','w149'):-0.172801,('q11','w150'):-0.0865913,('q11','w151'):-0.0865913,('q11','w154'):-0.0865913,('q11','w157'):-0.171284,('q11','w159'):-0.171284,('q11','w163'):-0.171662,('q11','w166'):-0.171662,('q11','w171'):-0.171662,('q11','w176'):-0.172041,('q11','w180'):-0.172041,('q11','w186'):-0.172041,('q11','w193'):-0.172421,('q11','w198'):-0.172421,('q11','w205'):-0.172421,('q11','w215'):-0.172801,('q11','w217'):-0.172801,('q12','q13'):0.187614,('q12','q14'):0.245342,('q12','w1'):0.0577275,('q12','w3'):0.0577275,('q12','w5'):0.0577275,('q12','w7'):0.0577275,('q12','w8'):0.114189,('q12','w11'):0.114189,('q12','w13'):0.114189,('q12','w14'):0.114189,('q12','w22'):0.114441,('q12','w24'):0.114441,('q12','w26'):0.114441,('q12','w28'):0.114441,('q12','w43'):0.114694,('q12','w45'):0.114694,('q12','w47'):0.114694,('q12','w49'):0.114694,('q12','w71'):0.114947,('q12','w73'):0.114947,('q12','w75'):0.114947,('q12','w77'):0.114947,('q12','w106'):0.115201,('q12','w109'):0.115201,('q12','w111'):0.115201,('q12','w112'):0.115201,('q12','w148'):-0.171284,('q12','w149'):-0.172801,('q12','w150'):-0.0865913,('q12','w151'):-0.0865913,('q12','w155'):-0.0865913,('q12','w158'):-0.171284,('q12','w159'):-0.171284,('q12','w163'):-0.171662,('q12','w166'):-0.171662,('q12','w172'):-0.171662,('q12','w176'):-0.172041,('q12','w180'):-0.172041,('q12','w187'):-0.172041,('q12','w193'):-0.172421,('q12','w198'):-0.172421,('q12','w206'):-0.172421,('q12','w216'):-0.172801,('q12','w217'):-0.172801,('q13','q14'):-1373.78,('q13','w1'):0.0577275,('q13','w4'):0.0577275,('q13','w6'):0.0577275,('q13','w7'):0.0577275,('q13','w15'):0.0570945,('q13','w17'):0.0570945,('q13','w19'):0.0570945,('q13','w21'):0.0570945,('q13','w29'):0.0572206,('q13','w30'):0.0572206,('q13','w33'):0.0572206,('q13','w34'):0.0572206,('q13','w50'):0.0573469,('q13','w51'):0.0573469,('q13','w54'):0.0573469,('q13','w55'):0.0573469,('q13','w78'):0.0574735,('q13','w79'):0.0574735,('q13','w82'):0.0574735,('q13','w83'):0.0574735,('q13','w113'):0.0576004,('q13','w115'):0.0576004,('q13','w117'):0.0576004,('q13','w119'):0.0576004,('q13','w150'):-0.0865913,('q13','w152'):-0.0856418,('q13','w153'):-0.0864005,('q13','w154'):-0.0865913,('q13','w155'):-0.0865913,('q13','w160'):-0.0856418,('q13','w162'):-0.0856418,('q13','w164'):-0.0858308,('q13','w167'):-0.0858308,('q13','w173'):-0.0858308,('q13','w177'):-0.0860203,('q13','w181'):-0.0860203,('q13','w188'):-0.0860203,('q13','w194'):-0.0862102,('q13','w199'):-0.0862102,('q13','w207'):-0.0862102,('q13','w218'):-0.0864005,('q13','w220'):-0.0864005,('q14','w1'):0.115455,('q14','w2'):0.0577275,('q14','w3'):0.0577275,('q14','w4'):0.0577275,('q14','w5'):0.0577275,('q14','w6'):0.0577275,('q14','w7'):0.0577275,('q14','w15'):0.0570945,('q14','w18'):0.0570945,('q14','w20'):0.0570945,('q14','w21'):0.0570945,('q14','w29'):0.0572206,('q14','w31'):0.0572206,('q14','w33'):0.0572206,('q14','w35'):0.0572206,('q14','w50'):0.0573469,('q14','w52'):0.0573469,('q14','w54'):0.0573469,('q14','w56'):0.0573469,('q14','w78'):0.0574735,('q14','w80'):0.0574735,('q14','w82'):0.0574735,('q14','w84'):0.0574735,('q14','w113'):0.0576004,('q14','w116'):0.0576004,('q14','w118'):0.0576004,('q14','w119'):0.0576004,('q14','w151'):-0.0865913,('q14','w152'):-0.0856418,('q14','w153'):-0.0864005,('q14','w154'):-0.0865913,('q14','w155'):-0.0865913,('q14','w161'):-0.0856418,('q14','w162'):-0.0856418,('q14','w164'):-0.0858308,('q14','w167'):-0.0858308,('q14','w174'):-0.0858308,('q14','w177'):-0.0860203,('q14','w181'):-0.0860203,('q14','w189'):-0.0860203,('q14','w194'):-0.0862102,('q14','w199'):-0.0862102,('q14','w208'):-0.0862102,('q14','w219'):-0.0864005,('q14','w220'):-0.0864005,('q15','q16'):-1376.57,('w1','w2'):0.0577275,('w1','w3'):0.0577275,('w1','w4'):0.0577275,('w8','w9'):0.114189,('w8','w10'):0.114189,('w8','w11'):0.114189,('w15','w16'):0.0570945,('w15','w17'):0.0570945,('w15','w18'):0.0570945,('w22','w23'):0.114441,('w22','w24'):0.114441,('w22','w25'):0.114441,('w29','w30'):0.0572206,('w29','w31'):0.0572206,('w29','w32'):0.0572206,('w36','w37'):8.59761,('w36','w38'):8.59761,('w36','w39'):8.59761,('w43','w44'):0.114694,('w43','w45'):0.114694,('w43','w46'):0.114694,('w50','w51'):0.0573469,('w50','w52'):0.0573469,('w50','w53'):0.0573469,('w57','w58'):0.285478,('w57','w59'):0.285478,('w57','w60'):0.285478,('w64','w65'):0.286108,('w64','w66'):0.286108,('w64','w67'):0.286108,('w71','w72'):0.114947,('w71','w73'):0.114947,('w71','w74'):0.114947,('w78','w79'):0.0574735,('w78','w80'):0.0574735,('w78','w81'):0.0574735,('w85','w86'):0.228381,('w85','w87'):0.228381,('w85','w88'):0.228381,('w92','w93'):0.228885,('w92','w94'):0.228885,('w92','w95'):0.228885,('w99','w100'):0.22939,('w99','w101'):0.22939,('w99','w102'):0.22939,('w106','w107'):0.115201,('w106','w108'):0.115201,('w106','w109'):0.115201,('w113','w114'):0.0576004,('w113','w115'):0.0576004,('w113','w116'):0.0576004,('w120','w121'):0.171285,('w120','w122'):0.171285,('w120','w123'):0.171285,('w127','w128'):0.171663,('w127','w129'):0.171663,('w127','w130'):0.171663,('w134','w135'):0.172042,('w134','w136'):0.172042,('w134','w137'):0.172042,('w141','w142'):0.172422,('w141','w143'):0.172422,('w141','w144'):0.172422}

Q={**linear, **quadratic}
sampleset=sampler_auto.sample_qubo(Q,num_reads=1000,label='RTU optimization 8steps')
print(sampleset)