male(tom).
male(bob).
male(peter).
male(jim).
female(pam).
female(liz).
female(pat).
female(ann).

parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,pat).
parent(bob,ann).
parent(bob,peter).
parent(pat,jim).

mother(X,Y):-
    parent(X,Y),
    female(X).

father(X,Y):-
    parent(X,Y),
    male(X).

sibling(X,Y):-
    parent(Z,X),
    parent(Z,Y).

sister(X,Y):-
    female(X),
    parent(Z,X),
    parent(Z,Y).

brother(X,Y):-
    male(X),
    parent(Z,X),
    parent(Z,Y).

grandfather(X,Y):-
    parent(Z,Y),
    father(X,Z).

grandmother(X,Y):-
    parent(Z,Y),
    mother(X,Z).

uncle(X,Y):-
    sibling(X,Z),
    parent(Z,Y),
    male(X).

aunt(X,Y):-
    sibling(X,Z),
    parent(Z,Y),
    female(X).

nephew(X,Y):-
    sibling(Z,Y),
    parent(Z,X),
    male(X).

niece(X,Y):-
    sibling(Z,Y),
    parent(Z,X),
    female(X).

cousine(X,Y):-
    parent(Z,X),
    uncle(Z,Y).

cousine(X,Y):-
    parent(Z,X),
    aunt(Z,Y).

