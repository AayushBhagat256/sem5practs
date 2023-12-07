male(raj).
male(khush).
male(sid).
male(atul).
male(dev).
female(hetal).
female(neha).
female(kajal).
female(chetna).

father(raj,khush).
father(raj,sid).
father(khush,atul).
father(sid,dev).
father(sid,chetna).

mother(hetal,khush).
mother(hetal,sid).
mother(neha,atul).
mother(kajal,dev).
mother(kajal,chetna).

wife(hetal,raj).
wife(neha,khush).
wife(kajal,sid).

parent(raj,hetal,khush).
parent(raj,hetal,sid).
parent(khush,neha,atul).
parent(sid,kajal,dev).
parent(sid,kajal,chetna).
%rules
sister(X,Y):-parent(A,B,X),parent(A,B,Y),female(X),X \==Y.
%if it satisfies this then X is sister and return true when parents A,B are same
brother(X,Y):-parent(A,B,X),parent(A,B,Y),male(X),X \==Y.
siblings(X,Y):-parent(A,B,X),parent(A,B,Y),X\==Y.

husband(X,Y):-wife(Y,X).
% for x son of y
son(X,Y,Z):-parent(X,Y,Z),male(Z).
daughter(X,Y,Z):-parent(X,Y,Z),female(Z).
grandfather(X,Y):-father(Z,Y),father(X,Z).
grandmother(X,Y):-father(Z,Y),mother(X,Z).

uncle(X,Y):-father(Z,Y),brother(Z,X).
aunt(X,Y):-uncle(Z,Y),wife(X,Z).

cousin(X,Y):-uncle(Z,X),father(Z,Y).



%https://youtu.be/FZ3irwe3Q_g?si=MrEK2Af3NclVtNAK