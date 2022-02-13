from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler_auto=EmbeddingComposite(DWaveSampler(solver={'topology__type':'pegasus'}))


linear={('q1','q1'):33206.7 q10,('q2','q2'):337.815,('q3','q3'):620.165,('q4','q4'):620.165,('q5','q5'):906.915,('q6','q6'):906.915,('q7','q7'):1189.79,('q8','q8'):1189.79,('q9','q9'):1470.43,('q10','q10'):1470.43,('q11','q11'):1752.31,('q12','q12'):1752.31,('q13','q13'):2036.28,('q14','q14'):2036.28,('q15','q15'):2043.94,('q16','q16'):2043.94,('w1','w1'):99508.5,('w2','w2'):99508.5,('w3','w3'):99508.5,('w4','w4'):99508.5,('w5','w5'):99508.5,('w6','w6'):99508.5,('w7','w7'):99508.5,('w8','w8'):99508.5,('w9','w9'):99508.5,('w10','w10'):99508.5,('w11','w11'):99508.5,('w12','w12'):99508.5,('w13','w13'):99508.5,('w14','w14'):99508.5,('w15','w15'):99508.5,('w16','w16'):99508.5,('w17','w17'):99508.5,('w18','w18'):99508.5,('w19','w19'):99508.5,('w20','w20'):99508.5,('w21','w21'):99508.5,('w22','w22'):99508.5,('w23','w23'):99508.5,('w24','w24'):99508.5,('w25','w25'):99508.5,('w26','w26'):99508.5,('w27','w27'):99508.5,('w28','w28'):99508.5,('w29','w29'):99508.5,('w30','w30'):99508.5,('w31','w31'):99508.5,('w32','w32'):99508.5,('w33','w33'):99508.5,('w34','w34'):99508.5,('w35','w35'):99508.5,('w36','w36'):99508.5,('w37','w37'):99508.5,('w38','w38'):99508.5,('w39','w39'):99508.5,('w40','w40'):99508.5,('w41','w41'):99508.5,('w42','w42'):99508.5,('w43','w43'):99508.5,('w44','w44'):99508.5,('w45','w45'):99508.5,('w46','w46'):99508.5,('w47','w47'):99508.5,('w48','w48'):99508.5,('w49','w49'):99508.5,('w50','w50'):99508.5,('w51','w51'):99508.5,('w52','w52'):99508.5,('w53','w53'):99508.5,('w54','w54'):99508.5,('w55','w55'):99508.5,('w56','w56'):99508.5}

