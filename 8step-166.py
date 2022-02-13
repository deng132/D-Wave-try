from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler_auto=EmbeddingComposite(DWaveSampler(solver={'topology__type':'pegasus'}))


linear={('q1','q1'):28162.1 q10,('q2','q2'):49.0294,('q3','q3'):276.826,('q4','q4'):276.826,('q5','q5'):516.605,('q6','q6'):516.605,('q7','q7'):775.1,('q8','q8'):775.1,('q9','q9'):1041.1,('q10','q10'):1041.1,('q11','q11'):1311.14,('q12','q12'):1311.14,('q13','q13'):1575.62,('q14','q14'):1575.62,('q15','q15'):1859.2,('q16','q16'):1859.2,('w1','w1'):84319.7,('w2','w2'):84319.7,('w3','w3'):84319.7,('w4','w4'):84319.7,('w5','w5'):84319.7,('w6','w6'):84319.7,('w7','w7'):84319.7,('w8','w8'):84319.7,('w9','w9'):84319.7,('w10','w10'):84319.7,('w11','w11'):84319.7,('w12','w12'):84319.7,('w13','w13'):84319.7,('w14','w14'):84319.7,('w15','w15'):84319.7,('w16','w16'):84319.7,('w17','w17'):84319.7,('w18','w18'):84319.7,('w19','w19'):84319.7,('w20','w20'):84319.7,('w21','w21'):84319.7,('w22','w22'):84319.7,('w23','w23'):84319.7,('w24','w24'):84319.7,('w25','w25'):84319.7,('w26','w26'):84319.7,('w27','w27'):84319.7,('w28','w28'):84319.7,('w29','w29'):84319.7,('w30','w30'):84319.7,('w31','w31'):84319.7,('w32','w32'):84319.7,('w33','w33'):84319.7,('w34','w34'):84319.7,('w35','w35'):84319.7,('w36','w36'):84319.7,('w37','w37'):84319.7,('w38','w38'):84319.7,('w39','w39'):84319.7,('w40','w40'):84319.7,('w41','w41'):84319.7,('w42','w42'):84319.7,('w43','w43'):84319.7,('w44','w44'):84319.7,('w45','w45'):84319.7,('w46','w46'):84319.7,('w47','w47'):84319.7,('w48','w48'):84319.7,('w49','w49'):84319.7,('w50','w50'):84319.7,('w51','w51'):84319.7,('w52','w52'):84319.7,('w53','w53'):84319.7,('w54','w54'):84319.7,('w55','w55'):84319.7,('w56','w56'):84319.7}

