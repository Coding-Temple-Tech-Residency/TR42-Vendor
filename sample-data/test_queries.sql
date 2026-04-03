-- SQLite

-- select 
--     u.first_name, 
--     u.last_name,
--     u.is_admin,
--     vu.role,
--     v.company_name
-- from user u
-- inner join vendor_user vu
-- using (user_id)
-- inner join vendor v
-- using (vendor_id)
-- limit 10;

-- Total Number of tickets per vendor

-- select v.company_name, count(t.ticket_id)
-- from vendor v
-- inner join work_orders wo
-- on v.vendor_id = wo.assigned_vendor
-- inner join ticket t
-- on wo.work_order_id = t.work_order_id
-- group by v.company_name
-- order by 2 desc;

-- -- Number of active tickets
-- select v.company_name, count(t.ticket_id)
-- from vendor v
-- inner join work_orders wo
-- on v.vendor_id = wo.assigned_vendor
-- inner join ticket t
-- on wo.work_order_id = t.work_order_id
-- where t.status = 'completed'
-- group by v.company_name
-- order by 2 desc;

-- number of submitted invoices by vendor
-- select v.company_name, count(i.invoice_id)
-- from invoice i
-- join line_item li
-- using (invoice_id)
-- join vendor v
-- using (vendor_id)
-- where i.invoice_status = 'submitted'
-- group by 1;

select 
    v.company_name,
    avg(julianday(t.completed_at) - julianday(t.assigned_at)) as avg_ticket_completion_time
from ticket t
join vendor v
using(vendor_id)
group by 1;
