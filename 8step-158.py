from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler_auto=EmbeddingComposite(DWaveSampler(solver={'topology__type':'pegasus'}))


linear={('q1','q1'):-214.734,('q2','q2'):-214.734,('q3','q3'):10.6177,('q4','q4'):10.6177,('q5','q5'):263.809,('q6','q6'):263.809,('q7','q7'):540.879,('q8','q8'):540.879,('q9','q9'):841.362,('q10','q10'):841.362,('q11','q11'):1153.67,('q12','q12'):1153.67,('q13','q13'):1500.21,('q14','q14'):1500.21,('q15','q15'):1843.32,('q16','q16'):1843.32,('w1','w1'):24.9383,('w2','w2'):49.3298,('w3','w3'):24.6648,('w4','w4'):49.4387,('w5','w5'):24.7193,('w6','w6'):147.993,('w7','w7'):49.5478,('w8','w8'):24.7738,('w9','w9'):123.327,('w10','w10'):123.599,('w11','w11'):49.6572,('w12','w12'):24.8285,('w13','w13'):98.6605,('w14','w14'):98.8783,('w15','w15'):99.0966,('w16','w16'):49.7668,('w17','w17'):24.8834,('w18','w18'):73.995,('w19','w19'):74.1583,('w20','w20'):74.322,('w21','w21'):74.4861,('w22','w22'):49.3298,('w23','w23'):49.7668,('w24','w24'):24.9383,('w25','w25'):24.9383,('w26','w26'):24.6648,('w27','w27'):24.8834,('w28','w28'):24.9383,('w29','w29'):24.9383,('w30','w30'):73.995,('w31','w31'):49.3298,('w32','w32'):49.3298,('w33','w33'):49.3298,('w34','w34'):24.6648,('w35','w35'):24.6648,('w36','w36'):24.6648,('w37','w37'):49.4387,('w38','w38'):24.7193,('w39','w39'):147.993,('w40','w40'):49.4387,('w41','w41'):24.7193,('w42','w42'):147.993,('w43','w43'):147.993,('w44','w44'):74.1583,('w45','w45'):49.4387,('w46','w46'):49.4387,('w47','w47'):24.7193,('w48','w48'):24.7193,('w49','w49'):147.993,('w50','w50'):49.5478,('w51','w51'):24.7738,('w52','w52'):123.327,('w53','w53'):123.599,('w54','w54'):49.5478,('w55','w55'):24.7738,('w56','w56'):123.327,('w57','w57'):123.599,('w58','w58'):123.327,('w59','w59'):74.322,('w60','w60'):49.5478,('w61','w61'):49.5478,('w62','w62'):24.7738,('w63','w63'):24.7738,('w64','w64'):123.327,('w65','w65'):123.599,('w66','w66'):123.599,('w67','w67'):49.6572,('w68','w68'):24.8285,('w69','w69'):98.6605,('w70','w70'):98.8783,('w71','w71'):99.0966,('w72','w72'):49.6572,('w73','w73'):24.8285,('w74','w74'):98.6605,('w75','w75'):98.8783,('w76','w76'):99.0966,('w77','w77'):98.6605,('w78','w78'):74.4861,('w79','w79'):49.6572,('w80','w80'):49.6572,('w81','w81'):24.8285,('w82','w82'):24.8285,('w83','w83'):98.6605,('w84','w84'):98.8783,('w85','w85'):98.8783,('w86','w86'):99.0966,('w87','w87'):99.0966,('w88','w88'):73.995,('w89','w89'):49.7668,('w90','w90'):49.7668,('w91','w91'):49.7668,('w92','w92'):24.8834,('w93','w93'):24.8834,('w94','w94'):24.8834,('w95','w95'):73.995,('w96','w96'):73.995,('w97','w97'):74.1583,('w98','w98'):74.1583,('w99','w99'):74.1583,('w100','w100'):74.322,('w101','w101'):74.322,('w102','w102'):74.322,('w103','w103'):74.4861,('w104','w104'):74.4861,('w105','w105'):74.4861}

