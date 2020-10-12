select outlet.name as name from outlet
inner join(
    select * from menu
    where name like "%Heineken%"
    order by price
    limit 1
) as heineken
on outlet.id = heineken.outlet_id;


select ta.name as name
from
(select * from outlet
where source='tripadvisor') as ta
inner join
(select * from outlet
where source='ubereats') as ue
on ue.name=ta.name
where ta.rating>=4.0 and ue.rating>=4.0;

select name from
(outlet
inner join
review as r1
on outlet.id = r1.outlet_id)
inner join
review as r2
on r1.outlet_id = r2.outlet_id
where (month(r1.date) - month(r2.date) = 1) and (r1.rating+r2.rating)/2<3.0;


select user.user from
(select r1.user_id
from (
    review as r1
    cross join
    review as r2
    on r1.user_id = r2.user_id
)
where ((month(r1.date)-month(r2.date)=1) or (month(r2.date)-month(r1.date)=1)) and (r1.rating+r2.rating)<6.0
) as r
inner join user
on r.user_id = user.id;
