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

-- select ticket_id, created_at, completed_at, assigned_at, due_date, start_time
-- from ticket
-- where completed_at is not null and due_date < completed_at
-- limit 10;

select 
    v.company_name,
    avg(julianday(t.completed_at) - julianday(t.assigned_at)) as avg_ticket_completion_time
from ticket t
join vendor v
using(vendor_id)
where t.completed_at >= datetime('now', '-30 days')
group by 1
order by 2 desc;


select 
    v.company_name,
    avg(julianday(t.completed_at) - julianday(t.assigned_at)) as avg_ticket_completion_time
from ticket t
join vendor v
using(vendor_id)
where t.completed_at >= datetime('now', '-60 days')
  and t.completed_at < datetime('now', '-30 days')
group by 1
order by 2 desc;

-- Unassigned work orders by well

-- select 
--     w.well_name, 
--     count(wo.work_order_id),
--     (
--         select count(*) 
--         from work_orders 
--         where current_status='unassigned'
--     ) as 'total unassigned'
-- from work_orders wo
-- join well w
-- using (well_id)
-- where current_status = 'unassigned'
-- group by well_id
-- order by 2 desc;

-- Tickets in progress
-- select v.vendor_code, count(*) as 'tickets in progress'
-- from ticket t
-- join vendor v
-- using (vendor_id)
-- where t.status='in progress'
-- group by vendor_id;

-- Tickets Completed by Vendor
-- select v.company_name, count(*) 
-- from ticket t
-- join vendor v
-- using(vendor_id)
-- where t.status='completed'
-- group by 1;

-- select 
--     status,
--     completed_at
-- from ticket
-- limit 20;