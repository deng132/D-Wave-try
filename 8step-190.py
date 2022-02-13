from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler_auto=EmbeddingComposite(DWaveSampler(solver={'topology__type':'pegasus'}))


linear={('q1','q1'):1909.28,('q2','q2'):1909.28,('q3','q3'):1905.59,('q4','q4'):1905.59,('q5','q5'):1912.43,('q6','q6'):1912.43,('q7','q7'):1916.54,('q8','q8'):1916.54,('q9','q9'):1919.29,('q10','q10'):1919.29,('q11','q11'):1926.06,('q12','q12'):1926.06,('q13','q13'):1934.15,('q14','q14'):1934.15,('q15','q15'):1940.88,('q16','q16'):1940.88,('w1','w1'):126151.,('w2','w2'):126151.,('w3','w3'):126151.,('w4','w4'):126151.,('w5','w5'):126151.,('w6','w6'):126151.,('w7','w7'):126151.,('w8','w8'):126151.,('w9','w9'):126151.,('w10','w10'):126151.,('w11','w11'):126151.,('w12','w12'):126151.,('w13','w13'):126151.,('w14','w14'):126151.,('w15','w15'):126151.,('w16','w16'):126151.,('w17','w17'):126151.,('w18','w18'):126151.,('w19','w19'):126151.,('w20','w20'):126151.,('w21','w21'):126151.,('w22','w22'):126151.,('w23','w23'):126151.,('w24','w24'):126151.,('w25','w25'):126151.,('w26','w26'):126151.,('w27','w27'):126151.,('w28','w28'):126151.,('w29','w29'):126151.,('w30','w30'):126151.,('w31','w31'):126151.,('w32','w32'):126151.,('w33','w33'):126151.,('w34','w34'):126151.,('w35','w35'):126151.,('w36','w36'):126151.,('w37','w37'):126151.,('w38','w38'):126151.,('w39','w39'):126151.,('w40','w40'):126151.,('w41','w41'):126151.,('w42','w42'):126151.,('w43','w43'):126151.,('w44','w44'):126151.,('w45','w45'):126151.,('w46','w46'):126151.,('w47','w47'):126151.,('w48','w48'):126151.,('w49','w49'):126151.,('w50','w50'):126151.,('w51','w51'):126151.,('w52','w52'):126151.,('w53','w53'):126151.,('w54','w54'):126151.,('w55','w55'):126151.,('w56','w56'):126151.}

