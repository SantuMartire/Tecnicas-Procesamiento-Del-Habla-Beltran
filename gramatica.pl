% =====================================================================
%  KBpracticaGramaticas.pl
%  Gramática DCG en Prolog
%  Palabras: empleada/o(s), trabaja/n, cobra/n, sueldo/s
%
%  Convenciones:
%     Género : m (masculino) | f (femenino)
%     Número : sg (singular) | pl (plural)
%     Verbos : vi (intransitivo) | vt (transitivo)
%
%  Uso (SWI-Prolog):
%     ?- [gramatica].
%     ?- o(A,[la,empleada,trabaja],[]).
%     ?- o(A,[los,empleados,cobran,sueldos],[]).
%     ?- o(A,[la,empleada,cobra,un,sueldo],[]).
% =====================================================================

% --- Reglas gramaticales ---
o(o(SN,SV))           --> sn(SN,_Gen,Num), sv(SV,Num).
sn(sn(DET,N),Gen,Num) --> det(DET,Gen,Num), n(N,Gen,Num).
sv(sv(VT,SN),Num)     --> vt(VT,Num), sn(SN,_Gen,_Num).
sv(sv(VI),Num)        --> vi(VI,Num).

% --- Determinantes ---
det(det(X),f,sg) --> [X], {member(X,[la,una])}.
det(det(X),f,pl) --> [X], {member(X,[las,unas])}.
det(det(X),m,sg) --> [X], {member(X,[el,un])}.
det(det(X),m,pl) --> [X], {member(X,[los,unos])}.

% --- Verbos intransitivos ---
vi(vi(trabaja), sg)  --> [trabaja].
vi(vi(trabajan),pl)  --> [trabajan].

% --- Verbos transitivos ---
vt(vt(cobra), sg)    --> [cobra].
vt(vt(cobran),pl)    --> [cobran].

% --- Sustantivos ---
n(n(X),f,sg) --> [X], {member(X,[empleada])}.
n(n(X),f,pl) --> [X], {member(X,[empleadas])}.
n(n(X),m,sg) --> [X], {member(X,[empleado,sueldo])}.
n(n(X),m,pl) --> [X], {member(X,[empleados,sueldos])}.
