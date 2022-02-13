from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler_auto=EmbeddingComposite(DWaveSampler(solver={'topology__type':'pegasus'}))


linear={('q1','q1'):58512.6 q10,('q2','q2'):2834.87,('q3','q3'):2669.94,('q4','q4'):2669.94,('q5','q5'):2527.68,('q6','q6'):2527.68,('q7','q7'):2402.57,('q8','q8'):2402.57,('q9','q9'):2265.71,('q10','q10'):2265.71,('q11','q11'):2135.87,('q12','q12'):2135.87,('q13','q13'):2024.22,('q14','q14'):2024.22,('q15','q15'):1951.91,('q16','q16'):1951.91,('w1','w1'):175371.,('w2','w2'):175371.,('w3','w3'):175371.,('w4','w4'):175371.,('w5','w5'):175371.,('w6','w6'):175371.,('w7','w7'):175371.,('w8','w8'):175371.,('w9','w9'):175371.,('w10','w10'):175371.,('w11','w11'):175371.,('w12','w12'):175371.,('w13','w13'):175371.,('w14','w14'):175371.,('w15','w15'):175371.,('w16','w16'):175371.,('w17','w17'):175371.,('w18','w18'):175371.,('w19','w19'):175371.,('w20','w20'):175371.,('w21','w21'):175371.,('w22','w22'):175371.,('w23','w23'):175371.,('w24','w24'):175371.,('w25','w25'):175371.,('w26','w26'):175371.,('w27','w27'):175371.,('w28','w28'):175371.,('w29','w29'):175371.,('w30','w30'):175371.,('w31','w31'):175371.,('w32','w32'):175371.,('w33','w33'):175371.,('w34','w34'):175371.,('w35','w35'):175371.,('w36','w36'):175371.,('w37','w37'):175371.,('w38','w38'):175371.,('w39','w39'):175371.,('w40','w40'):175371.,('w41','w41'):175371.,('w42','w42'):175371.,('w43','w43'):175371.,('w44','w44'):175371.,('w45','w45'):175371.,('w46','w46'):175371.,('w47','w47'):175371.,('w48','w48'):175371.,('w49','w49'):175371.,('w50','w50'):175371.,('w51','w51'):175371.,('w52','w52'):175371.,('w53','w53'):175371.,('w54','w54'):175371.,('w55','w55'):175371.,('w56','w56'):175371.}

