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

-- select 
--     c.employee_number,
--     sum(completed_at <= due_date),
--     sum(completed_at <= due_date) * 1.0 / count(t.ticket_id),
--     count(t.ticket_id)
-- from ticket t
-- join contractors c
-- on t.assigned_contractor = c.contractor_id
-- where t.status='completed' and t.completed_at > '2025-09-31' and t.vendor_id='99d37a94-dff8-4a1a-9144-2ed3c16fd181'
-- group by c.contractor_id
-- order by 3 desc;

select t.ticket_id, t.completed_at
from ticket t
join contractors c
on t.assigned_contractor = c.contractor_id
where c.employee_number = 'EMP8417' and t.completed_at >= '2025-09-30';

