import math

alfa = (math.sqrt(5)-1)/2

def calcDeltaT(tm,t0):
    dt= (1-alfa)*(tm-t0)
    return dt

def gss(f,t0, tm,delta):
    t0,tm = (min(t0,tm),max(t0,tm))
    j=0
    deltaT = calcDeltaT(tm,t0)
    t1=t0
    t4=tm
    t2 = t0+deltaT
    t3 = t4-deltaT
    t=t1
    l=0
    while True:
        q=f(t)
        if (t==t1):
            q1=q
            if(j<4):
                q0=q1
                q_best = q1
                t_best = t
                j=1
                t=t2
                continue
        elif (t==t2):
            q2=q
        elif (t==t3):
            q3=q
        else:
            q4=q
        if(q<q_best):
            q_best=q
            t_best=t
            l+=1
        j+=1
        if(j<4):
            if(t==t2):
                t=t3
            else:
                t=t4
            continue
        if(j>=J):
            if l>0:
                return tm,t0,q0,q_best,t_best,deltaT,j,l
            else:
                print "BLAD"
                break
        if(abs(deltaT)<delta):
            return tm, t0, q0, q_best, t_best, deltaT, j, l
        if (r==0):
            if(q1<min(q2,q3,q4)):
                t3=t2
                q3=q2
                t2=t1
                q2=q1
                deltaT=(1+alfa)*deltaT
                t1=t1-deltaT
                t=t1
                continue
            elif(q4<min(q1,q2,q3)):
                t2=t3
                q2=q3
                t3=t4
                q3=q4
                deltaT=(1+alfa)*deltaT
                t4=t4+deltaT
                t=t4
                continue
        if(q2<=q3):
            t4=t3
            q4=q3
            t3=t2
            q3=q2
            deltaT=alfa*deltaT
            t2=t1+deltaT
            t=t2
            continue
        else:
            t1=t2
            q1=q2
            t2=t3
            q2=q3
            deltaT=alfa*deltaT
            t3=t4-deltaT
            t=t3
            continue





# t0, tm - punkty graniczne przedzialu, tm>t0  -> [tm;t0]
t0 = 1
tm = 10
#Delta - wymagana dokladnosc bezwzgledna, delta>0
delta = 0.0000001
# r - wariant algorytmu
# r=0 -> minimum poszukiwane jest w przedziale otwartym
# r=1 -> minumum poszukiwane jest w przedziale domknietym
r=0
#I - Maksymalna dopuszczalna liczba obliczen wartosci funkcji
J = math.ceil(3+5*math.log((tm-t0)/delta))
#jesli r=0, J powinno byc troche wieksze
if r==0:
    J=J+15

#f - funkcja do zbadania
f = lambda x: math.pow(x,4)+7*math.pow(x,2)-12



print "t0 = {0}; tm = {1}; r = {2}; I = {3}; delta = {4};".format(t0,tm,r,J,delta)

tm, t0, q0, q_best, t_best, deltaT, j, l = gss(f,tm,t0,delta)

print "Ekstremum funkcji: t = {0} q = {1}".format(round(t_best),round(q_best))
print "Ekstremum funkcji: t = {0} q = {1}".format(t_best,q_best)
