#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


def nonuniform(csections, Q, HDB):
    g = float(9.8)
    dhini = float(0.5)
    H = np.empty(len(csections))
    
    # 下流端水位
    # 添字dがi-1、添字pがiの値
    s = csections[0]
    Qd = Q
    Hd = HDB
    H[0] = Hd
    Ad,_,_,_,_ = s.H2ABSKRc(Hd)
    ied, _, Betad, _= s.HQ2IeAlphaBetaVsub(Hd, Qd)
    
    for i in range(1, len(csections)):
        # 収束計算の初期値は限界流時水位+1mm
        sp, sd = csections[i], csections[i-1]
        Qp = Q
        Hp = sp.Hc(Qp)
        Ap,_,_,_,_ = sp.H2ABSKRc(Hp)
        iep, _, Betap, _= sp.HQ2IeAlphaBetaVsub(Hp, Qp)
        dx = sp.distance - sd.distance
            
        E1 = Betap*0.5/g*Qp**2.0/Ap**2.0 + Hp
        E2 = Betad*0.5/g*Qd**2.0/Ad**2.0 + Hd + 0.5*dx*(ied + iep)
        
        Hp = Hp + float(0.001)
        dh = dhini
        for n in range(1000):
            Ap,_,_,_,_ = sp.H2ABSKRc(Hp)
            iep, _, Betap, _= sp.HQ2IeAlphaBetaVsub(Hp, Qp)
        
            E1 = Betap*0.5/g*Qp**2.0/Ap**2.0 + Hp
            E2 = Betad*0.5/g*Qd**2.0/Ad**2.0 + Hd + 0.5*dx*(ied + iep)
            
            if np.abs(E1 - E2) < 0.00001 : 
                break
            elif E1 > E2 :
                dh *= float(0.5)
                Hp -= dh
            else:
                Hp += dh
                
        H[i] = Hp
        Qd, Hd, ied, Ad, Betad = Qp, Hp, iep, Ap, Betap
        
    return H

