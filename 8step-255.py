from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler_auto=EmbeddingComposite(DWaveSampler(solver={'topology__type':'pegasus'}))


linear={('q1','q1'):30589.8 q10,('q2','q2'):89.0201,('q3','q3'):337.42,('q4','q4'):337.42,('q5','q5'):604.671,('q6','q6'):604.671,('q7','q7'):890.419,('q8','q8'):890.419,('q9','q9'):1176.78,('q10','q10'):1176.78,('q11','q11'):1463.67,('q12','q12'):1463.67,('q13','q13'):1748.43,('q14','q14'):1748.43,('q15','q15'):2037.61,('q16','q16'):2037.61,('w1','w1'):91603.,('w2','w2'):91603.,('w3','w3'):91603.,('w4','w4'):91603.,('w5','w5'):91603.,('w6','w6'):91603.,('w7','w7'):91603.,('w8','w8'):91603.,('w9','w9'):91603.,('w10','w10'):91603.,('w11','w11'):91603.,('w12','w12'):91603.,('w13','w13'):91603.,('w14','w14'):91603.,('w15','w15'):91603.,('w16','w16'):91603.,('w17','w17'):91603.,('w18','w18'):91603.,('w19','w19'):91603.,('w20','w20'):91603.,('w21','w21'):91603.,('w22','w22'):91603.,('w23','w23'):91603.,('w24','w24'):91603.,('w25','w25'):91603.,('w26','w26'):91603.,('w27','w27'):91603.,('w28','w28'):91603.,('w29','w29'):91603.,('w30','w30'):91603.,('w31','w31'):91603.,('w32','w32'):91603.,('w33','w33'):91603.,('w34','w34'):91603.,('w35','w35'):91603.,('w36','w36'):91603.,('w37','w37'):91603.,('w38','w38'):91603.,('w39','w39'):91603.,('w40','w40'):91603.,('w41','w41'):91603.,('w42','w42'):91603.,('w43','w43'):91603.,('w44','w44'):91603.,('w45','w45'):91603.,('w46','w46'):91603.,('w47','w47'):91603.,('w48','w48'):91603.,('w49','w49'):91603.,('w50','w50'):91603.,('w51','w51'):91603.,('w52','w52'):91603.,('w53','w53'):91603.,('w54','w54'):91603.,('w55','w55'):91603.,('w56','w56'):91603.}

