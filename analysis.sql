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