quadratic={('q1','q2'):28091.3,('q1','q3'):28217.6,('q1','q4'):110.995,('q1','q5'):28199.1,('q1','q6'):92.4949,('q1','q7'):28180.6,('q1','q8'):73.9954,('q1','q9'):55.4962,('q1','q10'):28162.1,('q1','q11'):28143.6,('q1','q12'):28143.6,('q1','q13'):28125.1,('q1','q14'):28125.1,('q1','w1'):-56213.1,('q1','w4'):-56213.1,('q1','w8'):-56213.1,('q1','w9'):-56213.1,('q1','w10'):-56213.1,('q1','w12'):-56213.1,('q1','w13'):-56213.1,('q1','w21'):-56213.1,('q1','w31'):-56213.1,('q2','q3'):28217.6,('q2','q4'):110.995,('q2','q5'):28199.1,('q2','q6'):92.4949,('q2','q7'):28180.6,('q2','q8'):73.9954,('q2','q9'):28162.1,('q2','q10'):28162.1,('q2','q11'):36.9973,('q2','q12'):28143.6,('q2','q13'):18.4986,('q2','q14'):28125.1,('q2','w1'):-24.6649,('q2','w3'):-24.6649,('q2','w4'):-12.3324,('q2','w8'):-36.9975,('q2','w9'):-24.6649,('q2','w10'):-12.3324,('q2','w11'):-12.3324,('q2','w12'):-56213.1,('q2','w19'):-56213.1,('q2','w27'):-56213.1,('q2','w37'):-56213.1,('q2','w44'):-56213.1,('q2','w49'):-56213.1,('q2','w54'):-56213.1,('q2','w56'):-56213.1,('q3','q4'):27933.9,('q3','q5'):28199.3,('q3','q6'):92.6991,('q3','q7'):28180.7,('q3','q8'):74.1587,('q3','q9'):55.6187,('q3','q10'):28162.2,('q3','q11'):28143.6,('q3','q12'):28143.6,('q3','q13'):28125.1,('q3','q14'):28125.1,('q3','w3'):-24.7193,('q3','w11'):-12.3596,('q3','w12'):-73.9966,('q3','w13'):-56213.1,('q3','w14'):-56213.1,('q3','w15'):-56213.1,('q3','w16'):-56213.1,('q3','w17'):-56213.1,('q3','w18'):-56213.1,('q3','w19'):-56213.1,('q3','w20'):-56213.1,('q3','w28'):-56213.1,('q3','w38'):-56213.1,('q4','q5'):28199.3,('q4','q6'):92.6991,('q4','q7'):28180.7,('q4','q8'):74.1587,('q4','q9'):28162.2,('q4','q10'):28162.2,('q4','q11'):37.079,('q4','q12'):37.079,('q4','q13'):18.5395,('q4','q14'):18.5395,('q4','w3'):-24.7193,('q4','w11'):-12.3596,('q4','w12'):-73.9966,('q4','w13'):-73.9966,('q4','w14'):-37.0792,('q4','w15'):-24.7193,('q4','w16'):-24.7193,('q4','w17'):-12.3596,('q4','w18'):-12.3596,('q4','w19'):-73.9966,('q4','w20'):-56213.1,('q4','w29'):-56213.1,('q4','w39'):-56213.1,('q4','w45'):-56213.1,('q4','w50'):-56213.1,('q5','q6'):27771.3,('q5','q7'):28180.9,('q5','q8'):74.3225,('q5','q9'):55.7415,('q5','q10'):28162.3,('q5','q11'):28143.7,('q5','q12'):28143.7,('q5','q13'):28125.1,('q5','q14'):28125.1,('q5','w3'):-24.7739,('q5','w11'):-12.3869,('q5','w12'):-61.6633,('q5','w20'):-61.7994,('q5','w21'):-56213.1,('q5','w22'):-56213.1,('q5','w23'):-56213.1,('q5','w24'):-56213.1,('q5','w25'):-56213.1,('q5','w26'):-56213.1,('q5','w27'):-56213.1,('q5','w28'):-56213.1,('q5','w29'):-56213.1,('q5','w30'):-56213.1,('q5','w40'):-56213.1,('q6','q7'):28180.9,('q6','q8'):74.3225,('q6','q9'):28162.3,('q6','q10'):28162.3,('q6','q11'):37.1609,('q6','q12'):37.1609,('q6','q13'):18.5804,('q6','q14'):18.5804,('q6','w3'):-24.7739,('q6','w11'):-12.3869,('q6','w12'):-61.6633,('q6','w20'):-61.7994,('q6','w21'):-61.6633,('q6','w22'):-37.161,('q6','w23'):-24.7739,('q6','w24'):-24.7739,('q6','w25'):-12.3869,('q6','w26'):-12.3869,('q6','w27'):-61.6633,('q6','w28'):-61.7994,('q6','w29'):-61.7994,('q6','w30'):-56213.1,('q6','w41'):-56213.1,('q6','w46'):-56213.1,('q6','w52'):-56213.1,('q7','q8'):27595.3,('q7','q9'):55.8646,('q7','q10'):28162.4,('q7','q11'):28143.8,('q7','q12'):28143.8,('q7','q13'):28125.2,('q7','q14'):28125.2,('q7','w3'):-24.8286,('q7','w11'):-12.4143,('q7','w12'):-49.3303,('q7','w20'):-49.4392,('q7','w30'):-49.5483,('q7','w31'):-56213.1,('q7','w32'):-56213.1,('q7','w33'):-56213.1,('q7','w34'):-56213.1,('q7','w35'):-56213.1,('q7','w36'):-56213.1,('q7','w37'):-56213.1,('q7','w38'):-56213.1,('q7','w39'):-56213.1,('q7','w40'):-56213.1,('q7','w41'):-56213.1,('q7','w48'):-56213.1,('q8','q9'):28162.4,('q8','q10'):28162.4,('q8','q11'):37.2429,('q8','q12'):37.2429,('q8','q13'):18.6214,('q8','q14'):18.6214,('q8','w3'):-24.8286,('q8','w11'):-12.4143,('q8','w12'):-49.3303,('q8','w20'):-49.4392,('q8','w30'):-49.5483,('q8','w31'):-49.3303,('q8','w32'):-37.2431,('q8','w33'):-24.8286,('q8','w34'):-24.8286,('q8','w35'):-12.4143,('q8','w36'):-12.4143,('q8','w37'):-49.3303,('q8','w38'):-49.4392,('q8','w39'):-49.4392,('q8','w40'):-49.5483,('q8','w41'):-49.5483,('q8','w47'):-56213.1,('q8','w48'):-56213.1,('q8','w53'):-56213.1,('q9','q10'):-692.225,('q9','q11'):37.3251,('q9','q12'):28143.9,('q9','q13'):18.6625,('q9','q14'):28125.2,('q9','w2'):-24.8834,('q9','w3'):-24.8834,('q9','w5'):-12.4417,('q9','w8'):-36.9975,('q9','w11'):-12.4417,('q9','w12'):-36.9975,('q9','w14'):-37.0792,('q9','w20'):-37.0792,('q9','w22'):-37.161,('q9','w30'):-37.161,('q9','w32'):-37.2431,('q9','w42'):-24.8834,('q9','w43'):-12.4417,('q9','w44'):-36.9975,('q9','w45'):-37.0792,('q9','w46'):-37.161,('q9','w47'):-37.2431,('q9','w48'):-37.2431,('q9','w50'):-56213.1,('q9','w51'):-56213.1,('q9','w52'):-56213.1,('q9','w53'):-56213.1,('q9','w55'):-56213.1,('q9','w56'):-56213.1,('q10','q11'):28143.9,('q10','q12'):28143.9,('q10','q13'):28125.2,('q10','q14'):28125.2,('q10','w2'):-56213.1,('q10','w5'):-56213.1,('q10','w8'):-56213.1,('q10','w14'):-56213.1,('q10','w22'):-56213.1,('q10','w32'):-56213.1,('q10','w42'):-56213.1,('q10','w43'):-56213.1,('q10','w44'):-56213.1,('q10','w45'):-56213.1,('q10','w46'):-56213.1,('q10','w47'):-56213.1,('q11','q12'):27229.3,('q11','q13'):28125.3,('q11','q14'):18.7037,('q11','w1'):-56213.1,('q11','w2'):-56213.1,('q11','w3'):-56213.1,('q11','w6'):-56213.1,('q11','w15'):-56213.1,('q11','w23'):-56213.1,('q11','w33'):-56213.1,('q12','q13'):28125.3,('q12','q14'):18.7037,('q12','w1'):-24.6649,('q12','w2'):-24.8834,('q12','w3'):-56213.1,('q12','w7'):-56213.1,('q12','w9'):-56213.1,('q12','w16'):-56213.1,('q12','w24'):-56213.1,('q12','w34'):-56213.1,('q12','w42'):-56213.1,('q12','w49'):-56213.1,('q12','w51'):-56213.1,('q13','q14'):27049.7,('q13','w3'):-12.4691,('q13','w4'):-56213.1,('q13','w5'):-56213.1,('q13','w6'):-56213.1,('q13','w7'):-56213.1,('q13','w11'):-56213.1,('q13','w17'):-56213.1,('q13','w25'):-56213.1,('q13','w35'):-56213.1,('q14','w3'):-12.4691,('q14','w4'):-12.3324,('q14','w5'):-12.4417,('q14','w6'):-12.4691,('q14','w7'):-12.4691,('q14','w10'):-56213.1,('q14','w11'):-56213.1,('q14','w18'):-56213.1,('q14','w26'):-56213.1,('q14','w36'):-56213.1,('q14','w43'):-56213.1,('q14','w54'):-56213.1,('q14','w55'):-56213.1,('q15','q16'):-1249.59,('w1','w49'):16.4433,('w2','w51'):16.5889,('w3','w11'):8.31276,('w3','w20'):16.4796,('w3','w30'):16.5159,('w3','w48'):16.5524,('w4','w54'):8.22161,('w5','w55'):8.29445,('w8','w56'):24.665,('w11','w20'):8.23976,('w11','w30'):8.25795,('w11','w48'):8.27618,('w12','w20'):49.3311,('w12','w30'):41.1088,('w12','w48'):32.8868,('w14','w50'):24.7194,('w20','w30'):41.1996,('w20','w48'):32.9594,('w22','w52'):24.774,('w30','w48'):33.0322,('w32','w53'):24.8287}

Q={**linear, **quadratic}
sampleset=sampler_auto.sample_qubo(Q,num_reads=1000,label='RTU optimization 8steps')
print(sampleset)