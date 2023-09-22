male(Akash).
male(Abay).
female(Naina).
female(Seema).

parent(Akash,Abay).
parent(Naina,Seema).

father(X,Y):-
    parent(X,Y),
    male(X).

mother(X,Y):-
    parent(X,Y),
    female(X).