quadratic={('q1','q2'):325.61,('q1','q3'):160.326,('q1','q4'):160.326,('q1','q5'):133.604,('q1','q6'):133.604,('q1','q7'):106.882,('q1','q8'):106.882,('q1','q9'):80.1612,('q1','q10'):80.1612,('q1','q11'):53.4406,('q1','q12'):53.4406,('q1','q13'):26.7202,('q1','q14'):26.7202,('q1','w2'):-32.8865,('q1','w3'):-16.4432,('q1','w6'):-98.6621,('q1','w9'):-82.2177,('q1','w13'):-65.7737,('q1','w18'):-49.33,('q1','w22'):-24.6649,('q1','w26'):-12.3324,('q1','w30'):-36.9975,('q1','w31'):-24.6649,('q1','w32'):-24.6649,('q1','w34'):-12.3324,('q1','w35'):-12.3324,('q1','w39'):-73.9966,('q1','w42'):-73.9966,('q1','w43'):-73.9966,('q1','w52'):-61.6633,('q1','w56'):-61.6633,('q1','w58'):-61.6633,('q1','w69'):-49.3303,('q1','w74'):-49.3303,('q1','w77'):-49.3303,('q1','w88'):-36.9975,('q1','w95'):-36.9975,('q2','q3'):160.326,('q2','q4'):160.326,('q2','q5'):133.604,('q2','q6'):133.604,('q2','q7'):106.882,('q2','q8'):106.882,('q2','q9'):80.1612,('q2','q10'):80.1612,('q2','q11'):53.4406,('q2','q12'):53.4406,('q2','q13'):26.7202,('q2','q14'):26.7202,('q2','w2'):-32.8865,('q2','w3'):-16.4432,('q2','w6'):-98.6621,('q2','w9'):-82.2177,('q2','w13'):-65.7737,('q2','w18'):-49.33,('q2','w30'):-36.9975,('q2','w31'):-24.6649,('q2','w32'):-24.6649,('q2','w33'):-24.6649,('q2','w34'):-12.3324,('q2','w35'):-12.3324,('q2','w36'):-12.3324,('q2','w39'):-73.9966,('q2','w42'):-73.9966,('q2','w49'):-73.9966,('q2','w52'):-61.6633,('q2','w56'):-61.6633,('q2','w64'):-61.6633,('q2','w69'):-49.3303,('q2','w74'):-49.3303,('q2','w83'):-49.3303,('q2','w95'):-36.9975,('q2','w96'):-36.9975,('q3','q4'):176.961,('q3','q5'):133.899,('q3','q6'):133.899,('q3','q7'):107.118,('q3','q8'):107.118,('q3','q9'):80.3382,('q3','q10'):80.3382,('q3','q11'):53.5586,('q3','q12'):53.5586,('q3','q13'):26.7792,('q3','q14'):26.7792,('q3','w4'):-32.9591,('q3','w5'):-16.4795,('q3','w6'):-98.6621,('q3','w10'):-82.3992,('q3','w14'):-65.9189,('q3','w19'):-49.4389,('q3','w37'):-24.7193,('q3','w38'):-12.3596,('q3','w39'):-73.9966,('q3','w43'):-73.9966,('q3','w44'):-37.0792,('q3','w45'):-24.7193,('q3','w46'):-24.7193,('q3','w47'):-12.3596,('q3','w48'):-12.3596,('q3','w49'):-73.9966,('q3','w53'):-61.7994,('q3','w57'):-61.7994,('q3','w65'):-61.7994,('q3','w70'):-49.4392,('q3','w75'):-49.4392,('q3','w84'):-49.4392,('q3','w97'):-37.0792,('q3','w99'):-37.0792,('q4','q5'):133.899,('q4','q6'):133.899,('q4','q7'):107.118,('q4','q8'):107.118,('q4','q9'):80.3382,('q4','q10'):80.3382,('q4','q11'):53.5586,('q4','q12'):53.5586,('q4','q13'):26.7792,('q4','q14'):26.7792,('q4','w4'):-32.9591,('q4','w5'):-16.4795,('q4','w6'):-98.6621,('q4','w10'):-82.3992,('q4','w14'):-65.9189,('q4','w19'):-49.4389,('q4','w40'):-24.7193,('q4','w41'):-12.3596,('q4','w42'):-73.9966,('q4','w43'):-73.9966,('q4','w44'):-37.0792,('q4','w45'):-24.7193,('q4','w46'):-24.7193,('q4','w47'):-12.3596,('q4','w48'):-12.3596,('q4','w49'):-73.9966,('q4','w53'):-61.7994,('q4','w57'):-61.7994,('q4','w66'):-61.7994,('q4','w70'):-49.4392,('q4','w75'):-49.4392,('q4','w85'):-49.4392,('q4','w98'):-37.0792,('q4','w99'):-37.0792,('q5','q6'):-3.83724,('q5','q7'):107.355,('q5','q8'):107.355,('q5','q9'):80.5155,('q5','q10'):80.5155,('q5','q11'):53.6768,('q5','q12'):53.6768,('q5','q13'):26.8383,('q5','q14'):26.8383,('q5','w7'):-33.0319,('q5','w8'):-16.5159,('q5','w9'):-82.2177,('q5','w10'):-82.3992,('q5','w15'):-66.0644,('q5','w20'):-49.548,('q5','w50'):-24.7739,('q5','w51'):-12.3869,('q5','w52'):-61.6633,('q5','w53'):-61.7994,('q5','w58'):-61.6633,('q5','w59'):-37.161,('q5','w60'):-24.7739,('q5','w61'):-24.7739,('q5','w62'):-12.3869,('q5','w63'):-12.3869,('q5','w64'):-61.6633,('q5','w65'):-61.7994,('q5','w66'):-61.7994,('q5','w71'):-49.5483,('q5','w76'):-49.5483,('q5','w86'):-49.5483,('q5','w100'):-37.161,('q5','w102'):-37.161,('q6','q7'):107.355,('q6','q8'):107.355,('q6','q9'):80.5155,('q6','q10'):80.5155,('q6','q11'):53.6768,('q6','q12'):53.6768,('q6','q13'):26.8383,('q6','q14'):26.8383,('q6','w7'):-33.0319,('q6','w8'):-16.5159,('q6','w9'):-82.2177,('q6','w10'):-82.3992,('q6','w15'):-66.0644,('q6','w20'):-49.548,('q6','w54'):-24.7739,('q6','w55'):-12.3869,('q6','w56'):-61.6633,('q6','w57'):-61.7994,('q6','w58'):-61.6633,('q6','w59'):-37.161,('q6','w60'):-24.7739,('q6','w61'):-24.7739,('q6','w62'):-12.3869,('q6','w63'):-12.3869,('q6','w64'):-61.6633,('q6','w65'):-61.7994,('q6','w66'):-61.7994,('q6','w71'):-49.5483,('q6','w76'):-49.5483,('q6','w87'):-49.5483,('q6','w101'):-37.161,('q6','w102'):-37.161,('q7','q8'):-208.775,('q7','q9'):80.6933,('q7','q10'):80.6933,('q7','q11'):53.7953,('q7','q12'):53.7953,('q7','q13'):26.8976,('q7','q14'):26.8976,('q7','w11'):-33.1048,('q7','w12'):-16.5524,('q7','w13'):-65.7737,('q7','w14'):-65.9189,('q7','w15'):-66.0644,('q7','w21'):-49.6574,('q7','w67'):-24.8286,('q7','w68'):-12.4143,('q7','w69'):-49.3303,('q7','w70'):-49.4392,('q7','w71'):-49.5483,('q7','w77'):-49.3303,('q7','w78'):-37.2431,('q7','w79'):-24.8286,('q7','w80'):-24.8286,('q7','w81'):-12.4143,('q7','w82'):-12.4143,('q7','w83'):-49.3303,('q7','w84'):-49.4392,('q7','w85'):-49.4392,('q7','w86'):-49.5483,('q7','w87'):-49.5483,('q7','w103'):-37.2431,('q7','w105'):-37.2431,('q8','q9'):80.6933,('q8','q10'):80.6933,('q8','q11'):53.7953,('q8','q12'):53.7953,('q8','q13'):26.8976,('q8','q14'):26.8976,('q8','w11'):-33.1048,('q8','w12'):-16.5524,('q8','w13'):-65.7737,('q8','w14'):-65.9189,('q8','w15'):-66.0644,('q8','w21'):-49.6574,('q8','w72'):-24.8286,('q8','w73'):-12.4143,('q8','w74'):-49.3303,('q8','w75'):-49.4392,('q8','w76'):-49.5483,('q8','w77'):-49.3303,('q8','w78'):-37.2431,('q8','w79'):-24.8286,('q8','w80'):-24.8286,('q8','w81'):-12.4143,('q8','w82'):-12.4143,('q8','w83'):-49.3303,('q8','w84'):-49.4392,('q8','w85'):-49.4392,('q8','w86'):-49.5483,('q8','w87'):-49.5483,('q8','w104'):-37.2431,('q8','w105'):-37.2431,('q9','q10'):-437.543,('q9','q11'):53.9141,('q9','q12'):53.9141,('q9','q13'):26.957,('q9','q14'):26.957,('q9','w16'):-33.1779,('q9','w17'):-16.5889,('q9','w18'):-49.33,('q9','w19'):-49.4389,('q9','w20'):-49.548,('q9','w21'):-49.6574,('q9','w88'):-36.9975,('q9','w89'):-24.8834,('q9','w90'):-24.8834,('q9','w91'):-24.8834,('q9','w92'):-12.4417,('q9','w93'):-12.4417,('q9','w94'):-12.4417,('q9','w95'):-36.9975,('q9','w96'):-36.9975,('q9','w97'):-37.0792,('q9','w98'):-37.0792,('q9','w99'):-37.0792,('q9','w100'):-37.161,('q9','w101'):-37.161,('q9','w102'):-37.161,('q9','w103'):-37.2431,('q9','w104'):-37.2431,('q9','w105'):-37.2431,('q10','q11'):53.9141,('q10','q12'):53.9141,('q10','q13'):26.957,('q10','q14'):26.957,('q10','w16'):-33.1779,('q10','w17'):-16.5889,('q10','w18'):-49.33,('q10','w19'):-49.4389,('q10','w20'):-49.548,('q10','w21'):-49.6574,('q10','w23'):-24.8834,('q10','w27'):-12.4417,('q10','w30'):-36.9975,('q10','w44'):-37.0792,('q10','w59'):-37.161,('q10','w78'):-37.2431,('q10','w88'):-36.9975,('q10','w89'):-24.8834,('q10','w90'):-24.8834,('q10','w92'):-12.4417,('q10','w93'):-12.4417,('q10','w96'):-36.9975,('q10','w97'):-37.0792,('q10','w98'):-37.0792,('q10','w100'):-37.161,('q10','w101'):-37.161,('q10','w103'):-37.2431,('q10','w104'):-37.2431,('q11','q12'):-683.184,('q11','q13'):27.0165,('q11','q14'):27.0165,('q11','w1'):-16.6255,('q11','w2'):-32.8865,('q11','w4'):-32.9591,('q11','w7'):-33.0319,('q11','w11'):-33.1048,('q11','w16'):-33.1779,('q11','w22'):-24.6649,('q11','w23'):-24.8834,('q11','w24'):-12.4691,('q11','w25'):-12.4691,('q11','w28'):-12.4691,('q11','w31'):-24.6649,('q11','w33'):-24.6649,('q11','w37'):-24.7193,('q11','w40'):-24.7193,('q11','w45'):-24.7193,('q11','w50'):-24.7739,('q11','w54'):-24.7739,('q11','w60'):-24.7739,('q11','w67'):-24.8286,('q11','w72'):-24.8286,('q11','w79'):-24.8286,('q11','w89'):-24.8834,('q11','w91'):-24.8834,('q12','q13'):27.0165,('q12','q14'):27.0165,('q12','w1'):-16.6255,('q12','w2'):-32.8865,('q12','w4'):-32.9591,('q12','w7'):-33.0319,('q12','w11'):-33.1048,('q12','w16'):-33.1779,('q12','w22'):-24.6649,('q12','w23'):-24.8834,('q12','w24'):-12.4691,('q12','w25'):-12.4691,('q12','w29'):-12.4691,('q12','w32'):-24.6649,('q12','w33'):-24.6649,('q12','w37'):-24.7193,('q12','w40'):-24.7193,('q12','w46'):-24.7193,('q12','w50'):-24.7739,('q12','w54'):-24.7739,('q12','w61'):-24.7739,('q12','w67'):-24.8286,('q12','w72'):-24.8286,('q12','w80'):-24.8286,('q12','w90'):-24.8834,('q12','w91'):-24.8834,('q13','q14'):-960.274,('q13','w1'):-16.6255,('q13','w3'):-16.4432,('q13','w5'):-16.4795,('q13','w8'):-16.5159,('q13','w12'):-16.5524,('q13','w17'):-16.5889,('q13','w24'):-12.4691,('q13','w26'):-12.3324,('q13','w27'):-12.4417,('q13','w28'):-12.4691,('q13','w29'):-12.4691,('q13','w34'):-12.3324,('q13','w36'):-12.3324,('q13','w38'):-12.3596,('q13','w41'):-12.3596,('q13','w47'):-12.3596,('q13','w51'):-12.3869,('q13','w55'):-12.3869,('q13','w62'):-12.3869,('q13','w68'):-12.4143,('q13','w73'):-12.4143,('q13','w81'):-12.4143,('q13','w92'):-12.4417,('q13','w94'):-12.4417,('q14','w1'):-16.6255,('q14','w3'):-16.4432,('q14','w5'):-16.4795,('q14','w8'):-16.5159,('q14','w12'):-16.5524,('q14','w17'):-16.5889,('q14','w25'):-12.4691,('q14','w26'):-12.3324,('q14','w27'):-12.4417,('q14','w28'):-12.4691,('q14','w29'):-12.4691,('q14','w35'):-12.3324,('q14','w36'):-12.3324,('q14','w38'):-12.3596,('q14','w41'):-12.3596,('q14','w48'):-12.3596,('q14','w51'):-12.3869,('q14','w55'):-12.3869,('q14','w63'):-12.3869,('q14','w68'):-12.4143,('q14','w73'):-12.4143,('q14','w82'):-12.4143,('q14','w93'):-12.4417,('q14','w94'):-12.4417,('q15','q16'):-1241.72}

Q={**linear, **quadratic}
sampleset=sampler_auto.sample_qubo(Q,num_reads=1000,label='RTU optimization 8steps')
print(sampleset)