quadratic={('q1','q2'):56594.6,('q1','q3'):58568.1,('q1','q4'):110.995,('q1','q5'):58549.6,('q1','q6'):92.4949,('q1','q7'):58531.1,('q1','q8'):73.9954,('q1','q9'):55.4962,('q1','q10'):58512.6,('q1','q11'):58494.1,('q1','q12'):58494.1,('q1','q13'):58475.6,('q1','q14'):58475.6,('q1','w1'):-116914.,('q1','w4'):-116914.,('q1','w8'):-116914.,('q1','w9'):-116914.,('q1','w10'):-116914.,('q1','w12'):-116914.,('q1','w13'):-116914.,('q1','w21'):-116914.,('q1','w31'):-116914.,('q2','q3'):58568.1,('q2','q4'):110.995,('q2','q5'):58549.6,('q2','q6'):92.4949,('q2','q7'):58531.1,('q2','q8'):73.9954,('q2','q9'):58512.6,('q2','q10'):58512.6,('q2','q11'):36.9973,('q2','q12'):58494.1,('q2','q13'):18.4986,('q2','q14'):58475.6,('q2','w1'):-24.6649,('q2','w3'):-24.6649,('q2','w4'):-12.3324,('q2','w8'):-36.9975,('q2','w9'):-24.6649,('q2','w10'):-12.3324,('q2','w11'):-12.3324,('q2','w12'):-116914.,('q2','w19'):-116914.,('q2','w27'):-116914.,('q2','w37'):-116914.,('q2','w44'):-116914.,('q2','w49'):-116914.,('q2','w54'):-116914.,('q2','w56'):-116914.,('q3','q4'):56699.9,('q3','q5'):58549.8,('q3','q6'):92.6991,('q3','q7'):58531.2,('q3','q8'):74.1587,('q3','q9'):55.6187,('q3','q10'):58512.7,('q3','q11'):58494.2,('q3','q12'):58494.2,('q3','q13'):58475.6,('q3','q14'):58475.6,('q3','w3'):-24.7193,('q3','w11'):-12.3596,('q3','w12'):-73.9966,('q3','w13'):-116914.,('q3','w14'):-116914.,('q3','w15'):-116914.,('q3','w16'):-116914.,('q3','w17'):-116914.,('q3','w18'):-116914.,('q3','w19'):-116914.,('q3','w20'):-116914.,('q3','w28'):-116914.,('q3','w38'):-116914.,('q4','q5'):58549.8,('q4','q6'):92.6991,('q4','q7'):58531.2,('q4','q8'):74.1587,('q4','q9'):58512.7,('q4','q10'):58512.7,('q4','q11'):37.079,('q4','q12'):37.079,('q4','q13'):18.5395,('q4','q14'):18.5395,('q4','w3'):-24.7193,('q4','w11'):-12.3596,('q4','w12'):-73.9966,('q4','w13'):-73.9966,('q4','w14'):-37.0792,('q4','w15'):-24.7193,('q4','w16'):-24.7193,('q4','w17'):-12.3596,('q4','w18'):-12.3596,('q4','w19'):-73.9966,('q4','w20'):-116914.,('q4','w29'):-116914.,('q4','w39'):-116914.,('q4','w45'):-116914.,('q4','w50'):-116914.,('q5','q6'):56790.5,('q5','q7'):58531.4,('q5','q8'):74.3225,('q5','q9'):55.7415,('q5','q10'):58512.8,('q5','q11'):58494.2,('q5','q12'):58494.2,('q5','q13'):58475.7,('q5','q14'):58475.7,('q5','w3'):-24.7739,('q5','w11'):-12.3869,('q5','w12'):-61.6633,('q5','w20'):-61.7994,('q5','w21'):-116914.,('q5','w22'):-116914.,('q5','w23'):-116914.,('q5','w24'):-116914.,('q5','w25'):-116914.,('q5','w26'):-116914.,('q5','w27'):-116914.,('q5','w28'):-116914.,('q5','w29'):-116914.,('q5','w30'):-116914.,('q5','w40'):-116914.,('q6','q7'):58531.4,('q6','q8'):74.3225,('q6','q9'):58512.8,('q6','q10'):58512.8,('q6','q11'):37.1609,('q6','q12'):37.1609,('q6','q13'):18.5804,('q6','q14'):18.5804,('q6','w3'):-24.7739,('q6','w11'):-12.3869,('q6','w12'):-61.6633,('q6','w20'):-61.7994,('q6','w21'):-61.6633,('q6','w22'):-37.161,('q6','w23'):-24.7739,('q6','w24'):-24.7739,('q6','w25'):-12.3869,('q6','w26'):-12.3869,('q6','w27'):-61.6633,('q6','w28'):-61.7994,('q6','w29'):-61.7994,('q6','w30'):-116914.,('q6','w41'):-116914.,('q6','w46'):-116914.,('q6','w52'):-116914.,('q7','q8'):56871.,('q7','q9'):55.8646,('q7','q10'):58512.9,('q7','q11'):58494.3,('q7','q12'):58494.3,('q7','q13'):58475.7,('q7','q14'):58475.7,('q7','w3'):-24.8286,('q7','w11'):-12.4143,('q7','w12'):-49.3303,('q7','w20'):-49.4392,('q7','w30'):-49.5483,('q7','w31'):-116914.,('q7','w32'):-116914.,('q7','w33'):-116914.,('q7','w34'):-116914.,('q7','w35'):-116914.,('q7','w36'):-116914.,('q7','w37'):-116914.,('q7','w38'):-116914.,('q7','w39'):-116914.,('q7','w40'):-116914.,('q7','w41'):-116914.,('q7','w48'):-116914.,('q8','q9'):58512.9,('q8','q10'):58512.9,('q8','q11'):37.2429,('q8','q12'):37.2429,('q8','q13'):18.6214,('q8','q14'):18.6214,('q8','w3'):-24.8286,('q8','w11'):-12.4143,('q8','w12'):-49.3303,('q8','w20'):-49.4392,('q8','w30'):-49.5483,('q8','w31'):-49.3303,('q8','w32'):-37.2431,('q8','w33'):-24.8286,('q8','w34'):-24.8286,('q8','w35'):-12.4143,('q8','w36'):-12.4143,('q8','w37'):-49.3303,('q8','w38'):-49.4392,('q8','w39'):-49.4392,('q8','w40'):-49.5483,('q8','w41'):-49.5483,('q8','w47'):-116914.,('q8','w48'):-116914.,('q8','w53'):-116914.,('q9','q10'):-1498.92,('q9','q11'):37.3251,('q9','q12'):58494.4,('q9','q13'):18.6625,('q9','q14'):58475.7,('q9','w2'):-24.8834,('q9','w3'):-24.8834,('q9','w5'):-12.4417,('q9','w8'):-36.9975,('q9','w11'):-12.4417,('q9','w12'):-36.9975,('q9','w14'):-37.0792,('q9','w20'):-37.0792,('q9','w22'):-37.161,('q9','w30'):-37.161,('q9','w32'):-37.2431,('q9','w42'):-24.8834,('q9','w43'):-12.4417,('q9','w44'):-36.9975,('q9','w45'):-37.0792,('q9','w46'):-37.161,('q9','w47'):-37.2431,('q9','w48'):-37.2431,('q9','w50'):-116914.,('q9','w51'):-116914.,('q9','w52'):-116914.,('q9','w53'):-116914.,('q9','w55'):-116914.,('q9','w56'):-116914.,('q10','q11'):58494.4,('q10','q12'):58494.4,('q10','q13'):58475.7,('q10','q14'):58475.7,('q10','w2'):-116914.,('q10','w5'):-116914.,('q10','w8'):-116914.,('q10','w14'):-116914.,('q10','w22'):-116914.,('q10','w32'):-116914.,('q10','w42'):-116914.,('q10','w43'):-116914.,('q10','w44'):-116914.,('q10','w45'):-116914.,('q10','w46'):-116914.,('q10','w47'):-116914.,('q11','q12'):57039.4,('q11','q13'):58475.8,('q11','q14'):18.7037,('q11','w1'):-116914.,('q11','w2'):-116914.,('q11','w3'):-116914.,('q11','w6'):-116914.,('q11','w15'):-116914.,('q11','w23'):-116914.,('q11','w33'):-116914.,('q12','q13'):58475.8,('q12','q14'):18.7037,('q12','w1'):-24.6649,('q12','w2'):-24.8834,('q12','w3'):-116914.,('q12','w7'):-116914.,('q12','w9'):-116914.,('q12','w16'):-116914.,('q12','w24'):-116914.,('q12','w34'):-116914.,('q12','w42'):-116914.,('q12','w49'):-116914.,('q12','w51'):-116914.,('q13','q14'):57107.9,('q13','w3'):-12.4691,('q13','w4'):-116914.,('q13','w5'):-116914.,('q13','w6'):-116914.,('q13','w7'):-116914.,('q13','w11'):-116914.,('q13','w17'):-116914.,('q13','w25'):-116914.,('q13','w35'):-116914.,('q14','w3'):-12.4691,('q14','w4'):-12.3324,('q14','w5'):-12.4417,('q14','w6'):-12.4691,('q14','w7'):-12.4691,('q14','w10'):-116914.,('q14','w11'):-116914.,('q14','w18'):-116914.,('q14','w26'):-116914.,('q14','w36'):-116914.,('q14','w43'):-116914.,('q14','w54'):-116914.,('q14','w55'):-116914.,('q15','q16'):-1306.49,('w1','w49'):16.4433,('w2','w51'):16.5889,('w3','w11'):8.31276,('w3','w20'):16.4796,('w3','w30'):16.5159,('w3','w48'):16.5524,('w4','w54'):8.22161,('w5','w55'):8.29445,('w8','w56'):24.665,('w11','w20'):8.23976,('w11','w30'):8.25795,('w11','w48'):8.27618,('w12','w20'):49.3311,('w12','w30'):41.1088,('w12','w48'):32.8868,('w14','w50'):24.7194,('w20','w30'):41.1996,('w20','w48'):32.9594,('w22','w52'):24.774,('w30','w48'):33.0322,('w32','w53'):24.8287}

Q={**linear, **quadratic}
sampleset=sampler_auto.sample_qubo(Q,num_reads=1000,label='RTU optimization 8steps')
print(sampleset)