quadratic={('q1','q2'):30502.7,('q1','q3'):30645.3,('q1','q4'):110.995,('q1','q5'):30626.8,('q1','q6'):92.4949,('q1','q7'):30608.3,('q1','q8'):73.9954,('q1','q9'):55.4962,('q1','q10'):30589.8,('q1','q11'):30571.3,('q1','q12'):30571.3,('q1','q13'):30552.8,('q1','q14'):30552.8,('q1','w1'):-61068.6,('q1','w4'):-61068.6,('q1','w8'):-61068.6,('q1','w9'):-61068.6,('q1','w10'):-61068.6,('q1','w12'):-61068.6,('q1','w13'):-61068.6,('q1','w21'):-61068.6,('q1','w31'):-61068.6,('q2','q3'):30645.3,('q2','q4'):110.995,('q2','q5'):30626.8,('q2','q6'):92.4949,('q2','q7'):30608.3,('q2','q8'):73.9954,('q2','q9'):30589.8,('q2','q10'):30589.8,('q2','q11'):36.9973,('q2','q12'):30571.3,('q2','q13'):18.4986,('q2','q14'):30552.8,('q2','w1'):-24.6649,('q2','w3'):-24.6649,('q2','w4'):-12.3324,('q2','w8'):-36.9975,('q2','w9'):-24.6649,('q2','w10'):-12.3324,('q2','w11'):-12.3324,('q2','w12'):-61068.6,('q2','w19'):-61068.6,('q2','w27'):-61068.6,('q2','w37'):-61068.6,('q2','w44'):-61068.6,('q2','w49'):-61068.6,('q2','w54'):-61068.6,('q2','w56'):-61068.6,('q3','q4'):30332.9,('q3','q5'):30627.,('q3','q6'):92.6991,('q3','q7'):30608.5,('q3','q8'):74.1587,('q3','q9'):55.6187,('q3','q10'):30589.9,('q3','q11'):30571.4,('q3','q12'):30571.4,('q3','q13'):30552.9,('q3','q14'):30552.9,('q3','w3'):-24.7193,('q3','w11'):-12.3596,('q3','w12'):-73.9966,('q3','w13'):-61068.6,('q3','w14'):-61068.6,('q3','w15'):-61068.6,('q3','w16'):-61068.6,('q3','w17'):-61068.6,('q3','w18'):-61068.6,('q3','w19'):-61068.6,('q3','w20'):-61068.6,('q3','w28'):-61068.6,('q3','w38'):-61068.6,('q4','q5'):30627.,('q4','q6'):92.6991,('q4','q7'):30608.5,('q4','q8'):74.1587,('q4','q9'):30589.9,('q4','q10'):30589.9,('q4','q11'):37.079,('q4','q12'):37.079,('q4','q13'):18.5395,('q4','q14'):18.5395,('q4','w3'):-24.7193,('q4','w11'):-12.3596,('q4','w12'):-73.9966,('q4','w13'):-73.9966,('q4','w14'):-37.0792,('q4','w15'):-24.7193,('q4','w16'):-24.7193,('q4','w17'):-12.3596,('q4','w18'):-12.3596,('q4','w19'):-73.9966,('q4','w20'):-61068.6,('q4','w29'):-61068.6,('q4','w39'):-61068.6,('q4','w45'):-61068.6,('q4','w50'):-61068.6,('q5','q6'):30150.6,('q5','q7'):30608.6,('q5','q8'):74.3225,('q5','q9'):55.7415,('q5','q10'):30590.1,('q5','q11'):30571.5,('q5','q12'):30571.5,('q5','q13'):30552.9,('q5','q14'):30552.9,('q5','w3'):-24.7739,('q5','w11'):-12.3869,('q5','w12'):-61.6633,('q5','w20'):-61.7994,('q5','w21'):-61068.6,('q5','w22'):-61068.6,('q5','w23'):-61068.6,('q5','w24'):-61068.6,('q5','w25'):-61068.6,('q5','w26'):-61068.6,('q5','w27'):-61068.6,('q5','w28'):-61068.6,('q5','w29'):-61068.6,('q5','w30'):-61068.6,('q5','w40'):-61068.6,('q6','q7'):30608.6,('q6','q8'):74.3225,('q6','q9'):30590.1,('q6','q10'):30590.1,('q6','q11'):37.1609,('q6','q12'):37.1609,('q6','q13'):18.5804,('q6','q14'):18.5804,('q6','w3'):-24.7739,('q6','w11'):-12.3869,('q6','w12'):-61.6633,('q6','w20'):-61.7994,('q6','w21'):-61.6633,('q6','w22'):-37.161,('q6','w23'):-24.7739,('q6','w24'):-24.7739,('q6','w25'):-12.3869,('q6','w26'):-12.3869,('q6','w27'):-61.6633,('q6','w28'):-61.7994,('q6','w29'):-61.7994,('q6','w30'):-61068.6,('q6','w41'):-61068.6,('q6','w46'):-61068.6,('q6','w52'):-61068.6,('q7','q8'):29956.9,('q7','q9'):55.8646,('q7','q10'):30590.2,('q7','q11'):30571.6,('q7','q12'):30571.6,('q7','q13'):30552.9,('q7','q14'):30552.9,('q7','w3'):-24.8286,('q7','w11'):-12.4143,('q7','w12'):-49.3303,('q7','w20'):-49.4392,('q7','w30'):-49.5483,('q7','w31'):-61068.6,('q7','w32'):-61068.6,('q7','w33'):-61068.6,('q7','w34'):-61068.6,('q7','w35'):-61068.6,('q7','w36'):-61068.6,('q7','w37'):-61068.6,('q7','w38'):-61068.6,('q7','w39'):-61068.6,('q7','w40'):-61068.6,('q7','w41'):-61068.6,('q7','w48'):-61068.6,('q8','q9'):30590.2,('q8','q10'):30590.2,('q8','q11'):37.2429,('q8','q12'):37.2429,('q8','q13'):18.6214,('q8','q14'):18.6214,('q8','w3'):-24.8286,('q8','w11'):-12.4143,('q8','w12'):-49.3303,('q8','w20'):-49.4392,('q8','w30'):-49.5483,('q8','w31'):-49.3303,('q8','w32'):-37.2431,('q8','w33'):-24.8286,('q8','w34'):-24.8286,('q8','w35'):-12.4143,('q8','w36'):-12.4143,('q8','w37'):-49.3303,('q8','w38'):-49.4392,('q8','w39'):-49.4392,('q8','w40'):-49.5483,('q8','w41'):-49.5483,('q8','w47'):-61068.6,('q8','w48'):-61068.6,('q8','w53'):-61068.6,('q9','q10'):-772.,('q9','q11'):37.3251,('q9','q12'):30571.6,('q9','q13'):18.6625,('q9','q14'):30553.,('q9','w2'):-24.8834,('q9','w3'):-24.8834,('q9','w5'):-12.4417,('q9','w8'):-36.9975,('q9','w11'):-12.4417,('q9','w12'):-36.9975,('q9','w14'):-37.0792,('q9','w20'):-37.0792,('q9','w22'):-37.161,('q9','w30'):-37.161,('q9','w32'):-37.2431,('q9','w42'):-24.8834,('q9','w43'):-12.4417,('q9','w44'):-36.9975,('q9','w45'):-37.0792,('q9','w46'):-37.161,('q9','w47'):-37.2431,('q9','w48'):-37.2431,('q9','w50'):-61068.6,('q9','w51'):-61068.6,('q9','w52'):-61068.6,('q9','w53'):-61068.6,('q9','w55'):-61068.6,('q9','w56'):-61068.6,('q10','q11'):30571.6,('q10','q12'):30571.6,('q10','q13'):30553.,('q10','q14'):30553.,('q10','w2'):-61068.6,('q10','w5'):-61068.6,('q10','w8'):-61068.6,('q10','w14'):-61068.6,('q10','w22'):-61068.6,('q10','w32'):-61068.6,('q10','w42'):-61068.6,('q10','w43'):-61068.6,('q10','w44'):-61068.6,('q10','w45'):-61068.6,('q10','w46'):-61068.6,('q10','w47'):-61068.6,('q11','q12'):29567.3,('q11','q13'):30553.,('q11','q14'):18.7037,('q11','w1'):-61068.6,('q11','w2'):-61068.6,('q11','w3'):-61068.6,('q11','w6'):-61068.6,('q11','w15'):-61068.6,('q11','w23'):-61068.6,('q11','w33'):-61068.6,('q12','q13'):30553.,('q12','q14'):18.7037,('q12','w1'):-24.6649,('q12','w2'):-24.8834,('q12','w3'):-61068.6,('q12','w7'):-61068.6,('q12','w9'):-61068.6,('q12','w16'):-61068.6,('q12','w24'):-61068.6,('q12','w34'):-61068.6,('q12','w42'):-61068.6,('q12','w49'):-61068.6,('q12','w51'):-61068.6,('q13','q14'):29373.5,('q13','w3'):-12.4691,('q13','w4'):-61068.6,('q13','w5'):-61068.6,('q13','w6'):-61068.6,('q13','w7'):-61068.6,('q13','w11'):-61068.6,('q13','w17'):-61068.6,('q13','w25'):-61068.6,('q13','w35'):-61068.6,('q14','w3'):-12.4691,('q14','w4'):-12.3324,('q14','w5'):-12.4417,('q14','w6'):-12.4691,('q14','w7'):-12.4691,('q14','w10'):-61068.6,('q14','w11'):-61068.6,('q14','w18'):-61068.6,('q14','w26'):-61068.6,('q14','w36'):-61068.6,('q14','w43'):-61068.6,('q14','w54'):-61068.6,('q14','w55'):-61068.6,('q15','q16'):-1357.29,('w1','w49'):16.4433,('w2','w51'):16.5889,('w3','w11'):8.31276,('w3','w20'):16.4796,('w3','w30'):16.5159,('w3','w48'):16.5524,('w4','w54'):8.22161,('w5','w55'):8.29445,('w8','w56'):24.665,('w11','w20'):8.23976,('w11','w30'):8.25795,('w11','w48'):8.27618,('w12','w20'):49.3311,('w12','w30'):41.1088,('w12','w48'):32.8868,('w14','w50'):24.7194,('w20','w30'):41.1996,('w20','w48'):32.9594,('w22','w52'):24.774,('w30','w48'):33.0322,('w32','w53'):24.8287}

Q={**linear, **quadratic}
sampleset=sampler_auto.sample_qubo(Q,num_reads=1000,label='RTU optimization 8steps')
print(sampleset)