

select a.c0,/*+asdsaind exdasaa*/ad, a.c1, b.c2
 c3, c4--, c5 --
, b.c6
,'a column ; value'c20
,'a d' c9
,'a' c10
,'' c11
, /**/c12
from table_a a
join table_b b
on a.c1 = b.c1 --;
where a.c3 = 'aaaa';select /*+ index  a.c1, b.c2
 c3, c4--, c5*/
b.c6
, 'a column -- /* ;value*/' c7
from table_a a
join table_b b
on a.c1 = b.c1
;-- aaa bbb


select 'a column --'''''' /* '' ;value*/';

select  1
;--select 'a column --'''''' /* '' ;value*/';

--select 'a column --'''''' /* '' ;value*/';
