%Gramáticas:
%Práctica:
% 1) -Realizar programa en Prolog, base de conocimiento y árbol sintáctico con las siguientes palabras:
%empleada/o, trabaja/n, cobra/n, sueldo/s

%- 2) -Convertir las categorías gramaticales en predicados de Prolog con argumentos que indican el género y el número.
%- 3) -Construir el árbol sintáctico.

% Reglas
o(o(SN,SV))           --> sn(SN,_Gen,Num), sv(SV,Num).
sn(sn(DET,N),Gen,Num) --> det(DET,Gen,Num), n(N,Gen,Num).
sv(sv(VT,SN),Num)     --> vt(VT,Num), sn(SN,_Gen,_Num).
sv(sv(VI),Num)        --> vi(VI,Num).

% Determinantes
det(det(X),f,sg) --> [X], {member(X,[la,una])}.
det(det(X),f,pl) --> [X], {member(X,[las,unas])}.
det(det(X),m,sg) --> [X], {member(X,[el,un])}.
det(det(X),m,pl) --> [X], {member(X,[los,unos])}.

% Verbos 
vi(vi(trabaja), sg)  --> [trabaja].
vi(vi(trabajan),pl)  --> [trabajan].
vt(vt(cobra),   sg)  --> [cobra].
vt(vt(cobran),  pl)  --> [cobran].

% Sustantivos
n(n(X),f,sg) --> [X], {member(X,[empleada])}.
n(n(X),f,pl) --> [X], {member(X,[empleadas])}.
n(n(X),m,sg) --> [X], {member(X,[empleado,sueldo])}.
n(n(X),m,pl) --> [X], {member(X,[empleados,sueldos])}.


%Realizar las siguientes consultas:

%2 ?- o(A, [el, empleado, trabaja, un, sueldo], []).
%false.

%3 ?- o(A, [el, empleado, trabaja, una, empleada], []).
%false.

%4 ?- o(A, [el, empleada, trabaja], []).
%false.

%5?- o(A, [la, empleada, trabaja], []).
%True. A = o(sn(det(la), n(empleada)), sv(vi(trabaja))) 

%6?- o(A, [los, empleados, sobran, sueldos], []).
%false.

%7?- o(A, [los, empleados, cobran, sueldos], []).
%false.

%8?- o(A, [los, empleados, cobran, los, sueldos], []).
%True. A = o(sn(det(los), n(empleados)), sv(vt(cobran), sn(det(los), n(sueldos)))) 

%9 ?-  o(A, [los, empleados, trabajan, los, sueldos], []).
%false.