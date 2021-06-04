import matplotlib.pyplot as plt

N = 48223786
S = N - 34709
I = 34709
beta = 0.6

sus = [] # Comportamiento de los suseptibles.
inf = [] # Comportamiento de los infectados.
prob = [] # Comportamiento probabilidad de infección.

def infection(S, I, N):
    t = 0
    while (t < 40):
        S, I = S - beta * ((S * I / N)), I + beta * ((S * I) / N)
        p = beta * (I / N)

        sus.append(S)
        inf.append(I)
        prob.append(p)
        t = t + 1

infection(S, I, N)
figure = plt.figure()
figure.canvas.set_window_title('Modelo SI')

figure.add_subplot(211)
inf_line, =plt.plot(inf, label='I(t)')

sus_line, = plt.plot(sus, label='S(t)')
plt.legend(handles=[inf_line, sus_line])

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0)) 

ax = figure.add_subplot(212)
prob_line = plt.plot(prob, label='p(t)')
plt.legend(handles=prob_line)

type(ax)  

vals = ax.get_yticks()
ax.set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals])


plt.xlabel('T')
plt.ylabel('p')

plt.show()