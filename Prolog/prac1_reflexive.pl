refl(P,Q):-P=Q.

associative_add(A,B,C):-
    E1 is A+B+C,
    E2 is B+C+A,
    write(E1),write(" "),write(E2),
    refl(E1,E2).

associative_mul(A,B,C):-
    E1 is A*B*C,
    E2 is B*C*A,
    write(E1),write(" "),write(E2),
    refl(E1,E2).

sum(X,Y):-
    S is X+Y,
    write(S).