quadratic={('q1','q2'):40774.2,('q1','q3'):42051.3,('q1','q4'):0.770798,('q1','q5'):42051.1,('q1','q6'):0.642326,('q1','q7'):42051.,('q1','q8'):0.513857,('q1','q9'):0.38539,('q1','q10'):42050.9,('q1','q11'):42050.8,('q1','q12'):42050.8,('q1','q13'):42050.6,('q1','q14'):42050.6,('q1','w1'):-84101.,('q1','w4'):-84101.,('q1','w8'):-84101.,('q1','w9'):-84101.,('q1','w10'):-84101.,('q1','w12'):-84101.,('q1','w13'):-84101.,('q1','w21'):-84101.,('q1','w31'):-84101.,('q2','q3'):42051.3,('q2','q4'):0.770798,('q2','q5'):42051.1,('q2','q6'):0.642326,('q2','q7'):42051.,('q2','q8'):0.513857,('q2','q9'):42050.9,('q2','q10'):42050.9,('q2','q11'):0.256926,('q2','q12'):42050.8,('q2','q13'):0.128463,('q2','q14'):42050.6,('q2','w1'):-0.171284,('q2','w3'):-0.171284,('q2','w4'):-0.0856418,('q2','w8'):-0.256927,('q2','w9'):-0.171284,('q2','w10'):-0.0856418,('q2','w11'):-0.0856418,('q2','w12'):-84101.,('q2','w19'):-84101.,('q2','w27'):-84101.,('q2','w37'):-84101.,('q2','w44'):-84101.,('q2','w49'):-84101.,('q2','w54'):-84101.,('q2','w56'):-84101.,('q3','q4'):40776.7,('q3','q5'):42051.1,('q3','q6'):0.643744,('q3','q7'):42051.,('q3','q8'):0.514991,('q3','q9'):0.386241,('q3','q10'):42050.9,('q3','q11'):42050.8,('q3','q12'):42050.8,('q3','q13'):42050.6,('q3','q14'):42050.6,('q3','w3'):-0.171662,('q3','w11'):-0.0858308,('q3','w12'):-0.513865,('q3','w13'):-84101.,('q3','w14'):-84101.,('q3','w15'):-84101.,('q3','w16'):-84101.,('q3','w17'):-84101.,('q3','w18'):-84101.,('q3','w19'):-84101.,('q3','w20'):-84101.,('q3','w28'):-84101.,('q3','w38'):-84101.,('q4','q5'):42051.1,('q4','q6'):0.643744,('q4','q7'):42051.,('q4','q8'):0.514991,('q4','q9'):42050.9,('q4','q10'):42050.9,('q4','q11'):0.257493,('q4','q12'):0.257493,('q4','q13'):0.128746,('q4','q14'):0.128746,('q4','w3'):-0.171662,('q4','w11'):-0.0858308,('q4','w12'):-0.513865,('q4','w13'):-0.513865,('q4','w14'):-0.257494,('q4','w15'):-0.171662,('q4','w16'):-0.171662,('q4','w17'):-0.0858308,('q4','w18'):-0.0858308,('q4','w19'):-0.513865,('q4','w20'):-84101.,('q4','w29'):-84101.,('q4','w39'):-84101.,('q4','w45'):-84101.,('q4','w50'):-84101.,('q5','q6'):40772.2,('q5','q7'):42051.,('q5','q8'):0.516128,('q5','q9'):0.387094,('q5','q10'):42050.9,('q5','q11'):42050.8,('q5','q12'):42050.8,('q5','q13'):42050.6,('q5','q14'):42050.6,('q5','w3'):-0.172041,('q5','w11'):-0.0860203,('q5','w12'):-0.428217,('q5','w20'):-0.429162,('q5','w21'):-84101.,('q5','w22'):-84101.,('q5','w23'):-84101.,('q5','w24'):-84101.,('q5','w25'):-84101.,('q5','w26'):-84101.,('q5','w27'):-84101.,('q5','w28'):-84101.,('q5','w29'):-84101.,('q5','w30'):-84101.,('q5','w40'):-84101.,('q6','q7'):42051.,('q6','q8'):0.516128,('q6','q9'):42050.9,('q6','q10'):42050.9,('q6','q11'):0.258062,('q6','q12'):0.258062,('q6','q13'):0.12903,('q6','q14'):0.12903,('q6','w3'):-0.172041,('q6','w11'):-0.0860203,('q6','w12'):-0.428217,('q6','w20'):-0.429162,('q6','w21'):-0.428217,('q6','w22'):-0.258063,('q6','w23'):-0.172041,('q6','w24'):-0.172041,('q6','w25'):-0.0860203,('q6','w26'):-0.0860203,('q6','w27'):-0.428217,('q6','w28'):-0.429162,('q6','w29'):-0.429162,('q6','w30'):-84101.,('q6','w41'):-84101.,('q6','w46'):-84101.,('q6','w52'):-84101.,('q7','q8'):40769.3,('q7','q9'):0.387948,('q7','q10'):42050.9,('q7','q11'):42050.8,('q7','q12'):42050.8,('q7','q13'):42050.6,('q7','q14'):42050.6,('q7','w3'):-0.172421,('q7','w11'):-0.0862102,('q7','w12'):-0.342571,('q7','w20'):-0.343327,('q7','w30'):-0.344085,('q7','w31'):-84101.,('q7','w32'):-84101.,('q7','w33'):-84101.,('q7','w34'):-84101.,('q7','w35'):-84101.,('q7','w36'):-84101.,('q7','w37'):-84101.,('q7','w38'):-84101.,('q7','w39'):-84101.,('q7','w40'):-84101.,('q7','w41'):-84101.,('q7','w48'):-84101.,('q8','q9'):42050.9,('q8','q10'):42050.9,('q8','q11'):0.258631,('q8','q12'):0.258631,('q8','q13'):0.129315,('q8','q14'):0.129315,('q8','w3'):-0.172421,('q8','w11'):-0.0862102,('q8','w12'):-0.342571,('q8','w20'):-0.343327,('q8','w30'):-0.344085,('q8','w31'):-0.342571,('q8','w32'):-0.258632,('q8','w33'):-0.172421,('q8','w34'):-0.172421,('q8','w35'):-0.0862102,('q8','w36'):-0.0862102,('q8','w37'):-0.342571,('q8','w38'):-0.343327,('q8','w39'):-0.343327,('q8','w40'):-0.344085,('q8','w41'):-0.344085,('q8','w47'):-84101.,('q8','w48'):-84101.,('q8','w53'):-84101.,('q9','q10'):-1283.17,('q9','q11'):0.259202,('q9','q12'):42050.8,('q9','q13'):0.129601,('q9','q14'):42050.6,('q9','w2'):-0.172801,('q9','w3'):-0.172801,('q9','w5'):-0.0864005,('q9','w8'):-0.256927,('q9','w11'):-0.0864005,('q9','w12'):-0.256927,('q9','w14'):-0.257494,('q9','w20'):-0.257494,('q9','w22'):-0.258063,('q9','w30'):-0.258063,('q9','w32'):-0.258632,('q9','w42'):-0.172801,('q9','w43'):-0.0864005,('q9','w44'):-0.256927,('q9','w45'):-0.257494,('q9','w46'):-0.258063,('q9','w47'):-0.258632,('q9','w48'):-0.258632,('q9','w50'):-84101.,('q9','w51'):-84101.,('q9','w52'):-84101.,('q9','w53'):-84101.,('q9','w55'):-84101.,('q9','w56'):-84101.,('q10','q11'):42050.8,('q10','q12'):42050.8,('q10','q13'):42050.6,('q10','q14'):42050.6,('q10','w2'):-84101.,('q10','w5'):-84101.,('q10','w8'):-84101.,('q10','w14'):-84101.,('q10','w22'):-84101.,('q10','w32'):-84101.,('q10','w42'):-84101.,('q10','w43'):-84101.,('q10','w44'):-84101.,('q10','w45'):-84101.,('q10','w46'):-84101.,('q10','w47'):-84101.,('q11','q12'):40762.8,('q11','q13'):42050.6,('q11','q14'):0.129887,('q11','w1'):-84101.,('q11','w2'):-84101.,('q11','w3'):-84101.,('q11','w6'):-84101.,('q11','w15'):-84101.,('q11','w23'):-84101.,('q11','w33'):-84101.,('q12','q13'):42050.6,('q12','q14'):0.129887,('q12','w1'):-0.171284,('q12','w2'):-0.172801,('q12','w3'):-84101.,('q12','w7'):-84101.,('q12','w9'):-84101.,('q12','w16'):-84101.,('q12','w24'):-84101.,('q12','w34'):-84101.,('q12','w42'):-84101.,('q12','w49'):-84101.,('q12','w51'):-84101.,('q13','q14'):40757.6,('q13','w3'):-0.0865913,('q13','w4'):-84101.,('q13','w5'):-84101.,('q13','w6'):-84101.,('q13','w7'):-84101.,('q13','w11'):-84101.,('q13','w17'):-84101.,('q13','w25'):-84101.,('q13','w35'):-84101.,('q14','w3'):-0.0865913,('q14','w4'):-0.0856418,('q14','w5'):-0.0864005,('q14','w6'):-0.0865913,('q14','w7'):-0.0865913,('q14','w10'):-84101.,('q14','w11'):-84101.,('q14','w18'):-84101.,('q14','w26'):-84101.,('q14','w36'):-84101.,('q14','w43'):-84101.,('q14','w54'):-84101.,('q14','w55'):-84101.,('q15','q16'):-1297.39,('w1','w49'):0.114189,('w2','w51'):0.115201,('w3','w11'):0.0577275,('w3','w20'):0.114441,('w3','w30'):0.114694,('w3','w48'):0.114947,('w4','w54'):0.0570945,('w5','w55'):0.0576004,('w8','w56'):0.171285,('w11','w20'):0.0572206,('w11','w30'):0.0573469,('w11','w48'):0.0574735,('w12','w20'):0.342577,('w12','w30'):0.285478,('w12','w48'):0.228381,('w14','w50'):0.171663,('w20','w30'):0.286108,('w20','w48'):0.228885,('w22','w52'):0.172042,('w30','w48'):0.22939,('w32','w53'):0.172422}

Q={**linear, **quadratic}
sampleset=sampler_auto.sample_qubo(Q,num_reads=1000,label='RTU optimization 8steps')
print(sampleset)