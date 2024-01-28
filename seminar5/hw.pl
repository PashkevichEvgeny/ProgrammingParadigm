% Rules
sum([], 0).
sum([H|T], SumFinal) :-
    sum(T, SumTemp),
    SumFinal is H + SumTemp.