quadratic={('q1','q2'):32969.5,('q1','q3'):33262.3,('q1','q4'):92.8262,('q1','q5'):33243.8,('q1','q6'):74.2861,('q1','q7'):33225.2,('q1','q8'):55.7464,('q1','q9'):37.2069,('q1','q10'):33206.7,('q1','q11'):33188.2,('q1','q12'):33188.2,('q1','q13'):33169.6,('q1','q14'):33169.6,('q1','w1'):-66339.,('q1','w4'):-66339.,('q1','w8'):-66339.,('q1','w9'):-66339.,('q1','w10'):-66339.,('q1','w12'):-66339.,('q1','w13'):-66339.,('q1','w21'):-66339.,('q1','w31'):-66339.,('q2','q3'):33262.3,('q2','q4'):92.8262,('q2','q5'):33243.8,('q2','q6'):74.2861,('q2','q7'):33225.2,('q2','q8'):55.7464,('q2','q9'):33206.7,('q2','q10'):33206.7,('q2','q11'):18.6676,('q2','q12'):33188.2,('q2','q13'):0.128463,('q2','q14'):33169.6,('q2','w1'):-12.4451,('q2','w3'):-12.4451,('q2','w4'):-0.0856418,('q2','w8'):-24.8046,('q2','w9'):-12.4451,('q2','w10'):-0.0856418,('q2','w11'):-0.0856418,('q2','w12'):-66339.,('q2','w19'):-66339.,('q2','w27'):-66339.,('q2','w37'):-66339.,('q2','w44'):-66339.,('q2','w49'):-66339.,('q2','w54'):-66339.,('q2','w56'):-66339.,('q3','q4'):32777.4,('q3','q5'):33243.9,('q3','q6'):74.4501,('q3','q7'):33225.4,('q3','q8'):55.8694,('q3','q9'):37.289,('q3','q10'):33206.8,('q3','q11'):33188.2,('q3','q12'):33188.2,('q3','q13'):33169.6,('q3','q14'):33169.6,('q3','w3'):-12.4726,('q3','w11'):-0.0858308,('q3','w12'):-61.8841,('q3','w13'):-66339.,('q3','w14'):-66339.,('q3','w15'):-66339.,('q3','w16'):-66339.,('q3','w17'):-66339.,('q3','w18'):-66339.,('q3','w19'):-66339.,('q3','w20'):-66339.,('q3','w28'):-66339.,('q3','w38'):-66339.,('q4','q5'):33243.9,('q4','q6'):74.4501,('q4','q7'):33225.4,('q4','q8'):55.8694,('q4','q9'):33206.8,('q4','q10'):33206.8,('q4','q11'):18.7088,('q4','q12'):18.7088,('q4','q13'):0.128746,('q4','q14'):0.128746,('q4','w3'):-12.4726,('q4','w11'):-0.0858308,('q4','w12'):-61.8841,('q4','w13'):-61.8841,('q4','w14'):-24.8594,('q4','w15'):-12.4726,('q4','w16'):-12.4726,('q4','w17'):-0.0858308,('q4','w18'):-0.0858308,('q4','w19'):-61.8841,('q4','w20'):-66339.,('q4','w29'):-66339.,('q4','w39'):-66339.,('q4','w45'):-66339.,('q4','w50'):-66339.,('q5','q6'):32582.6,('q5','q7'):33225.5,('q5','q8'):55.9928,('q5','q9'):37.3714,('q5','q10'):33206.9,('q5','q11'):33188.2,('q5','q12'):33188.2,('q5','q13'):33169.6,('q5','q14'):33169.6,('q5','w3'):-12.5001,('q5','w11'):-0.0860203,('q5','w12'):-49.524,('q5','w20'):-49.6334,('q5','w21'):-66339.,('q5','w22'):-66339.,('q5','w23'):-66339.,('q5','w24'):-66339.,('q5','w25'):-66339.,('q5','w26'):-66339.,('q5','w27'):-66339.,('q5','w28'):-66339.,('q5','w29'):-66339.,('q5','w30'):-66339.,('q5','w40'):-66339.,('q6','q7'):33225.5,('q6','q8'):55.9928,('q6','q9'):33206.9,('q6','q10'):33206.9,('q6','q11'):18.7502,('q6','q12'):18.7502,('q6','q13'):0.12903,('q6','q14'):0.12903,('q6','w3'):-12.5001,('q6','w11'):-0.0860203,('q6','w12'):-49.524,('q6','w20'):-49.6334,('q6','w21'):-49.524,('q6','w22'):-24.9142,('q6','w23'):-12.5001,('q6','w24'):-12.5001,('q6','w25'):-0.0860203,('q6','w26'):-0.0860203,('q6','w27'):-49.524,('q6','w28'):-49.6334,('q6','w29'):-49.6334,('q6','w30'):-66339.,('q6','w41'):-66339.,('q6','w46'):-66339.,('q6','w52'):-66339.,('q7','q8'):32390.,('q7','q9'):37.4539,('q7','q10'):33207.,('q7','q11'):33188.3,('q7','q12'):33188.3,('q7','q13'):33169.6,('q7','q14'):33169.6,('q7','w3'):-12.5277,('q7','w11'):-0.0862102,('q7','w12'):-37.1642,('q7','w20'):-37.2463,('q7','w30'):-37.3285,('q7','w31'):-66339.,('q7','w32'):-66339.,('q7','w33'):-66339.,('q7','w34'):-66339.,('q7','w35'):-66339.,('q7','w36'):-66339.,('q7','w37'):-66339.,('q7','w38'):-66339.,('q7','w39'):-66339.,('q7','w40'):-66339.,('q7','w41'):-66339.,('q7','w48'):-66339.,('q8','q9'):33207.,('q8','q10'):33207.,('q8','q11'):18.7915,('q8','q12'):18.7915,('q8','q13'):0.129315,('q8','q14'):0.129315,('q8','w3'):-12.5277,('q8','w11'):-0.0862102,('q8','w12'):-37.1642,('q8','w20'):-37.2463,('q8','w30'):-37.3285,('q8','w31'):-37.1642,('q8','w32'):-24.9692,('q8','w33'):-12.5277,('q8','w34'):-12.5277,('q8','w35'):-0.0862102,('q8','w36'):-0.0862102,('q8','w37'):-37.1642,('q8','w38'):-37.2463,('q8','w39'):-37.2463,('q8','w40'):-37.3285,('q8','w41'):-37.3285,('q8','w47'):-66339.,('q8','w48'):-66339.,('q8','w53'):-66339.,('q9','q10'):-970.847,('q9','q11'):18.833,('q9','q12'):33188.3,('q9','q13'):0.129601,('q9','q14'):33169.6,('q9','w2'):-12.5554,('q9','w3'):-12.5554,('q9','w5'):-0.0864005,('q9','w8'):-24.8046,('q9','w11'):-0.0864005,('q9','w12'):-24.8046,('q9','w14'):-24.8594,('q9','w20'):-24.8594,('q9','w22'):-24.9142,('q9','w30'):-24.9142,('q9','w32'):-24.9692,('q9','w42'):-12.5554,('q9','w43'):-0.0864005,('q9','w44'):-24.8046,('q9','w45'):-24.8594,('q9','w46'):-24.9142,('q9','w47'):-24.9692,('q9','w48'):-24.9692,('q9','w50'):-66339.,('q9','w51'):-66339.,('q9','w52'):-66339.,('q9','w53'):-66339.,('q9','w55'):-66339.,('q9','w56'):-66339.,('q10','q11'):33188.3,('q10','q12'):33188.3,('q10','q13'):33169.6,('q10','q14'):33169.6,('q10','w2'):-66339.,('q10','w5'):-66339.,('q10','w8'):-66339.,('q10','w14'):-66339.,('q10','w22'):-66339.,('q10','w32'):-66339.,('q10','w42'):-66339.,('q10','w43'):-66339.,('q10','w44'):-66339.,('q10','w45'):-66339.,('q10','w46'):-66339.,('q10','w47'):-66339.,('q11','q12'):32006.4,('q11','q13'):33169.6,('q11','q14'):0.129887,('q11','w1'):-66339.,('q11','w2'):-66339.,('q11','w3'):-66339.,('q11','w6'):-66339.,('q11','w15'):-66339.,('q11','w23'):-66339.,('q11','w33'):-66339.,('q12','q13'):33169.6,('q12','q14'):0.129887,('q12','w1'):-12.4451,('q12','w2'):-12.5554,('q12','w3'):-66339.,('q12','w7'):-66339.,('q12','w9'):-66339.,('q12','w16'):-66339.,('q12','w24'):-66339.,('q12','w34'):-66339.,('q12','w42'):-66339.,('q12','w49'):-66339.,('q12','w51'):-66339.,('q13','q14'):31813.,('q13','w3'):-0.0865913,('q13','w4'):-66339.,('q13','w5'):-66339.,('q13','w6'):-66339.,('q13','w7'):-66339.,('q13','w11'):-66339.,('q13','w17'):-66339.,('q13','w25'):-66339.,('q13','w35'):-66339.,('q14','w3'):-0.0865913,('q14','w4'):-0.0856418,('q14','w5'):-0.0864005,('q14','w6'):-0.0865913,('q14','w7'):-0.0865913,('q14','w10'):-66339.,('q14','w11'):-66339.,('q14','w18'):-66339.,('q14','w26'):-66339.,('q14','w36'):-66339.,('q14','w43'):-66339.,('q14','w54'):-66339.,('q14','w55'):-66339.,('q15','q16'):-1361.66,('w1','w49'):8.29673,('w2','w51'):8.37024,('w3','w11'):0.0577275,('w3','w20'):8.31504,('w3','w30'):8.3334,('w3','w48'):8.3518,('w4','w54'):0.0570945,('w5','w55'):0.0576004,('w8','w56'):16.5364,('w11','w20'):0.0572206,('w11','w30'):0.0573469,('w11','w48'):0.0574735,('w12','w20'):41.2561,('w12','w30'):33.016,('w12','w48'):24.7762,('w14','w50'):16.5729,('w20','w30'):33.0889,('w20','w48'):24.8309,('w22','w52'):16.6095,('w30','w48'):24.8857,('w32','w53'):16.6462}

Q={**linear, **quadratic}
sampleset=sampler_auto.sample_qubo(Q,num_reads=1000,label='RTU optimization 8steps')
print(sampleset)