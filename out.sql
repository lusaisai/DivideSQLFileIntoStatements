select a.c0, ad, a.c1, b.c2 c3, c4 , b.c6 ,'a column ; value'c20 ,'a d' c9 ,'a' c10 ,'' c11 , /**/c12 from table_a a join table_b b on a.c1 = b.c1  where a.c3 = 'aaaa';
select   b.c6 , 'a column -- /* ;value*/' c7 from table_a a join table_b b on a.c1 = b.c1 ;
select 'a column --'''''' /* '' ;value*/';
select 1 ;
