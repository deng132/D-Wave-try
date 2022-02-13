from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler_auto=EmbeddingComposite(DWaveSampler(solver={'topology__type':'pegasus'}))


linear={('q1','q1'):107.393,('q2','q2'):107.393,('q3','q3'):355.731,('q4','q4'):355.731,('q5','q5'):627.517,('q6','q6'):627.517,('q7','q7'):896.672,('q8','q8'):896.672,('q9','q9'):1200.29,('q10','q10'):1200.29,('q11','q11'):1201.65,('q12','q12'):1201.65,('q13','q13'):1511.09,('q14','q14'):1511.09,('q15','q15'):1847.07,('q16','q16'):1847.07,('w1','w1'):83172.2,('w2','w2'):83172.2,('w3','w3'):83172.2,('w4','w4'):83172.2,('w5','w5'):83172.2,('w6','w6'):83172.2,('w7','w7'):83172.2,('w8','w8'):83172.2,('w9','w9'):83172.2,('w10','w10'):83172.2,('w11','w11'):83172.2,('w12','w12'):83172.2,('w13','w13'):83172.2,('w14','w14'):83172.2,('w15','w15'):83172.2,('w16','w16'):83172.2,('w17','w17'):83172.2,('w18','w18'):83172.2,('w19','w19'):83172.2,('w20','w20'):83172.2,('w21','w21'):83172.2,('w22','w22'):83172.2,('w23','w23'):83172.2,('w24','w24'):83172.2,('w25','w25'):83172.2,('w26','w26'):83172.2,('w27','w27'):83172.2,('w28','w28'):83172.2,('w29','w29'):83172.2,('w30','w30'):83172.2,('w31','w31'):83172.2,('w32','w32'):83172.2,('w33','w33'):83172.2,('w34','w34'):83172.2,('w35','w35'):83172.2,('w36','w36'):83172.2,('w37','w37'):83172.2,('w38','w38'):83172.2,('w39','w39'):83172.2,('w40','w40'):83172.2,('w41','w41'):83172.2,('w42','w42'):83172.2,('w43','w43'):83172.2,('w44','w44'):83172.2,('w45','w45'):83172.2,('w46','w46'):83172.2,('w47','w47'):83172.2,('w48','w48'):83172.2,('w49','w49'):83172.2,('w50','w50'):83172.2,('w51','w51'):83172.2,('w52','w52'):83172.2,('w53','w53'):83172.2,('w54','w54'):83172.2,('w55','w55'):83172.2,('w56','w56'):83172.2}

