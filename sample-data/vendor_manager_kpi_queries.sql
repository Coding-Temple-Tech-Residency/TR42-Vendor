-- Test Vendor: 99d37a94-dff8-4a1a-9144-2ed3c16fd181

-- select 
--     vc.full_name,
--     round(avg(cp.rating), 2),
--     count(cp.ticket_id)
-- from 
-- (
-- select 
--     c.contractor_id,
--     u.first_name || " " || u.last_name as full_name
-- from contractors c
-- join user u
-- using (user_id)
-- where vendor_id = '99d37a94-dff8-4a1a-9144-2ed3c16fd181'
-- ) as vc
-- join contractor_performance cp
-- using (contractor_id)
-- group by 1
-- order by 2 desc;

select ticket_id, completed_at, vendor_id
from ticket
where  status='completed';