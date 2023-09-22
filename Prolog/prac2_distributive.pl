refl(P,Q):-P=Q.

distributive(A,B,C):-
    L1 is B+C,
    L is A*L1,
    E1 is A*B,
    E2 is A*C,
    E3 is E1+E2,
    refl(L,E3).