quadratic={('q1','q2'):27668.8,('q1','q3'):27816.7,('q1','q4'):92.6652,('q1','q5'):27798.2,('q1','q6'):74.1247,('q1','q7'):27779.7,('q1','q8'):55.5847,('q1','q9'):37.0449,('q1','q10'):27761.1,('q1','q11'):27761.1,('q1','q12'):27761.1,('q1','q13'):27742.6,('q1','q14'):27742.6,('q1','w1'):-55448.1,('q1','w4'):-55448.1,('q1','w8'):-55448.1,('q1','w9'):-55448.1,('q1','w10'):-55448.1,('q1','w12'):-55448.1,('q1','w13'):-55448.1,('q1','w21'):-55448.1,('q1','w31'):-55448.1,('q2','q3'):27816.7,('q2','q4'):92.6652,('q2','q5'):27798.2,('q2','q6'):74.1247,('q2','q7'):27779.7,('q2','q8'):55.5847,('q2','q9'):27761.1,('q2','q10'):27761.1,('q2','q11'):36.9973,('q2','q12'):27761.1,('q2','q13'):18.4986,('q2','q14'):27742.6,('q2','w1'):-24.6649,('q2','w3'):-24.6649,('q2','w4'):-12.3324,('q2','w8'):-24.6966,('q2','w9'):-24.6649,('q2','w10'):-12.3324,('q2','w11'):-12.3324,('q2','w12'):-55448.1,('q2','w19'):-55448.1,('q2','w27'):-55448.1,('q2','w37'):-55448.1,('q2','w44'):-55448.1,('q2','w49'):-55448.1,('q2','w54'):-55448.1,('q2','w56'):-55448.1,('q3','q4'):27499.,('q3','q5'):27798.4,('q3','q6'):74.2884,('q3','q7'):27779.8,('q3','q8'):55.7074,('q3','q9'):37.1266,('q3','q10'):27761.2,('q3','q11'):27761.2,('q3','q12'):27761.2,('q3','q13'):27742.6,('q3','q14'):27742.6,('q3','w3'):-24.7193,('q3','w11'):-12.3596,('q3','w12'):-61.7768,('q3','w13'):-55448.1,('q3','w14'):-55448.1,('q3','w15'):-55448.1,('q3','w16'):-55448.1,('q3','w17'):-55448.1,('q3','w18'):-55448.1,('q3','w19'):-55448.1,('q3','w20'):-55448.1,('q3','w28'):-55448.1,('q3','w38'):-55448.1,('q4','q5'):27798.4,('q4','q6'):74.2884,('q4','q7'):27779.8,('q4','q8'):55.7074,('q4','q9'):27761.2,('q4','q10'):27761.2,('q4','q11'):37.079,('q4','q12'):37.079,('q4','q13'):18.5395,('q4','q14'):18.5395,('q4','w3'):-24.7193,('q4','w11'):-12.3596,('q4','w12'):-61.7768,('q4','w13'):-61.7768,('q4','w14'):-24.7511,('q4','w15'):-24.7193,('q4','w16'):-24.7193,('q4','w17'):-12.3596,('q4','w18'):-12.3596,('q4','w19'):-61.7768,('q4','w20'):-55448.1,('q4','w29'):-55448.1,('q4','w39'):-55448.1,('q4','w45'):-55448.1,('q4','w50'):-55448.1,('q5','q6'):27310.6,('q5','q7'):27779.9,('q5','q8'):55.8304,('q5','q9'):37.2086,('q5','q10'):27761.3,('q5','q11'):27761.2,('q5','q12'):27761.2,('q5','q13'):27742.7,('q5','q14'):27742.7,('q5','w3'):-24.7739,('q5','w11'):-12.3869,('q5','w12'):-49.4165,('q5','w20'):-49.5256,('q5','w21'):-55448.1,('q5','w22'):-55448.1,('q5','w23'):-55448.1,('q5','w24'):-55448.1,('q5','w25'):-55448.1,('q5','w26'):-55448.1,('q5','w27'):-55448.1,('q5','w28'):-55448.1,('q5','w29'):-55448.1,('q5','w30'):-55448.1,('q5','w40'):-55448.1,('q6','q7'):27779.9,('q6','q8'):55.8304,('q6','q9'):27761.3,('q6','q10'):27761.3,('q6','q11'):37.1609,('q6','q12'):37.1609,('q6','q13'):18.5804,('q6','q14'):18.5804,('q6','w3'):-24.7739,('q6','w11'):-12.3869,('q6','w12'):-49.4165,('q6','w20'):-49.5256,('q6','w21'):-49.4165,('q6','w22'):-24.8057,('q6','w23'):-24.7739,('q6','w24'):-24.7739,('q6','w25'):-12.3869,('q6','w26'):-12.3869,('q6','w27'):-49.4165,('q6','w28'):-49.5256,('q6','w29'):-49.5256,('q6','w30'):-55448.1,('q6','w41'):-55448.1,('q6','w46'):-55448.1,('q6','w52'):-55448.1,('q7','q8'):27126.8,('q7','q9'):37.2908,('q7','q10'):27761.4,('q7','q11'):27761.3,('q7','q12'):27761.3,('q7','q13'):27742.7,('q7','q14'):27742.7,('q7','w3'):-24.8286,('q7','w11'):-12.4143,('q7','w12'):-37.0564,('q7','w20'):-37.1383,('q7','w30'):-37.2202,('q7','w31'):-55448.1,('q7','w32'):-55448.1,('q7','w33'):-55448.1,('q7','w34'):-55448.1,('q7','w35'):-55448.1,('q7','w36'):-55448.1,('q7','w37'):-55448.1,('q7','w38'):-55448.1,('q7','w39'):-55448.1,('q7','w40'):-55448.1,('q7','w41'):-55448.1,('q7','w48'):-55448.1,('q8','q9'):27761.4,('q8','q10'):27761.4,('q8','q11'):37.2429,('q8','q12'):37.2429,('q8','q13'):18.6214,('q8','q14'):18.6214,('q8','w3'):-24.8286,('q8','w11'):-12.4143,('q8','w12'):-37.0564,('q8','w20'):-37.1383,('q8','w30'):-37.2202,('q8','w31'):-37.0564,('q8','w32'):-24.8605,('q8','w33'):-24.8286,('q8','w34'):-24.8286,('q8','w35'):-12.4143,('q8','w36'):-12.4143,('q8','w37'):-37.0564,('q8','w38'):-37.1383,('q8','w39'):-37.1383,('q8','w40'):-37.2202,('q8','w41'):-37.2202,('q8','w47'):-55448.1,('q8','w48'):-55448.1,('q8','w53'):-55448.1,('q9','q10'):-803.425,('q9','q11'):37.3251,('q9','q12'):27761.4,('q9','q13'):18.6625,('q9','q14'):27742.7,('q9','w2'):-24.8834,('q9','w3'):-24.8834,('q9','w5'):-12.4417,('q9','w8'):-24.6966,('q9','w11'):-12.4417,('q9','w12'):-24.6966,('q9','w14'):-24.7511,('q9','w20'):-24.7511,('q9','w22'):-24.8057,('q9','w30'):-24.8057,('q9','w32'):-24.8605,('q9','w42'):-24.8834,('q9','w43'):-12.4417,('q9','w44'):-24.6966,('q9','w45'):-24.7511,('q9','w46'):-24.8057,('q9','w47'):-24.8605,('q9','w48'):-24.8605,('q9','w50'):-55448.1,('q9','w51'):-55448.1,('q9','w52'):-55448.1,('q9','w53'):-55448.1,('q9','w55'):-55448.1,('q9','w56'):-55448.1,('q10','q11'):27761.4,('q10','q12'):27761.4,('q10','q13'):27742.7,('q10','q14'):27742.7,('q10','w2'):-55448.1,('q10','w5'):-55448.1,('q10','w8'):-55448.1,('q10','w14'):-55448.1,('q10','w22'):-55448.1,('q10','w32'):-55448.1,('q10','w42'):-55448.1,('q10','w43'):-55448.1,('q10','w44'):-55448.1,('q10','w45'):-55448.1,('q10','w46'):-55448.1,('q10','w47'):-55448.1,('q11','q12'):26923.4,('q11','q13'):27742.8,('q11','q14'):18.7037,('q11','w1'):-55448.1,('q11','w2'):-55448.1,('q11','w3'):-55448.1,('q11','w6'):-55448.1,('q11','w15'):-55448.1,('q11','w23'):-55448.1,('q11','w33'):-55448.1,('q12','q13'):27742.8,('q12','q14'):18.7037,('q12','w1'):-24.6649,('q12','w2'):-24.8834,('q12','w3'):-55448.1,('q12','w7'):-55448.1,('q12','w9'):-55448.1,('q12','w16'):-55448.1,('q12','w24'):-55448.1,('q12','w34'):-55448.1,('q12','w42'):-55448.1,('q12','w49'):-55448.1,('q12','w51'):-55448.1,('q13','q14'):26708.8,('q13','w3'):-12.4691,('q13','w4'):-55448.1,('q13','w5'):-55448.1,('q13','w6'):-55448.1,('q13','w7'):-55448.1,('q13','w11'):-55448.1,('q13','w17'):-55448.1,('q13','w25'):-55448.1,('q13','w35'):-55448.1,('q14','w3'):-12.4691,('q14','w4'):-12.3324,('q14','w5'):-12.4417,('q14','w6'):-12.4691,('q14','w7'):-12.4691,('q14','w10'):-55448.1,('q14','w11'):-55448.1,('q14','w18'):-55448.1,('q14','w26'):-55448.1,('q14','w36'):-55448.1,('q14','w43'):-55448.1,('q14','w54'):-55448.1,('q14','w55'):-55448.1,('q15','q16'):-1243.89,('w1','w49'):16.4433,('w2','w51'):16.5889,('w3','w11'):8.31276,('w3','w20'):16.4796,('w3','w30'):16.5159,('w3','w48'):16.5524,('w4','w54'):8.22161,('w5','w55'):8.29445,('w8','w56'):16.4644,('w11','w20'):8.23976,('w11','w30'):8.25795,('w11','w48'):8.27618,('w12','w20'):41.1845,('w12','w30'):32.9443,('w12','w48'):24.7043,('w14','w50'):16.5007,('w20','w30'):33.0171,('w20','w48'):24.7588,('w22','w52'):16.5372,('w30','w48'):24.8135,('w32','w53'):16.5737}

Q={**linear, **quadratic}
sampleset=sampler_auto.sample_qubo(Q,num_reads=1000,label='RTU optimization 8steps')
print(sampleset)