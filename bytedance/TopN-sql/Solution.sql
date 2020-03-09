select a.*
from (
select country,city,visitors, row_number() over (partition by city order by visitors desc ) rank
from tripdata
order by country,city,visitors desc
) a
where a.rank<=3;